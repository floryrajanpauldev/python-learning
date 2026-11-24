
import pyttsx3

engine = pyttsx3.init()

messages = [
    "Good morning!",
    "Welcome to Python.",
    "Let's learn something new today."
]

for message in messages:
    engine.say(message)

engine.runAndWait()