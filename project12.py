import time
from plyer import notification

user_input=(int(input("Enter your study duration in hours: ")))
total_study_time=0

while(True):
    time.sleep(3600*user_input)
    total_study_time=total_study_time+user_input
    notification.notify(title="Study Tracker",
        message=f"You have studied for {total_study_time} hours.",
        timeout=2)