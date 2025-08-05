import tkinter as tk

root = tk.Tk()
root.title("Hermes – Main Screen")
root.geometry("800x500")
root.configure(bg = '#2c3e50')


# switch pages
def show_page(page_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    if page_name == "Default":
        content_frame.configure(bg = '#34495e')
        status_title = tk.Label(content_frame, text = "System Status",
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
            label = tk.Label(content_frame, text=line,
                             font = ('Ubuntu Mono', 13),
                             bg = '#34495e', fg='white', cursor = 'arrow')
            label.pack(anchor = 'w', padx = 30, pady = 10)

    elif page_name == "Hermes":
        content_frame.configure(bg = 'white')
        label = tk.Label(content_frame, text = "Hermes AI Core",
                         font = ('Ubuntu Mono', 20), bg = 'white', fg = 'black')
        label.pack(pady = (20, 10))

        desc = tk.Label(content_frame, text = "Mission AI interface and control center.",
                        font = ('Ubuntu Mono', 12), bg = 'white', fg = 'black')
        desc.pack(pady = (0, 20))

        # Button to Route Planner page
        route_btn = tk.Button(content_frame, text = "Open Route Planner",
                              font = ('Ubuntu Mono', 12),
                              activebackground = '#34495e', activeforeground = 'black',
                              relief = 'raised', bd = 3,
                              padx = 10, pady = 5,
                              command = lambda: show_page("Route Planner"))
        route_btn.pack(pady = 10)

    elif page_name == "Route Planner":
        content_frame.configure(bg = 'white')
        label = tk.Label(content_frame, text = "Route Planner",
                         font = ('Ubuntu Mono', 20), bg = 'white', fg = 'black')
        label.pack(pady=(20, 10))

        note = tk.Label(content_frame, text = "This page will have the route planning functionality",
                        font=('Ubuntu Mono', 12), bg = 'white', fg = 'black', wraplength = 500, justify = 'center')
        note.pack(pady = 20)

    else:
        content_frame.configure(bg = 'white')
        label = tk.Label(content_frame, text = f"{page_name} Page",
                         font = ('Ubuntu Mono', 20), bg = 'white', fg = 'black')
        label.pack(expand = True)

# hover on buttons
def on_enter(e):
    e.widget['bg'] = '#1abc9c'

def on_leave(e):
    e.widget['bg'] = '#34495e'

# Main layout
main_frame = tk.Frame(root, bg = '#2c3e50')
main_frame.pack(fill = 'both', expand = True)

# Left panel
left_panel = tk.Frame(main_frame, bg = '#2c3e50', width = 200)
left_panel.pack(side = 'left', fill = 'y', padx = (20, 10), pady = 20)

# title
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



# Content frame (right side)
content_frame = tk.Frame(main_frame, bg = '#34495e')
content_frame.pack(side = 'left', fill = 'both', expand = True, padx = (10, 20), pady = 20)


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
