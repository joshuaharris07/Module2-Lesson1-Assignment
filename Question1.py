# Showcase Your Dance Moves!

# Task 1: Code Correction
# Below is a piece of Python code with incorrect indentation. Your task is to correct it.

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")
# The code following if and else statements must be indented.



# Task 2: Your Mood Today Ask the user how they feel today. 
# If they say "happy", print "That's great to hear!"
# If they say "sad", print "I hope your day gets better!". 
# Ensure your if statement is properly indented.

user_mood = input("How do you feel today? (happy/sad) ").lower()
# Converted the answer to lower case to avoid issues with if/elif statements.

if user_mood == "happy":
    print("That's great to hear!")
elif user_mood == "sad":
    print("I hope your day gets better!")
else:
    print("Good luck sorting out that feeling!")