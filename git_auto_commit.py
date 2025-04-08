import os
from git import Repo
from datetime import datetime

# Caminho do seu repositório local
repo_path = os.path.dirname(os.path.abspath(__file__))

# Inicializa o repositório Git
repo = Repo(repo_path)

# Verifica alterações e adiciona arquivos modificados ou não rastreados
repo.git.add('--all')

# Cria mensagem de commit com timestamp
commit_message = f"Atualização automática em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Só faz commit se houver mudanças
if repo.is_dirty(untracked_files=True):
    repo.index.commit(commit_message)
    print(f"Commit realizado: {commit_message}")

    # Realiza push para o repositório remoto
    origin = repo.remote(name='origin')
    origin.push()
    print("Push enviado com sucesso para o GitHub.")
else:
    print("Nenhuma mudança detectada. Nenhum commit foi feito.")
