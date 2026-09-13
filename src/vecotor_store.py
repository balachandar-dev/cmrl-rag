import chromadb
from embedder import embedding

client = chromadb.PersistentClient(path="../database")

collection = client.get_or_create_collection(
    name="cmrl"
)

collection.add(
    ids=["1"],
    documents=[
        "Little Mount station provides parking, lift and escalator."
    ],
    embeddings=[embedding],      # from previous step
    metadatas=[
        {
            "page": 2,
            "station": "Little Mount"
        }
    ]
)

result = collection.get()

print(result["documents"])
print(result["metadatas"])
