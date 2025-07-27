import tkinter as tk

root = tk.Tk()
root.title("Hermes – Main Screen")
root.geometry("800x500")
root.configure(bg = '#2c3e50')

# Main layout
main_frame = tk.Frame(root, bg = '#2c3e50')
main_frame.pack(fill = 'both', expand = True)

# Left panel
left_panel = tk.Frame(main_frame, bg = '#2c3e50', width = 200)
left_panel.pack(side = 'left', fill = 'y', padx = (20, 10), pady = 20)

# App title
title = tk.Label(left_panel, text = "HERMES", font = ('Ubuntu Mono', 30, 'bold'),
                 bg = '#2c3e50', fg = '#3498db', cursor = 'arrow')
title.pack(pady = (0, 40))

# Navigation buttons
button_labels = ["Hermes", "Diagnostics", "Mission Logs", "Settings"]

for label in button_labels:
    b = tk.Label(left_panel, text = label,
                 font = ('Ubuntu Mono', 14),
                 bg = '#34495e', fg = 'white',
                 bd = 3, relief = 'raised',
                 padx = 10, pady = 15,
                 cursor = 'arrow', width = 18)
    b.pack(pady = 10)
    b.bind("<Enter>", lambda e, b = b: b.config(bg = '#3498db', relief = 'sunken'))
    b.bind("<Leave>", lambda e, b = b: b.config(bg = '#34495e', relief = 'raised'))

# System status
right_panel = tk.Frame(main_frame, bg = '#34495e')
right_panel.pack(side = 'right', fill = 'both', expand = True, padx = (10, 20), pady = 20)

status_title = tk.Label(right_panel, text = "System Status",
                        font = ('Ubuntu Mono', 18, 'bold'),
                        bg = '#34495e', fg = '#3498db', cursor = 'arrow')
status_title.pack(pady = (20, 10))

status_lines = [
    "AI Core: Online",
    "Navigation: Ready",
    "Sensors: Active",
    "Shield Integrity: Nominal",
    "Life Support: Stable"
]

for line in status_lines:
    label = tk.Label(right_panel, text = line,
                     font = ('Ubuntu Mono', 13),
                     bg = '#34495e', fg = 'white', cursor = 'arrow')
    label.pack(anchor = 'w', padx = 30, pady = 10)

root.mainloop()
