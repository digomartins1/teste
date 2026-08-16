# ferramentas/formatador.py

def criar_banner(texto):
    tamanho = len(texto) + 8
    borda = "=" * tamanho
    return f"\n{borda}\n    {texto.upper()}\n{borda}\n"