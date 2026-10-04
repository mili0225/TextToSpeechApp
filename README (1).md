# Text-to-Speech Desktop Application

## 1. Project Objective

The objective of this project is to develop a Text-to-Speech Desktop Application using Python that converts user-entered text into audible speech.

## 2. Features

- Text input
- Text-to-speech conversion
- Voice type selection
- Speech speed selection
- Volume selection
- Play speech
- Pause speech
- Resume speech
- Stop speech
- Save audio as a WAV file
- Empty text validation

## 3. Technologies Used

- Python
- Tkinter
- pyttsx3
- Windows Speech API (SAPI)

## 4. Application Requirements

- Python 3.x
- Windows operating system
- Required Python packages:
  - pyttsx3
  - pywin32

## 5. Installation

Open PowerShell in the project folder and install the required packages:

```bash
python -m pip install pyttsx3 pywin32
```

## 6. How to Run

Run the main Python file:

```bash
python app.py
```

The application window will open.

## 7. How to Use

1. Enter text in the text box.
2. Select a voice from the Voice Type dropdown.
3. Adjust the Speech Speed.
4. Adjust the Volume.
5. Click **Play** to hear the speech.
6. Click **Pause** to pause the speech.
7. Click **Play** again to resume.
8. Click **Stop** to stop the speech.
9. Click **Save Audio** to save the speech as a WAV file.

## 8. Validation and Testing

The application was tested using:

- Empty text
- Short text
- Long text
- Different voices
- Different speech speeds
- Different volume levels
- Pause and resume
- Stop
- WAV audio saving

When the text box is empty, the application displays a warning asking the user to enter some text.

## 9. Project Structure

```text
TextToSpeechApp/
│
├── app.py
├── test_voice.py
└── Documentation/
    └── project_documentation.docx
```

## 10. Documentation

Detailed project documentation is provided in:

`Documentation/project_documentation.docx`

The documentation contains the objective, technologies, GUI, features, testing, debugging, usage instructions, and conclusion.

## 11. Note

This project is a Python desktop application built with Tkinter. Mobile responsiveness is therefore not applicable to the desktop GUI.

The current application does not require external API endpoints because the text-to-speech functionality is provided through the local Windows Speech API.
