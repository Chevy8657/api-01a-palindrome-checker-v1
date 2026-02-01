from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Palindrome Checker", version="v1")

class Health(BaseModel):
    ok: bool

class PalindromeResponse(BaseModel):
    input: str
    is_palindrome: bool

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/is-palindrome", response_model=PalindromeResponse)
def is_palindrome(text: str = Query(..., description="Text to check for palindrome")):
    # Normalize: remove whitespace, make lowercase
    normalized = "".join(ch.lower() for ch in text if not ch.isspace())
    return {"input": text, "is_palindrome": normalized == normalized[::-1]}
