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

    def get_contract(self, contract_id):
        return self.db.get_contract(contract_id)

    def get_contracts_list(self):
        return self.db.get_all_contracts()

    def get_projects_ids(self):
        return [str(x[0]) for x in self.db.get_all_projects_ids()]

    def get_contracts_ids(self):
        return [str(x[0]) for x in self.db.get_all_contracts_ids()]

    def get_all_contracts_by_project(self, project_id):
        return self.db.get_all_contracts_by_project(project_id)

    def count_active_contracts_by_project(self, project_id):
        return self.db.count_active_contracts_by_project(project_id)

    def add_contract(self):
        pass

    def add_project(self):
        active_count = self.db.count_all_active_contracts()
        if active_count:
            return self.db.add_project(input("Input project name: "))
        else:
            return "Can't create a project when there aren't any active contracts!"

    def change_contract_status(self, contract_id, status: str):
        return self.db.change_contract_status(status, contract_id)

    def add_contract_to_project(self, contract_id: int, project_id: int):
        return self.db.add_contract_to_project(contract_id, project_id)
