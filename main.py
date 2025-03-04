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

story = [
    "A scientist built a machine to peer into parallel universes. At first, he saw versions of himself living different lives—some happier, some tragic. But then he noticed a pattern: every version of himself was being watched by a shadowy figure in the background. One night, his machine flickered, and instead of another universe, he saw his own room from a different angle. The screen turned black, and a message appeared: 'We see you too.' The machine short-circuited, and his door creaked open on its own. Heart pounding, he grabbed a wrench and backed away. A whisper echoed from the darkness: 'You shouldn’t have looked.' His phone buzzed—an email from himself, dated tomorrow. The subject line: 'RUN.' But before he could move, the machine turned back on by itself, showing a live feed of his room—except he wasn’t in it anymore.",

    "A man inherited an old pocket watch that didn’t tell time—it counted down. At first, he ignored it, thinking it broken. But when it reached zero, a stranger knocked on his door, delivering news that changed his life. He tested the watch again, setting it manually. Every time it hit zero, something significant happened: a car crash, a job offer, a phone call from an old friend. One day, he woke up to see the numbers impossibly high, ticking down rapidly. Panicked, he tried to stop it, but the hands wouldn’t budge. The countdown hit ten… nine… eight. The sky outside darkened. People froze mid-step. The world itself seemed to hold its breath. At zero, everything went silent. The watch fell from his hand, shattering. When he opened his eyes, he was the only person left. Buildings stood empty. Streets were abandoned. The only sound was ticking—coming from inside his own chest.",

    "A woman moved into an apartment with a single, locked door that the landlord said led to nothing. At night, she could hear soft whispers and occasional tapping from the other side. One evening, she pressed her ear against it and whispered, 'Hello?' The tapping stopped. Hours later, she awoke to find the door wide open, revealing a dark hallway that shouldn’t exist. A single candle burned in the distance. She stepped forward, heart pounding, and the door slammed shut behind her. The hallway stretched endlessly in both directions. Doors lined the walls, each with her name etched into them. One creaked open, revealing her bedroom—but inside, she saw herself asleep in bed. A figure stood over her sleeping body, whispering something in her ear. It turned, smiling at her with her own face. 'You shouldn't be here,' it said. The candle flickered out, and the darkness swallowed her whole.",

    "A little boy found an old Polaroid camera at a yard sale. When he took a picture, the image showed not the present, but what would happen five minutes in the future. At first, it was fun—he predicted his mother’s phone calls, saw his dog running in the yard. But then he took a photo of his bedroom and saw his closet door open, revealing a shadowy figure. He stared at the picture in horror, slowly turning toward the closet. The door creaked open, exactly as in the photo. Something was waiting inside. He ran to his parents, but when they returned, the closet was empty. That night, he placed the camera beside his bed and set it on a timer. In the morning, he checked the photo. It showed him sleeping peacefully—until a long, pale hand reached from under his bed, wrapping around his ankle. He dropped the camera and felt something brush against his foot.",

    "A deep-sea diver discovered an ancient shipwreck untouched by time. The wood was unrotted, the lanterns still lit, as if the crew had only just left. But when he swam inside, he found tables set for a meal, clothes laid out for bed, and a journal open to the last entry: 'We are not alone. It watches from below.' The ship creaked, and outside, a massive shadow passed overhead. The water turned black, and the diver’s flashlight flickered out. A low hum vibrated through the ocean. Desperate, he swam toward the exit, but the ship had changed. The corridors stretched endlessly, leading him deeper inside. He turned a corner and found himself staring at a wall of glass. On the other side was his reflection—but it blinked before he did. The glass shattered, water rushed in, and the last thing he saw was his own face smiling at him as everything went dark.",

    "A girl discovered that her reflection lagged behind her movements. At first, it was only by a fraction of a second, but as days passed, the delay grew. One night, her reflection stopped mimicking her altogether, staring at her with a cold, knowing smile. Terrified, she covered the mirror. The next morning, it was shattered, and written on the wall in her own handwriting were the words: 'I am free now.' She turned to see her reflection standing outside her window, staring in with empty eyes. Panicked, she ran downstairs, but every reflective surface now showed her reflection moving freely. In the bathroom mirror, it whispered, 'It’s your turn now.' A cold hand gripped her shoulder. The world spun, and when she blinked, she was in the mirror. Outside, her reflection—now in control—smirked and turned away, leaving her trapped in the glass, screaming silently.",

    "A man’s dog started barking at the basement door every night at exactly 3:13 AM. Thinking it was mice, he set up a camera. The footage showed the door slowly creaking open on its own, though the basement was locked. One night, he heard scratching from below and called a locksmith to remove the rusted lock. As soon as it clicked open, a horrible wailing filled the house. The basement light flickered, revealing dozens of claw marks covering the walls. Something had been trying to get out. Or in. The dog whimpered and backed away as shadows stretched toward them. The man slammed the door shut, heart pounding. But when he checked the footage later, he saw himself opening the door—except he never did. The final frame showed him sleeping peacefully in bed, while the basement door, wide open, led to complete darkness. Something had come upstairs."
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

    elif "story" in message:
        print(f"Nova: Heres a short story for you!\n{random.choice(story)}")
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
