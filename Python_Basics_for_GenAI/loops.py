# A list of text chunks extracted from a PDF document
document_chunks = [
    "Introduction to Generative AI and LLMs.",
    "Understanding Retrieval-Augmented Generation (RAG).",
    "Fine-tuning open-source models like Llama 3."
]

# Using a 'for loop' to iterate through the chunks
processed_prompts = []
for index, chunk in enumerate(document_chunks):
    # Simulating sending each chunk to an embedding API
    processed_prompts.append(chunk)
    print(f"Processing Chunk {index + 1}: Generating embedding for -> '{chunk}'")


print("All chunks successfully processed!")
print(f"Processed Prompts: {processed_prompts}")