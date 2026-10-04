import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

for voice in voices:
    print(voice.name)

for voice in voices:
    if "Zira" in voice.name:
        print("\nTrying:", voice.name)

        engine.setProperty("voice", voice.id)

        print("After setting:")
        print(engine.getProperty("voice"))

        engine.setProperty("rate", 300)
        engine.setProperty("volume", 1.0)

        engine.say("This is the Zira voice test.")
        engine.runAndWait()
        break

engine.stop()