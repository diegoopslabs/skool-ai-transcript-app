"""
Exercise 2: Song Collection

Now that you know how to work with individual variables, let's organize multiple
songs together using lists! Lists let you store many items in a single collection.

Concepts covered:
- Lists (storing multiple items together)
- Accessing list items by index
- Adding and removing items from lists
- Looping through lists with for loops
- List operations (length, sorting)

Learning Goals:
- Create and modify lists
- Access specific items in a list
- Use loops to process each item
- Understand list indexing (starting at 0!)

Run this exercise: uv run exercise/python/02_song_collection.py
"""

# ============================================================================
# WHAT ARE LISTS?
# ============================================================================
# A list is like a playlist - it holds multiple items in order.
# In Python, we create lists using square brackets [ ]
# Each item in the list is separated by a comma


# ============================================================================
# EXAMPLE CODE
# ============================================================================

# Creating a list of song titles
playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]

# Displaying the whole list
print("🎵 My Playlist 🎵")
print(playlist)

# Accessing individual songs by index (position)
# IMPORTANT: Lists start counting at 0, not 1!
print("\nFirst song:", playlist[0])  # Index 0 = first item
print("Second song:", playlist[1])  # Index 1 = second item
print("Third song:", playlist[2])  # Index 2 = third item

# Finding out how many songs are in the playlist
print("\nTotal songs:", len(playlist))

# Adding a new song to the end of the playlist
playlist.append("Imagine")
print("\nAfter adding a song:", playlist)

# Looping through the playlist to show each song
print("\n🎵 Playing all songs:")
for song in playlist:
    print("♪ Now playing:", song)

# You can also loop with index numbers
print("\n🎵 Numbered playlist:")
for i in range(len(playlist)):
    print(f"{i + 1}. {playlist[i]}")  # i + 1 because humans count from 1!


# ============================================================================
# YOUR TURN: TODO EXERCISES
# ============================================================================

# TODO 1: Create your own playlist
# Create a list called my_playlist with at least 5 of your favorite songs
# Stuck? Ask your AI assistant: "How do I create a list in Python?"

my_playlist = []  # TODO: Add your favorite songs here (in quotes, separated by commas)


# TODO 2: Display your playlist information
# Print the total number of songs and the entire playlist
# HINT: Use len() to get the count

print("\n🎵 My Personal Playlist 🎵")
# TODO: Print how many songs are in my_playlist
# TODO: Print the entire my_playlist


# TODO 3: Access specific songs
# Print the first song and the last song in your playlist
# HINT: First song is index 0, last song is index -1 (Python magic!)
# Meta-help: "How do I access the last item in a Python list?"

# TODO: Print your first song (index 0)
# TODO: Print your last song (index -1)


# TODO 4: Add more songs
# Use the append() method to add 2 more songs to your playlist

# TODO: Add your 6th favorite song
# TODO: Add your 7th favorite song
# TODO: Print the playlist to see the additions


# TODO 5: Loop through your playlist
# Use a for loop to print each song with a music note ♪
# HINT: Look at the example "Playing all songs" loop above
# If loops are confusing, try asking: "Explain for loops in Python with a playlist example"

print("\n🎵 Now Playing:")
# TODO: Write a for loop that prints each song in my_playlist


# TODO 6: Create a numbered playlist
# Loop through your playlist and print each song with its position number
# HINT: Humans count from 1, but lists start at 0. Add 1 to the index!

print("\n🎵 Playlist (numbered):")
# TODO: Write a for loop using range(len(my_playlist))
# TODO: Print each song with its number (e.g., "1. Song Name")


# ============================================================================
# BONUS CHALLENGES (Optional)
# ============================================================================

# BONUS 1: Remove a song from your playlist
# Use the remove() method to delete a song you don't like anymore
# Meta-help: "How do I remove an item from a list in Python?"


# BONUS 2: Sort your playlist alphabetically
# HINT: Look up the sorted() function or the .sort() method
# Try asking: "What's the difference between sorted() and .sort() in Python?"


# BONUS 3: Create a list of artists
# Make a separate list with artist names, then loop through both lists together
# This is tricky! You might want to ask: "How do I loop through two lists at the same time?"


# ============================================================================
# TESTING YOUR CODE
# ============================================================================

# When you run this file, you should see:
# - The example playlist with 4 songs
# - Your personal playlist with at least 5 songs
# - The first and last song from your playlist
# - Your playlist with 2 more songs added (7 total)
# - Each song displayed in a loop
# - A numbered version of your playlist
