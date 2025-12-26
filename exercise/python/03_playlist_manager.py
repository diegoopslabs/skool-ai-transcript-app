"""
Exercise 3: Playlist Manager

Functions are reusable blocks of code that perform specific tasks. Let's create
functions to manage your music playlists like a real music app!

Concepts covered:
- Defining functions with def
- Function parameters (inputs)
- Return values (outputs)
- Calling functions
- Code organization and reusability

Learning Goals:
- Write your own functions
- Pass information to functions using parameters
- Get results back from functions using return
- Understand why functions make code cleaner and reusable

Run this exercise: uv run exercise/python/03_playlist_manager.py
"""

# ============================================================================
# WHAT ARE FUNCTIONS?
# ============================================================================
# Functions are like tools in a toolbox - each one does a specific job.
# Instead of writing the same code over and over, you write it once in a function
# and then "call" that function whenever you need it.
#
# Functions have:
# - A name (like add_song)
# - Parameters (inputs they need)
# - A body (the code that runs)
# - Often a return value (the result they give back)


# ============================================================================
# EXAMPLE CODE
# ============================================================================

# Defining a simple function that takes NO parameters
def greet_music_lover():
    """This function prints a greeting. It doesn't need any input."""
    print("🎵 Welcome, music lover! 🎵")

# Calling the function
greet_music_lover()


# Defining a function that takes parameters
def display_song(title, artist):
    """
    This function takes two parameters: title and artist.
    It displays them in a nice format.
    """
    print(f"♪ {title} by {artist}")

# Calling the function with arguments
display_song("Imagine", "John Lennon")
display_song("Thriller", "Michael Jackson")


# Defining a function that RETURNS a value
def calculate_total_duration(song1_minutes, song2_minutes):
    """
    This function calculates the total duration of two songs.
    It RETURNS the result instead of just printing it.
    """
    total = song1_minutes + song2_minutes
    return total

# Calling the function and storing the result
total_time = calculate_total_duration(3.5, 4.2)
print(f"\nTotal playlist duration: {total_time} minutes")


# Function that returns a value and uses it in another function
def format_duration(minutes):
    """Converts decimal minutes to minutes and seconds."""
    whole_minutes = int(minutes)
    seconds = int((minutes - whole_minutes) * 60)
    return f"{whole_minutes}m {seconds}s"

print(f"Formatted: {format_duration(3.5)}")


# ============================================================================
# YOUR TURN: TODO EXERCISES
# ============================================================================

# TODO 1: Create a function to add a song to a playlist
# Write a function called add_song that takes two parameters:
# - playlist (a list)
# - song_name (a string)
# The function should add the song to the playlist and print a confirmation
# Stuck? Ask: "How do I write a function that modifies a list in Python?"

def add_song(playlist, song_name):
    """Add a song to the playlist and print a confirmation."""
    # TODO: Use the append() method to add song_name to playlist
    # TODO: Print a message like "Added 'Song Name' to playlist"
    pass  # Remove this 'pass' when you add your code


# TODO 2: Test your add_song function
my_playlist = ["Yesterday", "Let It Be"]
print("\n🎵 Building My Playlist 🎵")
# TODO: Call add_song to add "Hey Jude" to my_playlist
# TODO: Call add_song to add another song of your choice
# TODO: Print my_playlist to see the results


# TODO 3: Create a function that returns a value
# Write a function called count_songs that takes a playlist and returns the count
# HINT: Use len() inside the function and return the result
# Meta-help: "How do I return a value from a function in Python?"

def count_songs(playlist):
    """Return the number of songs in a playlist."""
    # TODO: Use len() to count the songs
    # TODO: Return the count
    pass  # Remove this 'pass' when you add your code


# Test your count_songs function
# TODO: Call count_songs with my_playlist and print the result


# TODO 4: Create a function to calculate total playlist duration
# Write a function called total_playlist_duration that takes a list of song durations
# (in minutes) and returns the total duration
# HINT: You can use sum() to add all numbers in a list

def total_playlist_duration(durations):
    """Calculate the total duration of all songs."""
    # TODO: Use sum() to add all the durations
    # TODO: Return the total
    pass  # Remove this 'pass' when you add your code


# Test your function
song_durations = [3.5, 4.2, 2.8, 5.1, 3.3]
# TODO: Call total_playlist_duration and print the result


# TODO 5: Create a function to find the longest song
# Write a function that takes a list of durations and returns the longest one
# HINT: Use the max() function
# Meta-help: "How do I find the maximum value in a list in Python?"

def find_longest_song(durations):
    """Return the duration of the longest song."""
    # TODO: Use max() to find the longest duration
    # TODO: Return it
    pass  # Remove this 'pass' when you add your code


# Test it
# TODO: Call find_longest_song with song_durations and print the result


# TODO 6: Create a function with multiple parameters
# Write a function called create_song_info that takes three parameters:
# - title
# - artist
# - duration
# It should RETURN a formatted string like: "Title by Artist (3.5 minutes)"

def create_song_info(title, artist, duration):
    """Create a formatted string with song information."""
    # TODO: Create a formatted string with all the info
    # TODO: Return the string
    pass  # Remove this 'pass' when you add your code


# Test it
# TODO: Call create_song_info with your favorite song's details and print it


# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# BONUS 1: Create a function that removes a song by name
# The function should search for the song and remove it if found
# HINT: Check if the song is in the list first with: if song in playlist
# Meta-help: "How do I remove an item from a list by value in Python?"


# BONUS 2: Create a function that finds the average song duration
# Take a list of durations and return the average
# HINT: Average = sum of all durations / number of durations


# BONUS 3: Create a function that takes a playlist and returns a shuffled version
# HINT: Look up the random.shuffle() function or random.sample()
# You'll need to: import random at the top of the file
# Meta-help: "How do I shuffle a list in Python?"


# ============================================================================
# TESTING YOUR CODE
# ============================================================================

# When you run this file, you should see:
# - The example functions working (greet, display_song, etc.)
# - Your add_song function adding songs to a playlist
# - Your count_songs function returning the count
# - Your total_playlist_duration calculating the total time
# - Your find_longest_song finding the max duration
# - Your create_song_info returning a formatted string
