# List of messages representing Chat History for OpenAI API
chat_history = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "What is embeddings?"}
]

# Dictionary representing LLM Metadata Response
llm_response = {
    "model": "gpt-4o",
    "usage": {
        "prompt_tokens": 120,
        "completion_tokens": 45
    },
    "finish_reason": "stop",
    "choices": [
        {"text": "Embeddings are vector representations of text."}
    ]
}

# Accessing data from dict and list (JSON parsing)
generated_text = llm_response["choices"][0]["text"]
total_tokens = llm_response["usage"]["prompt_tokens"] + llm_response["usage"]["completion_tokens"]

print(f"AI Response: {generated_text}")
print(f"Total Tokens Used: {total_tokens}")