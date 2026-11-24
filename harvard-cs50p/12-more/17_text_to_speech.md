# Python Text-to-Speech (TTS)

Text-to-Speech (TTS) converts written text into spoken audio.

Python provides packages such as `pyttsx3` that allow applications to read text aloud.

## 1. Install pyttsx3

```bash
pip install pyttsx3
```

`pyttsx3` is an offline text-to-speech library.

## 2. Basic Text-to-Speech Example

```python
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello! Welcome to Python programming.")

engine.runAndWait()
```

**Explanation:**
- `import pyttsx3`: Imports the text-to-speech library.
- `pyttsx3.init()`: Initializes the speech engine.
- `engine.say()`: Adds text to be spoken.
- `engine.runAndWait()`: Processes the speech and waits until it finishes.

## 3. Customize Voice Speed and Volume

```python
import pyttsx3

engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 150)

# Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)

engine.say("Generators produce values one at a time.")
engine.runAndWait()
```

## 4. Save Speech to an Audio File

```python
import pyttsx3

engine = pyttsx3.init()

engine.save_to_file(
    "Hello! This is Python text to speech.",
    "speech.mp3"
)

engine.runAndWait()
```

**Note:** The supported audio format and file extension depend on the speech engine and operating system. MP3 output is not guaranteed on every system.

## 5. Useful Methods

| Method | Purpose |
|---|---|
| `pyttsx3.init()` | Initializes the speech engine |
| `engine.say()` | Adds text to speak |
| `engine.runAndWait()` | Processes the speech |
| `engine.setProperty()` | Changes voice, speed, or volume |
| `engine.save_to_file()` | Saves speech to an audio file |

## 6. Real-World Applications

- Accessibility tools for people with visual impairments.
- Reading documents and articles aloud.
- Voice assistants.
- Educational applications.
- Automated announcements.

## Key Takeaways

- TTS stands for Text-to-Speech.
- `pyttsx3` is a Python library for offline speech generation.
- `say()` converts text into spoken output.
- `runAndWait()` executes the speech.
- Voice speed and volume can be customized.