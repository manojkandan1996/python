import time
import random

def typing_test():
    sentences = [
        "Python is a powerful programming language.",
        "Typing speed is measured in words per minute.",
        "OpenAI and Microsoft collaborate on AI projects.",
        "Practice makes perfect when learning to type quickly."
    ]

    sentence = random.choice(sentences)
    print("\nType the following sentence:")
    print(f"\n📝 {sentence}\n")

    input("Press Enter when you're ready to start...")
    start_time = time.time()

    typed = input("\nStart typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    time_taken_minutes = time_taken / 60

    original_words = sentence.strip().split()
    typed_words = typed.strip().split()

    correct = sum(ow == tw for ow, tw in zip(original_words, typed_words))
    total_words = len(original_words)

    accuracy = (correct / total_words) * 100
    wpm = len(typed_words) / time_taken_minutes

    print("\n===== Typing Test Result =====")
    print(f"⏱ Time Taken: {time_taken:.2f} seconds")
    print(f"📏 Total Words Typed: {len(typed_words)}")
    print(f"🎯 Accuracy: {accuracy:.2f}%")
    print(f"⚡ WPM: {wpm:.2f}")

typing_test()