import openai
import os

def clean_document(document_path: str):
    file_content_string = None
    with open(document_path, 'r') as f:
        file_content_string = f.read()
    return clean_text(file_content_string)


def clean_text(text_to_clean: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    pass
