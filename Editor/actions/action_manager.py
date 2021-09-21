from actions.remove_action import RemoveAction
from actions.open_action import OpenAction
from actions.create_file import CreateFile
from actions.info_action import InfoAction


class ActionManager(object):
    def __init__(self):
        self.remove_action = RemoveAction()
        self.open_action = OpenAction()
        # doadaje fajl gde ce se dodati tabela
        self.create_file = CreateFile()
        self.inof_action = InfoAction()
