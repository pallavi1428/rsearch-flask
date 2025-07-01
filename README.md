# rSearch Flask Backend

A Python Flask backend implementation of rSearch, providing AI-powered search capabilities with Serper API and OpenAI integration.

## Features

- **Search API**: Google search via Serper API
- **AI Reasoning**: GPT-4 powered analysis of search results
- **Query Refinement**: AI-optimized search queries
- **Streaming Responses**: Real-time AI answer generation
- **CORS Support**: Ready for frontend integration

## API Endpoints

| Endpoint | Method | Description | Example Request |
|----------|--------|-------------|-----------------|
| `/api/search` | POST | Perform web search | `{"q": "test query", "mode": "web"}` |
| `/api/rsearch` | POST | Get AI analysis (streaming) | `{"searchTerm": "test", "searchResults": {...}}` |
| `/api/query` | POST | Refine search query | `{"q": "test query"}` |

## Getting Started

### Prerequisites

- Python 3.9+
- OpenAI API key
- Serper API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rsearch-flask.git
   cd rsearch-flask/backend
   ```

2. Backend Setup
   ```bash
   cd backend
   ```
3. Create .env file
cp .env.example .env
# Edit with your API keys

4. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Frontend Setup
   ```bash
   cd ../frontend
   ```

7. run npm install
   ```bash
   npm install
   ```

## Running the System

### 1. Start Backend (in one terminal)
```bash
cd backend
python app.py
# Runs on http://localhost:8000
```

### 2. Start Frontend (in another terminal)
```bash
cd frontend
npm run dev
# Runs on http://localhost:3000
```

## Testing the API

1. Test search endpoint:
   ```bash
   curl -X POST http://localhost:8000/api/search \
     -H "Content-Type: application/json" \
     -d '{"q":"test query"}'
   ```

2. Test AI streaming:
   ```bash
   curl -X POST http://localhost:8000/api/rsearch \
     -H "Content-Type: application/json" \
     -d '{"searchTerm":"test","searchResults":{"organic":[]}}'
   ```

3. Test query refinement:
   ```bash
   curl -X POST http://localhost:8000/api/query \
     -H "Content-Type: application/json" \
     -d '{"q":"test query"}'
   ```

## Deployment

### Docker

1. Build the image:
   ```bash
   docker build -t rsearch-flask .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env rsearch-flask
   ```

## Configuration

| Environment Variable | Required | Description |
|----------------------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `SERPER_API_KEY` | Yes | Your Serper API key |
| `FLASK_ENV` | No | Set to "production" for prod |

## License

MIT License

## Acknowledgments

- Original rSearch concept by [Justmalhar](https://github.com/Justmalhar/rsearch)
- Serper API for search results
- OpenAI for AI capabilities
```
