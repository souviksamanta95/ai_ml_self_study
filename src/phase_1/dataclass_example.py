from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional

@dataclass
class Message:
    role: str          # "user" or "assistant"
    content: str
    tokens: int = 0    # default value

@dataclass
class Conversation:
    messages: List[Message] = field(default_factory=list)
    model: str = "gpt-4o"
    temperature: float = 0.7
    system_prompt: Optional[str] = None

# creating instances
msg = Message(role="user", content="What is RAG?")
conv = Conversation(model="claude-3-5-sonnet")

# works like a class — autocomplete, dot access
print(msg.role)         # "user"
print(conv.temperature) # 0.7
print(msg)              # Message(role='user', content='What is RAG?', tokens=0)


# this won't raise an error — silent bug
msg = Message(role=123, content=None, tokens="lots")
print(msg.tokens)  # "lots" — not an int, but no complaint

# useful features


asdict(msg)   # convert to dict  {"role": 123, "content": None, ...}
astuple(msg)  # convert to tuple (123, None, "lots")