import json

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("Your answer (1-4): "))
            if q['options'][answer - 1].lower() == q['answer'].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The answer is {q['answer']}.")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.")
    
    print(f"\n🎉 Your final score: {score} out of {len(questions)}")

# Run the quiz
questions = load_questions('quiz_data.json')
run_quiz(questions)