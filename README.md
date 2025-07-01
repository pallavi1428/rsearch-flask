
```markdown
# rSearch Flask Backend

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.2-green.svg)
![OpenAI](https://img.shields.io/badge/openai-1.0+-brightgreen.svg)

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

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```bash
   echo "OPENAI_API_KEY=your_openai_key" > .env
   echo "SERPER_API_KEY=your_serper_key" >> .env
   ```

### Running the Server

**Development:**
```bash
python app.py
```

**Production (using Waitress):**
```bash
waitress-serve --port=8000 app:app
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

### Cloud Deployment

Recommended services:
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service
- Heroku

## Configuration

| Environment Variable | Required | Description |
|----------------------|----------|-------------|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `SERPER_API_KEY` | Yes | Your Serper API key |
| `FLASK_ENV` | No | Set to "production" for prod |

## Frontend Integration

Connect your frontend by setting the base URL:
```javascript
const API_BASE_URL = 'http://localhost:8000';
```

## Troubleshooting

**Common Issues:**
- `404 Not Found`: Ensure endpoint paths match exactly
- `CORS Errors`: Verify CORS middleware is properly configured
- `Streaming Issues`: Check OpenAI API key and model availability

## License

MIT License

## Acknowledgments

- Original rSearch concept by [Justmalhar](https://github.com/Justmalhar/rsearch)
- Serper API for search results
- OpenAI for AI capabilities
```

This README includes:

1. **Key Metadata**: Badges showing Python/Flask versions
2. **Clear Feature List**: Highlights core capabilities
3. **API Documentation**: Endpoint specifications
4. **Setup Instructions**: From installation to deployment
5. **Configuration Guide**: Environment variables
6. **Troubleshooting**: Common issues and solutions
7. **Deployment Options**: Docker and cloud platforms

You can customize the deployment and license sections as needed for your specific use case. The README provides everything needed for developers to understand, install, and use your backend service.