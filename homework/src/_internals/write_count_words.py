import os

def write_count_words(counter,output_folder):
    # Crear carpeta si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar los resultados
    output_path=os.path.join(output_folder,"results.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")
