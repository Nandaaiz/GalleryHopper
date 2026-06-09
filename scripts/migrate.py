from database import galleries_collection
from bst import BST
from data import load_data

# Cria a árvore e carrega os dados
tree = BST()
load_data(tree)

# Pega todas as galerias da BST
galleries = tree.list_all()


# Converte para formato MongoDB e insere
def migrate():
    # Limpa a collection antes de inserir
    galleries_collection.delete_many({})

    documents = []
    for g in galleries:
        doc = {
            "name": g.name,
            "neighborhood": g.neighborhood,
            "art_style": g.art_style,
            "type": g.type,
            "alias": g.alias,
            "city": "New York"
        }
        documents.append(doc)

    galleries_collection.insert_many(documents)
    print(f"{len(documents)} galleries inserted into MongoDB!")


if __name__ == "__main__":
    migrate()