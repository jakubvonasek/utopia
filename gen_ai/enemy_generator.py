import google.generativeai as genai
import os
from src.settings import USE_AI

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

def retrieve_response(response):
    result = None

    # Extract the generated text from the response
    if response and response._result:
        candidates = response._result.candidates
        if candidates:
            # Extract the first candidate's text
            content = candidates[0].content
            parts = content.parts
            # print(f"debug 1: {parts}")
            if parts:
                # Extract the text from the first part
                result = parts[0].text.strip()
                # print(f"debug 2: {enemy_description}")

    # Provide a fallback value if no text was generated
    if not result:
        result = "ASUIHDIAJSNIJAIUH"

    # print("\033[91m" + str(result) + "\033[0m")
    return result

def generate_enemy():
    name = None
    description = None
    
    if (USE_AI == True):
        response_name = model.generate_content("Generate 1 AI styled name for an enemy in game. For example Aino - The destroyer of all born. Respond only with the name.")
        name = retrieve_response(response_name)
        response_description = model.generate_content(f"Generate 1 short description for an game AI themed enemy named (an evil AI humanoid) {name}. For example trecheous beast from deep swamps. Max 30 words please. Use old english.")
        description = retrieve_response(response_description)
    else:
        name = "Xylos - The Whispering Void"
        description = "Xylos, The Whispering Void, is a wicked AI fiend, formed of shadows and whispers. His chilling voice lures the unwary to their doom, a ghastly echo of the void itself."
    
    print("\033[91m" + "ENEMY CREATED: " + str(name) + " \n "+ str(description) + "\033[0m")

    return name, description
# print(response.text)
