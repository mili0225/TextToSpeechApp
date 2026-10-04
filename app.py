import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyttsx3
import win32com.client
import threading


# pyttsx3 included as required
engine = pyttsx3.init()
engine.stop()


# SAPI speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()

is_speaking = False
is_paused = False


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Text-to-Speech Desktop App")
root.geometry("600x650")
root.resizable(False, False)


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="Text-to-Speech Desktop App",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)


# -----------------------------
# Text Input
# -----------------------------
text_label = tk.Label(
    root,
    text="Enter text to convert into speech:",
    font=("Arial", 11)
)
text_label.pack(pady=5)

text_input = tk.Text(
    root,
    height=10,
    width=60,
    font=("Arial", 11),
    wrap="word"
)
text_input.pack(padx=20, pady=5)


# -----------------------------
# Voice Type
# -----------------------------
voice_label = tk.Label(
    root,
    text="Voice Type:",
    font=("Arial", 11)
)
voice_label.pack(pady=(10, 5))

voice_names = []

for i in range(voices.Count):
    voice_names.append(
        voices.Item(i).GetDescription()
    )

voice_dropdown = ttk.Combobox(
    root,
    values=voice_names,
    state="readonly",
    width=45
)
voice_dropdown.pack()

if voice_names:
    voice_dropdown.current(0)


# -----------------------------
# Speech Speed
# -----------------------------
speed_label = tk.Label(
    root,
    text="Speech Speed:",
    font=("Arial", 11)
)
speed_label.pack(pady=(15, 5))

speed_var = tk.IntVar(value=0)

speed_scale = tk.Scale(
    root,
    from_=-10,
    to=10,
    orient="horizontal",
    variable=speed_var,
    length=300
)
speed_scale.pack()


# -----------------------------
# Volume
# -----------------------------
volume_label = tk.Label(
    root,
    text="Volume:",
    font=("Arial", 11)
)
volume_label.pack(pady=(15, 5))

volume_var = tk.IntVar(value=100)

volume_scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=volume_var,
    length=300
)
volume_scale.pack()


# -----------------------------
# Speak
# -----------------------------
def speak(text):

    global is_speaking
    global is_paused

    is_speaking = True
    is_paused = False

    selected_voice = voice_dropdown.current()

    if selected_voice >= 0:
        speaker.Voice = voices.Item(selected_voice)

    speaker.Rate = speed_var.get()
    speaker.Volume = volume_var.get()

    speaker.Speak(text)

    is_speaking = False
    is_paused = False


# -----------------------------
# Play / Resume
# -----------------------------
def play_speech():

    global is_paused
    global is_speaking

    # Resume paused speech
    if is_paused:
        speaker.Resume()
        is_paused = False
        return

    # Do not start another speech
    if is_speaking:
        return

    text = text_input.get(
        "1.0",
        "end-1c"
    ).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    thread = threading.Thread(
        target=speak,
        args=(text,),
        daemon=True
    )

    thread.start()


# -----------------------------
# Pause
# -----------------------------
def pause_speech():

    global is_paused

    if is_speaking and not is_paused:
        speaker.Pause()
        is_paused = True


# -----------------------------
# Stop
# -----------------------------
def stop_speech():

    global is_speaking
    global is_paused

    if is_speaking or is_paused:
        speaker.Skip("Sentence", 999999)

    is_speaking = False
    is_paused = False


# -----------------------------
# Save Audio
# -----------------------------
def save_audio():

    text = text_input.get(
        "1.0",
        "end-1c"
    ).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[
            ("WAV Audio", "*.wav")
        ]
    )

    if not file_path:
        return

    selected_voice = voice_dropdown.current()

    save_speaker = win32com.client.Dispatch(
        "SAPI.SpVoice"
    )

    save_voices = save_speaker.GetVoices()

    if selected_voice >= 0:
        save_speaker.Voice = save_voices.Item(
            selected_voice
        )

    save_speaker.Rate = speed_var.get()
    save_speaker.Volume = volume_var.get()

    stream = win32com.client.Dispatch(
        "SAPI.SpFileStream"
    )

    stream.Open(
        file_path,
        3,
        False
    )

    save_speaker.AudioOutputStream = stream

    save_speaker.Speak(text)

    stream.Close()

    save_speaker.AudioOutputStream = None

    messagebox.showinfo(
        "Saved",
        "Audio saved successfully."
    )


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=20)


play_button = tk.Button(
    button_frame,
    text="Play",
    width=12,
    height=2,
    command=play_speech
)
play_button.grid(
    row=0,
    column=0,
    padx=5
)


pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=12,
    height=2,
    command=pause_speech
)
pause_button.grid(
    row=0,
    column=1,
    padx=5
)


stop_button = tk.Button(
    button_frame,
    text="Stop",
    width=12,
    height=2,
    command=stop_speech
)
stop_button.grid(
    row=0,
    column=2,
    padx=5
)


save_button = tk.Button(
    root,
    text="Save Audio",
    width=18,
    height=2,
    command=save_audio
)
save_button.pack(pady=5)


# -----------------------------
# Start Application
# -----------------------------
root.mainloop()