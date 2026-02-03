# Chatbot Tutorial: Learning from User Input

# Objective:
# This tutorial will guide you through building a simple
# decision-making chatbot in Python. The core concept we'll
# focus on is how the chatbot can *learn* from user
# input to adapt its responses over time.
# We'll use a dictionary to store learned associations
# between user phrases and chatbot responses.

# --- Chatbot Core Logic ---

# This dictionary will store the chatbot's knowledge.
# The keys will be user phrases (as lowercase strings for easier matching),
# and the values will be the chatbot's pre-programmed or learned responses.
# Initially, it contains a few default responses.
chatbot_knowledge = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm a program, so I don't have feelings, but I'm ready to assist!",
    "what is your name": "I am a simple learning chatbot.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!"
}

def get_response(user_input):
    # The purpose of this function is to find the best possible response
    # for the given user input.

    # Convert user input to lowercase for case-insensitive matching.
    # This makes it easier for the chatbot to recognize variations of the same phrase.
    # For example, "Hello" and "hello" should be treated the same.
    processed_input = user_input.lower()

    # First, check if we have a direct match in our knowledge base.
    # If a direct match is found, it's likely the most relevant response.
    if processed_input in chatbot_knowledge:
        return chatbot_knowledge[processed_input]

    # If no direct match is found, we can try to infer something or prompt the user.
    # For a simple learning chatbot, if we don't know, we ask the user to teach us.
    # This is where the "learning" aspect comes in.
    else:
        return None # Signal that we don't have a direct answer

def learn_response(user_input, bot_response):
    # This function is responsible for teaching the chatbot a new response.
    # It takes the user's original input and the desired bot response.

    # Convert user input to lowercase to store it consistently in our knowledge base.
    processed_input = user_input.lower()

    # Add or update the entry in the chatbot_knowledge dictionary.
    # If the user_input already exists, this will overwrite the old response
    # with the new one, allowing the bot to learn updated information.
    chatbot_knowledge[processed_input] = bot_response
    print(f"Thank you! I've learned that '{user_input}' should be answered with '{bot_response}'.")

# --- Chatbot Interaction Loop ---

def start_chatbot():
    # This function runs the main loop of the chatbot.
    print("Chatbot: Hello! Type 'quit' to exit.")

    while True:
        # Get input from the user.
        user_input = input("You: ")

        # Check if the user wants to quit.
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break # Exit the loop and end the program.

        # Get a response from the chatbot.
        response = get_response(user_input)

        # If the chatbot has a known response:
        if response:
            print(f"Chatbot: {response}")
        else:
            # If the chatbot doesn't know the answer, it prompts the user to teach it.
            print("Chatbot: I don't know how to respond to that. Can you teach me?")
            # Ask for the desired response from the user.
            new_response = input("Chatbot: What should I say instead? ")
            # Use the learn_response function to add this new knowledge.
            learn_response(user_input, new_response)

# --- Example Usage ---

# To start the chatbot, simply call the start_chatbot function.
# You can then interact with it in your terminal.
# Try typing different phrases and see how it responds.
# If it doesn't know, teach it! Then try typing the same phrase again.

if __name__ == "__main__":
    start_chatbot()

# Example of direct interaction with learning:
# You: hello
# Chatbot: Hi there! How can I help you today?
# You: how is the weather today
# Chatbot: I don't know how to respond to that. Can you teach me?
# Chatbot: What should I say instead? It's sunny and warm!
# Thank you! I've learned that 'how is the weather today' should be answered with 'It's sunny and warm!'.
# You: How is the weather today
# Chatbot: It's sunny and warm!
# You: bye
# Chatbot: Goodbye! Have a great day!