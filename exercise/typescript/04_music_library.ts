/**
 * Exercise 4: Music Library
 *
 * Now for TypeScript's superpower: INTERFACES! Interfaces define the shape of objects,
 * making your code self-documenting and catching errors at compile-time.
 *
 * Concepts covered:
 * - Interfaces (defining object shapes)
 * - Object types and type annotations
 * - Arrays of objects with interfaces
 * - Nested data structures
 * - Type safety for complex data
 *
 * Run this exercise: node exercise/typescript/04_music_library.ts
 */

// ============================================================================
// WHAT ARE INTERFACES?
// ============================================================================
// Interfaces define the "shape" of an object - what properties it has and their types.
// Think of it as a blueprint or contract for objects.
//
// Why use interfaces?
// 1. Type safety - TypeScript catches missing or wrong properties
// 2. Documentation - Anyone reading your code knows what data looks like
// 3. Autocomplete - Your editor can suggest properties!
// 4. Refactoring safety - Change the interface, find all problems instantly


// ============================================================================
// TYPE DEFINITIONS
// ============================================================================

// Define an interface for a song
interface Song {
    title: string;
    artist: string;
    album?: string;      // ? means optional property
    duration: number;
    year: number;
    genre: string;
    rating?: number;     // Optional rating (1-5)
}

// You can also define types (similar to interfaces for objects)
type PlaylistName = string;


// ============================================================================
// EXAMPLE CODE
// ============================================================================

// Creating an object that matches the Song interface
const song: Song = {
    title: "Bohemian Rhapsody",
    artist: "Queen",
    album: "A Night at the Opera",
    duration: 5.55,
    year: 1975,
    genre: "Rock"
    // rating is optional, so we can omit it
};

console.log("🎵 Song Object Example 🎵");
console.log(`Title: ${song.title}`);
console.log(`Artist: ${song.artist}`);
console.log(`Duration: ${song.duration} minutes`);

// TypeScript PREVENTS typos and wrong types!
// Try these and see errors:
// song.titl = "test";        // ERROR! Property 'titl' doesn't exist
// song.duration = "5:55";    // ERROR! Can't assign string to number

// Adding a property
song.rating = 5;
console.log(`Rating: ${song.rating} stars`);

// Looping through object properties
console.log("\n🎵 All song information:");
for (const key in song) {
    console.log(`${key}: ${song[key as keyof Song]}`);
}


// Creating an array of Song objects (typed!)
const musicLibrary: Song[] = [
    {
        title: "Imagine",
        artist: "John Lennon",
        duration: 3.03,
        year: 1971,
        genre: "Pop"
    },
    {
        title: "Billie Jean",
        artist: "Michael Jackson",
        duration: 4.54,
        year: 1982,
        genre: "Pop"
    },
    {
        title: "Smells Like Teen Spirit",
        artist: "Nirvana",
        duration: 5.01,
        year: 1991,
        genre: "Rock"
    }
];

console.log("\n🎵 Music Library 🎵");
for (const song of musicLibrary) {
    console.log(`♪ ${song.title} by ${song.artist} (${song.genre})`);
}

// TypeScript ensures every object in the array matches the Song interface!


// ============================================================================
// YOUR TURN: TODO EXERCISES
// ============================================================================

// TODO 1: Create your own song object
// Create a constant called mySong with type Song
// Include: title, artist, album, duration, year, genre, rating
// Stuck? Ask: "How do I create an object that matches an interface in TypeScript?"

const mySong: Song = {
    // TODO: Fill in all the properties for your favorite song
    title: "",
    artist: "",
    duration: 0,
    year: 0,
    genre: ""
};


// TODO 2: Display your song information
// Print at least 4 properties from mySong
// Type experiment: Notice how your editor autocompletes property names!

console.log("\n🎵 My Favorite Song 🎵");
// TODO: Print the title
// TODO: Print the artist
// TODO: Print the genre
// TODO: Print the rating (if you added it)


// TODO 3: Create your music library
// Create an array called myLibrary with type Song[]
// Add at least 3 song objects
// HINT: Each object must match the Song interface exactly!

const myLibrary: Song[] = [
    // TODO: Add at least 3 song objects here
];


// TODO 4: Loop through your library
// Use a for...of loop to display all songs
// Meta-help: "How do I iterate over an array of objects in TypeScript?"

console.log("\n🎵 My Music Library 🎵");
// TODO: Loop through myLibrary
// TODO: Print each song's title and artist


// TODO 5: Filter songs by genre
// Loop through and print only songs of a specific genre
// HINT: Use an if statement inside the loop

console.log("\n🎵 Filtering by Genre 🎵");
// TODO: Pick a genre from your library
// TODO: Print only songs that match that genre


// TODO 6: Calculate library statistics
// Calculate and print:
// - Total songs
// - Total duration
// - Average duration

console.log("\n📊 Library Statistics 📊");
// TODO: Print total songs (use myLibrary.length)
// TODO: Loop to calculate total duration
// TODO: Calculate and print average duration


// TODO 7: Create a function to find songs by artist
// Write a typed function that returns an array of songs
// Function signature: findSongsByArtist(library: Song[], artistName: string): Song[]
// Type hint: Notice how the return type is Song[] - an array of Song objects!

function findSongsByArtist(library: Song[], artistName: string): Song[] {
    // TODO: Create an empty array with type Song[]
    // TODO: Loop through the library
    // TODO: If song.artist matches artistName, add to the array
    // TODO: Return the array
    return [];  // Replace this
}

// Test your function
// TODO: Call findSongsByArtist with an artist from your library
// TODO: Print the results


// TODO 8: Create an interface for a Playlist
// Define a new interface called Playlist with:
// - name (string)
// - songs (Song[])
// - createdDate (string)
// Then create a playlist object using this interface
// Meta-help: "How do I create nested interfaces in TypeScript?"

interface Playlist {
    // TODO: Define the properties
}

// TODO: Create a playlist object using your Playlist interface
// TODO: Add some songs from your library to it


// ============================================================================
// BONUS CHALLENGES (Optional)
// ============================================================================

// BONUS 1: Add a method to the Playlist interface
// Interfaces can include function signatures!
// Try adding: getTotalDuration(): number;
// Then implement it in your playlist object


// BONUS 2: Create a union type for Genre
// Instead of genre: string, create: type Genre = "Rock" | "Pop" | "Jazz" | "Classical"
// This restricts genre to only these values!
// Then update the Song interface to use this type


// BONUS 3: Create a function with a generic type
// Generics let you create flexible, reusable functions
// Try: function getFirst<T>(array: T[]): T | undefined
// This is advanced! Ask: "How do generics work in TypeScript?"


// BONUS 4: Use the Record type
// Create an object that groups songs by genre
// Type: Record<string, Song[]> means keys are strings, values are Song arrays


// ============================================================================
// TESTING YOUR CODE
// ============================================================================

// When you run this file, you should see:
// - Example song object with type safety
// - Your favorite song displayed
// - Your music library with multiple songs
// - Songs filtered by genre
// - Library statistics (count, total/average duration)
// - Results from finding songs by artist
// - A playlist object with songs

// Run with: node exercise/typescript/04_music_library.ts

export {};
