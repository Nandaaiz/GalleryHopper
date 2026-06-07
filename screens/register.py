import tkinter as tk
from styles import *
from user import user_manager

def setup_register(frame, show_login):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="GalleryHopper", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=40)
    tk.Label(frame, text="Create your account", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=4)

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=100, pady=20)

    # Name
    tk.Label(frame, text="NAME", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="center")
    entry_name = tk.Entry(frame, width=30, font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT,
                          relief="flat", bd=0, highlightthickness=1,
                          highlightbackground=COLOR_BORDER, justify="center")
    entry_name.pack(pady=6)

    # Email
    tk.Label(frame, text="EMAIL", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="center")
    entry_email = tk.Entry(frame, width=30, font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT,
                           relief="flat", bd=0, highlightthickness=1,
                           highlightbackground=COLOR_BORDER, justify="center")
    entry_email.pack(pady=6)

    # Password
    tk.Label(frame, text="PASSWORD", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(anchor="center")
    entry_password = tk.Entry(frame, width=30, font=BODY_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT,
                              relief="flat", bd=0, highlightthickness=1,
                              highlightbackground=COLOR_BORDER, justify="center", show="•")
    entry_password.pack(pady=6)

    # Message label
    msg_label = tk.Label(frame, text="", font=SMALL_FONT, bg=COLOR_BG, fg="red")
    msg_label.pack(pady=4)

    def do_register():
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()

        if not name or not email or not password:
            msg_label.config(text="Please fill in all fields.")
            return

        success, message = user_manager.register(name, email, password)
        if success:
            msg_label.config(text=message, fg=COLOR_ACCENT)
            frame.after(1500, show_login)
        else:
            msg_label.config(text=message, fg="red")

    # Register button
    btn = tk.Canvas(frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = btn.create_rectangle(0, 0, 300, 36, fill=COLOR_ACCENT, outline=COLOR_ACCENT)
    btn.create_text(150, 18, text="Create Account", fill="white", font=BODY_FONT)
    btn.bind("<Button-1>", lambda e: do_register())
    btn.bind("<Enter>", lambda e: btn.itemconfig(rect, fill="#3a4e2c"))
    btn.bind("<Leave>", lambda e: btn.itemconfig(rect, fill=COLOR_ACCENT))
    btn.pack(pady=16)

    # Back to login
    back_btn = tk.Canvas(frame, width=200, height=30, bg=COLOR_BG, highlightthickness=0)
    back_btn.create_text(100, 15, text="← Back to login", fill=COLOR_ACCENT, font=SMALL_FONT)
    back_btn.bind("<Button-1>", lambda e: show_login())
    back_btn.pack(pady=4)