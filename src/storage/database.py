import psycopg2
import src.storage.create_database as db
import datetime
from src.config import (
    DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT
)
from src.entities.project import Project

db_config = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_NAME,
    'port': DB_PORT
}


class Database:
    def __init__(self):
        db.create_database()
        db.create_tables()
        self._conn = psycopg2.connect(**db_config)
        self._cursor = self._conn.cursor()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
        print("Bye!")

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def add_project(self, name: str):
        active_count = self.all_active_contracts()
        if active_count:
            sql = """
                INSERT INTO project (name, date_of_creation)
                VALUES (%s, %s);
            """
            self.execute(sql, (name, datetime.datetime.today().strftime('%Y-%m-%d')))
            print("Project added!")
        else:
            print("Can't create a project without any active contracts!")

    def add_contract(self, name: str):
        try:
            sql = """
                INSERT INTO contract (name, date_of_creation, status)
                VALUES (%s, %s, %s);
            """
            self.execute(sql, (name, datetime.datetime.today().strftime('%Y-%m-%d'), 'draft'))
            print("Contract added!")
        except Exception as e:
            print(e)

    def change_contract_status(self, status, contract_id):
        if status not in ['draft', 'active', 'completed']:
            print("No such status!")
        else:
            if status == 'active':
                date_of_approval = datetime.datetime.today().strftime('%Y-%m-%d')
                sql = "UPDATE contract SET status = %s, date_of_approval = %s WHERE id = %s;"
                self.execute(sql, (status, date_of_approval, contract_id))
            sql = "UPDATE contract SET status = %s WHERE id = %s;"
            self.execute(sql, (status, contract_id))

    def add_contract_to_project(self, contract_id: int, project_id: int):
        self.execute("SELECT status FROM contract WHERE id = %s;", (contract_id,))
        status = self.fetchone()[0]
        self.execute("SELECT project_id FROM contract WHERE id = %s;", (contract_id,))
        has_parent_project = type(self.fetchone()[0]) is int
        active_count = self.active_contracts_count(project_id)
        if not has_parent_project:
            if active_count < 2:
                if status == 'active':
                    sql = "UPDATE contract SET project_id = %s WHERE id = %s;"
                    self.execute(sql, (project_id, contract_id))
                    print("Added to project!")
                else:
                    print("Contract is not active!")
            else:
                print("Project already has an active contract!")
        else:
            print("Contract is already used in another project!")

    def del_contract(self, contract_id: int):
        sql = "DELETE from contract WHERE id = %s;"
        self.execute(sql, (contract_id,))
        print("Deleted!")

    def del_project(self, project_id: int):
        sql = "DELETE from project WHERE id = %s;"
        self.execute(sql, (project_id,))
        print("Deleted!")

    def get_contract(self, contract_id: int):
        sql = "SELECT * FROM contract WHERE id = %s;"
        self.execute(sql, (contract_id,))
        return self.fetchone()

    def get_project(self, project_id: int):
        sql = "SELECT * FROM project WHERE id = %s;"
        self.execute(sql, (project_id,))
        return self.fetchone()

    def get_all_contracts(self):
        return self.query("SELECT * FROM contract ORDER BY name;")

    def get_all_projects(self):
        return self.query("SELECT * FROM project ORDER BY name;")

    def get_all_active_contracts(self):
        return self.query("SELECT * FROM contract WHERE status = 'active' ORDER BY name;")

    def all_active_contracts(self):
        return self.query("SELECT COUNT(*) FROM contract WHERE status = 'active';")

    def active_contracts_count(self, project_id: int):
        sql = "SELECT COUNT(*) FROM contract WHERE project_id = %s AND status = 'active'"
        self.execute(sql, (project_id,))
        return self.fetchone()[0]
