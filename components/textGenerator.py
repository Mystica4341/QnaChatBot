from haystack.components.generators import HuggingFaceAPIGenerator
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator
from haystack.components.builders import PromptBuilder
from components.token import secret_GEMINI

#initialize prompt builder and template
template = """
Using the information contained in the context that match with the Question, provide a comprehensive and moderate answer for the Question.
Translate answer if possible
Only provide an "[Url]: url of article" at bottom of the answer if meta section has the url else DO NOT provide

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{question}}
Answer:
"""

prompt_builder = PromptBuilder(template=template)

#initialize generator
generator = GoogleAIGeminiGenerator(model="gemini-pro", api_key=secret_GEMINI)