import os
from git import Repo, Actor
from datetime import datetime

class GitAutoCommit:
    def __init__(self, repo_path, author_name="SyncDBtoGit", author_email="noreply@syncdbtogit.com"):
        self.repo_path = repo_path
        self.author = Actor(author_name, author_email)
        self.repo = self._init_repo()

    def _init_repo(self):
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            print("Inicializando repositório Git...")
            return Repo.init(self.repo_path)
        return Repo(self.repo_path)

    def commit_changes(self, message=None):
        self.repo.git.add(A=True)
        if self.repo.is_dirty():
            commit_msg = message or f"Auto commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            self.repo.index.commit(commit_msg, author=self.author)
            print(f"✔️ Commit realizado: {commit_msg}")
        else:
            print("✅ Nenhuma mudança detectada para versionar.")
