import chromadb
from embedder import embedding
from ingest import all_chunks

client = chromadb.PersistentClient(path="../database")

collection = client.get_or_create_collection(
    name="cmrl"
)

result = collection.get()

for index, chunk in enumerate(all_chunks):
    embedding = embedding(chunk["text"])

    collection.add(
        ids=[str(index)],
        documents=[chunk["text"]],
        embeddings=[embedding],
        metadatas=[
            {
                "page": chunk["page"]
            }
        ]
    )

print(result["documents"])
print(result["metadatas"])
