from prettytable import PrettyTable
from cli_controller import CLIController


class CLI:
    def __init__(self):
        self.controller = None
        self.exit_prompt = ", 0 - exit"
        self.back_prompt = ", 0 - go back"
        self.project_list_prompt = ", 8 - show projects list"
        self.contract_list_prompt = ", 9 - show contracts list"
        self.hint_prompt = " (enter a number): "

    def run(self):
        print('Hello! Setting up the database...')
        # here the database is created
        self.controller = CLIController()

        while True:
            prompt = "I want to work with 1 - projects, 2 - contracts"
            entity_choice = self.input_with_check(prompt, ['1', '2'], back_mode=False)
            if self.always_available_operations(entity_choice):
                self.controller.close_database()
                print("Bye!")
                break
            match entity_choice:
                case '1':
                    self.project_dialog()
                case '2':
                    self.contract_dialog()

    def input_with_check(self, prompt: str, values_list: list, back_mode=True):
        prompt += (self.project_list_prompt + self.contract_list_prompt +
                   (self.back_prompt if back_mode else self.exit_prompt) + self.hint_prompt)
        values_list.extend(['8', '9', '0'])
        while True:
            value = input(prompt)
            if value not in values_list:
                print("No such option! Try again!")
                continue
            else:
                return value

    def always_available_operations(self, choice):
        if choice in ['8', '9', '0']:
            match choice:
                case '8':
                    self.show_projects_list()
                case '9':
                    self.show_contracts_list()
                case '0':
                    return True

    def project_dialog(self):
        pass

    def contract_dialog(self):
        pass

    def show_projects_list(self):
        projects_list = self.controller.get_projects_list()
        table = PrettyTable()
        table.field_names = ["Project id", "Name", "Date of creation (yyyy-mm-dd)"]
        table.add_rows(projects_list)
        print(table)

    def show_contracts_list(self):
        contracts_list = self.controller.get_contracts_list()
        table = PrettyTable()
        f = " (yyyy-mm-dd)"
        table.field_names = ["Contract id", "Name", f"Date of creation{f}",
                             f"Date of approval{f}", "Status", "In project"]
        table.add_rows(contracts_list)
        print(table)
