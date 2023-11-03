from random import random

attack_dict = {}

with open('attacks.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',')
        attack_dict[str(values[1])] = {'id': int(values[0]),
                                       'name': str(values[1]),
                                       'type': str(values[2]),
                                       'category': str(values[3]),
                                       'damage': int(values[4]),
                                       'probability': float(values[5]),
                                       'ap': int(values[6])}

class Pokemon:
    def __init__(self, name, hp_i, att_val, def_val, att1, att2, att3, att4):
        self.name = name
        self.type = type
        self.hp_i = hp_i
        self.hp_f = hp_i
        self.active = True
        self.att_val = att_val
        self.def_val = def_val
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4

    def get_damage(self, dmg):
        self.hp_f -= dmg
        if self.hp_f <= 0:
            self.active = False

    def do_damage(self, opponent, attack):
        att = attack_dict[attack]
        print(f"{self.name} ({self.hp_f}/{self.hp_i}) attacks with {att['name']}.")
        if random() < att['probability']:
            dmg = int(att['damage'] * self.att_val / opponent.def_val)
            opponent.get_damage(dmg)
            print(f"Success! {self.name} hits {opponent.name} with {dmg} points.")
