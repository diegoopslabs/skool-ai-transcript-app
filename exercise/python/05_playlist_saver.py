"""
Exercise 5: Playlist Saver

Learn how to save your playlists to files and load them back later! This exercise
teaches file I/O (input/output) and JSON format - skills used in real applications.

Concepts covered:
- File I/O (reading and writing files)
- JSON format (JavaScript Object Notation)
- Error handling with try/except
- Data persistence
- Working with file paths

Learning Goals:
- Save data to files so it persists between program runs
- Read data from files
- Use JSON to store complex data structures
- Handle errors gracefully when files don't exist

Run this exercise: uv run exercise/python/05_playlist_saver.py
"""

import json
import os

# ============================================================================
# WHAT IS FILE I/O AND JSON?
# ============================================================================
# File I/O lets you save data to your computer and load it later.
# JSON is a text format for storing structured data (like dictionaries and lists).
#
# Why JSON?
# - Easy to read and write
# - Works with dictionaries, lists, strings, numbers
# - Used everywhere: web APIs, config files, data storage
#
# Python's json module converts Python data to JSON and back:
# - json.dump() / json.dumps() -> Python to JSON
# - json.load() / json.loads() -> JSON to Python


# ============================================================================
# EXAMPLE CODE
# ============================================================================

# Creating a sample playlist (list of song dictionaries)
example_playlist = [
    {"title": "Imagine", "artist": "John Lennon", "duration": 3.03},
    {"title": "Billie Jean", "artist": "Michael Jackson", "duration": 4.54},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 5.55}
]

print("🎵 Original Playlist 🎵")
for song in example_playlist:
    print(f"♪ {song['title']} by {song['artist']}")


# Saving the playlist to a file
def save_playlist(playlist, filename):
    """Save a playlist to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(playlist, file, indent=2)  # indent=2 makes it pretty
    print(f"\n✅ Playlist saved to {filename}")


# Loading a playlist from a file
def load_playlist(filename):
    """Load a playlist from a JSON file."""
    try:
        with open(filename, 'r') as file:
            playlist = json.load(file)
        print(f"\n✅ Playlist loaded from {filename}")
        return playlist
    except FileNotFoundError:
        print(f"\n❌ File {filename} not found!")
        return []


# Testing save and load
save_playlist(example_playlist, "example_playlist.json")
loaded_playlist = load_playlist("example_playlist.json")

print("\n🎵 Loaded Playlist 🎵")
for song in loaded_playlist:
    print(f"♪ {song['title']} by {song['artist']}")


# ============================================================================
# YOUR TURN: TODO EXERCISES
# ============================================================================

# TODO 1: Create your own playlist to save
# Make a list of at least 3 song dictionaries with title, artist, duration
# HINT: Use what you learned in Exercise 4

my_playlist = []  # TODO: Add your song dictionaries here


# TODO 2: Save your playlist to a file
# Call the save_playlist function to save my_playlist to "my_playlist.json"
# Stuck? Ask: "How do I call a function that takes two parameters?"

# TODO: Call save_playlist with my_playlist and "my_playlist.json"


# TODO 3: Load your playlist back
# Call load_playlist to load "my_playlist.json" and store it in a variable
# Print the loaded playlist to verify it worked
# Meta-help: "How do I load data from a JSON file in Python?"

# TODO: Call load_playlist and store the result in loaded_my_playlist
# TODO: Print the loaded playlist (loop through and display songs)


# TODO 4: Add error handling
# Try to load a file that doesn't exist and see what happens
# The load_playlist function already has error handling - test it!

print("\n🔍 Testing Error Handling 🔍")
# TODO: Try to load a file that doesn't exist, like "nonexistent.json"
# TODO: Notice how the try/except prevents the program from crashing


# TODO 5: Create a function to add a song and auto-save
# Write a function that:
# 1. Loads the playlist from a file
# 2. Adds a new song to it
# 3. Saves it back to the file
# This is a practical pattern used in real apps!

def add_song_and_save(filename, new_song):
    """Add a song to a playlist file and save it."""
    # TODO: Load the playlist from filename
    # TODO: Append new_song to the playlist
    # TODO: Save the updated playlist back to filename
    # TODO: Print a confirmation message
    pass  # Remove this when you add your code


# Test your function
new_song = {"title": "Your Choice", "artist": "Your Favorite Artist", "duration": 3.30}
# TODO: Call add_song_and_save to add new_song to "my_playlist.json"
# TODO: Load and print the playlist to verify the song was added


# TODO 6: Create a function to remove a song by title
# Write a function that loads a playlist, removes a song by title, and saves it back
# HINT: Use a loop to find the song, then use list.remove()

def remove_song_and_save(filename, song_title):
    """Remove a song from a playlist file by title."""
    # TODO: Load the playlist
    # TODO: Loop through to find the song with matching title
    # TODO: Remove it from the list
    # TODO: Save the updated playlist
    # TODO: Print a confirmation
    pass  # Remove this when you add your code


# Test it
# TODO: Call remove_song_and_save to remove a song from "my_playlist.json"


# TODO 7: Create multiple playlists
# Create and save at least 3 different playlists with different themes
# Examples: "workout.json", "chill.json", "party.json"
# Meta-help: "How can I organize multiple playlists in my music app?"

# TODO: Create a workout playlist (energetic songs)
# TODO: Create a chill playlist (relaxing songs)
# TODO: Create another themed playlist of your choice
# TODO: Save each one to a different file


# TODO 8: Create a playlist manager menu
# This combines everything! Create a simple text-based menu that lets you:
# - List all saved playlists
# - Load and display a playlist
# - Create a new playlist
# - Add songs to a playlist
# - Save playlists
# This is advanced but rewarding!

def playlist_menu():
    """A simple playlist manager with a menu."""
    print("\n🎵 Playlist Manager 🎵")
    print("1. List all playlists")
    print("2. Load a playlist")
    print("3. Create new playlist")
    print("4. Add song to playlist")
    print("5. Save and exit")

    # TODO: Get user input with input()
    # TODO: Use if/elif statements to handle each menu option
    # TODO: This is a big challenge - break it into small steps!
    # Meta-help: "How do I create a menu-driven program in Python?"
    pass


# Uncomment to test your menu:
# playlist_menu()


# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# BONUS 1: Add data validation
# Before saving, check that each song has required fields (title, artist, duration)
# Print warnings for invalid songs
# HINT: Use "key" in dictionary to check if a key exists


# BONUS 2: Create a backup function
# Write a function that saves a playlist to both .json and a backup file
# Example: save_with_backup("my_playlist.json") also creates "my_playlist.backup.json"


# BONUS 3: Merge playlists
# Create a function that loads two playlists and combines them into one
# Remove duplicates (same title and artist)
# Meta-help: "How do I merge two lists and remove duplicates in Python?"


# BONUS 4: Export playlist as text
# Create a function that saves a playlist as a human-readable .txt file
# Format: "1. Song Title by Artist (3:30)"
# HINT: You'll need to convert decimal duration to minutes:seconds


# ============================================================================
# TESTING YOUR CODE
# ============================================================================

# When you run this file, you should see:
# - Example playlist saved and loaded
# - Your playlist saved to my_playlist.json
# - Your playlist loaded back successfully
# - Error handling working when loading nonexistent files
# - Songs being added and removed from the saved file
# - Multiple themed playlists created and saved

# Check the exercise/python/ folder - you should see JSON files created!
