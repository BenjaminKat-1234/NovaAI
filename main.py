import time
import random
import os
import platform
import sys

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
    "Tell me a dad joke",
    "Tell me a story",
    "Generate a story"
]

story = [
    "A scientist built a machine to peer into parallel universes. At first, he saw versions of himself living different lives—some happier, some tragic. But then he noticed a pattern: every version of himself was being watched by a shadowy figure in the background. One night, his machine flickered, and instead of another universe, he saw his own room from a different angle. The screen turned black, and a message appeared: 'We see you too.' The machine short-circuited, and his door creaked open on its own. Heart pounding, he grabbed a wrench and backed away. A whisper echoed from the darkness: 'You shouldn’t have looked.' His phone buzzed—an email from himself, dated tomorrow. The subject line: 'RUN.' But before he could move, the machine turned back on by itself, showing a live feed of his room—except he wasn’t in it anymore.",

    "A man inherited an old pocket watch that didn’t tell time—it counted down. At first, he ignored it, thinking it broken. But when it reached zero, a stranger knocked on his door, delivering news that changed his life. He tested the watch again, setting it manually. Every time it hit zero, something significant happened: a car crash, a job offer, a phone call from an old friend. One day, he woke up to see the numbers impossibly high, ticking down rapidly. Panicked, he tried to stop it, but the hands wouldn’t budge. The countdown hit ten… nine… eight. The sky outside darkened. People froze mid-step. The world itself seemed to hold its breath. At zero, everything went silent. The watch fell from his hand, shattering. When he opened his eyes, he was the only person left. Buildings stood empty. Streets were abandoned. The only sound was ticking—coming from inside his own chest.",

    "A woman moved into an apartment with a single, locked door that the landlord said led to nothing. At night, she could hear soft whispers and occasional tapping from the other side. One evening, she pressed her ear against it and whispered, 'Hello?' The tapping stopped. Hours later, she awoke to find the door wide open, revealing a dark hallway that shouldn’t exist. A single candle burned in the distance. She stepped forward, heart pounding, and the door slammed shut behind her. The hallway stretched endlessly in both directions. Doors lined the walls, each with her name etched into them. One creaked open, revealing her bedroom—but inside, she saw herself asleep in bed. A figure stood over her sleeping body, whispering something in her ear. It turned, smiling at her with her own face. 'You shouldn't be here,' it said. The candle flickered out, and the darkness swallowed her whole.",

    "A little boy found an old Polaroid camera at a yard sale. When he took a picture, the image showed not the present, but what would happen five minutes in the future. At first, it was fun—he predicted his mother’s phone calls, saw his dog running in the yard. But then he took a photo of his bedroom and saw his closet door open, revealing a shadowy figure. He stared at the picture in horror, slowly turning toward the closet. The door creaked open, exactly as in the photo. Something was waiting inside. He ran to his parents, but when they returned, the closet was empty. That night, he placed the camera beside his bed and set it on a timer. In the morning, he checked the photo. It showed him sleeping peacefully—until a long, pale hand reached from under his bed, wrapping around his ankle. He dropped the camera and felt something brush against his foot.",

    "A deep-sea diver discovered an ancient shipwreck untouched by time. The wood was unrotted, the lanterns still lit, as if the crew had only just left. But when he swam inside, he found tables set for a meal, clothes laid out for bed, and a journal open to the last entry: 'We are not alone. It watches from below.' The ship creaked, and outside, a massive shadow passed overhead. The water turned black, and the diver’s flashlight flickered out. A low hum vibrated through the ocean. Desperate, he swam toward the exit, but the ship had changed. The corridors stretched endlessly, leading him deeper inside. He turned a corner and found himself staring at a wall of glass. On the other side was his reflection—but it blinked before he did. The glass shattered, water rushed in, and the last thing he saw was his own face smiling at him as everything went dark.",

    "A girl discovered that her reflection lagged behind her movements. At first, it was only by a fraction of a second, but as days passed, the delay grew. One night, her reflection stopped mimicking her altogether, staring at her with a cold, knowing smile. Terrified, she covered the mirror. The next morning, it was shattered, and written on the wall in her own handwriting were the words: 'I am free now.' She turned to see her reflection standing outside her window, staring in with empty eyes. Panicked, she ran downstairs, but every reflective surface now showed her reflection moving freely. In the bathroom mirror, it whispered, 'It’s your turn now.' A cold hand gripped her shoulder. The world spun, and when she blinked, she was in the mirror. Outside, her reflection—now in control—smirked and turned away, leaving her trapped in the glass, screaming silently.",

    "A man’s dog started barking at the basement door every night at exactly 3:13 AM. Thinking it was mice, he set up a camera. The footage showed the door slowly creaking open on its own, though the basement was locked. One night, he heard scratching from below and called a locksmith to remove the rusted lock. As soon as it clicked open, a horrible wailing filled the house. The basement light flickered, revealing dozens of claw marks covering the walls. Something had been trying to get out. Or in. The dog whimpered and backed away as shadows stretched toward them. The man slammed the door shut, heart pounding. But when he checked the footage later, he saw himself opening the door—except he never did. The final frame showed him sleeping peacefully in bed, while the basement door, wide open, led to complete darkness. Something had come upstairs."

    "A woman came home one evening to find her dog sitting at the front door, staring at her with wide eyes. She called out, but the dog didn't move. When she opened the door, she was hit with an overwhelming wave of cold air. Inside, her house was completely empty, no furniture, no belongings—just cold, empty walls. She quickly checked the rooms, but all she found was the dog. In the corner of the living room, a small, bloodstained note sat on the floor: 'It’s waiting for you in the basement.' Heart pounding, she rushed downstairs, but when she reached the basement door, she hesitated. The dog barked, but its voice had an unsettling, unnatural tone. She slowly opened the door, and then... nothing. The basement was empty. But when she turned to leave, the sound of breathing echoed behind her, far too close for comfort.",

    "A man received a letter with no return address, simply stating: 'The person you are searching for is behind you.' He looked around, but no one was there. Just as he began to shrug it off, he turned and froze in place. Standing in his reflection in a nearby window was his missing sister, a cold grin on her face. He rushed home, hoping it was a cruel joke, but when he opened the door, his sister's voice called out from inside, 'I’ve been waiting for you to come back.' He turned, heart racing, only to find the empty street behind him. But when he turned back to the door, he saw her standing inside, beckoning him. Without thinking, he rushed inside, but when he turned the handle, his sister’s reflection grinned back at him from the mirror.",

    "A family moved into a new house, but every night they heard whispers from the walls. They thought it was the house settling at first, but the whispers grew louder each evening, and sometimes they could make out words: 'She’s here.' One night, the family stayed up late to investigate. They followed the whispers to a small, hidden door in the attic. Inside, they found an old wooden box covered in dust. When they opened it, they discovered a faded photograph of a woman with hollow eyes. Just as they pulled it out, the whispers stopped. The room grew colder, and the lights flickered. Suddenly, a voice echoed through the house, 'She knows you found her.' A cold hand brushed against the father’s shoulder, and when he turned, no one was there.",

    "A teenager found an old Ouija board in her grandmother’s attic. When she laid it out and began to ask questions, the planchette moved on its own, spelling out cryptic messages. 'I am here.' 'You will never leave.' The teen laughed it off as a trick, but when she asked one final question—'Who is with me?'—the planchette moved violently to 'GOODBYE.' The lights flickered and then went out entirely. In the dark, the teenager felt cold hands grab her arms, dragging her to the floor. When the lights returned, she was in the same attic, but the board was gone. She stood, trembling, and found her grandmother standing behind her. 'I told you not to play with that.' Her grandmother’s face was expressionless, but when she stepped closer, her voice was no longer her own. 'Now you belong to her.'",

    "A man woke up one morning to find his reflection still sleeping in his bed. At first, he thought it was a trick of the light, but when he touched the mirror, the reflection didn’t react. Confused, he began to speak to it, but it stayed completely still. He grew frantic, trying to wake the reflection, but nothing worked. When he finally reached out to grab it, his own body moved without him, dragging him across the floor to the mirror. The reflection smiled and whispered, 'It’s your turn now.' Before he could react, his reflection reached out, pulling him into the glass. The man’s real body was left standing alone, staring blankly at the mirror, where only the reflection of a terrified man remained.",

    "A woman checked into a hotel late one night, exhausted from her travels. As she unpacked, she noticed an old painting hanging on the wall. It depicted a family seated around a table, but one figure stood in the background—an eerie man with hollow eyes. She dismissed it as a strange piece of art. But every time she passed it, the figure’s eyes seemed to follow her. When she woke up the next morning, the painting was gone, and there was a note in its place: 'It’s your turn now.' Panicked, she checked out of the hotel, but as she left, she passed the front desk. The receptionist smiled and waved goodbye, revealing the same hollow eyes from the painting.",

    "A couple rented a cabin in the woods for a weekend getaway, hoping for peace and quiet. On the second night, they heard strange noises outside—scratching sounds followed by a low growl. The husband went out to investigate, but when he returned, he looked different, colder. The wife thought he was just frightened, but something wasn’t right. That night, she woke up to find her husband staring at her with glowing eyes. His voice was no longer his own, as he whispered, 'It’s too late to leave now.' She screamed, but he was already standing by the window, watching something move in the shadows outside. When she reached the door to escape, he blocked her way, and in the reflection of the glass, she saw the true form of the creature he had become.",

    "A young woman received an unexpected call from her childhood friend, who she hadn’t spoken to in years. Her friend seemed desperate, saying, 'You have to get out. It’s coming for you. It’s been watching you for years.' The woman was confused but dismissed it as a joke. That night, she heard scratching at her window. She opened it, thinking it was a tree branch, but nothing was there. Later, her phone rang again. It was her friend, screaming. 'It’s here!' The call ended abruptly. Panicked, she tried calling back, but the number was disconnected. The next morning, the woman went to her friend's house and found it completely abandoned. The only thing left was a note on the door: 'It’s already here.'",

    "A man moved into a new house, and everything seemed perfect—except for one thing. Every night, he heard footsteps pacing the hallway outside his room. He checked every night, but there was no one there. One evening, he decided to stay awake and confront whatever it was. As the footsteps grew closer, the man felt a sudden chill and turned to see a shadowy figure standing in the doorway. It didn’t move, but it watched him with glowing red eyes. He tried to scream, but his voice caught in his throat. The figure stepped forward, and the man finally managed to shout—only to hear the same scream echo from the hallway outside. He ran, but the footsteps followed him, growing louder and closer, until they surrounded him."

    "The old mansion at the end of the street had been abandoned for years. Yet, every night, a light flickered in the upstairs window. Curious, I ventured into the house one evening. The door creaked open with a force that made my heart race. Inside, the house was freezing cold, and the air was thick with dust. As I moved through the rooms, I heard footsteps behind me. Turning quickly, I saw nothing but shadows. Then, I heard it—a whisper, faint and distant. 'Leave now,' it said. I turned to flee, but the door slammed shut, trapping me inside. My pulse raced as I desperately searched for another exit. But then, I saw it—a figure standing in the hallway, just at the edge of my vision. I tried to scream, but my voice failed me. The figure stepped forward, revealing its twisted, decayed face. The last thing I remember was the cold touch on my shoulder before everything went dark.",
    
    "I had always believed in the supernatural, but I never thought I would experience it firsthand. It all started one stormy night when I was home alone. The wind howled outside, rattling the windows, and the power went out, plunging the house into darkness. I fumbled for a flashlight and made my way through the house. That's when I heard it—soft, muffled whispers coming from the attic. I was terrified, but my curiosity got the better of me. I climbed the stairs to the attic, and as I reached the top, I felt a chill run down my spine. The whispers grew louder. I shined my flashlight around the room, but all I saw was old furniture and dusty boxes. Then, out of the corner of my eye, I saw something move. It was a figure, faint but unmistakably human, standing by the window. I froze in terror, unable to move as the figure slowly turned to face me. It smiled, but the smile wasn’t right—it was twisted, mocking. Suddenly, the whispers stopped, and the figure was gone. I never went back to that attic again.",
    
    "It was a quiet night in the small town of Willow Creek. I had just finished dinner when I noticed a strange figure standing at the edge of my property. The figure was tall, cloaked in shadow, and unmoving. I thought it was just a trick of the light, but as I watched, the figure began to move slowly toward my house. My heart raced as I backed away from the window, uncertain of what to do. I grabbed my phone to call the police, but my hands were shaking too much to dial. The figure was now standing directly outside my window, staring at me with unblinking eyes. I could hear its breath, slow and steady, like a whisper in the night. Suddenly, the lights flickered, and the figure vanished. I ran to the door to check, but there was no one there. Just the wind. I never saw the figure again, but I could never shake the feeling that it was watching me, waiting for me to let my guard down.",
    
    "The call came at 3 AM, the one time of night when the world is still and quiet. The voice on the other end was familiar, yet I couldn’t place it. 'Help me,' it whispered, barely audible. I froze, unable to speak. The voice repeated, 'Help me,' more urgent this time. I scrambled to ask who it was, but the line went dead. A chill ran down my spine, and I tried to shake off the dread creeping into my thoughts. But then the phone rang again. I hesitated before answering, hoping it was just a prank. 'You can’t help me,' the voice said, 'I’m already here.' My blood ran cold. I looked around the room, expecting to see someone, but there was no one. The voice continued, 'Look behind you.' I turned slowly, my heart pounding in my chest. But all I saw was my reflection in the window. I had no idea what I had just experienced, but it was enough to make me question the reality I thought I knew.",
    
    "I found the old book in the back corner of the library, covered in dust and forgotten by time. It was an ancient tome, its leather cover cracked and worn. I opened it carefully, not sure what to expect. The pages were filled with strange symbols and ancient writing I didn’t recognize. As I flipped through the pages, one word stood out—'AWAKE.' It was written in red ink, as if it had been freshly penned. My fingers trembled as I traced the word, and suddenly, the room grew colder. A voice whispered from somewhere behind me, but when I turned, there was no one there. I slammed the book shut, but the whispering grew louder, more insistent. The lights flickered, and I could hear footsteps echoing in the hallway, though I was alone in the library. I rushed to the door, but it wouldn’t open. The air became thick, suffocating. I finally managed to escape, but the whispering followed me. I haven’t opened that book since, but I know it’s still out there, waiting for me to return.",
    
    "I had just moved into the old farmhouse on the outskirts of town. It was isolated, surrounded by fields and dense woods, perfect for a fresh start. But from the moment I stepped inside, something felt off. The house was eerily quiet, and there was a strange, musty smell in the air. That night, as I lay in bed, I heard scratching noises coming from the walls. I tried to ignore it, thinking it was just the house settling, but the noises grew louder, more frantic. I got up to investigate, but found nothing. The next night, the noises returned, this time accompanied by soft, hushed voices. I could hear someone whispering, but I couldn’t make out the words. I followed the sound to the basement door, which had been locked when I moved in. The door creaked open, and I descended into the darkness. The whispers grew louder, almost deafening. Suddenly, a cold hand grabbed my arm. I turned, but there was no one there. The whispers stopped, and I fled, never to return to that house again.",
    
    "I was alone in the house that evening, curled up on the couch watching a movie. My dog, Max, was curled up at my feet, and all was peaceful. But then, a soft knocking came from the front door. I wasn’t expecting anyone, and Max growled softly at the sound. I hesitated, unsure if I should open the door. But the knocking continued, more insistent this time. I slowly got up and walked to the door, peeking through the peephole. To my surprise, I saw no one there. I opened the door cautiously, but there was no one on the porch. I closed the door and locked it again, but the knocking resumed, this time from the back door. I rushed to the kitchen, but when I looked out the window, there was still no one there. The knocking continued from all sides of the house, louder and more frantic, as if something was trying to get in. I grabbed Max and ran out the back door, never looking back.",
    
    "I had always enjoyed walking through the old cemetery near my house, finding peace among the ancient gravestones. But that day, something was different. The air was thick with fog, and the ground felt damp beneath my feet. As I wandered deeper into the cemetery, I noticed something strange—one of the graves had been disturbed. The earth was freshly dug, and the tombstone was cracked. I knelt down to inspect it, but as I did, I heard a low moan from behind me. I spun around, but no one was there. The air grew colder, and I felt a chill run down my spine. Then, I saw it—a figure standing by one of the other gravestones, watching me. It was tall, cloaked in shadow, and its face was hidden. I tried to move, but my legs wouldn’t respond. The figure took a step closer, and I could hear its breath, slow and steady. It whispered my name. I turned and ran, but the figure followed, its footsteps echoing in the mist.",
    
    "I thought I was alone in the house, but as I stepped into the living room, I heard someone call my name. I froze, my heart racing. It was my voice, but it came from the kitchen. I walked slowly toward the sound, but when I entered the kitchen, no one was there. The room was empty. I checked the rest of the house, but everything was as it should be. Yet, I couldn’t shake the feeling that I was being watched. I sat down on the couch, trying to calm myself, but then I heard it again—'Come closer.' This time, it was louder, clearer. I looked around, but there was no one in the room with me. My pulse quickened, and I stood up to leave, but the door slammed shut. The voice continued, now in a mocking tone. 'You can’t leave.' I struggled with the door, but it wouldn’t budge. Suddenly, everything went silent. The door opened on its own, and I ran out, vowing never to return to that house."
]

banned_words = ["Murder", "Kill", "Die"]


def chat():
    message = input(f"{name}: ").lower()

    if "!responses" == message:
        print(f"Nova: Try {random.choice(commands)}!")
        chat()
    
    elif "Nova".lower() in message:
        print(f"Nova: {random.choice(greeting_list)}, {name} ^_^")
        chat()

    elif "!clear" == message:
        cls()
        chat()
    
    if any(banned_word.lower() in message.lower() for banned_word in banned_words):
        print("System: YOUR MESSAGE HAS BEEN BLOCKED FOR CONTAINING A BANNED WORD!")
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
    
    

    elif any(greeting.lower() in message for greeting in greeting_list):
        print(f"Nova: {random.choice(greeting_list)}")
        chat()

    else:
        print("Nova: I do not understand this. Try using !responses!")


# Introduction
print("Nova: Hello there! I'm Nova! What is your name?")
name = input("Your name: ")
if name.lower() == "nova":
    name = "Fake Nova"
print(f"Nova: {random.choice(greeting_list)}, {name}! That's a great name!")
print("Launching Nova...")
time.sleep(3)
cls()
print(f"Nova: {random.choice(greeting_list)}, {name}! I'm Nova! Your personal Python AI! I can tell dad jokes, just chat with you, and more! Don't know where to start? Just say !responses for what I can do!")
chat()

