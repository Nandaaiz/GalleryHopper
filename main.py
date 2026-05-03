from bst import BST
from data import load_data

tree = BST()
load_data(tree)


# Menu functions

def show_results(results):
    text_results.delete("1.0", tk.END)
    if results:
        for g in results:
            type_label = "🏛 Museum" if g.type == "museum" else "🖼 Gallery"
            text_results.insert(tk.END, f"{type_label} | {g.name} - {g.neighborhood} - {', '.join(g.art_style)}\n")
    else:
        text_results.insert(tk.END, "No galleries found.")

def search_by_name(tree):
    name = input("Enter gallery name: ")
    result = tree.search(name)
    if result:
        print("Found:", result.name, "-", result.neighborhood, "-", ", ".join(result.art_style))
    else:
        print("Gallery not found.")

def filter_by_neighborhood(tree):
    neighborhood = input("Enter neighborhood: ").lower()
    results = [g for g in tree.list_all() if g.neighborhood.lower() == neighborhood]
    if results:
        for g in results:
            print("-", g.name, "-", ", ".join(g.art_style))
    else:
        print("No galleries found in this neighborhood.")

def filter_by_art_style(tree):
    style = input("Enter art style: ").lower()
    results = [g for g in tree.list_all() if style in [s.lower() for s in g.art_style]]
    if results:
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("No galleries found with this art style.")

def list_all(tree):
    print("\nAll galleries in alphabetical order:")
    for g in tree.list_all():
        print("-", g.name, "-", g.neighborhood, "-", ", ".join(g.art_style))

def list_all_styles(tree):
    styles = set()
    for g in tree.list_all():
        for style in g.art_style:
            styles.add(style)
    sorted_styles = sorted(styles)
    print("\nAvailable art styles:")
    for i, style in enumerate(sorted_styles, 1):
        print(f"{i}. {style}")
    choice = input("\nEnter the number to explore a style (or 0 to go back): ")
    if choice == "0":
        return
    if choice.isdigit() and 1 <= int(choice) <= len(sorted_styles):
        selected = sorted_styles[int(choice) - 1]
        results = [g for g in tree.list_all() if selected.lower() in [s.lower() for s in g.art_style]]
        print(f"\nGalleries with '{selected}':")
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("Invalid option.")

def menu():
    while True:
        print("\n=== GalleryHopper ===")
        print("1. Search gallery by name")
        print("2. Filter by neighborhood")
        print("3. Filter by art style")
        print("4. List all galleries")
        print("5. Show all art styles")
        print("0. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            search_by_name(tree)
        elif option == "2":
            filter_by_neighborhood(tree)
        elif option == "3":
            filter_by_art_style(tree)
        elif option == "4":
            list_all(tree)
        elif option == "5":
            list_all_styles(tree)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# menu()

# Menu functions

def search_by_name(tree):
    name = input("Enter gallery name: ")
    result = tree.search(name)
    if result:
        print("Found:", result.name, "-", result.neighborhood, "-", ", ".join(result.art_style))
    else:
        print("Gallery not found.")

def filter_by_neighborhood(tree):
    neighborhood = input("Enter neighborhood: ").lower()
    results = [g for g in tree.list_all() if g.neighborhood.lower() == neighborhood]
    if results:
        for g in results:
            print("-", g.name, "-", ", ".join(g.art_style))
    else:
        print("No galleries found in this neighborhood.")

def filter_by_art_style(tree):
    style = input("Enter art style: ").lower()
    results = [g for g in tree.list_all() if style in [s.lower() for s in g.art_style]]
    if results:
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("No galleries found with this art style.")

def list_all(tree):
    print("\nAll galleries in alphabetical order:")
    for g in tree.list_all():
        print("-", g.name, "-", g.neighborhood, "-", ", ".join(g.art_style))


def list_all_styles(tree):
    styles = set()
    for g in tree.list_all():
        for style in g.art_style:
            styles.add(style)

    sorted_styles = sorted(styles)

    print("\nAvailable art styles:")
    for i, style in enumerate(sorted_styles, 1):
        print(f"{i}. {style}")

    choice = input("\nEnter the number to explore a style (or 0 to go back): ")

    if choice == "0":
        return

    if choice.isdigit() and 1 <= int(choice) <= len(sorted_styles):
        selected = sorted_styles[int(choice) - 1]
        results = [g for g in tree.list_all() if selected.lower() in [s.lower() for s in g.art_style]]
        print(f"\nGalleries with '{selected}':")
        for g in results:
            print("-", g.name, "-", g.neighborhood)
    else:
        print("Invalid option.")

def menu():
    while True:
        print("\n=== GalleryHopper ===")
        print("1. Search gallery by name")
        print("2. Filter by neighborhood")
        print("3. Filter by art style")
        print("4. List all galleries")
        print("5. Show all art styles")
        print("0. Exit")

        option = input("\nChoose an option: ")

        if option == "1":
            search_by_name(tree)
        elif option == "2":
            filter_by_neighborhood(tree)
        elif option == "3":
            filter_by_art_style(tree)
        elif option == "4":
            list_all(tree)
        elif option == "5":
            list_all_styles(tree)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

#menu()