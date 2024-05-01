import streamlit as st

def bot_response(user_input):
    # This is where you would implement your chatbot's response generation.
    # For now, it just echoes the user's input.
    return "You said: " + user_input

def main():
    st.title("Simple Chatbot")

    # Initialize an empty list to store the conversation.
    conversation = []

    user_input = st.text_input("You: ")

    if st.button("Send"):
        # Append the user's question to the conversation.
        conversation.append("You: " + user_input)

        # Get the bot's response and append it to the conversation.
        bot_reply = bot_response(user_input)
        conversation.append("Bot: " + bot_reply)

        # Display the conversation.
        for line in conversation:
            st.write(line)

if __name__ == "__main__":
    main()
