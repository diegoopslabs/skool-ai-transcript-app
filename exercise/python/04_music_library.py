"""
Exercise 4: Music Library

Dictionaries (also called "dicts") let you store data in key-value pairs, perfect
for organizing complex information like a music library with songs, artists, and metadata.

Concepts covered:
- Dictionaries (key-value pairs)
- Nested data structures (lists of dictionaries)
- Accessing and modifying dictionary values
- Iterating through dictionaries
- Organizing complex data

Learning Goals:
- Create and use dictionaries to store structured data
- Access values using keys
- Work with nested structures (lists of dicts)
- Build a realistic music library data model

Run this exercise: uv run exercise/python/04_music_library.py
"""

# ============================================================================
# WHAT ARE DICTIONARIES?
# ============================================================================
# Dictionaries are like real dictionaries - you look up a KEY to get a VALUE.
# Instead of using index numbers (0, 1, 2), you use meaningful names.
#
# Example: Instead of song[0], song[1], song[2] for title, artist, duration,
# you can use: song["title"], song["artist"], song["duration"]
#
# Dictionaries use curly braces { } and have key: value pairs


# ============================================================================
# EXAMPLE CODE
# ============================================================================

# Creating a dictionary to represent a single song
song = {
    "title": "Bohemian Rhapsody",
    "artist": "Queen",
    "album": "A Night at the Opera",
    "duration": 5.55,
    "year": 1975,
    "genre": "Rock"
}

print("🎵 Song Dictionary Example 🎵")
print(f"Title: {song['title']}")
print(f"Artist: {song['artist']}")
print(f"Duration: {song['duration']} minutes")

# Modifying a dictionary value
song["duration"] = 5.59  # Oops, correcting the duration
print(f"Corrected duration: {song['duration']}")

# Adding a new key-value pair
song["rating"] = 5  # Out of 5 stars
print(f"Rating: {song['rating']} stars")

# Looping through dictionary keys and values
print("\n🎵 All song information:")
for key, value in song.items():
    print(f"{key}: {value}")


# Creating a music library: a LIST of DICTIONARIES
music_library = [
    {
        "title": "Imagine",
        "artist": "John Lennon",
        "duration": 3.03,
        "genre": "Pop"
    },
    {
        "title": "Billie Jean",
        "artist": "Michael Jackson",
        "duration": 4.54,
        "genre": "Pop"
    },
    {
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "duration": 5.01,
        "genre": "Rock"
    }
]

print("\n🎵 Music Library 🎵")
for song in music_library:
    print(f"♪ {song['title']} by {song['artist']} ({song['genre']})")


# ============================================================================
# YOUR TURN: TODO EXERCISES
# ============================================================================

# TODO 1: Create your own song dictionary
# Create a dictionary called my_song with these keys:
# - title, artist, album, duration, year, genre, rating (1-5)
# Use one of your favorite songs!
# Stuck? Ask: "How do I create a dictionary in Python?"

my_song = {}  # TODO: Add key-value pairs for your song


# TODO 2: Display your song information
# Print at least 4 pieces of information from your my_song dictionary
# HINT: Use my_song["key_name"] to access values

print("\n🎵 My Favorite Song 🎵")
# TODO: Print the title
# TODO: Print the artist
# TODO: Print the genre
# TODO: Print the rating


# TODO 3: Modify your song dictionary
# Change the rating of your song to a different value
# Add a new key called "play_count" with how many times you've listened to it
# Meta-help: "How do I add a new key to an existing dictionary in Python?"

# TODO: Change the rating
# TODO: Add a play_count key
# TODO: Print the updated rating and play_count


# TODO 4: Create your music library
# Create a list called my_library with at least 3 song dictionaries
# Each song should have: title, artist, duration, genre
# HINT: It's a list of dictionaries, like the example music_library above

my_library = []  # TODO: Add at least 3 song dictionaries here


# TODO 5: Loop through your library
# Write a for loop that displays all songs in a nice format
# HINT: for song in my_library:

print("\n🎵 My Music Library 🎵")
# TODO: Loop through my_library and print each song's title and artist


# TODO 6: Filter songs by genre
# Loop through your library and print only the songs of a specific genre (your choice)
# HINT: Use an if statement inside the loop: if song["genre"] == "Rock":
# Meta-help: "How do I filter a list based on a condition in Python?"

print("\n🎵 Filtering by Genre 🎵")
# TODO: Pick a genre and print only songs of that genre


# TODO 7: Calculate statistics
# Write code that calculates and prints:
# - Total number of songs in your library
# - Total duration of all songs combined
# - Average duration
# HINT: Loop through, add up durations, then divide by the count

print("\n📊 Library Statistics 📊")
# TODO: Calculate total songs (use len())
# TODO: Calculate total duration (loop and sum)
# TODO: Calculate average duration (total / count)


# TODO 8: Find songs by artist
# Write a function that takes an artist name and returns a list of all songs by that artist
# This combines concepts from the previous exercise!

def find_songs_by_artist(library, artist_name):
    """Return a list of songs by the specified artist."""
    # TODO: Create an empty list called found_songs
    # TODO: Loop through the library
    # TODO: If song["artist"] matches artist_name, add it to found_songs
    # TODO: Return found_songs
    pass  # Remove this when you add your code


# Test your function
# TODO: Call find_songs_by_artist with an artist in your library
# TODO: Print the results


# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# BONUS 1: Create a function to find the highest-rated song
# Loop through the library and return the song dictionary with the highest rating
# HINT: You'll need to add "rating" to your song dictionaries first
# Meta-help: "How do I find the dictionary with the maximum value for a key?"


# BONUS 2: Organize songs by genre
# Create a new dictionary where keys are genres and values are lists of songs
# Example: {"Rock": [song1, song2], "Pop": [song3, song4]}
# This is advanced! Ask: "How do I group items in a list by a common property?"


# BONUS 3: Create a playlist dictionary
# Make a dictionary that represents a playlist with:
# - name: "Workout Mix"
# - songs: [list of song dictionaries]
# - created_date: a date string
# - total_duration: calculated from all songs


# ============================================================================
# TESTING YOUR CODE
# ============================================================================

# When you run this file, you should see:
# - The example song dictionary displayed
# - Your favorite song information
# - Your music library with multiple songs
# - Songs filtered by genre
# - Library statistics (count, total duration, average)
# - Results from finding songs by artist
