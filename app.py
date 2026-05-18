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

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ── frames ────────────────────────────────────────────
frame_home          = tk.Frame(window)
frame_neighborhoods = tk.Frame(window)
frame_styles        = tk.Frame(window)
frame_results       = tk.Frame(window)
frame_details       = tk.Frame(window)

for frame in (frame_home, frame_neighborhoods, frame_styles, frame_results, frame_details):
    frame.grid(row=0, column=0, sticky="nsew")

# ── helper ────────────────────────────────────────────
def show_frame(frame):
    frame.tkraise()

# ── show results ──────────────────────────────────────
def show_results(results, title="Results", show_neighborhood=True):
    label_results_title.config(text=title)
    listbox_results.delete(0, tk.END)
    if results:
        for g in results:
            type_label = "🏛" if g.type == "museum" else "🖼"
            if show_neighborhood:
                listbox_results.insert(tk.END, f"{type_label} {g.name} — {g.neighborhood}")
            else:
                listbox_results.insert(tk.END, f"{type_label} {g.name}")
    else:
        listbox_results.insert(tk.END, "No results found.")
    show_frame(frame_results)

# ── show details ──────────────────────────────────────
def show_details(gallery):
    setup_details(frame_details, gallery, lambda: show_frame(frame_results))
    show_frame(frame_details)

# ── search by name ────────────────────────────────────
def search_by_name():
    name = entry_search.get()
    listbox_results.delete(0, tk.END)
    label_results_title.config(text="Search Result")
    if not name:
        listbox_results.insert(tk.END, "Please insert a gallery name.")
    else:
        result = tree.search(name)
        if result:
            type_label = "🏛" if result.type == "museum" else "🖼"
            listbox_results.insert(tk.END, f"{type_label} {result.name} — {result.neighborhood} — {', '.join(result.art_style)}")
        else:
            listbox_results.insert(tk.END, "Gallery not found.")
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
entry_search = tk.Entry(frame_home, width=40)

# ── setup screens ─────────────────────────────────────
setup_home(
    frame_home,
    entry_search,
    search_by_name,
    load_neighborhoods,
    load_styles,
    list_all,
    show_frame,
    frame_neighborhoods,
    frame_styles,
    window.quit
)

label_results_title, listbox_results = setup_results(
    frame_results,
    lambda: show_frame(frame_home)
)

# ── click on result ───────────────────────────────────
def on_result_click(event):
    selection = listbox_results.curselection()
    if selection:
        selected_text = listbox_results.get(selection[0])
        for g in tree.list_all():
            if g.name in selected_text:
                show_details(g)
                break

listbox_results.bind("<Double-Button-1>", on_result_click)

# ── start ─────────────────────────────────────────────
show_frame(frame_home)
window.mainloop()
