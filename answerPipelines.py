from fastapi import APIRouter
from components.embedders import text_embedder
from components.retriever import retriever
from components.textGenerator import prompt_builder, generator
from haystack import Pipeline

# Initialize the router
answer_router = APIRouter()

# Initialize pipeline
awsering_pipeline = Pipeline()
# Add components to your pipeline
awsering_pipeline.add_component("text_embedder", text_embedder)
awsering_pipeline.add_component("retriever", retriever)
awsering_pipeline.add_component("prompt_builder", prompt_builder)
awsering_pipeline.add_component("llm", generator)

# Now, connect the components to each other
awsering_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
awsering_pipeline.connect("retriever.documents", "prompt_builder.documents")
awsering_pipeline.connect("prompt_builder.prompt", "llm")

# Run the pipeline
@answer_router.post("/ask")
async def ask(question: str):
    response = awsering_pipeline.run({"text_embedder": {"text": question}, "prompt_builder": {"question": question}})
    return response["llm"]["replies"][0]

#ask question
# question = input("What is your question? ")
# response = awsering_pipeline.run({"text_embedder": {"text": question}, "prompt_builder": {"question": question}})
# print(response["llm"]["replies"][0])