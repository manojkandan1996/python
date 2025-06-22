import json, os, time, argparse
from datetime import datetime

FILE = "times.json"
STATE = "current.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def save_state(task):
    with open(STATE, "w") as f:
        json.dump({"task": task, "start": time.time()}, f)

def load_state():
    if not os.path.exists(STATE):
        return None
    with open(STATE) as f:
        return json.load(f)

def delete_state():
    if os.path.exists(STATE):
        os.remove(STATE)

def start(task):
    if load_state():
        print("⚠️ A task is already running. Stop it first.")
        return
    save_state(task)
    print(f"▶️ Started tracking: {task}")

def stop():
    state = load_state()
    if not state:
        print("❌ No task is currently running.")
        return
    elapsed = time.time() - state["start"]
    task = state["task"]
    data = load_data()
    data[task] = data.get(task, 0) + elapsed
    save_data(data)
    delete_state()
    print(f"⏹️ Stopped: {task} | Time: {round(elapsed/60, 2)} min")

def report():
    data = load_data()
    if not data:
        print("No time tracked yet.")
        return
    print("📊 Time Spent on Tasks:")
    for task, seconds in data.items():
        mins = round(seconds / 60, 2)
        print(f"- {task}: {mins} min")

def main():
    parser = argparse.ArgumentParser(description="Time Tracker CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("start").add_argument("task")
    sub.add_parser("stop")
    sub.add_parser("report")

    args = parser.parse_args()
    if args.cmd == "start":
        start(args.task)
    elif args.cmd == "stop":
        stop()
    elif args.cmd == "report":
        report()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
