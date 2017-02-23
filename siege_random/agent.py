import logging
import random
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)


@assist.action('greeting')
def greet_and_start():
    speech = "Hello! Do you want an attack or defense operator?"
    return ask(speech)


@assist.action("user-gives-attdef")
def ask_for_operator(attdef):
    if attdef == 'attack':
        attackers = ['sledge', 'thatcher', 'ash', 'thermite', 'twitch', 'montagne', 'glaz', 'fuzee', 'blitz', 'IQ', 'buck', 'blackbeard', 'capitao', 'hibana', 'jackal'];
        operator = random.choice(attackers)
    else:
        defenders = ['smoke', 'mute', 'castle', 'pulse', 'doc', 'rook', 'kapkan', 'lord chanka', 'bandit', 'jager', 'frost', 'valkyrie', 'caveira', 'echo', 'mira'];
        operator = random.choice(defenders)
    
    speech = operator

    return ask(speech)


if __name__ == '__main__':
    app.run(debug=true)
