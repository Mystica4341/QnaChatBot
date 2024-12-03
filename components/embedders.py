from haystack.components.embedders import HuggingFaceAPITextEmbedder
from haystack.components.embedders import HuggingFaceAPIDocumentEmbedder
from components.token import secret_HF

#Initialize text embedder
text_embedder = HuggingFaceAPITextEmbedder(api_type="serverless_inference_api",
                                    api_params={"model": "sentence-transformers/bert-base-nli-mean-tokens"},
                                    token=secret_HF)


# Initialize document embedder
doc_embedder = HuggingFaceAPIDocumentEmbedder(api_type="serverless_inference_api",
                                    api_params={"model": "sentence-transformers/bert-base-nli-mean-tokens"},
                                    token=secret_HF)

