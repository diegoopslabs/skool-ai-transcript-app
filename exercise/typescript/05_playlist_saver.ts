/**
 * Exercise 5: Playlist Saver
 *
 * Learn to work with JSON in TypeScript while maintaining type safety!
 * Since we're using browser-compatible TypeScript (no Node.js fs module),
 * we'll use JSON and localStorage concepts that work in browsers.
 *
 * Concepts covered:
 * - JSON.stringify() and JSON.parse()
 * - Type assertions with as keyword
 * - Working with localStorage (browser API)
 * - Type guards and validation
 * - Simulating data persistence
 *
 * Run this exercise: node exercise/typescript/05_playlist_saver.ts
 */

// ============================================================================
// ABOUT JSON AND TYPE SAFETY
// ============================================================================
// JSON (JavaScript Object Notation) is a text format for storing data.
// In TypeScript:
// - JSON.stringify() converts objects to JSON strings
// - JSON.parse() converts JSON strings back to objects
//
// IMPORTANT: JSON.parse() returns type 'any' (no type safety!)
// We use TYPE ASSERTIONS to tell TypeScript what type we expect.
//
// Note: This exercise simulates data persistence. In browsers, you'd use
// localStorage. In Node.js, you'd use the fs module. We're keeping it simple!


// ============================================================================
// TYPE DEFINITIONS
// ============================================================================

interface Song {
    title: string;
    artist: string;
    duration: number;
    genre: string;
}

interface Playlist {
    name: string;
    songs: Song[];
    createdDate: string;
}


// ============================================================================
// EXAMPLE CODE
// ============================================================================

// Creating a sample playlist
const examplePlaylist: Playlist = {
    name: "Classic Rock Favorites",
    songs: [
        { title: "Imagine", artist: "John Lennon", duration: 3.03, genre: "Pop" },
        { title: "Billie Jean", artist: "Michael Jackson", duration: 4.54, genre: "Pop" },
        { title: "Bohemian Rhapsody", artist: "Queen", duration: 5.55, genre: "Rock" }
    ],
    createdDate: "2024-12-25"
};

console.log("🎵 Original Playlist 🎵");
console.log(`Playlist: ${examplePlaylist.name}`);
for (const song of examplePlaylist.songs) {
    console.log(`♪ ${song.title} by ${song.artist}`);
}


// Converting to JSON string
function playlistToJSON(playlist: Playlist): string {
    return JSON.stringify(playlist, null, 2);  // null, 2 for pretty formatting
}

const jsonString = playlistToJSON(examplePlaylist);
console.log("\n📄 JSON String:");
console.log(jsonString);


// Converting from JSON string back to object
function jsonToPlaylist(jsonString: string): Playlist {
    // JSON.parse returns 'any' type - we use 'as Playlist' to assert the type
    const playlist = JSON.parse(jsonString) as Playlist;
    return playlist;
}

const loadedPlaylist = jsonToPlaylist(jsonString);
console.log("\n🎵 Loaded from JSON 🎵");
console.log(`Playlist: ${loadedPlaylist.name}`);
console.log(`Songs: ${loadedPlaylist.songs.length}`);


// Simulating localStorage (browser API for storing data)
// Note: This won't actually persist in Node.js, but demonstrates the concept
const storage: { [key: string]: string } = {};  // Simulated storage

function savePlaylist(playlist: Playlist, key: string): void {
    const json = JSON.stringify(playlist);
    storage[key] = json;
    console.log(`\n✅ Saved playlist "${playlist.name}" to key: ${key}`);
}

function loadPlaylist(key: string): Playlist | null {
    const json = storage[key];
    if (!json) {
        console.log(`\n❌ No playlist found for key: ${key}`);
        return null;
    }
    const playlist = JSON.parse(json) as Playlist;
    console.log(`\n✅ Loaded playlist "${playlist.name}" from key: ${key}`);
    return playlist;
}

// Testing save and load
savePlaylist(examplePlaylist, "myPlaylist");
const retrieved = loadPlaylist("myPlaylist");
if (retrieved) {
    console.log(`Retrieved playlist has ${retrieved.songs.length} songs`);
}


// ============================================================================
// YOUR TURN: TODO EXERCISES
// ============================================================================

// TODO 1: Create your own playlist to save
// Create a Playlist object with at least 3 songs
// Make sure each song matches the Song interface!
// Stuck? Ask: "How do I create an object that matches an interface?"

const myPlaylist: Playlist = {
    // TODO: Fill in the playlist properties
    name: "",
    songs: [],
    createdDate: ""
};


// TODO 2: Convert your playlist to JSON
// Use JSON.stringify() to convert myPlaylist to a JSON string
// Print the JSON string to see what it looks like
// Meta-help: "What does JSON.stringify() do in TypeScript?"

// TODO: Create a variable jsonData and assign JSON.stringify(myPlaylist, null, 2)
// TODO: Print jsonData


// TODO 3: Parse the JSON back to an object
// Use JSON.parse() with a type assertion to convert the JSON back
// Type hint: const parsed = JSON.parse(jsonData) as Playlist;

// TODO: Parse jsonData back to a Playlist object
// TODO: Print the playlist name and song count to verify it worked


// TODO 4: Use the save and load functions
// Test the savePlaylist and loadPlaylist functions with your playlist

// TODO: Save myPlaylist with the key "myFavorites"
// TODO: Load it back using loadPlaylist("myFavorites")
// TODO: Print the loaded playlist's information


// TODO 5: Handle missing data
// Try to load a playlist that doesn't exist
// The function returns null - use an if statement to check

console.log("\n🔍 Testing Error Handling 🔍");
// TODO: Try to load a playlist with key "nonexistent"
// TODO: Check if the result is null
// TODO: Print an appropriate message


// TODO 6: Create a type guard function
// Write a function that checks if an object is a valid Song
// This is useful for validating JSON data!
// Meta-help: "What are type guards in TypeScript?"

function isSong(obj: any): obj is Song {
    // TODO: Check if obj has all required Song properties
    // TODO: Return true if valid, false otherwise
    // HINT: Check typeof obj.title === "string", etc.
    return false;  // Replace this
}

// Test your type guard
const testObj = { title: "Test", artist: "Artist", duration: 3.5, genre: "Rock" };
// TODO: Call isSong with testObj and print the result


// TODO 7: Create a function to add a song and save
// Write a function that:
// 1. Loads a playlist
// 2. Adds a new song
// 3. Saves it back
// This combines multiple concepts!

function addSongAndSave(playlistKey: string, newSong: Song): void {
    // TODO: Load the playlist using loadPlaylist
    // TODO: If playlist is null, print error and return
    // TODO: Add newSong to playlist.songs
    // TODO: Save the updated playlist
    // TODO: Print a confirmation message
}

// Test your function
const newSong: Song = {
    title: "Your Choice",
    artist: "Your Favorite Artist",
    duration: 3.30,
    genre: "Rock"
};
// TODO: Call addSongAndSave to add newSong to "myFavorites"


// TODO 8: Create multiple playlists
// Create and save at least 3 different themed playlists
// Examples: workout, chill, party, studying

// TODO: Create a workout playlist
// TODO: Create a chill playlist
// TODO: Create another themed playlist
// TODO: Save each one with a different key
// TODO: Load them back and display their names


// TODO 9: Create a function to list all saved playlists
// Write a function that returns all playlist keys from storage
// Type hint: Object.keys(storage) returns string[]

function listAllPlaylists(): string[] {
    // TODO: Return all keys from the storage object
    return [];  // Replace this
}

// TODO: Call listAllPlaylists and print the results


// TODO 10: Create a function to merge playlists
// Write a function that takes two playlist keys and creates a combined playlist
// Remove duplicate songs (same title and artist)

function mergePlaylists(key1: string, key2: string, newName: string): Playlist | null {
    // TODO: Load both playlists
    // TODO: If either is null, return null
    // TODO: Combine the songs arrays
    // TODO: Remove duplicates (this is challenging!)
    // TODO: Create and return a new Playlist object
    return null;  // Replace this
}

// Test your merge function
// TODO: Create two playlists, save them, then merge them


// ============================================================================
// BONUS CHALLENGES (Optional)
// ============================================================================

// BONUS 1: Add data validation
// Create a function validatePlaylist(obj: any): obj is Playlist
// that checks if an object is a valid Playlist with valid Songs
// Use your isSong function to validate each song!


// BONUS 2: Create a backup system
// Write a function that saves a playlist to two keys: the original and a backup
// Example: saveWithBackup saves to "myPlaylist" and "myPlaylist_backup"


// BONUS 3: Add playlist metadata
// Extend the Playlist interface to include:
// - totalDuration (calculated from songs)
// - lastModified (timestamp)
// Create functions to automatically update these when saving


// BONUS 4: Implement search functionality
// Create a function searchAllPlaylists(query: string): Song[]
// that searches through ALL saved playlists for songs matching the query


// ============================================================================
// TESTING YOUR CODE
// ============================================================================

// When you run this file, you should see:
// - Example playlist converted to JSON and back
// - Your playlist saved and loaded
// - Error handling when loading nonexistent playlists
// - Type guard validating song objects
// - Songs being added to saved playlists
// - Multiple themed playlists created and saved
// - List of all saved playlist keys
// - Playlists being merged together

// Run with: node exercise/typescript/05_playlist_saver.ts

export {};
