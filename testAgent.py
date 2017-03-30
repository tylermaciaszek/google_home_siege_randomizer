import xml.etree.ElementTree as ET
import os

if __name__ == '__main__':
    operator = 'Twitch'
    root = ET.parse('data.xml').getroot()
    attackers = []
    for attacker in root.iter('attacker'):
        attackers.append(attacker.text)
    print(attackers)
    defenders = []
    for defender in root.iter('defender'):
        defenders.append(defender.text)
    print(defenders)

    for attacker in root.findall('attacker'):
        print(attacker.find('ctu').text)
        print(operator)
        if attacker.text == operator:
            print('yes')
        else:
            print('no')
           
