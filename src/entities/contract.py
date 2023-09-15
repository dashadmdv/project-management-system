import datetime


class Contract:
    def __init__(self, name, date_of_creation=None,
                 date_of_approval=None, status='draft', parent_project=None):
        self._name = name
        self._date_of_creation = date_of_creation or datetime.datetime.today().strftime('%Y-%m-%d')
        self._date_of_approval = date_of_approval
        self._status = status
        self._parent_project = parent_project

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
    def status(self, status: str):
        if status not in ['draft', 'active', 'completed']:
            pass
        else:
            if status == 'active':
                self._date_of_approval = datetime.datetime.today().strftime('%Y-%m-%d')
            self._status = status

    @property
    def parent_project(self):
        return self._parent_project

    @parent_project.setter
    def parent_project(self, project_id: int):
        if self._parent_project:
            pass
        else:
            self._parent_project = project_id
