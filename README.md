# study-tracker
This Python script utilizes the time and plyer.notification modules to create a study tracker that reminds the user to take breaks after a specified study duration. The script begins by prompting the user to input their study duration in hours.

It initializes a variable total_study_time to keep track of the total hours studied.

The script enters an infinite loop using while(True) and employs the time.sleep function to pause the script for the user-specified study duration converted to seconds.

After the specified study duration has passed, it increments the total_study_time by the input study duration.

The script then triggers a system notification through the notification.notify function. The notification displays the title "Study Tracker" and a message indicating the total hours the user has studied.

The timeout parameter is set to 2, specifying the duration in seconds for which the notification should remain visible.

The script continues this process indefinitely, allowing the user to track their study duration and take regular breaks.
