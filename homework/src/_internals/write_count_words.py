import os

def write_count_words(counter):
    # Crear carpeta si no existe
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # Guardar los resultados
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")
