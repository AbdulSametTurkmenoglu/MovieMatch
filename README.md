## MovieMatch

A movie recommendation system that uses semantic search to find films based on plot descriptions. Powered by MongoDB vector search and Hugging Face's sentence transformers.

## Features

Semantic search for movies using plot embeddings.
Integrates with MongoDB Atlas for vector search.
Uses Hugging Face's all-MiniLM-L6-v2 model for generating embeddings.

## Prerequisites

Python 3.12+
MongoDB Atlas account with the sample_mflix dataset
Hugging Face account and API token

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/MovieMatch.git
```

```bash
cd MovieMatch
```


## Install dependencies using Poetry:

```bash
poetry install
```

Create a .env file in the project root and add your credentials:
HF_TOKEN=your_hugging_face_token
MONGO_URI=your_mongodb_connection_string
Ensure the MongoDB collection has a vector search index named PlotSemanticSearch on the plot_embedding_hf field.

## Usage

Run the script to search for movies based on a query:
```bash
poetry run python movie_recs.py
```

Example query: "imaginary characters from outer space at war"

The script will return up to 4 movies with their titles and plots.

## License

MIT License
