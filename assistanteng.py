import random
import subprocess
from fuzzywuzzy import fuzz
import pyttsx3



# convert text to lowercase and remove accents
def normalize_text(text):
    return text.lower()

# Checking whether the text is similar to a command
def is_command_similar(text, command_phrase):
    similarity = fuzz.ratio(text, command_phrase)
    return similarity > 50  # tolerate 50% similarity

# List of commands for different tasks (in lower case)

commands = {
    # SKILLs
    normalize_text("github"): "start %USERPROFILE%\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
    normalize_text("code"): "start skills\\VS-Code-Starter\\open.lnk",
    normalize_text("download"): "explorer %USERPROFILE%\\Downloads",
    normalize_text("desktop"): "explorer %USERPROFILE%\\Desktop\\Desktop",
    normalize_text("browser"): 'start "" http://www.google.com',
    normalize_text("console"): "start cmd.exe",
    normalize_text("shut down"): "shutdown /s /t 5",
    normalize_text("system control"): "control",
    normalize_text("calender"): "start outlookcal:",
    normalize_text("task manager"): "taskmgr",
    normalize_text("settings"): "start ms-settings:",
    normalize_text("recycle bin"): "start shell:RecycleBinFolder",
    normalize_text("system info"): "msinfo32",
    normalize_text("ip address"): "ipconfig",


    # USER SKILLs
    normalize_text("your command"): "your action",
    
            #
            #here you can add your own commands
            #
}

# audio command phrases for different tasks
audio_files = {
    normalize_text("github"): ["Of course master, here is GitHub Desktop", "GitHub Desktop is started for you Lord", "But of course master, I am starting GitHub Desktop"], 
    normalize_text("code"): ["Of course master, let's code", "Visual Studio code started for you", "But of course master, you can start coding"],        
    normalize_text("download"): ["Yes master, the download folder is open", "Of course master, I open the download folder", "Here is the download folder my master"],
    normalize_text("desktop"): ["Of course master, I open the desktop", "I open the desktop", "Here is the desktop my excellency"],
    normalize_text("browser"): ["Of course master, I open a browser", "Here is the browser my excellency", "Of course master, I open a browser"],
    normalize_text("console"): ["Sir, I am starting the console", "I am starting the console my Excellency", "Here is the command line you want my Excellency"],
    normalize_text("shut down"): ["As you wish, you have turned off the computer", "The computer will be turned off in 5 seconds my excellency", "But sure master, I will turn off the computer"],
    normalize_text("system control"): ["Here is the control panel my excellency", "Of course master, I open the control panel"],
    normalize_text("calender"): ["Here is the calendar my excellency", "Of course master, I open the calendar"],
    normalize_text("task manager"): ["Here is the task manager my excellency", "Of course master, I open the task manager"],
    normalize_text("settings"): ["Here are the settings my excellency", "Of course master, I open the settings"],
    normalize_text("recycle bin"): ["Here is the wastebasket my excellency", "Of course master, I open the wastebasket"],
    normalize_text("system info"): ["Here is the system information my excellency", "Of course master, I open the system information"],
    normalize_text("ip address"): ["Here is the IP address my Excellency", "Of course master, I show the IP address"],

    
    # USER SKILLs
    normalize_text("your command"): ["Here you can add your own commands", "You can choose in commands what action this command does", "And in audio files, where we are now, you can type what should be said"],
    
            #
            #here you can add your own commands
            #
}

# TTS-Engine
engine = pyttsx3.init()

engine.setProperty('rate', 150)  # 150 words per minute
engine.setProperty('language', 'en')





while True:
    user_input = input("Befehl: ")
    user_input_normalized = normalize_text(user_input)

    best_match_command = None
    best_similarity = 0

    # Find the best matching command
    for command in commands:
        similarity = fuzz.ratio(user_input_normalized, command)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match_command = command

    if best_match_command is not None:
        subprocess.run(commands[best_match_command], shell=True)

        if best_match_command in audio_files:
            random_sentence = random.choice(audio_files[best_match_command])

            engine.say(random_sentence)
            engine.runAndWait()
    else:
        print("Could not find a matching command. Try again.")
