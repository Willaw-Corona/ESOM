import tkinter as tk
import platform

def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }
    return "\n".join(f"{key}: {value}" for key, value in info.items())

# Create the main window
root = tk.Tk()
root.title("System Information")

# Create a text widget to display system info
text = tk.Text(root, wrap=tk.WORD, width=50, height=15)
text.insert(tk.END, get_system_info())
text.config(state=tk.DISABLED)  # Make the text widget read-only
text.pack(padx=10, pady=10)

# Run the application
root.mainloop()