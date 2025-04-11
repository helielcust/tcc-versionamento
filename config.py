# config.py

import os

# Caminho do repositório local Git
REPO_PATH = r"C:\Users\helie\Desktop\SyncDBtoGit"

# Configurações de conexão com o banco de dados
DB_CONFIG = {
    "host": "localhost",
    "username": "root",
    "password": "root",
    "database": "sakila",
    "port": "3306"
}

# Caminho do interpretador Python no ambiente do cliente
PYTHON_PATH = r"C:\Users\helie\AppData\Local\Programs\Python\Python313\python.exe"

# Nome da tarefa agendada no Windows
TASK_NAME = "SyncDBtoGit - Extração Automática"

# Caminho completo para o arquivo .bat
BATCH_FILE_PATH = os.path.join(REPO_PATH, "run_syncdbtogit.bat")
