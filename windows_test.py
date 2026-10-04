import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

voices = speaker.GetVoices()

print("Number of voices:", voices.Count)

# Test David
print("Speaking with David - slow")
speaker.Voice = voices.Item(0)
speaker.Rate = -8
speaker.Volume = 100
speaker.Speak("This is Microsoft David speaking slowly.")

# Test Zira
print("Speaking with Zira - fast")
speaker.Voice = voices.Item(2)
speaker.Rate = 8
speaker.Volume = 100
speaker.Speak("This is Microsoft Zira speaking quickly.")

print("Test completed.")