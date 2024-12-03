from datasets import load_dataset
from components.documentStore import document_store
from haystack.dataclasses.document import Document
from components.embedders import doc_embedder

#dataset
dataset = load_dataset("bilgeyucel/seven-wonders", split="train")
docs = [Document(content=doc["content"], meta=doc["meta"]) for doc in dataset]

#embedded Doc
embeddedDocs = doc_embedder.run(docs)

#write documents
try:
  document_store.write_documents(embeddedDocs['documents'])
  print(' Documents wrote to the vectorDB Successfully')
except Exception as e:
  print('Error: ', e)