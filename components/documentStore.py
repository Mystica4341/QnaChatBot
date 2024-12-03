from datasets import load_dataset
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from components.token import secret_QDRANT

#initialize Qdrant db doc
document_store = QdrantDocumentStore(
    url="4ba16ed0-b91c-4ceb-b080-8c5ba38cafc1.us-east4-0.gcp.cloud.qdrant.io:6333", # Replace with your instance URL
    api_key=secret_QDRANT,                                                             # Replace with your API key
    index="my_collection",                                                          # Name of the collection
    similarity="cosine",                                                            # Similarity metric: cosine, dot, or euclidean
    embedding_dim=768,                                                              # Embedding dimension (must match your embedding model)
    #use_sparse_embeddings=True,
    #recreate_index=True,
    #return_embedding=True,
    #wait_result_from_api=True,
)