import argparse
from datetime import datetime
import os

DIARY_FILE = "diary.txt"

def write_entry(text):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(DIARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n{text}\n{'-'*40}\n")
    print("📝 Entry saved!")

def read_entries():
    if not os.path.exists(DIARY_FILE):
        print("📂 No diary entries found.")
        return
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        print("\n📖 Diary Entries:\n")
        print(f.read())

def main():
    parser = argparse.ArgumentParser(description="Personal Diary CLI")
    subparsers = parser.add_subparsers(dest="command")

    write_parser = subparsers.add_parser("write", help="Write a new diary entry")
    write_parser.add_argument("entry", help="Your diary entry text in quotes")

    subparsers.add_parser("read", help="Read all diary entries")

    args = parser.parse_args()

    if args.command == "write":
        write_entry(args.entry)
    elif args.command == "read":
        read_entries()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
