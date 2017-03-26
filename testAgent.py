import xml.etree.ElementTree as ET
import os

if __name__ == '__main__':
    root = ET.parse('data.xml').getroot()
    attackers = []
    for attacker in root.iter('attacker'):
        attackers.append(attacker.text)
    print(attackers)
