# zerocall-backend
# ZeroCall AI - Backend

FastAPI backend for ZeroCall AI Voice IVR.

## Setup

1. Create virtual environment: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Set env: `GEMINI_API_KEY=your_key`
5. Run: `uvicorn main:app --reload`

## API Endpoints

- `GET /` - Health check
- `POST /chat` - Send query, get AI response

## Deploy

Hosted on Render.com (Free Tier)
