import logging
import random
import os
from flask import Flask
from flask_assistant import Assistant, ask, tell, context_manager
import xml.etree.ElementTree as ET

app = Flask(__name__)
assist = Assistant(app)
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
root = ET.parse('data.xml').getroot()
operator = ''


@assist.action('greeting')
def greet_and_start():
    speech = "Hello! Do you want an attack or defense operator?"
    return ask(speech)


@assist.action("user-gives-attdef")
def ask_for_operator(attdef):
    if attdef == 'attack':
        attackers = []
        for attacker in root.iter('attacker'):
            attackers.append(attacker.text)
        random.shuffle(attackers)
        global operator = random.choice(attackers)
    else:
        defenders = []
        for defender in root.iter('defender'):
            defenders.append(defender.text)
        random.shuffle(defenders)
        global operator = random.choice(defenders)
    
    speech = operator

    return ask(speech)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
