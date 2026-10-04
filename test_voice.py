import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()

print("Available voices:")

for i in range(voices.Count):
    print(i, voices.Item(i).GetDescription())

print("\nSpeaking David...")
speaker.Voice = voices.Item(0)
speaker.Speak("This is David.")

print("\nSpeaking Hazel...")
speaker.Voice = voices.Item(1)
speaker.Speak("This is Hazel.")

print("\nSpeaking Zira...")
speaker.Voice = voices.Item(2)
speaker.Speak("This is Zira.")

print("\nTest completed.")