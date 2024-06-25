import os 
from datetime import date

def assess_mood():
    moods = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']
    mood_values = [2, 1, 0, -1, -2]

    ask_mood = input("How are you feeling today? ").lower()

    while ask_mood not in moods:
        ask_mood = input("How are you feeling today? ")

    mood_value = mood_values[moods.index(ask_mood)]

    today = str(date.today())
    mood_diary_path = os.path.join('data', 'mood_diary.txt')

    if not os.path.exists('data'):
        os.makedirs('data')

    if os.path.exists(mood_diary_path):
        with open(mood_diary_path, 'r') as file:
            entries = file.readlines()
            for entry in entries:
                entry_date, _ = entry.strip().split(",")
                if entry_date == today:
                    print("Sorry, you have already entered your mood today.")
                    return

    with open(mood_diary_path, 'a') as file:
        file.write(f"{today},{mood_value}\n")
    print("Mood stored successfully.")

    diagnose_disorder()
         
def diagnose_disorder():
    mood_diary_path = os.path.join('data', 'mood_diary.txt')

    if not os.path.exists(mood_diary_path):
        return

    with open(mood_diary_path, 'r') as file:
        entries = file.readlines()

    if len(entries) < 7:
        return

    last_7_entries = [int(entry.strip().split(",")[1]) for entry in entries[-7:]]

    happy_count = last_7_entries.count(2)
    relaxed_count = last_7_entries.count(1)
    apathetic_count = last_7_entries.count(0)
    sad_count = last_7_entries.count(-1)
    angry_count = last_7_entries.count(-2)

    total = sum(last_7_entries)
    average_mood_value = round(total / 7)

    if average_mood_value == 2:
        average_mood = "happy"
    elif average_mood_value == 1:
        average_mood = "relaxed"
    elif average_mood_value == 0:
        average_mood = "apathetic"
    elif average_mood_value == -1:
        average_mood = "sad"
    elif average_mood_value == -2:
        average_mood = "angry"

    if happy_count >= 5:
        diagnosis = "manic"
    elif sad_count >= 4:
        diagnosis = "depressive"
    elif apathetic_count >= 6:
        diagnosis = "schizoid"
    else:
        diagnosis = average_mood

    print(f"Your diagnosis: {diagnosis}!")
    