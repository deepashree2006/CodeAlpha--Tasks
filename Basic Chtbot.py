# 🟢 Basic Chatbot
# Goal: A simple chatbot that replies to user input using if-else conditions

print("Chatbot: Hi, I'm your friendly bot! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()  # take user input and convert it to lowercase

    # check user input and reply accordingly
    if user == "hello":
        print("Chatbot: Hello! How are you?")
    elif user == "how are you":
        print("Chatbot: I'm fine, thanks for asking!")
    elif user == "hi":
        print("Chatbot: Hi there!")
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break  # stop the loop
    else:
        print("Chatbot: Sorry, I didn’t understand that.")
