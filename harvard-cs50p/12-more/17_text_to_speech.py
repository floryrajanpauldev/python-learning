import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Get text from user
text = input("Enter something for me to say: ")

# Configure speech
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# Speak the text
engine.say(text)
engine.runAndWait()

