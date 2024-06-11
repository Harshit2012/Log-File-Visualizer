import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import matplotlib.pyplot as plt

def read_log_file(file_path):
    data = {"errors": 0, "warnings": 0, "info": 0}
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                data["errors"] += 1
            elif "WARNING" in line:
                data["warnings"] += 1
            elif "INFO" in line:
                data["info"] += 1
    return data

def generate_graph(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values, color=['red', 'orange', 'blue'])
    plt.xlabel('Log Type')
    plt.ylabel('Count')
    plt.title('Log File Visualizer')
    plt.show()

def on_browse_click():
    file_path = filedialog.askopenfilename(filetypes=[("Log files", "*.log")])
    if file_path:
        log_data = read_log_file(file_path)
        generate_graph(log_data)
        with open(file_path, 'r') as file:
            log_text.delete("1.0", tk.END)
            log_text.insert(tk.END, file.read())

root = tk.Tk()
root.title("Log Analyzer")

main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10)

heading_label = ttk.Label(main_frame, text="Log Analyzer", font=("Helvetica", 16))
heading_label.pack()

subheading_label = ttk.Label(main_frame, text="Select a log file and analyze its data", font=("Helvetica", 12))
subheading_label.pack(pady=5)

browse_button = ttk.Button(main_frame, text="Browse", command=on_browse_click)
browse_button.pack(pady=10)

log_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=50, height=10)
log_text.pack()

root.mainloop()