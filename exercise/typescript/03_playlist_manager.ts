/**
 * Exercise 3: Playlist Manager
 *
 * Functions in TypeScript are typed too! You specify types for parameters and return values.
 * This makes your code safer and helps catch errors before running.
 *
 * Concepts covered:
 * - Function declarations with type annotations
 * - Parameter types and return types
 * - void return type (for functions that don't return anything)
 * - Type inference in function returns
 * - Function signatures as documentation
 *
 * Run this exercise: node exercise/typescript/03_playlist_manager.ts
 */

// ============================================================================
// WHAT ARE TYPED FUNCTIONS?
// ============================================================================
// In TypeScript, functions have types for:
// 1. Parameters - what goes IN (always use explicit types!)
// 2. Return value - what comes OUT (can be explicit or inferred)
//
// Syntax:
// function name(param: type): returnType { }
//
// IMPORTANT: Always explicitly type function parameters!
// TypeScript can't infer parameter types, so you MUST specify them.
// Return types can be inferred, but explicit types are good documentation.


// ============================================================================
// TYPE DEFINITIONS
// ============================================================================

// We'll use these types for our music functions
// (You'll learn more about interfaces in the next exercise!)


// ============================================================================
// EXAMPLE CODE
// ============================================================================

// Function with NO parameters and NO return value (void)
function greetMusicLover(): void {
    console.log("🎵 Welcome, music lover! 🎵");
}

greetMusicLover();


// Function with parameters (MUST be explicitly typed)
function displaySong(title: string, artist: string): void {
    console.log(`♪ ${title} by ${artist}`);
}

displaySong("Imagine", "John Lennon");
displaySong("Thriller", "Michael Jackson");


// Function that RETURNS a value (return type can be explicit or inferred)
function calculateTotalDuration(song1Minutes: number, song2Minutes: number): number {
    const total = song1Minutes + song2Minutes;
    return total;
}

// TypeScript knows totalTime is a number!
const totalTime = calculateTotalDuration(3.5, 4.2);
console.log(`\nTotal playlist duration: ${totalTime} minutes`);


// Function with inferred return type (TypeScript figures it out)
function formatDuration(minutes: number) {  // Return type is inferred as string
    const wholeMinutes = Math.floor(minutes);
    const seconds = Math.floor((minutes - wholeMinutes) * 60);
    return `${wholeMinutes}m ${seconds}s`;
}

console.log(`Formatted: ${formatDuration(3.5)}`);
// Hover over formatDuration to see TypeScript inferred the return type!


// Function with array parameter
function countSongs(playlist: string[]): number {
    return playlist.length;
}

const myList = ["Song 1", "Song 2", "Song 3"];
console.log(`Song count: ${countSongs(myList)}`);


// ============================================================================
// YOUR TURN: TODO EXERCISES
// ============================================================================

// TODO 1: Create a function to add a song to a playlist
// Write a function called addSong with:
// - Parameters: playlist (string[]), songName (string)
// - Return type: void
// The function should add the song and print a confirmation
// Stuck? Ask: "How do I write a typed function in TypeScript?"

function addSong(playlist: string[], songName: string): void {
    // TODO: Use .push() to add songName to playlist
    // TODO: Print a message like "Added 'Song Name' to playlist"
}


// TODO 2: Test your addSong function
const myPlaylist: string[] = ["Yesterday", "Let It Be"];
console.log("\n🎵 Building My Playlist 🎵");
// TODO: Call addSong to add "Hey Jude" to myPlaylist
// TODO: Call addSong to add another song of your choice
// TODO: Print myPlaylist to see the results


// TODO 3: Create a function that returns a value
// Write a function called countSongsInPlaylist that:
// - Takes a playlist (string[]) parameter
// - Returns the count (number)
// Type hint: Always explicitly type parameters, return type is optional but recommended!

function countSongsInPlaylist(playlist: string[]): number {
    // TODO: Return the length of the playlist
    return 0;  // Replace this
}

// Test it
// TODO: Call countSongsInPlaylist with myPlaylist and print the result


// TODO 4: Create a function to calculate total playlist duration
// Write a function called totalPlaylistDuration that:
// - Takes durations (number[]) parameter
// - Returns the total (number)
// HINT: Use reduce() or a loop to sum the array
// Meta-help: "How do I sum an array of numbers in TypeScript?"

function totalPlaylistDuration(durations: number[]): number {
    // TODO: Calculate the sum of all durations
    // TODO: Return the total
    return 0;  // Replace this
}

// Test your function
const songDurations: number[] = [3.5, 4.2, 2.8, 5.1, 3.3];
// TODO: Call totalPlaylistDuration and print the result


// TODO 5: Create a function to find the longest song
// Write a function that takes durations (number[]) and returns the max
// Let TypeScript INFER the return type this time (don't specify it)

function findLongestSong(durations: number[]) {
    // TODO: Use Math.max() with the spread operator: Math.max(...durations)
    // TODO: Return it
    return 0;  // Replace this
}

// Test it
// TODO: Call findLongestSong and print the result
// Type experiment: Hover over the function to see TypeScript inferred return type: number


// TODO 6: Create a function with multiple parameters
// Write a function called createSongInfo that:
// - Takes: title (string), artist (string), duration (number)
// - Returns: a formatted string (string)
// Practice explicit typing for all parameters AND the return type

function createSongInfo(title: string, artist: string, duration: number): string {
    // TODO: Return a formatted string like: "Title by Artist (3.5 minutes)"
    return "";  // Replace this
}

// Test it
// TODO: Call createSongInfo with your favorite song and print the result


// TODO 7: Function with optional parameter
// TypeScript lets you make parameters optional with ?
// Create a function displaySongInfo that takes title (string) and optionally artist (string)
// Meta-help: "How do I create optional parameters in TypeScript?"

function displaySongInfo(title: string, artist?: string): void {
    // TODO: If artist is provided, print "Title by Artist"
    // TODO: If artist is NOT provided, print just "Title"
    // HINT: Use if (artist) { } to check if it's provided
}

// Test both cases
// TODO: Call displaySongInfo with just a title
// TODO: Call displaySongInfo with title and artist


// ============================================================================
// BONUS CHALLENGES (Optional)
// ============================================================================

// BONUS 1: Create a function with a default parameter
// TypeScript allows default values: function greet(name: string = "friend")
// Create a function that has a default genre parameter


// BONUS 2: Create a function that returns multiple values using a tuple
// Return type: [string, number] for [title, duration]
// Example: function getFirstSong(): [string, number] { return ["Song", 3.5]; }


// BONUS 3: Function overloading
// TypeScript supports function overloads - multiple signatures for the same function
// This is advanced! Try asking: "How does function overloading work in TypeScript?"


// ============================================================================
// TESTING YOUR CODE
// ============================================================================

// When you run this file, you should see:
// - Example functions working (greet, displaySong, calculateTotalDuration)
// - Your addSong function adding songs to a playlist
// - Your countSongsInPlaylist returning the count
// - Your totalPlaylistDuration calculating total time
// - Your findLongestSong finding the max duration
// - Your createSongInfo returning a formatted string
// - Your displaySongInfo working with and without the optional parameter

// Run with: node exercise/typescript/03_playlist_manager.ts

export {};
