from data import get_response
 
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.\n")
 
    while True:
        user = input("You:")
 
        if user.lower() == "bye":
            print("Chatbot: Goodbye")
            break
 
        response = get_response(user)
        print("Chatbot:", response)
 
chatbot()