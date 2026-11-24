import cowsay
import pyttsx3

engine = pyttsx3.init()

message = input("What should the cow say? ")

# Display the message using cowsay
cowsay.cow(message)

# Speak the same message
engine.say(message)
engine.runAndWait()