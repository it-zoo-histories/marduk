import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_nlu.model import Interpreter
import time

class LogicCore(object):
    def __init__(self):
        self.intrepreter = RasaNLUInterpreter('models/current/nlu')
        self.nluModel = Interpreter.load('./models/current/nlu')
        self.dialogue = Agent.load('./models/current/dialogue', interpreter=self.intrepreter)
        self.unknown_command = "я вас не понял, попробуйте ещё раз"

    def newMessage(self, message): 
        response_from_dialogue = self.dialogue.handle_message(sender_id=1, message=message)
        print(response_from_dialogue)
        if len(response_from_dialogue) == 0:
            return ""
        else:
            return response_from_dialogue

    def interpreter(self, message):
        print("recognized: ", self.nluModel.parse(message))