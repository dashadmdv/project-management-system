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

        prompt = "I want to work with 1 - projects, 2 - contracts"
        while True:
            entity_choice = self.input_with_check(
                prompt, ['1', '2'], back_mode=False)
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
        prompt += (self.project_list_prompt +
                   self.contract_list_prompt +
                   (self.back_prompt if back_mode else self.exit_prompt) +
                   self.hint_prompt)
        values_list.extend(['8', '9', '0'])
        while True:
            value = input(prompt)
            if value not in values_list:
                print("No such option! Try again!")
                continue
            return value

    # so that we can input id = 8 or 9
    def input_id_with_check(
            self, prompt: str, values_list: list, back_mode=True):
        prompt += (", or also _8 (with _ !) - show projects list" + ", _9 (with _ !) - show " +
                   "contracts list" + (self.back_prompt if back_mode else self.exit_prompt)) + ": "
        values_list.extend(['_8', '_9', '0'])
        while True:
            value = input(prompt)
            if value not in values_list:
                print("No such option! Try again!")
                continue
            return value

    def always_available_operations(self, choice):
        if choice in ['8', '9', '0']:
            match choice:
                case '8':
                    self.show_projects_list()
                    return False
                case '9':
                    self.show_contracts_list()
                    return False
                case '0':
                    return True

    def always_available_operations_input_id(self, choice):
        if choice in ['_8', '_9', '0']:
            match choice:
                case '_8':
                    self.show_projects_list()
                case '_9':
                    self.show_contracts_list()
                case '0':
                    return True
        else:
            return True

    def project_dialog(self):
        prompt = (
            "Choose an option 1 - create project, 2 - add a contract to the project, " +
            "3 - complete the contract")
        while True:
            project_action_choice = self.input_with_check(
                prompt, ['1', '2', '3'])
            if self.always_available_operations(project_action_choice):
                break
            match project_action_choice:
                case '1':
                    print(self.controller.add_project())
                case '2':
                    project_ids = self.controller.get_projects_ids()
                    if not project_ids:
                        print("There are no projects!")
                        continue
                    project_id = None
                    contract_id = None
                    while True:
                        while True:
                            project_id = self.input_id_with_check(
                                "Select project to add to (ENTER ID)",
                                self.controller.get_projects_ids())
                            if self.always_available_operations_input_id(
                                    project_id):
                                if self.controller.count_active_contracts_by_project(
                                        project_id) == 1:
                                    print(
                                        "This project already has an active contract! Choose another one!")
                                    continue
                                break
                        if project_id == '0':
                            break
                        while True:
                            contract_id = self.input_id_with_check(
                                "Select contract to add to (ENTER ID)",
                                self.controller.get_contracts_ids())
                            if self.always_available_operations_input_id(
                                    contract_id):
                                break
                        if contract_id == "0":
                            continue
                        break
                    if project_id == '0':
                        continue
                    if int(project_id) and int(contract_id):
                        print(self.controller.add_contract_to_project(
                            contract_id, project_id))
                case '3':
                    project_ids = self.controller.get_projects_ids()
                    if not project_ids:
                        print("There are no projects!")
                        continue
                    while True:
                        project_id = self.input_id_with_check(
                            "Select project that has the needed contract (ENTER ID)",
                            self.controller.get_projects_ids())
                        if not self.always_available_operations_input_id(
                                project_id):
                            continue
                        break

                    if not int(project_id):
                        continue

                    contracts_list = self.show_contracts_list(
                        source=self.controller.get_all_contracts_by_project(project_id))
                    if not contracts_list:
                        print("There are no contracts!")
                        continue
                    while True:
                        contract_id = self.input_id_with_check("Select contract to complete (ENTER ID)",
                                                               [str(x[0]) for x in contracts_list])
                        if not self.always_available_operations_input_id(
                                contract_id):
                            continue
                        break
                    if not int(contract_id):
                        continue
                    if self.controller.get_contract(
                            contract_id)[-2] == 'completed':
                        print(
                            "The contract is already completed! Choose another one!")
                        continue
                    print(self.controller.change_contract_status(
                        contract_id, 'completed'))

    def contract_dialog(self):
        prompt = "Choose an option 1 - create a contract, 2 - approve the contract, 3 - complete the contract"
        while True:
            contract_action_choice = self.input_with_check(
                prompt, ['1', '2', '3'])
            if self.always_available_operations(contract_action_choice):
                break
            match contract_action_choice:
                case '1':
                    print(self.controller.add_contract())
                case '2':
                    contract_ids = self.controller.get_contracts_ids()
                    if not contract_ids:
                        print("There are no contracts!")
                        continue
                    while True:
                        contract_id = self.input_id_with_check(
                            "Select contract to approve (ENTER ID)", contract_ids)
                        if not self.always_available_operations_input_id(
                                contract_id):
                            continue
                        break
                    if not int(contract_id):
                        continue
                    if self.controller.get_contract(
                            contract_id)[-2] == 'active':
                        print("The contract is already approved! Choose another one!")
                        continue
                    elif self.controller.get_contract(contract_id)[-2] == 'completed':
                        print("The contract is completed! Choose another one!")
                        continue
                    print(self.controller.change_contract_status(
                        contract_id, 'active'))
                case '3':
                    contract_ids = self.controller.get_contracts_ids()
                    if not contract_ids:
                        print("There are no contracts!")
                        continue
                    while True:
                        contract_id = self.input_id_with_check(
                            "Select contract to complete (ENTER ID)", contract_ids)
                        if not self.always_available_operations_input_id(
                                contract_id):
                            continue
                        break
                    if not int(contract_id):
                        continue
                    if self.controller.get_contract(
                            contract_id)[-2] == 'completed':
                        print(
                            "The contract is already completed! Choose another one!")
                        continue
                    print(self.controller.change_contract_status(
                        contract_id, 'completed'))

    def show_projects_list(self):
        projects_list = self.controller.get_projects_list()
        table = PrettyTable()
        table.field_names = ["Project id", "Name",
                             "Date of creation (yyyy-mm-dd)"]
        table.add_rows(projects_list)
        if not projects_list:
            print("There are no contracts!")
        else:
            print(table)

    def show_contracts_list(self, source=None):
        contracts_list = source if source is not None else self.controller.get_contracts_list()
        table = PrettyTable()
        f = " (yyyy-mm-dd)"
        table.field_names = ["Contract id", "Name", f"Date of creation{f}",
                             f"Date of approval{f}", "Status", "In project"]
        table.add_rows(contracts_list)
        if not contracts_list:
            print("There are no contracts!")
        else:
            print(table)
        return contracts_list
