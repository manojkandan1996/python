import psutil
import time
import winsound

def check_battery(threshold=20):
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}% | Charging: {'Yes' if plugged else 'No'}")

    if percent <= threshold and not plugged:
        print("⚠️ Battery low! Please plug in the charger.")
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 sec

# Check battery every 60 seconds
while True:
    check_battery()
    time.sleep(60)