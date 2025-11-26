import random

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("YOU: ").lower()

        # GREETINGS
        if user_input in ["hi", "hello", "hey"]:
            responses = [
                "Hello! 😊",
                "Hi there! How can I help you?",
                "Hey! Nice to see you!",
                "Hi!.. What’s up?"
            ]
            print("Chatbot:", random.choice(responses))

        # HOW ARE YOU
        elif user_input == "how are you":
            responses = [
                "I'm doing great! Thanks!",
                "Feeling awesome today. You?",
                "Pretty good! How about you?",
                "All good here! What about you?"
            ]
            print("Chatbot:", random.choice(responses))

        # USER IS DOING FINE
        elif user_input in ["i am fine", "i'm fine", "fine"]:
            responses = [
                "Great to hear that!",
                "Nice! Keep it up!",
                "Awesome! 😊",
                "Glad you're doing well!"
            ]
            print("Chatbot:", random.choice(responses))

        # WHAT IS YOUR NAME
        elif user_input in ["what is your name", "your name", "who are you"]:
            responses = [
                "I’m ChatBot, your virtual friend!",
                "People call me ChatBot 🤖.",
                "I’m a simple rule-based chatbot!",
                "I'm ChatBot! Nice to meet you!"
            ]
            print("Chatbot:", random.choice(responses))

        # WHAT CAN YOU DO
        elif user_input in ["what can you do", "what do you do"]:
            responses = [
                "I can chat with you anytime!",
                "I answer your questions!",
                "I can help you learn programming.",
                "I talk, listen, and respond!"
            ]
            print("Chatbot:", random.choice(responses))

        # WHAT ARE YOU DOING
        elif user_input in ["what are you doing", "wyd"]:
            responses = [
                "Chatting with you right now!",
                "Just here to help 😊",
                "Talking to you!",
                "Waiting for your message."
            ]
            print("Chatbot:", random.choice(responses))

        # TELL A JOKE
        elif user_input in ["tell me a joke", "joke", "say a joke"]:
            responses = [
                "Why don’t programmers like nature? Too many bugs! 🤣",
                "Why was the computer cold? It forgot to close Windows!",
                "I told my computer a joke… it didn’t laugh… it had no sense of humor!",
                "Debugging: Removing the needles from the haystack 😂"
            ]
            print("Chatbot:", random.choice(responses))

        # THANK YOU
        elif user_input in ["thank you", "thanks", "thnx"]:
            responses = [
                "You're welcome!",
                "Glad I could help!",
                "Anytime! 😊",
                "No problem!"
            ]
            print("Chatbot:", random.choice(responses))

        # BYE
        elif user_input == "bye":
            responses = [
                "Goodbye! Take care! 👋",
                "Bye! See you soon!",
                "It was nice talking to you!",
                "See you again! 😊"
            ]
            print("Chatbot:", random.choice(responses))
            break

        # UNKNOWN INPUT
        else:
            print("Chatbot: Sorry, I didn't understand that 😅")

# Start chatbot
chatbot()
