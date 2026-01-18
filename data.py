import random
 
qa = {
    "hi": ["Hello!", "Hi there!", "Hey "],
    "hello": ["Hello!", "Hi!", "Hey "],
    "how are you": ["I'm good!", "Doing great!", "All good "],
    "what is your name": ["I'm a Python Chatbot "],
    "who created you": ["I was created using Python."],
    "what can you do": ["I can answer common questions."],
    "bye": ["Goodbye ", "See you soon!", "Take care!"],
    "thank you": ["You're welcome ", "Anytime!", "Glad to help!"],
    "what is python": ["Python is a programming language."],
    "what is ai": ["AI means Artificial Intelligence."],
    "what is machine learning": ["Machine Learning learns from data."],
    "what is your purpose": ["To help and chat with you."],
    "where are you from": ["I live inside your computer "],
    "are you human": ["No, I'm a bot "],
    "do you sleep": ["Bots never sleep "],
    "what is coding": ["Coding means writing instructions."],
    "what is selenium": ["Selenium is used for browser automation."],
    "what is automation": ["Automation does tasks automatically."],
    "what is database": ["Database stores data."],
    "what is sql": ["SQL manages databases."],
    "what is flask": ["Flask is a Python web framework."],
    "what is django": ["Django is a Python framework."],
    "what is api": ["API connects applications."],
    "what is json": ["JSON is a data format."],
    "what is loop": ["Loop repeats tasks."],
    "what is function": ["Function is reusable code."],
    "what is class": ["Class is a blueprint."],
    "what is object": ["Object is instance of class."],
    "what is inheritance": ["Inheritance reuses code."],
    "what is polymorphism": ["Same method, different behavior."],
    "what is encapsulation": ["Data hiding concept."],
    "what is exception": ["Error during execution."],
    "what is debugging": ["Fixing bugs."],
    "what is github": ["GitHub hosts code."],
    "what is cloud": ["Cloud provides online services."],
    "what is linux": ["Linux is an OS."],
    "what is windows": ["Windows is an OS by Microsoft."],
    "what is browser": ["Browser accesses websites."],
    "what is internet": ["Internet connects computers."],
    "what is html": ["HTML builds web pages."],
    "what is css": ["CSS styles web pages."],
    "what is javascript": ["JavaScript adds interaction."],
    "what is data": ["Data is information."],
    "what is chatbot": ["Chatbot talks like humans."],
    "tell me a joke": ["Why do programmers hate bugs? Because they cause errors "],
    "default": ["Sorry, I didn't understand "]
}
 
def get_response(user_input):
    user_input = user_input.lower()
    for question in qa:
        if question in user_input:
            return random.choice(qa[question])
    return random.choice(qa["default"])