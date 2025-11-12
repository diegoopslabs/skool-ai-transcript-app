"""
Student Profile Quiz
====================
This script collects information about your programming background and interests
to create a personalized learning experience with AI-generated exercises.

Run this script first before using EXERCISE_GENERATOR.md with your AI agent.
"""

from pathlib import Path
from datetime import datetime


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def get_choice(question, options, allow_multiple=False):
    """Get user choice from a list of options."""
    print(question)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")

    if allow_multiple:
        print("\nEnter numbers separated by commas (e.g., 1,3,4):")
    else:
        print("\nEnter number:")

    while True:
        try:
            response = input("> ").strip()
            if not response:
                print("Please enter a value.")
                continue

            if allow_multiple:
                # Filter out empty strings from split (handles cases like "1,,3" or ",1,2,")
                choices = [int(x.strip()) for x in response.split(",") if x.strip()]
                if not choices:
                    print("Please enter at least one number.")
                    continue
                if all(1 <= c <= len(options) for c in choices):
                    return [options[c - 1] for c in choices]
            else:
                choice = int(response)
                if 1 <= choice <= len(options):
                    return options[choice - 1]
            print(f"Please enter valid number(s) between 1 and {len(options)}")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")


def get_text(question, required=True):
    """Get free text input from user."""
    print(question)
    while True:
        response = input("> ").strip()
        if response or not required:
            return response
        print("This field is required. Please provide an answer.")


def main():
    print_header("Welcome to the AI-Powered Learning Experience!")

    print("This quiz will help create personalized programming exercises just for you.")
    print("Your responses will be saved to exercise/STUDENT_PROFILE.md, which an AI agent will")
    print("use to generate custom exercises in Python and TypeScript.")
    print("\nLet's get started!\n")

    profile = {}

    # Question 1: Programming experience
    print_header("Programming Experience")
    has_programmed = get_choice(
        "Have you programmed before?",
        ["Yes, I have programming experience", "No, I'm completely new to programming"]
    )
    profile["has_programmed"] = has_programmed.startswith("Yes")

    # Question 2: Languages (if applicable)
    if profile["has_programmed"]:
        print_header("Programming Languages")
        languages = get_choice(
            "Which programming languages have you used? (select all that apply)",
            [
                "Python",
                "JavaScript/TypeScript",
                "Java",
                "C/C++",
                "Go",
                "Ruby",
                "PHP",
                "Other"
            ],
            allow_multiple=True
        )
        profile["languages"] = languages

        if "Other" in languages:
            other_langs = get_text("Please specify other languages:")
            profile["other_languages"] = other_langs
    else:
        profile["languages"] = []

    # Question 3: Skill level
    print_header("Skill Level")
    skill_level = get_choice(
        "How would you rate your programming skill level?",
        [
            "Complete Beginner (never written code)",
            "Beginner (basic understanding, need lots of guidance)",
            "Intermediate (comfortable with basics, ready for complex concepts)",
            "Advanced (experienced, looking for deeper understanding)"
        ]
    )
    profile["skill_level"] = skill_level

    # Question 4: Interest theme
    print_header("Exercise Theme")
    print("Programming is more fun when it relates to your interests!")
    interest_theme = get_choice(
        "What topic would you like your exercises to be based on?",
        [
            "Fitness & Gym (workout tracking, exercise logs, fitness calculators)",
            "Sports (statistics, team management, game simulation)",
            "Music (playlist management, audio processing, music theory)",
            "Cooking (recipe management, meal planning, nutrition)",
            "Finance (budgeting, investment tracking, expense analysis)",
            "Gaming (game mechanics, character stats, inventory systems)",
            "Other (describe your interest)"
        ]
    )
    profile["interest_theme"] = interest_theme

    if "Other" in interest_theme:
        custom_theme = get_text("Please describe your interest:")
        profile["custom_theme"] = custom_theme

    # Question 5: Specific interest details
    print_header("Specific Focus")
    specific_focus = get_text(
        "Within this theme, is there something specific you'd like to explore?\n"
        "(e.g., 'powerlifting tracking', 'soccer statistics', 'recipe scaling')\n"
        "Leave blank if you're open to anything:",
        required=False
    )
    if specific_focus:
        profile["specific_focus"] = specific_focus

    # Question 6: Learning style
    print_header("Learning Style")
    learning_style = get_choice(
        "What learning approach works best for you?",
        [
            "Hands-on (I learn by doing and experimenting)",
            "Conceptual (I prefer understanding theory first)",
            "Balanced (Mix of explanation and practice)",
            "Exploratory (Give me challenges and let me figure it out)"
        ]
    )
    profile["learning_style"] = learning_style

    # Question 7: Time commitment
    print_header("Scope")
    scope = get_choice(
        "What kind of exercise experience are you looking for?",
        [
            "Quick Start (1-2 simple exercises, ~30 minutes)",
            "Standard Workshop (3-5 exercises, ~2 hours)",
            "Deep Dive (Comprehensive series, 4+ hours)",
            "Let the AI decide based on my profile"
        ]
    )
    profile["scope"] = scope

    # Generate profile document
    print_header("Generating Your Profile")

    profile["timestamp"] = datetime.now().isoformat()

    markdown_content = generate_markdown(profile)

    # Save to file in exercise directory
    output_path = Path("exercise/STUDENT_PROFILE.md")
    # Ensure the directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown_content, encoding="utf-8")

    print(f"✓ Profile saved to {output_path}")
    print("\n" + "=" * 70)
    print("  Next Steps")
    print("=" * 70)
    print("\n1. Review your profile in exercise/STUDENT_PROFILE.md")
    print("2. Open exercise/EXERCISE_GENERATOR.md with your AI agent (e.g., Claude Code)")
    print("3. The AI will read your profile and create personalized exercises")
    print("4. Start learning!\n")
    print("Tip: You can re-run this script anytime to update your profile.\n")


def generate_markdown(profile):
    """Generate markdown content for the student profile."""
    content = [
        "# Student Profile",
        "",
        "## Programming Background",
        "",
        f"**Has Programmed Before:** {'Yes' if profile['has_programmed'] else 'No'}",
        ""
    ]

    # Show languages only if there are any (excluding "Other")
    languages_to_show = [lang for lang in profile.get("languages", []) if lang != "Other"]
    if languages_to_show or profile.get("other_languages"):
        content.append("**Familiar Languages:**")
        for lang in languages_to_show:
            content.append(f"- {lang}")
        if profile.get("other_languages"):
            content.append(f"- {profile['other_languages']}")
        content.append("")

    content.extend([
        f"**Skill Level:** {profile['skill_level']}",
        "",
        "## Learning Preferences",
        "",
    ])

    # Show custom theme if provided, otherwise show selected theme
    if profile.get("custom_theme"):
        content.extend([
            f"**Interest Theme:** {profile['custom_theme']} (custom)",
            ""
        ])
    else:
        content.extend([
            f"**Interest Theme:** {profile['interest_theme']}",
            ""
        ])

    if profile.get("specific_focus"):
        content.extend([
            f"**Specific Focus:** {profile['specific_focus']}",
            ""
        ])

    content.extend([
        f"**Learning Style:** {profile['learning_style']}",
        "",
        f"**Exercise Scope:** {profile['scope']}",
    ])

    return "\n".join(content)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nQuiz cancelled. Run the script again when you're ready!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please report this issue if it persists.")
