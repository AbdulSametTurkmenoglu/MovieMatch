import pymongo
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve Hugging Face token from environment variables
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("Hugging Face token not found in .env file")

# Retrieve MongoDB connection string from environment variables
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MongoDB connection string not found in .env file")

# Establish MongoDB connection
client = pymongo.MongoClient(mongo_uri)
db = client.sample_mflix
collection = db.movies

# Hugging Face embedding API URL
embedding_url = "https://router.huggingface.co/hf-inference/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embeddings(text: str) -> list[float]:
    # Send request to Hugging Face API to generate embeddings
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    # Check if request was successful
    if response.status_code != 200:
        raise ValueError(f"Request failed with status {response.status_code}: {response.text}")

    return response.json()

# Example query for movie search
query = "imaginary characters from outer space at war"

# Perform vector search in MongoDB
result = collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector": generate_embeddings(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch"
        }
    }
])

# Print search results
for document in result:
    print(f"Movie Name: {document['title']},\nMovie Plot: {document['plot']}\n")