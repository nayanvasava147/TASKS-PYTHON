import nltk
import spacy
from nltk.chat.util import Chat, reflections

nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me ChatBot.']),
    (r'what can you do?', ['I can answer your questions, provide information, and chat with you.']),
    (r'quit|bye|exit', ['Goodbye!', 'Bye!', 'Have a great day!']),
    (r'(.*) your name (.*)', ['I am a chatbot, you can call me ChatBot.']),
    (r'(.*) (age|old) (.*)', ['I am just a program, so I don\'t have an age.']),
    (r'(.*) (weather|temperature) (.*)', ['I am not connected to the internet, so I cannot provide weather information.']),
    (r'(.*) (thank you|thanks) (.*)', ['You\'re welcome!', 'No problem!', 'Glad to help!']),
    (r'(.*)', ['I am not sure I understand. Can you rephrase that?', 'Could you elaborate on that?'])
]

chatbot = Chat(patterns, reflections)

def chatbot_response(user_input):
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    tokens = [token.text for token in doc]
    response = chatbot.respond(user_input)
    return response

def chat():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'bye', 'exit']:
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()