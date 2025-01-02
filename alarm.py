import datetime
import time

def alarm_clock():
    print("=== Simple Alarm Clock ===")
    alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour): ")

    try:
        
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    print(f"Alarm is set for {alarm_time}. Waiting...")

    while True:
       
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")

        
        if current_time == alarm_time:
            print("\nWake up! It's time!")
            break

        
        
        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
