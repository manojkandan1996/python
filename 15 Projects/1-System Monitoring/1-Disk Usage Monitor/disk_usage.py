import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    print(f"Disk usage for path: {path}")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used: {used // (2**30)} GB")
    print(f"Free: {free // (2**30)} GB")

get_disk_usage()  # You can change this to another path like "C:\\" on Windows