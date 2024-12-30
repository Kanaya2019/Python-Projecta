import tkinter as tk
import time

# Create the root window
root = tk.Tk()
root.title("Digital Clock")

# Set the size of the window
root.geometry("400x200")

# Define a label to display the time
label = tk.Label(root, font=("Arial", 50), background="black", foreground="white")
label.pack(expand=True)

# Function to update the time on the label
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format the time in HH:MM:SS
    label.config(text=current_time)
    label.after(1000, update_time)  # Call this function every 1000ms (1 second)

# Call the update_time function to start the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
