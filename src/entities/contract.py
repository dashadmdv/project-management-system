import datetime


class Contract:
    def __init__(self, name):
        self._name = name
        self._date_of_creation = datetime.datetime.today().strftime('%d-%m-%Y')
        self._date_of_approval = None
        self._status = 'draft'
        self._parent_project = None

    @property
    def name(self):
        return self._name

    @property
    def date_of_creation(self):
        return self._date_of_creation

    @property
    def date_of_approval(self):
        return self._date_of_approval

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, s: str):
        if s not in ['draft', 'active', 'completed']:
            pass
        else:
            if s == 'active':
                self._date_of_approval = datetime.datetime.today().strftime('%d/%m/%Y')
            self._status = s

    @property
    def parent_project(self):
        return self._parent_project

    @parent_project.setter
    def parent_project(self, project_id: int):
        if self._parent_project:
            pass
        else:
            self._parent_project = project_id
