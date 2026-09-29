import ollama

text = """
Little Mount station provides lift, parking,
escalator and bicycle facilities. """

response = ollama.embed(
    model="nomic-embed-text",
    input=text
)

embedding = response["embeddings"][0]

def get_embedding(text: str) -> list[float]:
    response = ollama.embed(
        model="nomic-embed-text",
        input=text
    )

    return response["embeddings"][0]
    
print(f"Dimensions : {len(embedding)}")
print(embedding[:10])