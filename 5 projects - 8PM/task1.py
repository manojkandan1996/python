#!/usr/bin/env python3
import argparse, json, os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {'pending': [], 'completed': []}
    with open(TASKS_FILE) as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def cmd_list(args):
    tasks = load_tasks()['pending']
    if not tasks:
        print("No pending tasks.")
    else:
        print("Pending Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def cmd_completed(args):
    tasks = load_tasks()['completed']
    if not tasks:
        print("No completed tasks.")
    else:
        print("Completed Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def cmd_add(args):
    tasks = load_tasks()
    tasks['pending'].append(args.desc)
    save_tasks(tasks)
    print(f'Added: "{args.desc}"')

def cmd_done(args):
    tasks = load_tasks()
    try:
        t = tasks['pending'].pop(args.idx - 1)
        tasks['completed'].append(t)
        save_tasks(tasks)
        print(f'Marked done: "{t}"')
    except IndexError:
        print("❌ Invalid task number.")

def main():
    parser = argparse.ArgumentParser(prog='task1.py',
        description="Simple CLI To‑Do")  # auto help & usage from argparse :contentReference[oaicite:1]{index=1}
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('list', help='List pending tasks').set_defaults(func=cmd_list)
    sub.add_parser('completed', help='View completed tasks').set_defaults(func=cmd_completed)

    p_add = sub.add_parser('add', help='Add a new task')
    p_add.add_argument('desc', help='Task description')
    p_add.set_defaults(func=cmd_add)

    p_done = sub.add_parser('done', help='Mark task as completed')
    p_done.add_argument('idx', type=int, help='Task number to mark done')
    p_done.set_defaults(func=cmd_done)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
