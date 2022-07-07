from cgi import print_arguments


print("Welcome to my quiz!")
playing = input("Do you want to play?" )
if playing != "yes":
    quit()
print("Okay! Lets play!")
score = 0
answer = input("Where is the capital of Italy? ")
if answer == "Rome":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
answer = input("Where is the capital of Norway? ")
if answer == "Oslo":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
answer = input("Where is the capital of Japan? ")
if answer == "Tokyo":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
answer = input("Where is the capital of France? ")
if answer == "Paris":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
