import pandas as pd
import json
from pydantic import BaseModel, Field
from openai import OpenAI
from google.colab import userdata
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors


print("Loading dataset...")
dataset = load_dataset("ag_news", split="train[:1000]")
 
# Extract the text column into a Python list
documents = dataset["text"]
 
print(f"Loaded {len(documents)} documents.")
print(f"Sample: {documents[0][:100]}...")