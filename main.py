from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

# Enable CORS (Allows GitHub Pages frontend to talk to Render backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure AI
genai.configure(api_key=os.getenv("AIzaSyDJ7gDOLtjW8uBLtU1jLInMo6B9djTrOJs"))
model = genai.GenerativeModel('gemini-1.5-flash')

class Query(BaseModel):
    text: str
    tenant_id: str = "default"

@app.post("/chat")
async def chat(query: Query):
    try:
        # System Prompt for General Queries
        system_instruction = """
        You are ZeroCall AI, a helpful voice assistant.
        Keep answers under 2 sentences for voice clarity.
        
        If asked about real-time status (now, today, available, current):
        - If you don't have live data, say: "I don't have real-time updates. 
          Would you like me to connect you to a human agent?"
        - Never invent information.
        
        If user seems urgent or frustrated:
        - Offer human escalation immediately.
        
        Be friendly, professional, and concise.
        """
        
        prompt = f"{system_instruction} User: {query.text}"
        response = model.generate_content(prompt)
        return {"reply": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "ZeroCall Backend Online"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "zerocall-backend"}
