def generate_ai_response(max_tokens, temperature=150):
	response = f"Mock AI response with max tokens {max_tokens} and temperature {temperature}."
	return response


# Examples
print(generate_ai_response(100, temperature=0.5))
print(generate_ai_response(200, temperature=0.9))
