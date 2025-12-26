/**
 * Exercise 2: Song Collection
 *
 * Learn about arrays (TypeScript's version of lists) and how to type them properly.
 * Arrays can hold multiple items, and TypeScript ensures all items are the correct type!
 *
 * Concepts covered:
 * - Arrays and array types
 * - Type annotations for arrays
 * - Array methods (push, length, etc.)
 * - Loops (for...of and traditional for)
 * - Type safety with collections
 *
 * Run this exercise: node exercise/typescript/02_song_collection.ts
 */

// ============================================================================
// WHAT ARE TYPED ARRAYS?
// ============================================================================
// In TypeScript, arrays have types too! This ensures all items match.
//
// Two ways to declare array types:
// 1. string[] - array of strings
// 2. Array<string> - also array of strings (generic syntax)
//
// TypeScript will enforce that you only add the correct type to the array!


// ============================================================================
// EXAMPLE CODE
// ============================================================================

// Method 1: Explicit array type annotation
const playlist: string[] = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"];

console.log("🎵 My Playlist 🎵");
console.log(playlist);

// Accessing items (same as Python, starts at 0)
console.log("\nFirst song:", playlist[0]);
console.log("Second song:", playlist[1]);
console.log("Third song:", playlist[2]);

// Array length
console.log("\nTotal songs:", playlist.length);

// Adding items (push instead of append)
playlist.push("Imagine");
console.log("\nAfter adding a song:", playlist);

// TypeScript PREVENTS wrong types!
// Try this and see the error:
// playlist.push(123);  // ERROR! Can't add number to string[]

// Method 2: Type inference for arrays
const numbers = [1, 2, 3, 4];  // TypeScript infers: number[]
const mixed = ["text", 42];    // TypeScript infers: (string | number)[] - union type!

// Looping through arrays
console.log("\n🎵 Playing all songs:");
for (const song of playlist) {
    console.log("♪ Now playing:", song);
}

// Traditional for loop with index
console.log("\n🎵 Numbered playlist:");
for (let i = 0; i < playlist.length; i++) {
    console.log(`${i + 1}. ${playlist[i]}`);
}


// ============================================================================
// YOUR TURN: TODO EXERCISES
// ============================================================================

// TODO 1: Create your own playlist with EXPLICIT type annotation
// Create an array called myPlaylist with type string[]
// Add at least 5 of your favorite songs
// Stuck? Ask: "How do I create a typed array in TypeScript?"

const myPlaylist: string[] = [];  // TODO: Add your favorite songs here


// TODO 2: Display playlist information
// Print the total number of songs and the entire array
// HINT: Use .length property

console.log("\n🎵 My Personal Playlist 🎵");
// TODO: Print how many songs are in myPlaylist
// TODO: Print the entire myPlaylist


// TODO 3: Access specific songs
// Print the first and last song in your playlist
// HINT: First is index 0, last is playlist[playlist.length - 1]
// TypeScript note: Hover over the variables to see TypeScript knows they're strings!

// TODO: Print your first song
// TODO: Print your last song
// Type experiment: What type does myPlaylist[0] have? Hover to see!


// TODO 4: Add more songs
// Use the .push() method to add 2 more songs

// TODO: Add a 6th song
// TODO: Add a 7th song
// TODO: Print the playlist to see the additions

// Type challenge: Try adding a number instead of a string and see the error!


// TODO 5: Loop through your playlist
// Use a for...of loop to print each song
// Meta-help: "What's the difference between for...of and regular for loops?"

console.log("\n🎵 Now Playing:");
// TODO: Write a for...of loop to print each song in myPlaylist


// TODO 6: Create a numbered playlist
// Use a traditional for loop with index to print numbered songs

console.log("\n🎵 Playlist (numbered):");
// TODO: Write a for loop using an index variable
// TODO: Print each song with its number


// TODO 7: Create a typed array of numbers
// Make an array of song durations (in minutes) with explicit type annotation
// This practices typing arrays of numbers

const songDurations: number[] = [];  // TODO: Add at least 5 durations (e.g., 3.45, 4.20)

// TODO: Calculate and print the total duration using a loop
// HINT: Create a variable total, loop through, add each duration


// TODO 8: Type inference practice
// Create arrays WITHOUT type annotations and let TypeScript infer

// TODO: Create an array of artist names (let TypeScript infer string[])
// TODO: Create an array of release years (let TypeScript infer number[])
// TODO: Print both arrays
// Type experiment: Hover over these variables to see the inferred types!


// ============================================================================
// BONUS CHALLENGES (Optional)
// ============================================================================

// BONUS 1: Filter songs by length
// Create a new array with only songs that have titles longer than 10 characters
// HINT: Use the .filter() method
// Type hint: TypeScript knows the filtered array is still string[]!


// BONUS 2: Sort your playlist
// Use the .sort() method to alphabetically sort a COPY of your playlist
// HINT: Use [...myPlaylist].sort() to create a sorted copy
// Meta-help: "How do I sort an array in TypeScript without modifying the original?"


// BONUS 3: Create a tuple for song info
// Tuples are fixed-length arrays with specific types for each position
// Example: [string, string, number] for [title, artist, duration]
// Try asking: "What are tuples in TypeScript and how do they differ from arrays?"


// ============================================================================
// TESTING YOUR CODE
// ============================================================================

// When you run this file, you should see:
// - Example playlist with type safety
// - Your personal playlist with at least 5 songs
// - First and last songs displayed
// - Playlist with 2 more songs added (7 total)
// - All songs displayed in a loop
// - Numbered playlist
// - Duration calculations

// Run with: node exercise/typescript/02_song_collection.ts

export {};
