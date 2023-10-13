import openai
import os
import json

def clean_document(document_path: str):
    file_content_string = None
    with open(document_path, 'r') as f:
        file_content_string = f.read()
    return clean_text(file_content_string)


def clean_text(text_to_clean: str):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    model = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Give a basic response to whatever you are prompted with."},
            {"role": "user", "content": text_to_clean}
        ],
    )
    print(response)
    return response
