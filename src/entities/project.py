import datetime


class Project:
    def __init__(self, name):
        self._name = name
        self._date_of_creation = datetime.datetime.today().strftime('%d-%m-%Y')
        self._contracts = []

    @property
    def name(self):
        return self._name

    @property
    def date_of_creation(self):
        return self._date_of_creation

    @property
    def contracts(self):
        return self._contracts

    def add_contract(self, contract_id: int):
        if contract_id not in self.contracts:
            self.contracts.append(contract_id)
