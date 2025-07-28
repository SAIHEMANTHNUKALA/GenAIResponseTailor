from fastapi import FastAPI
from pydantic import BaseModel
import openai

# Set your OpenAI API key
client = openai.OpenAI(api_key="APIKEY")

# Create FastAPI app
app = FastAPI()

# Request model
class SentenceRequest(BaseModel):
    sentence: str


    

# Endpoint
@app.post("/tune-sentence")
async def tune_sentence(request: SentenceRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant that rewrites text to be more very professionally and ."},
                {"role": "user", "content": f"Rewrite the following sentence very professionally:\n\n{request.sentence}"}
            ],
            temperature=0.7
        )

        professional_output = response.choices[0].message.content.strip()

        return {
            "original_input": request.sentence,
            "professional_output": professional_output
        }

    except Exception as e:
        return {"error": str(e)}