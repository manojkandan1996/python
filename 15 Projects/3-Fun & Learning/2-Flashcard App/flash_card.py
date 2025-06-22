import json
import random

def load_flashcards(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def run_flashcards(cards):
    score = 0
    random.shuffle(cards)

    for i, card in enumerate(cards, 1):
        print(f"\nQ{i}: {card['question']}")
        input("Press Enter to see the answer...")
        print(f"💡 Answer: {card['answer']}")

        feedback = input("Did you get it right? (y/n): ").strip().lower()
        if feedback == 'y':
            score += 1

    print(f"\n🎯 You got {score} out of {len(cards)} correct!")

# Example usage
flashcards = load_flashcards('flash_data.json')
run_flashcards(flashcards)