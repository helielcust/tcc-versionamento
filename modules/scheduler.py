import os
import subprocess

def criar_bat_script(script_py_path, bat_path):
    python_path = r"C:\Users\helie\AppData\Local\Programs\Python\Python313\python.exe"
    with open(bat_path, "w") as bat_file:
        bat_file.write(f'@echo off\n"{python_path}" "{script_py_path}"\n')

def criar_tarefa_agendada(nome_tarefa, bat_path, intervalo_min=15):
    comando = [
        "schtasks",
        "/Create",
        "/SC", "MINUTE",               # Executar a cada X minutos
        "/MO", str(intervalo_min),     # Intervalo de minutos
        "/TN", nome_tarefa,            # Nome da tarefa
        "/TR", bat_path,               # Caminho do .bat
        "/F"                           # Força a criação (sobrescreve se já existir)
    ]
    try:
        subprocess.run(comando, check=True)
        print(f"✅ Tarefa agendada '{nome_tarefa}' criada para executar a cada {intervalo_min} minutos.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Erro ao criar tarefa agendada: {e}")

def agendar_execucao(script_py_path, nome_tarefa="SyncDBtoGit", intervalo_min=15):
    bat_path = os.path.join(os.path.dirname(script_py_path), "executar_syncdbtogit.bat")
    criar_bat_script(script_py_path, bat_path)
    criar_tarefa_agendada(nome_tarefa, bat_path, intervalo_min)
