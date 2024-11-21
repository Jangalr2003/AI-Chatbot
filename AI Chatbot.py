import google.generativeai as ai

# Configuration
API_KEY = "AIzaSyAzcLD5-4GhkbrnTHf552UYyo-a3KAZfag"
ai.configure(api_key=API_KEY)

# Initialize the model and chat instance
def initialize_chat(model_name="gemini-pro"):
    try:
        model = ai.GenerativeModel(model_name)
        return model.start_chat()
    except Exception as e:
        print(f"Error initializing the model: {e}")
        return None

# Main chat function
def chat_with_model(chat_instance):
    if not chat_instance:
        print("Chatbot initialization failed. Exiting...")
        return

    print("Chatbot is ready! Type 'bye' to exit.")
    while True:
        try:
            # User input
            user_message = input("You: ").strip()
            if not user_message:  # Skip empty input
                print("Chatbot: Please say something.")
                continue
            if user_message.lower() == "bye":  # Exit condition
                print("Chatbot: Goodbye!")
                break
            
            # Process input (Optional pre-processing step can be added here)
            
            # Get response from the chatbot
            response = chat_instance.send_message(user_message)
            print("Chatbot:", response.text)
        except Exception as e:
            print(f"Error during conversation: {e}")
            break

# Run the chatbot
if __name__ == "__main__":  # Corrected the condition
    chat_instance = initialize_chat()
    chat_with_model(chat_instance)
