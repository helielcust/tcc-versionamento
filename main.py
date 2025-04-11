from modules.structure import create_all_folders
from modules.extractor import extract_all_objects
from modules.git_auto_commit import auto_commit_and_push
from modules.scheduler import create_bat_file, create_task
from db.mysql import MySQL

# Importa as configurações centralizadas
from config import REPO_PATH, DB_CONFIG, PYTHON_PATH, TASK_NAME, BATCH_FILE_PATH
import os

def main():
    print("🔧 Iniciando SyncDBtoGit...")

    # --- INICIALIZAÇÃO DO BANCO DE DADOS ---
    mysql = MySQL(**DB_CONFIG)

    # --- ESTRUTURA DE DIRETÓRIOS ---
    print("📁 Criando estrutura de diretórios...")
    create_all_folders(REPO_PATH)

    # --- EXTRAÇÃO DOS OBJETOS ---
    print("📤 Extraindo objetos do banco de dados...")
    extract_all_objects(mysql, REPO_PATH)

    # --- COMMIT E PUSH ---
    print("📦 Realizando commit e push automáticos...")
    auto_commit_and_push(REPO_PATH)

    # --- ARQUIVO BAT ---
    print("📄 Gerando arquivo .bat para execução automática...")
    create_bat_file(BATCH_FILE_PATH, PYTHON_PATH, os.path.abspath(__file__))

    # --- TAREFA AGENDADA ---
    print("⏰ Criando tarefa agendada no Windows...")
    create_task(task_name=TASK_NAME, bat_path=BATCH_FILE_PATH)

    print("✅ SyncDBtoGit finalizado com sucesso!")

if __name__ == "__main__":
    main()
