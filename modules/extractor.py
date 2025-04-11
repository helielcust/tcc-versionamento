import os
from db.mysql import MySQL

class DBExtractor:
    def __init__(self, mysql: MySQL, output_dir: str):
        self.mysql = mysql
        self.output_dir = output_dir

    def _save_to_file(self, folder, name, content):
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, f"{name}.sql")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    def extract_tables(self, database):
        tables = self.mysql.query(f"SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = '{database}' AND TABLE_TYPE = 'BASE TABLE';")
        for (table,) in tables:
            ddl = self.mysql.query(f"SHOW CREATE TABLE `{database}`.`{table}`;")[0][1]
            self._save_to_file(os.path.join(self.output_dir, "tables"), table, ddl)

    def extract_views(self, database):
        views = self.mysql.query(f"SELECT TABLE_NAME FROM information_schema.views WHERE TABLE_SCHEMA = '{database}';")
        for (view,) in views:
            ddl = self.mysql.query(f"SHOW CREATE VIEW `{database}`.`{view}`;")[0][1]
            self._save_to_file(os.path.join(self.output_dir, "views"), view, ddl)

    def extract_procedures(self, database):
        procedures = self.mysql.query(f"SELECT ROUTINE_NAME FROM information_schema.routines WHERE ROUTINE_SCHEMA = '{database}' AND ROUTINE_TYPE = 'PROCEDURE';")
        for (proc,) in procedures:
            ddl = self.mysql.query(f"SHOW CREATE PROCEDURE `{database}`.`{proc}`;")[0][2]
            self._save_to_file(os.path.join(self.output_dir, "procedures"), proc, ddl)

    def extract_functions(self, database):
        functions = self.mysql.query(f"SELECT ROUTINE_NAME FROM information_schema.routines WHERE ROUTINE_SCHEMA = '{database}' AND ROUTINE_TYPE = 'FUNCTION';")
        for (func,) in functions:
            ddl = self.mysql.query(f"SHOW CREATE FUNCTION `{database}`.`{func}`;")[0][2]
            self._save_to_file(os.path.join(self.output_dir, "functions"), func, ddl)

    def extract_triggers(self, database):
        triggers = self.mysql.query(f"SELECT TRIGGER_NAME FROM information_schema.triggers WHERE TRIGGER_SCHEMA = '{database}';")
        for (trigger,) in triggers:
            ddl = self.mysql.query(f"SHOW CREATE TRIGGER `{database}`.`{trigger}`;")[0][2]
            self._save_to_file(os.path.join(self.output_dir, "triggers"), trigger, ddl)

    def extract_events(self, database):
        events = self.mysql.query(f"SELECT EVENT_NAME FROM information_schema.events WHERE EVENT_SCHEMA = '{database}';")
        for (event,) in events:
            ddl = self.mysql.query(f"SHOW CREATE EVENT `{database}`.`{event}`;")[0][2]
            self._save_to_file(os.path.join(self.output_dir, "events"), event, ddl)

    def extract_all(self, database):
        self.extract_tables(database)
        self.extract_views(database)
        self.extract_procedures(database)
        self.extract_functions(database)
        self.extract_triggers(database)
        self.extract_events(database)
