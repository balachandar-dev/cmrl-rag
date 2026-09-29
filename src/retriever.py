from embedder import get_embedding
from vector_store import collection 

question = "Is parking available at Little mount"

query_embeddings = get_embedding(question)

results = collection.query(
    query_embeddings=[query_embeddings],
    n_results=3
)

print(f"results{results}")

documents = results["documents"]
metadatas = results["metadatas"]

if documents is None or metadatas is None:
    raise ValueError("No results returned from Chroma")

docs = documents[0]
metas = metadatas[0]

for doc, meta in zip(docs, metas):
    print("=" * 40)
    print(f"Page: {meta['page']}")
    print(doc)