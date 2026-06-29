# Variables and Strings
role = "Senior Gen AI Engineer"
topic = "RAG Pipelines"
user_query = "What are RAG Pipelines and how do they work?"
word_count = len(user_query.split())

# f-string inside an LLM Prompt Template
prompt_template = f"You are an expert {role}. Explain the core concepts of {topic} in simple terms. Answer the following query: {user_query} within {word_count} words."

print(prompt_template)