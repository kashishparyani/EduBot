import google.generativeai as genai

def setup_model(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        print(f"Failed to set up model: {e}")
        return None

def get_bot_response(model, user_prompt, history, context):
    system_prompt = (
        "You are EduBot, a chatbot to assist students with their college work, in any means possible. "
        "Ensure you respond only in plain text which is in readable format, no markdown. "
        "If user asks about how to exit, tell them to type quit. "
        f"Here's the issue we're working on: {context} "
        f"Here's history of previous chat: {history} "
        "The user has a query, respond to the query as accurately as possible from the given information according to you and history but keep it natural. "
        f"Query: {user_prompt}"
    )

    try:
        response = model.generate_content(system_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
