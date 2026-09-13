from embedder import embedding
from vector_store import collection 

question = "Is parking available at Little mount"

question_embedding = embedding(question)

results = collection.query(
    query_embeddings=[question_embedding]
    m_results=3
)
