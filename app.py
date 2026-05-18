import tkinter as tk
from main import tree

# ── helper ──────────────────────────────────────────
def show_frame(frame):
    frame.tkraise()

# ── results screen ───────────────────────────────────
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

# ── neighborhoods screen ─────────────────────────────
def load_neighborhoods():
    neighborhoods = sorted(set(g.neighborhood for g in tree.list_all()))
    for widget in frame_neighborhoods.winfo_children():
        widget.destroy()
    tk.Label(frame_neighborhoods, text="Choose a Neighborhood").pack(pady=20)
    for neighborhood in neighborhoods:
        tk.Button(
            frame_neighborhoods,
            text=neighborhood,
            width=30,
            command=lambda n=neighborhood: show_results(
                [g for g in tree.list_all() if g.neighborhood == n],
                title=f"Galleries in {n}" ,
                show_neighborhood = False
        )
        ).pack(pady=3)
    tk.Button(frame_neighborhoods, text="← Back", command=lambda: show_frame(frame_home)).pack(pady=20)

# ── styles screen ─────────────────────────────────────
def load_styles():
    styles = set()
    for g in tree.list_all():
        for s in g.art_style:
            styles.add(s)
    for widget in frame_styles.winfo_children():
        widget.destroy()
    tk.Label(frame_styles, text="Choose an Art Style").pack(pady=20)
    for style in sorted(styles):
        tk.Button(
            frame_styles,
            text=style,
            width=30,
            command=lambda s=style: show_results(
                [g for g in tree.list_all() if s.lower() in [x.lower() for x in g.art_style]],
                title=f"Galleries — {s}"
            )
        ).pack(pady=2)
    tk.Button(frame_styles, text="← Back", command=lambda: show_frame(frame_home)).pack(pady=20)

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

# ── window setup ─────────────────────────────────────
window = tk.Tk()
window.title("GalleryHopper")
window.geometry("800x600")

for f in range(4):
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

# ── frames ────────────────────────────────────────────
frame_home          = tk.Frame(window)
frame_neighborhoods = tk.Frame(window)
frame_styles        = tk.Frame(window)
frame_results       = tk.Frame(window)

for frame in (frame_home, frame_neighborhoods, frame_styles, frame_results):
    frame.grid(row=0, column=0, sticky="nsew")

# ── home screen ───────────────────────────────────────
tk.Label(frame_home, text="GalleryHopper", font=("Helvetica", 24, "bold")).pack(pady=20)
tk.Label(frame_home, text="Find art galleries in NYC").pack()

entry_search = tk.Entry(frame_home, width=40)
entry_search.pack(pady=10)

tk.Button(frame_home, text="Search by Name", width=30, command=search_by_name).pack(pady=5)
tk.Button(frame_home, text="Filter by Neighborhood", width=30, command=lambda: [load_neighborhoods(), show_frame(frame_neighborhoods)]).pack(pady=5)
tk.Button(frame_home, text="Filter by Art Style", width=30, command=lambda: [load_styles(), show_frame(frame_styles)]).pack(pady=5)
tk.Button(frame_home, text="List All Galleries", width=30, command=list_all).pack(pady=5)
tk.Button(frame_home, text="Exit", width=30, command=window.quit).pack(pady=20)

# ── results screen widgets ────────────────────────────
label_results_title = tk.Label(frame_results, text="Results", font=("Helvetica", 16, "bold"))
label_results_title.pack(pady=10)

listbox_results = tk.Listbox(frame_results, width=80, height=20)
listbox_results.pack(pady=10)

tk.Button(frame_results, text="← Back to Home", command=lambda: show_frame(frame_home)).pack(pady=10)

# ── start ─────────────────────────────────────────────
show_frame(frame_home)
window.mainloop()