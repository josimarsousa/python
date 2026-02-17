#arquivos binarios
#visualizador de arquivos em formato binário
import sys
import itertools

def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x}" for v in b])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        padding = " " * 3 * (bytes_por_linha - len(b))
        print(f"{hex_view} {padding}{tview}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python arquivosbinarios.py <arquivo>")
        sys.exit(1)
    caminho = sys.argv[1]
    with open(caminho, "rb") as f:
        imagem = f.read()
    imprime_bytes(imagem)
