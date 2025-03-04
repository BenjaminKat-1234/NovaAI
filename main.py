import time
import random
import os
import platform

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

greeting_list = ["Hello","Hola","Hi", "Howdy", "Are you kidding me", "Greetings", "Sup", "Yo", "Oi"]

jokes = [
    "What did one hat say to the other? You wait here, I'll go on ahead.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why couldn't the bicycle stand up by itself? It was two-tired.",
    "What did the fish say when it hit the wall? Dam!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look sad? Because it had too many problems.",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don’t eggs tell jokes? They might crack up.",
    "Why couldn't the leopard hide? Because he was always spotted.",
    "How does a penguin build its house? Igloos it together!",
    "Why do bees have sticky hair? Because they use honeycombs.",
    "What did the grape do when he got stepped on? Nothing, he just let out a little wine.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What did the janitor say when he jumped out of the closet? Supplies!",
    "Why don’t skeletons ever start a band? They don’t have the organs for it.",
    "What do you call an alligator in a vest? An investigator.",
    "Why did the cookie go to the doctor? Because he felt crummy.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "What did the left eye say to the right eye? Between you and me, something smells.",
    "Why did the coffee file a police report? It got mugged.",
    "How do you organize a space party? You planet.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why did the golfer bring an extra pair of socks? In case he got a hole in one.",
    "Why do bananas have to put on sunscreen? Because they peel.",
    "How do cows stay up to date? They read the moos-paper.",
    "What did the big flower say to the little flower? Hi, bud!",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "Why do ducks have feathers? To cover their butt-quacks.",
    "What does a nosy pepper do? Gets jalapeño business!",
    "Why did the computer go to the doctor? It had a virus.",
    "Why can’t you trust stairs? Because they’re always up to something.",
    "What do you call a pile of cats? A meowtain.",
    "Why don’t elephants use computers? They’re afraid of the mouse.",
    "How does a vampire start a letter? Tomb it may concern.",
    "Why don’t secret agents sleep? Because they’re always under cover.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the belt get arrested? It was holding up a pair of pants.",
    "What’s brown and sticky? A stick.",
    "Why did the clock get kicked out of class? It tocked too much.",
    "Why did the chicken go to the seance? To get to the other side.",
    "What do you call a dog that can do magic? A Labracadabrador.",
    "Why don’t mountains get tired? Because they peak.",
    "What did the fisherman say to the magician? Pick a cod, any cod.",
    "Why are ghosts bad liars? Because they are too transparent.",
    "How do you make holy water? You boil the hell out of it."
]

commands = [
    "Tell me a joke",
    "Tell me a dad joke"
]

def chat():
    message = input(f"{name}: ").lower()  # Convert to lowercase for case insensitivity

    if "!responses" == message:
        print(f"Nova: Try {random.choice(commands)}!")
        chat()

    elif "!clear" == message:
        cls()
        chat()

    elif "joke" in message:
        print(f"Nova: {random.choice(jokes)}")
        chat()

    elif any(char in message for char in "1234567890"):
        print(f"Nova: I'm bad with numbers.")
        chat()

    elif any(greeting.lower() in message for greeting in greeting_list):  # Adjusted to check against lowercase
        print(f"Nova: {random.choice(greeting_list)}")
        chat()

    else:
        print("Nova: I do not understand this. Try using !responses!")  # Proper indentation
        chat()


# Introduction
print("Nova: Hello there! I'm Nova! What is your name?")
name = input("Your name: ")
print(f"Nova: {random.choice(greeting_list)}, {name}! That's a great name!")
print("Launching Nova...")
time.sleep(3)
cls()
print(f"Nova: {random.choice(greeting_list)}, {name}! I'm Nova! Your personal Python AI! I can tell dad jokes, just chat with you, and more! Don't know where to start? Just say !responses for what I can do!")
chat()

