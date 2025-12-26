/**
 * Exercise 1: My First Playlist
 *
 * Welcome to TypeScript! You'll learn the same concepts as the Python version,
 * but with TypeScript's type system that helps catch errors before you run your code.
 *
 * Concepts covered:
 * - Variables (storing data in named containers)
 * - Data types (strings, numbers, booleans)
 * - Type annotations and type inference
 * - Console output
 * - Basic calculations
 *
 * Run this exercise: node exercise/typescript/01_my_first_playlist.ts
 */

// ============================================================================
// WHAT ARE TYPES IN TYPESCRIPT?
// ============================================================================
// TypeScript adds TYPES to JavaScript. Types tell you what kind of data a variable holds.
// There are two ways to use types:
//
// 1. EXPLICIT TYPE ANNOTATIONS - You tell TypeScript the type:
//    const name: string = "value"
//
// 2. TYPE INFERENCE - TypeScript figures out the type automatically:
//    const name = "value"  // TypeScript knows this is a string!
//
// Both approaches provide type safety! TypeScript enforces types either way.
// Let's see both in action...


// ============================================================================
// EXAMPLE CODE
// ============================================================================

// Method 1: EXPLICIT type annotations (great for learning!)
const songTitle: string = "Bohemian Rhapsody";  // Type annotation: : string
const artist: string = "Queen";
const durationMinutes: number = 5.55;  // Type annotation: : number
const yearReleased: number = 1975;
const isFavorite: boolean = true;  // Type annotation: : boolean

// Method 2: TYPE INFERENCE (TypeScript is smart!)
const songTitle2 = "Imagine";  // TypeScript infers: string
const artist2 = "John Lennon";  // TypeScript infers: string
const duration2 = 3.03;  // TypeScript infers: number

// IMPORTANT: Even with inference, TypeScript enforces types!
// Try this and you'll get an error:
// let test = true;  // TypeScript infers: boolean
// test = "hello";   // ERROR! Can't assign string to boolean

console.log("🎵 Song Information (with explicit types) 🎵");
console.log("Title:", songTitle);
console.log("Artist:", artist);
console.log("Duration:", durationMinutes, "minutes");
console.log("Released:", yearReleased);
console.log("Favorite?", isFavorite);

// Calculations work the same way
const durationSeconds: number = durationMinutes * 60;
console.log("That's", durationSeconds, "seconds!");

console.log("\n🎵 Song Information (with type inference) 🎵");
console.log("Title:", songTitle2);
console.log("Artist:", artist2);

// ============================================================================
// YOUR TURN: TODO EXERCISES
// ============================================================================

// TODO 1: Create variables for YOUR favorite song using EXPLICIT type annotations
// Practice adding : string, : number, : boolean after variable names
// Stuck? Ask your AI assistant: "How do I add type annotations in TypeScript?"

const mySongTitle: string = "TODO: Put your song title here";
const myArtist: string = "TODO: Put the artist name here";
const myDuration: number = 0.0;  // TODO: Change to actual duration
const myYear: number = 2024;  // TODO: Change to release year
const myIsFavorite: boolean = true;  // Already correct!

// Type hint: Notice how the : type syntax tells TypeScript what each variable holds


// TODO 2: Display your song information
// Use console.log() to show your song's details
// HINT: Look at the example above

console.log("\n🎵 My Favorite Song 🎵");
// TODO: Add console.log statements to display:
// - Your song title
// - Your artist
// - Your duration
// - Your year
// - Whether it's your favorite


// TODO 3: Calculate duration in seconds using type inference
// This time, DON'T add type annotations - let TypeScript infer the type!
// Meta-help: "What's the difference between type annotations and type inference?"

// TODO: Create a variable called myDurationSeconds (no type annotation!)
// TODO: Calculate it by multiplying myDuration by 60
// TODO: Print the result
// Experiment: Hover over myDurationSeconds in your editor - TypeScript knows it's a number!


// TODO 4: Create a second song with mixed annotation styles
// Practice BOTH explicit annotations AND inference
// For example: use explicit types for strings, let TypeScript infer numbers

// TODO: Create variables for a second song
// TODO: Use explicit type annotation for song2Title and song2Artist
// TODO: Let TypeScript infer the types for song2Duration and song2Year
// TODO: Print all the information

// Type challenge: Try assigning a wrong type to see TypeScript catch the error!
// For example, try: let test: number = "hello";  (this will error!)


// ============================================================================
// BONUS CHALLENGES (Optional)
// ============================================================================

// BONUS 1: Calculate total duration with explicit return type awareness
// Add the durations of both songs
// Type hint: When you add two numbers, TypeScript infers the result is a number


// BONUS 2: Combine strings using the + operator
// Create a variable that combines song title and artist
// Example: "Bohemian Rhapsody by Queen"
// Try both with and without type annotations - TypeScript will infer string!


// BONUS 3: Type experimentation
// Try these experiments to understand TypeScript's type checking:
// 1. Create a variable with inference, then try to assign a different type
// 2. Create a variable with explicit type, then try to assign a wrong type
// 3. Hover over variables in your editor to see inferred types


// ============================================================================
// TESTING YOUR CODE
// ============================================================================

// When you run this file, you should see:
// - Example song information (with both annotation styles)
// - YOUR favorite song information
// - Duration calculations in seconds
// - Your second song's information

// Run with: node exercise/typescript/01_my_first_playlist.ts

// Make this file a module to avoid variable name conflicts
export {};
