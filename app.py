import tkinter as tk
from main import tree
from styles import *
from screens.home import setup_home
from screens.results import setup_results
from screens.details import setup_details
from screens.neighborhoods import setup_neighborhoods
from screens.styles_screen import setup_styles

# ── window setup ─────────────────────────────────────
window = tk.Tk()
window.title(WINDOW_TITLE)
window.geometry(WINDOW_SIZE)
window.configure(bg=COLOR_BG)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ── frames ────────────────────────────────────────────
frame_home          = tk.Frame(window, bg=COLOR_BG)
frame_neighborhoods = tk.Frame(window, bg=COLOR_BG)
frame_styles        = tk.Frame(window, bg=COLOR_BG)
frame_results       = tk.Frame(window, bg=COLOR_BG)
frame_details       = tk.Frame(window, bg=COLOR_BG)

for frame in (frame_home, frame_neighborhoods, frame_styles, frame_results, frame_details):
    frame.grid(row=0, column=0, sticky="nsew")

# ── helper ────────────────────────────────────────────
def show_frame(frame):
    frame.tkraise()

# ── show details ──────────────────────────────────────
def show_details(gallery):
    setup_details(frame_details, gallery, lambda: show_frame(frame_results))
    show_frame(frame_details)

# ── set back command ──────────────────────────────────
def set_back_command(command):
    back_btn.bind("<Button-1>", lambda e: command())

# ── show results ──────────────────────────────────────
def show_results(results, title="Results", show_neighborhood=True, back_command=None):
    label_results_title.config(text=title)
    if back_command:
        set_back_command(back_command)
    else:
        set_back_command(lambda: show_frame(frame_home))
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    if results:
        for i, g in enumerate(results):
            type_label = "🏛 Museum" if g.type == "museum" else "🖼 Gallery"
            item_frame = tk.Frame(scroll_frame, bg=COLOR_WHITE, pady=12)
            item_frame.grid(row=i // 2, column=i % 2, pady=4, padx=20, sticky="nsew")
            scroll_frame.grid_columnconfigure(0, weight=1, minsize=200)
            scroll_frame.grid_columnconfigure(1, weight=1, minsize=200)
            tk.Label(item_frame, text=type_label, font=SMALL_FONT, bg=COLOR_WHITE, fg=COLOR_ACCENT).pack(anchor="w", padx=16)
            tk.Label(item_frame, text=g.name, font=SUBHEAD_FONT, bg=COLOR_WHITE, fg=COLOR_TEXT).pack(anchor="w", padx=16)
            if show_neighborhood:
                tk.Label(item_frame, text=g.neighborhood, font=DETAIL_FONT, bg=COLOR_WHITE, fg=COLOR_GRAY).pack(anchor="w", padx=16, pady=(0, 8))
            item_frame.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))
            for child in item_frame.winfo_children():
                child.bind("<Button-1>", lambda e, gallery=g: show_details(gallery))
    else:
        tk.Label(scroll_frame, text="No results found.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=20)
    show_frame(frame_results)

# ── search by name ────────────────────────────────────
def search_by_name():
    name = entry_search.get()
    if not name or name == "Search by gallery name.":
        show_results([], title="Search Result")
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        msg_frame = tk.Frame(scroll_frame, bg=COLOR_BG, width=600)
        msg_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        msg_frame.grid_columnconfigure(0, weight=1)
        tk.Label(msg_frame, text="Please insert a gallery name.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=40)
        show_frame(frame_results)
    else:
        result = tree.search(name)
        if result:
            show_results([result], title="Search Result")
        else:
            show_results([], title="Search Result")
            for widget in scroll_frame.winfo_children():
                widget.destroy()
            msg_frame = tk.Frame(scroll_frame, bg=COLOR_BG, width=600)
            msg_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
            msg_frame.grid_columnconfigure(0, weight=1)
            tk.Label(msg_frame, text="Gallery not found.", font=BODY_FONT, bg=COLOR_BG, fg=COLOR_GRAY).pack(pady=40)
            show_frame(frame_results)
# ── list all ──────────────────────────────────────────
def list_all():
    show_results(tree.list_all(), title="All Galleries & Museums")

# ── load neighborhoods ────────────────────────────────
def load_neighborhoods():
    setup_neighborhoods(frame_neighborhoods, tree, show_results, lambda: show_frame(frame_home))

# ── load styles ───────────────────────────────────────
def load_styles():
    setup_styles(frame_styles, tree, show_results, lambda: show_frame(frame_home))

# ── entry search ──────────────────────────────────────
entry_search = tk.Entry(frame_home, width=40, font=BODY_FONT, relief="solid", bd=1)
entry_search.insert(0, "Search by gallery name...")
entry_search.config(fg=COLOR_GRAY)

def on_entry_click(e):
    if entry_search.get() == "Search by gallery name...":
        entry_search.delete(0, tk.END)
        entry_search.config(fg=COLOR_TEXT)

def on_focus_out(e):
    if entry_search.get() == "":
        entry_search.insert(0, "Search by gallery name...")
        entry_search.config(fg=COLOR_GRAY)

entry_search.bind("<FocusIn>", on_entry_click)
entry_search.bind("<FocusOut>", on_focus_out)
entry_search.bind("<Return>", lambda e: search_by_name())

# ── setup screens ─────────────────────────────────────
setup_home(
    frame_home,
    entry_search,
    load_neighborhoods,
    load_styles,
    list_all,
    show_frame,
    frame_neighborhoods,
    frame_styles,
    window.quit
)

label_results_title, scroll_frame, back_btn = setup_results(
    frame_results,
    lambda: show_frame(frame_home)
)

# ── start ─────────────────────────────────────────────
show_frame(frame_home)
window.mainloop()