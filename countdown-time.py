import time  # Time-related functions
import threading  # For handling parallel execution
import tkinter as tk  # GUI library
from tkinter import messagebox  # For displaying alert messages
import winsound  # For playing alert sounds (Windows only)

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Countdown Timer")  # Window title
        self.root.geometry("400x300")  # Set window size
        self.root.configure(bg="#222222")  # Set background color
        
        self.time_left = 0  # Stores remaining time
        self.running = False  # Flag to check if timer is running
        
        # Label for user input
        self.label = tk.Label(root, text="Enter time (seconds):", font=("Arial", 14), bg="#222222", fg="#ffffff")
        self.label.pack(pady=10)
        
        # Input field for time entry
        self.entry = tk.Entry(root, font=("Arial", 14), width=10, justify='center')
        self.entry.pack()
        
        # Timer display label
        self.timer_display = tk.Label(root, text="00:00", font=("Arial", 30, "bold"), bg="#222222", fg="#00ff00")
        self.timer_display.pack(pady=20)
        
        # Frame to hold buttons
        button_frame = tk.Frame(root, bg="#222222")
        button_frame.pack()
        
        # Start button
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, font=("Arial", 12), width=10, bg="#007BFF", fg="#ffffff")
        self.start_button.grid(row=0, column=0, padx=5, pady=5)
        
        # Pause button
        self.pause_button = tk.Button(button_frame, text="Pause", command=self.pause_timer, font=("Arial", 12), width=10, bg="#FFC107", fg="#222222")
        self.pause_button.grid(row=0, column=1, padx=5, pady=5)
        
        # Resume button
        self.resume_button = tk.Button(button_frame, text="Resume", command=self.resume_timer, font=("Arial", 12), width=10, bg="#28A745", fg="#ffffff")
        self.resume_button.grid(row=1, column=0, padx=5, pady=5)
        
        # Reset button
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer, font=("Arial", 12), width=10, bg="#DC3545", fg="#ffffff")
        self.reset_button.grid(row=1, column=1, padx=5, pady=5)
        
    # Function to start the countdown timer
    def start_timer(self):
        try:
            self.time_left = int(self.entry.get())  # Get time from input
            self.running = True  # Set running flag
            self.countdown()  # Start countdown process
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")  # Error handling
    
    # Countdown logic
    def countdown(self):
        if self.time_left > 0 and self.running:
            mins, secs = divmod(self.time_left, 60)  # Convert seconds to minutes and seconds
            self.timer_display.config(text=f"{mins:02d}:{secs:02d}")  # Update timer display
            self.time_left -= 1  # Decrease time left
            self.root.after(1000, self.countdown)  # Call countdown again after 1 second
        elif self.time_left == 0 and self.running:
            self.timer_display.config(text="Time's Up!")  # Display "Time's Up!"
            self.running = False  # Stop timer
            winsound.Beep(1000, 1000)  # Play alert sound (Windows only)
            messagebox.showinfo("Countdown Timer", "Time's up!")  # Show popup alert
    
    # Function to pause timer
    def pause_timer(self):
        self.running = False  # Stop countdown
    
    # Function to resume paused timer
    def resume_timer(self):
        if not self.running and self.time_left > 0:
            self.running = True
            self.countdown()
    
    # Function to reset timer
    def reset_timer(self):
        self.running = False  # Stop countdown
        self.time_left = 0  # Reset time
        self.timer_display.config(text="00:00")  # Reset display
        self.entry.delete(0, tk.END)  # Clear input field
        
# Main program execution
if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = CountdownTimer(root)  # Instantiate CountdownTimer class
    root.mainloop()  # Run the GUI event loop
