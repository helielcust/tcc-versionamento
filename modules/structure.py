import os

def create_all_folders(base_path: str):
    """
    Cria a estrutura de diretórios padrão do projeto SyncDBtoGit.
    """
    folders = [
        "tables",
        "views",
        "procedures",
        "functions",
        "triggers",
        "events"
    ]

    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
