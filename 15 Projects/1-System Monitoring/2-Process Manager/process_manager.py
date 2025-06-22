import psutil

def list_processes():
    print(f"{'PID':<10}{'Name':<25}{'Status'}")
    print("-" * 50)
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            print(f"{proc.info['pid']:<10}{proc.info['name']:<25}{proc.info['status']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=3)
        print(f"Process {pid} terminated.")
    except psutil.NoSuchProcess:
        print("No such process found.")
    except psutil.AccessDenied:
        print("Permission denied to terminate this process.")
    except Exception as e:
        print(f"Error: {e}")

# Main Interface
list_processes()
pid = int(input("\nEnter the PID of the process to kill: "))
kill_process(pid)