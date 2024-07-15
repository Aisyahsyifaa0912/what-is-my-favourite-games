import random

# Define a list of video game titles and their corresponding clues and answers
video_games = [
    {
        "title": "The Legend of Zelda: Breath of the Wild",
        "clues": [
            "This game features a hero named Link.",
            "It was released for the Nintendo Switch and Wii U.",
            "It received widespread acclaim for its open-world design.",
            "Developed and published by Nintendo."
        ],
        "options": ["Super Mario Odyssey", "Breath of the Wild", "Splatoon 2", "Mario Kart 8 Deluxe"],
        "correct_answer": "Breath of the Wild"
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "clues": [
            "Based on a series of novels by Andrzej Sapkowski.",
            "It features the main character Geralt of Rivia.",
            "Developed by CD Projekt Red.",
            "It received numerous awards including Game of the Year."
        ],
        "options": ["Divinity: Original Sin 2", "Dark Souls III", "The Witcher 3", "Dragon Age: Inquisition"],
        "correct_answer": "The Witcher 3"
    },
    {
        "title": "Red Dead Redemption 2",
        "clues": [
            "A Western-themed action-adventure game.",
            "Developed by Rockstar Games.",
            "It serves as a prequel to a previous game in the series.",
            "The protagonist is Arthur Morgan."
        ],
        "options": ["Grand Theft Auto V", "Red Dead Redemption 2", "Far Cry 5", "Borderlands 3"],
        "correct_answer": "Red Dead Redemption 2"
    }
]

def play_game():
    print("Welcome to the Video Game Guessing Game!")
    print("Try to guess the video game based on the clues provided.")
    print("")

    score = 0
    random.shuffle(video_games)

    for game in video_games:
        print("Clues:")
        for clue in game["clues"]:
            print("- " + clue)
        print("")

        print("Choose the correct game from the options:")
        for i, option in enumerate(game["options"], start=1):
            print(f"{i}. {option}")
        
        while True:
            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        user_answer = game["options"][user_choice - 1]
        correct_answer = game["correct_answer"]

        if user_answer == correct_answer:
            print("Congratulations! That's the correct answer.")
            score += 1
        else:
            print(f"Sorry, the correct answer was: {correct_answer}")

        print("")

    print(f"Game Over! Your final score is: {score}/{len(video_games)}")

if __name__ == "__main__":
    play_game()
