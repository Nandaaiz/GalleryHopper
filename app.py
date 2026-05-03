import tkinter as tk
from main import tree

def show_results(results):
    text_results.delete("1.0", tk.END)
    if results:
        for g in results:
            text_results.insert(tk.END, f"{g.name} - {g.neighborhood} - {', '.join(g.art_style)}\n")
    else:
        text_results.insert(tk.END, "No galleries found.")

def search_by_name():
    name = entry_search.get()
    result = tree.search(name)
    text_results.delete("1.0", tk.END)
    if result:
        text_results.insert(tk.END, f"{result.name} - {result.neighborhood} - {', '.join(result.art_style)}\n")
    else:
        text_results.insert(tk.END, "Gallery not found.")

def filter_by_neighborhood():
    neighborhood = entry_search.get()
    results = [g for g in tree.list_all() if g.neighborhood.lower() == neighborhood.lower()]
    show_results(results)

def filter_by_art_style():
    style = entry_search.get()
    results = [g for g in tree.list_all() if style.lower() in [s.lower() for s in g.art_style]]
    show_results(results)

def list_all():
    show_results(tree.list_all())

def show_all_styles():
    styles = set()
    for g in tree.list_all():
        for style in g.art_style:
            styles.add(style)
    text_results.delete("1.0", tk.END)
    for i, style in enumerate(sorted(styles), 1):
        text_results.insert(tk.END, f"{i}. {style}\n")

# Window
window = tk.Tk()
window.title("GalleryHopper")
window.geometry("800x600")

# Title
label_title = tk.Label(window, text="GalleryHopper")
label_title.pack(pady=20)

label_subtitle = tk.Label(window, text="Find art galleries in NYC")
label_subtitle.pack()

# Search field
entry_search = tk.Entry(window, width=40)
entry_search.pack(pady=10)

# Buttons
btn_search = tk.Button(window, text="Search by Name", width=30, command=search_by_name)
btn_search.pack(pady=5)

btn_neighborhood = tk.Button(window, text="Filter by Neighborhood", width=30, command=filter_by_neighborhood)
btn_neighborhood.pack(pady=5)

btn_style = tk.Button(window, text="Filter by Art Style", width=30, command=filter_by_art_style)
btn_style.pack(pady=5)

btn_all = tk.Button(window, text="List All Galleries", width=30, command=list_all)
btn_all.pack(pady=5)

btn_styles = tk.Button(window, text="Show All Art Styles", width=30, command=show_all_styles)
btn_styles.pack(pady=5)

# Results area
text_results = tk.Text(window, width=80, height=15)
text_results.pack(pady=10)

window.mainloop()