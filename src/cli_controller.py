from src.storage.database import Database


class CLIController:
    def __init__(self):
        try:
            db = Database()
        except Exception as e:
            print(f'Unable to connect!\n{e}')
            exit()
        else:
            self.db = db

    def close_database(self):
        self.db.close()

    def get_projects_list(self):
        return self.db.get_all_projects()

    def get_contracts_list(self):
        return self.db.get_all_contracts()

    def add_contract(self):
        pass

    def add_project(self):
        pass

    def is_active(self):
        pass

    def add_contract_to_project(self, contract_id: int, project_id: int):
        pass
