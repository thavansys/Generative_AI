def route_question(questions):
    question = questions.lower()

    if "pdf" in question:
        return "Use RAG"
    
    elif "translate" in question:
        return "Use Translation Model"
    
    else:
        return "Use LLM"
    
print(route_question("translate to tamil"))