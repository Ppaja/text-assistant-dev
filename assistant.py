import random
import subprocess
from fuzzywuzzy import fuzz
import pyttsx3
import subprocess

# Funktion zur Umwandlung von Text in Kleinbuchstaben und Entfernung von Akzenten
def normalize_text(text):
    return text.lower()

# Funktion zur Überprüfung, ob der erkannte Text einem Befehl ähnlich ist
def is_command_similar(text, command_phrase):
    similarity = fuzz.ratio(text, command_phrase)
    return similarity > 50  # Ähnlichkeitsgrenze anpassen

# Liste von Befehlen für verschiedene Aufgaben (in Kleinbuchstaben)
commands = {
    # SKILLs
    normalize_text("github"): "start %USERPROFILE%\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe",
    normalize_text("code"): "start skills\\VS-Code-Starter\\open.lnk",
    normalize_text("öffne den download"): "explorer %USERPROFILE%\\Downloads",
    normalize_text("öffne den desktop"): "explorer %USERPROFILE%\\Desktop\\Desktop",
    normalize_text("öffne einen browser"): 'start "" http://www.google.com',
    normalize_text("öffne die konsole"): "start cmd.exe",
    normalize_text("schalte den computer aus"): "shutdown /s /t 5",
    normalize_text("öffne die Systemsteuerung"): "control",
    normalize_text("öffne den Kalender"): "start outlookcal:",
    normalize_text("öffne den Task-Manager"): "taskmgr",
    normalize_text("öffne die Einstellungen"): "start ms-settings:",
    normalize_text("öffne den Papierkorb"): "start shell:RecycleBinFolder",
    normalize_text("öffne die Systeminformationen"): "msinfo32",
    normalize_text("zeige die IP-Adresse"): "ipconfig",




    # USER SKILLs
    normalize_text("öffne star wars"): "\"D:\\Battlefront23\\STAR WARS Battlefront II\\starwarsbattlefrontii.exe",
    normalize_text("steamapps c"): "explorer \"C:\\Program Files (x86)\\Steam\\steamapps\\common\"",
    normalize_text("steamapps d"): "explorer \"D:\\SteamLibrary\\steamapps\\common\""
}

# Dictionary mit Zuordnung von Befehlen zu Audiodateien (als Listen)
audio_files = {
    normalize_text("github"): ["Natürlich Meister, hier ist der GitHub Desktop", "GitHub Desktop ist für Sie gestartet Lord", "Aber natürlich Herr, ich starte GitHub Desktop"], 
    normalize_text("code"): ["Natürlich Meister, lass uns coden", "Visual Studio Code für Sie gestartet", "Aber natürlich Herr, Sie können beginnen zu coden"],        
    normalize_text("öffne den download ordner"): ["Ja Herr, der download Ordner ist offen", "Natürllich Meister, ich öffne den download Ordner", "Hier ist der download Ordner mein Gebieter"],
    normalize_text("öffne den desktop"): ["Natürllich Meister, ich öffne den Desktop", "Ich öffne den Desktop", "Hier ist der Desktop meine Exzellenz"],
    normalize_text("öffne einen browser"): ["Natürllich Meister, ich öffne einen Browser", "Hier ist der Browser meine Exzellenz", "Selbstverständlich Meister, ich öffne einen Browser"],
    normalize_text("öffne die konsole"): ["Herr, ich starte die Konsole", "Ich starte die Konsole meine Exzellenz", "Hier ist die gewünschte Befehlszeile meine Exzellenz"],
    normalize_text("schalte den computer aus"): ["Wie ihr wünscht, ihr habt den Computer ausgeschaltet", "Der Computer wird in 5 Sekunden ausgeschaltet meine Exzellenz", "Aber sicher Meister, ich schalte den Computer aus"],
    normalize_text("öffne die Systemsteuerung"): ["Hier ist die Systemsteuerung meine Exzellenz", "Natürllich Meister, ich öffne die Systemsteuerung"],
    normalize_text("öffne den Kalender"): ["Hier ist der Kalender meine Exzellenz", "Natürllich Meister, ich öffne den Kalender"],
    normalize_text("öffne den Task-Manager"): ["Hier ist der Task-Manager meine Exzellenz", "Natürllich Meister, ich öffne den Task-Manager"],
    normalize_text("öffne die Einstellungen"): ["Hier ist die Einstellungen meine Exzellenz", "Natürllich Meister, ich öffne die Einstellungen"],
    normalize_text(" offene den Papierkorb"): ["Hier ist der Papierkorb meine Exzellenz", "Natürllich Meister, ich öffne den Papierkorb"],
    normalize_text("öffne die Systeminformationen"): ["Hier ist die Systeminformationen meine Exzellenz", "Natürllich Meister, ich öffne die Systeminformationen"],
    normalize_text("zeige die IP-Adresse"): ["Hier ist die IP-Adresse meine Exzellenz", "Natürllich Meister, ich zeige die IP-Adresse"],
    # USER SKILLs
    normalize_text("öffne star wars"): ["Möge die Macht mit Ihnen sein mein Meister", "Ich starte Star Wars, mein Meister", "Die Macht ist stark in Euch mein Meister. Ich starte Star Wars"],
    normalize_text("steamapps c"): ["Hier ist der SteamApps Ordner C meine Exzellenz", "Wie ihr wählt, der SteamApps Ordner C ist offen", "Hier ist der SteamApps Ordner C meine Exzellenz"],
    normalize_text("steamapps d"): ["Hier ist der SteamApps Ordner D meine Exzellenz", "Wie ihr wählt, der SteamApps Ordner D ist offen", "Hier ist der SteamApps Ordner D meine Exzellenz"]
}

# Initialisiere die TTS-Engine
engine = pyttsx3.init()

engine.setProperty('rate', 150)  # Reduziert die Sprechgeschwindigkeit auf 150 Wörter pro Minute


while True:
    user_input = input("Befehl: ")
    user_input_normalized = normalize_text(user_input)

    best_match_command = None
    best_similarity = 0

    # Finde den am besten passenden Befehl
    for command in commands:
        similarity = fuzz.ratio(user_input_normalized, command)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match_command = command

    if best_match_command is not None:
        # Führe den gefundenen Befehl aus
        subprocess.run(commands[best_match_command], shell=True)

        # Überprüfen, ob Audiozeilen für den Befehl vorhanden sind
        if best_match_command in audio_files:
            # Wähle einen zufälligen Satz aus der Liste der Sätze aus
            random_sentence = random.choice(audio_files[best_match_command])

            # Spiele die Sprachausgabe direkt ab
            engine.say(random_sentence)
            engine.runAndWait()
    else:
        print("Befehl nicht erkannt. Bitte erneut eingeben.")
