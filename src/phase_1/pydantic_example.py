from pydantic import BaseModel, Field
from typing import List, Optional, Literal
import json

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
    tokens: int = 0

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "gpt-4o"
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = None

# valid — works fine
msg = Message(role="user", content="What is RAG?")

# pydantic coerces types where it can
msg2 = Message(role="user", content="hello", tokens="5")
print(msg2.tokens)  # 5 (int) — string "5" auto-converted

# invalid — raises ValidationError with clear message
try:
    bad = Message(role="robot", content="hello")
except Exception as e:
    print(e)
# role must be 'user', 'assistant', or 'system'

# parse from dict (e.g. API response)
data = {"role": "assistant", "content": "RAG stands for..."}
msg = Message(**data)          # validated instantly

# or from json string
raw_json = '{"role": "user", "content": "explain embeddings"}'
msg = Message.model_validate_json(raw_json)

# export to dict or json
msg.model_dump()               # {"role": "user", "content": "..."}
msg.model_dump_json()          # '{"role":"user","content":"..."}'

# this is exactly what LangChain, FastAPI, OpenAI SDK do internally