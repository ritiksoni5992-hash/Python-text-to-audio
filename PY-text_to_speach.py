import pyttsx3
engine = pyttsx3.init()

# text file name
text_file="Add-Text-File"

# Audio file to save speach
audio_file="PY-Audio.mp3"


# Read text file
with open(text_file, "r",encoding="utf-8") as f:
    content = f.read()
print(content)

to_save=input("Enter [y] to save text to speach audio : ")

# Save Audio
def save():
    print("Saving...")
    engine.save_to_file(content, audio_file)
    print(f"Audio Saved to : {audio_file}")

# if want to save
save() if to_save=="y" else print(f"Audio NOT Saved")

# Speach
engine.say(content)
engine.runAndWait()
