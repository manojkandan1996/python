import time
import argparse
import platform

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        print('\a')  # Beep for Linux/macOS

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\r⏳ {mins:02d}:{secs:02d}", end='')
        time.sleep(1)
        seconds -= 1
    print("\r⏰ 00:00")

def pomodoro(work_min=25, break_min=5, rounds=1):
    for i in range(rounds):
        print(f"\n🍅 Pomodoro #{i+1} – Work for {work_min} minutes")
        countdown(work_min * 60)
        print("⏸️ Break time!")
        beep()
        if i < rounds - 1:
            countdown(break_min * 60)
            print("✅ Break over!")
            beep()
    print("\n🎉 All sessions complete! Great job!")
    beep()

def main():
    parser = argparse.ArgumentParser(description="Pomodoro Timer CLI")
    parser.add_argument("--work", type=int, default=25, help="Work duration in minutes")
    parser.add_argument("--short-break", type=int, default=5, help="Short break in minutes")
    parser.add_argument("--rounds", type=int, default=1, help="Number of pomodoro rounds")
    args = parser.parse_args()

    pomodoro(args.work, args.short_break, args.rounds)

if __name__ == "__main__":
    main()
