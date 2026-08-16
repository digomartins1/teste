# main.py
import os
import sys
import urllib.request

# ================= ⚙️ CONFIGURAÇÃO DO SEU GITHUB =================
# 👉 SUBSTÍTUA COM OS SEUS DADOS:
GITHUB_USER = "digomartins1"  # Ex: "maria-dev"
GITHUB_REPO = "teste"  # Ex: "meu-sistema-python"
BRANCH = "main"  # Geralmente é 'main' ou 'master'

# Link base público do GitHub
BASE_RAW_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

# Lista de todos os módulos que o sistema precisa para funcionar
ARQUIVOS_NECESSARIOS = [
    "modulo_mensagens.py",
    "modulo_matematica.py",
    "ferramentas/formatador.py"
]


# =================================================================


def verificar_e_baixar_modulos():
    """Verifica se os módulos existem na máquina; se não, baixa do GitHub."""
    print("🔍 Checando se todos os módulos estão instalados...")

    diretorio_local = os.path.dirname(os.path.abspath(__file__))
    houve_download = False

    for arquivo in ARQUIVOS_NECESSARIOS:
        caminho_arquivo = os.path.join(diretorio_local, arquivo)

        # Se o arquivo não existir localmente:
        if not os.path.exists(caminho_arquivo):
            houve_download = True
            url_arquivo = BASE_RAW_URL + arquivo
            print(f"⚠️ Módulo ausente: '{arquivo}'. Baixando...")

            try:
                # Cria a pasta caso o arquivo esteja em uma subpasta (ex: ferramentas/)
                pasta = os.path.dirname(caminho_arquivo)
                if pasta and not os.path.exists(pasta):
                    os.makedirs(pasta, exist_ok=True)

                # Faz o download do arquivo público
                urllib.request.urlretrieve(url_arquivo, caminho_arquivo)
                print(f"   ✅ '{arquivo}' baixado com sucesso!")
            except Exception as erro:
                print(f"   ❌ Falha ao baixar '{arquivo}': {erro}")
                print("   Verifique se o repositório é público e se os nomes estão corretos.")
                sys.exit(1)

    if houve_download:
        print("✨ Todos os módulos ausentes foram restaurados!\n")
    else:
        print("✅ Todos os módulos já estão presentes.\n")


# ================= EXECUÇÃO DO PROGRAMA =================
if __name__ == "__main__":
    # 1º Passo: Checar e baixar os arquivos ausentes
    verificar_e_baixar_modulos()

    # 2º Passo: Fazer o import DEPOIS de garantir que foram baixados
    import modulo_mensagens
    import modulo_matematica
    from ferramentas import formatador

    # 3º Passo: Usar as funções dos módulos normalmente
    banner = formatador.criar_banner("sistema iniciado com sucesso")
    print(banner)

    modulo_mensagens.dar_boas_vindas("Visitante")

    resultado_soma = modulo_matematica.somar(15, 25)
    resultado_mult = modulo_matematica.multiplicar(10, 5)

    print(f"📊 Teste Matemático:")
    print(f"   -> 15 + 25 = {resultado_soma}")
    print(f"   -> 10 x 5  = {resultado_mult}\n")

    modulo_mensagens.exibir_despedida()