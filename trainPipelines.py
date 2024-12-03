from haystack import Pipeline
from haystack.components.converters import DOCXToDocument
from haystack.components.preprocessors import DocumentCleaner
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.writers import DocumentWriter
from components.documentStore import document_store
from components.embedders import doc_embedder

# Initialize pipeline
train_pipeline = Pipeline()
# Add components to your pipeline
train_pipeline.add_component("converter", DOCXToDocument())
train_pipeline.add_component("cleaner", DocumentCleaner(remove_empty_lines=False, remove_extra_whitespaces=False))
train_pipeline.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=1))
train_pipeline.add_component("embedder", doc_embedder)
train_pipeline.add_component("writer", DocumentWriter(document_store))

# Now, connect the components to each other
train_pipeline.connect("converter", "cleaner")
train_pipeline.connect("cleaner", "splitter")
train_pipeline.connect("splitter", "embedder")
train_pipeline.connect("embedder", "writer")