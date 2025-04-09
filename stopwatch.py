import tkinter as tk
import time

# Global variable to track if the timer is running or stopped
running = False

# Function to start the timer
def start_timer():
    global running
    # Setting 'running' to False to indicate the timer isn't running
    running = False
    if not running:
        # Capturing the current time when the timer starts
        start_time = time.time()
        # Calling the update_time function to start the time display
        update_time(start_time)

# Function to stop the timer
def stop_timer():
    global running
    # Setting 'running' to True, which stops the time updates
    running = True

# Function to update the time display every 10 milliseconds
def update_time(start_time):
    global running
    # If the timer is not stopped (running == False), we update the time
    if not running:
        # Calculate the elapsed time since the start of the timer
        elapsed_time = time.time() - start_time
        # Convert the elapsed time to hours, minutes, seconds, and milliseconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)

        # Update the label to show the formatted time
        time_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}")
        # Call this function again after 10 milliseconds to keep the timer running
        root.after(10, update_time, start_time)

# Create the main Tkinter window
root = tk.Tk()
root.title("Stopwatch")  # Set the window title

# Create a label to display the timer in hours:minutes:seconds:milliseconds format
time_display = tk.Label(root, text="00:00:00:000", font=("Helvetica", 30))
time_display.pack()

# Create a button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
# Create a button to stop the timer
stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)

# Add buttons to the window
start_button.pack()
stop_button.pack()

# Start the Tkinter event loop
root.mainloop()