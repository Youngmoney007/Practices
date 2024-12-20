import time


lyrics = [
    "You were alone, left out in the cold,",
    "Clinging to the ruin of your broken home.",
    "We all need someone to hold,",
    "Don't let go...",
    "Someone to stay, someone to stay..."
]

def print_lyrics_with_delay(lyrics, delay=2):
    for line in lyrics:
        print(line)
        time.sleep(delay)


print("🎶 Starting the song... 🎶")
print_lyrics_with_delay(lyrics, delay=1)
print("🎶 End of snippet! 🎶")
