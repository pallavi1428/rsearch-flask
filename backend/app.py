from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import httpx
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_endpoint(mode):
    endpoint_map = {
        "images": "https://google.serper.dev/images",
        "videos": "https://google.serper.dev/videos",
        "places": "https://google.serper.dev/places",
        "news": "https://google.serper.dev/news",
        "shopping": "https://google.serper.dev/shopping",
        "scholar": "https://google.serper.dev/search",
        "patents": "https://google.serper.dev/search",
        "web": "https://google.serper.dev/search",
        "search": "https://google.serper.dev/search"
    }
    return endpoint_map.get(mode, "https://google.serper.dev/search")


# API Endpoints

@app.route('/api/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        endpoint = get_endpoint(data.get('mode', 'web'))
        
        params = {
            "q": data['q'],
            "gl": data.get('gl', 'us'),
            "hl": data.get('hl', 'en')
        }

        if data.get('mode') == "scholar":
            params["type"] = "scholar"
            params["engine"] = "google_scholar"
        elif data.get('mode') == "patents":
            params["type"] = "patents"
            params["engine"] = "google"

        with httpx.Client() as http_client:
            response = http_client.post(
                endpoint,
                headers={"X-API-KEY": os.getenv("SERPER_API_KEY")},
                json=params
            )
            return jsonify(response.json())

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/api/rsearch', methods=['POST'])
def rsearch():
    def generate():
        try:
            data = request.get_json()

            # If no searchResults provided, perform a search first
            if not data.get('searchResults'):
                search_data = {
                    "q": data['searchTerm'],
                    "mode": data.get('mode', 'web')
                }
                search_response = search()
                search_results = json.loads(search_response.get_data())
                data['searchResults'] = {
                    "organic": search_results.get("organic", []),
                    "knowledgeGraph": search_results.get("knowledgeGraph")
                }

            # Extract organic results properly
            organic_results = data['searchResults'].get("organic", [])

            prompt = f"""
            Question: {data['searchTerm']}
            Search Results: {organic_results}

            Based on the above search results, please provide a comprehensive answer.
            """

            # Stream OpenAI response
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )

            for chunk in response:
                if chunk.choices[0].delta.content:
                    # Yield plain text content, no JSON or data:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            traceback.print_exc()
            # Yield an error line in plain text
            yield f"\n[ERROR] {str(e)}\n"

    # Note: 'text/plain' instead of 'text/event-stream'
    return Response(stream_with_context(generate()), mimetype='text/plain')


@app.route('/api/query', methods=['POST'])
def query_refinement():
    try:
        data = request.get_json()
        prompt = f"""
        Original query: {data['q']}
        Please refine this search query to be more effective.
        Return only the refined query without any additional text.
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({
            "refined_query": response.choices[0].message.content,
            "explanation": "The query was refined to improve search results"
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/')
def root():
    return jsonify({"message": "API is running"})

if __name__ == '__main__':
    app.run(port=8000, debug=True)