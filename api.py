"""
Handles LLM model initialization and API calls.
"""

class LLMModelWrapper:
    def __init__(self, client):
        self.client = client

    
    def chat_completion(self, model, messages):
        return self.client.chat.completions.create(model=model, messages=messages)
