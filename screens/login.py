import tkinter as tk
from styles import *
from user import user_manager

def setup_login(frame, show_home, show_register):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="GalleryHopper", font=TITLE_FONT, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=40)
    tk.Label(frame, text="Sign in to your account", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=4)

    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=100, pady=20)

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

    def do_login():
        email = entry_email.get()
        password = entry_password.get()
        success, result = user_manager.login(email, password)
        if success:
            show_home(result)
        else:
            msg_label.config(text=result)

    # Login button
    btn = tk.Canvas(frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    rect = btn.create_rectangle(0, 0, 300, 36, fill=COLOR_ACCENT, outline=COLOR_ACCENT)
    btn.create_text(150, 18, text="Sign In", fill="white", font=BODY_FONT)
    btn.bind("<Button-1>", lambda e: do_login())
    btn.bind("<Enter>", lambda e: btn.itemconfig(rect, fill="#3a4e2c"))
    btn.bind("<Leave>", lambda e: btn.itemconfig(rect, fill=COLOR_ACCENT))
    btn.pack(pady=16)

    # Register link
    tk.Label(frame, text="Don't have an account?", font=SMALL_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack()
    reg_btn = tk.Canvas(frame, width=200, height=30, bg=COLOR_BG, highlightthickness=0)
    reg_btn.create_text(100, 15, text="Create account →", fill=COLOR_ACCENT, font=SMALL_FONT)
    reg_btn.bind("<Button-1>", lambda e: show_register())
    reg_btn.pack(pady=4)

# Divider
    tk.Frame(frame, height=1, bg=COLOR_BORDER).pack(fill="x", padx=100, pady=16)

    # Guest button
    guest_btn = tk.Canvas(frame, width=300, height=36, bg=COLOR_BG, highlightthickness=0)
    rect_guest = guest_btn.create_rectangle(0, 0, 300, 36, fill=COLOR_WHITE, outline=COLOR_BORDER)
    guest_btn.create_text(150, 18, text="Continue as Guest", fill=COLOR_GRAY, font=SMALL_FONT)
    guest_btn.bind("<Button-1>", lambda e: show_home({"name": "Guest", "email": ""}))
    guest_btn.bind("<Enter>", lambda e: guest_btn.itemconfig(rect_guest, fill=COLOR_ACCENT_LT, outline=COLOR_ACCENT))
    guest_btn.bind("<Leave>", lambda e: guest_btn.itemconfig(rect_guest, fill=COLOR_WHITE, outline=COLOR_BORDER))
    guest_btn.pack(pady=4)