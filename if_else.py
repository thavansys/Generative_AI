def route_questions(questions):
    question = questions.lower()

    if "pdf" in question:
        return "Use RAG"
    
    elif "translate" in question:
        return "Use Translation Model"
    
    else:
        return "Use LLM"
    
print(route_questions("translate to tamil"))