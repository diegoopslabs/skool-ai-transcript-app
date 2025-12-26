"""
Exercise 1: My First Playlist

Welcome to your first programming exercise! You'll learn how to store and display
information about your favorite songs using variables - the building blocks of programming.

Concepts covered:
- Variables (storing data in named containers)
- Data types (strings, numbers, booleans)
- String formatting and output
- Basic calculations

Learning Goals:
- Understand what variables are and how to create them
- Learn different types of data (text, numbers, true/false)
- Display information to the screen
- Perform simple calculations

Run this exercise: uv run exercise/python/01_my_first_playlist.py
"""

# ============================================================================
# WHAT ARE VARIABLES?
# ============================================================================
# Think of variables as labeled boxes that hold information.
# You give each box a name, and you can put different types of things in them:
# - Text (strings): song titles, artist names
# - Numbers (integers): track numbers, year released
# - Decimals (floats): song duration in minutes
# - True/False (booleans): is it your favorite?


# ============================================================================
# EXAMPLE CODE
# ============================================================================
# Here's how we create variables for a song:

song_title = "Bohemian Rhapsody"  # Text goes in quotes
artist = "Queen"
duration_minutes = 5.55  # Decimals for precise times
year_released = 1975
is_favorite = True  # Boolean: True or False (no quotes!)

# Display the song information
print("🎵 Song Information 🎵")
print("Title:", song_title)
print("Artist:", artist)
print("Duration:", duration_minutes, "minutes")
print("Released:", year_released)
print("Favorite?", is_favorite)

# We can also do calculations with number variables
duration_seconds = duration_minutes * 60
print("That's", duration_seconds, "seconds!")


# ============================================================================
# YOUR TURN: TODO EXERCISES
# ============================================================================

# TODO 1: Create variables for YOUR favorite song
# Replace the values below with your actual favorite song's information
# Stuck? Ask your AI assistant: "How do I create a variable in Python?"

my_song_title = "TODO: Put your song title here"
my_artist = "TODO: Put the artist name here"
my_duration = 0.0  # TODO: Change this to the actual duration (e.g., 3.45 for 3 minutes 27 seconds)
my_year = 2024  # TODO: Change to the year your song was released
my_is_favorite = True  # This one is already correct! It's your favorite, right?


# TODO 2: Display your song information
# Use print() statements to show your song's details
# HINT: Look at how we displayed the example song above
# If you're unsure about print(), try asking: "How does the print() function work in Python?"

print("\n🎵 My Favorite Song 🎵")
# TODO: Add print statements here to display:
# - Your song title
# - Your artist
# - Your duration
# - Your year
# - Whether it's your favorite


# TODO 3: Calculate and display the duration in seconds
# HINT: Remember, there are 60 seconds in a minute
# Meta-help: "How do I multiply two numbers in Python?"

# TODO: Create a variable called my_duration_seconds
# TODO: Calculate it by multiplying my_duration by 60
# TODO: Print the result


# TODO 4: Create a second favorite song
# Now create variables for another song you love!

# TODO: Create variables for a second song (use names like song2_title, song2_artist, etc.)
# TODO: Print all the information about your second song
# Challenge: Can you calculate how many seconds BOTH songs are combined?


# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# BONUS 1: Calculate the total duration of both songs in minutes
# For help with this challenge, you could ask: "How do I add two numbers and store the result?"


# BONUS 2: Create a variable that combines the song title and artist into one string
# Example: "Bohemian Rhapsody by Queen"
# HINT: You can combine strings with the + operator
# Meta-help: "How do I combine strings in Python?"


# ============================================================================
# TESTING YOUR CODE
# ============================================================================

# When you run this file, you should see:
# - Information about the example song (Bohemian Rhapsody)
# - Information about YOUR favorite song
# - Duration calculations in seconds
# - (If you did the TODOs) Your second song's information

if __name__ == "__main__":
    print("\n✅ Exercise complete! Check your output above.")
    # Your code runs automatically when the file loads!
