import IPython
from IPython.display import clear_output, HTML, display
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('models/current/nlu')
messages = ["Hi! you can chat in this window. Type 'stop' to end the conversation."]
agent = Agent.load('./models/current/dialogue', interpreter=interpreter)

def chatlogs_html(messages):
    messages_html = ""
    for m in messages:
        if m.endswith('.jpg'):
             messages_html += "<img src={}, alt='Tiger pub'></img>".format(m)
        else:
             messages_html += "<p>{}</p>".format(m)
    chatbot_html = """<div class="chat-window" {}</div>""".format(messages_html)
    return chatbot_html

def messagesPrint(messages):
    for m in messages:
        print("new messages: ", m)        

while True:
    messagesPrint(messages)
    time.sleep(3)
    a = input()
    messages.append("[YOU]: " + a)

    if a == 'stop':
        break
    
    response = agent.handle_message(a)
    for r in response:
        print(r)
        messages.append("[BOT]: " + r.get('text'))
