# -*- coding: utf-8 -*-
from .magic import Spell
import random



class player:
    def __init__(self,name, hp , mp , atk  ,df ,magic,items):
        self.hp = hp
        self.name = name
        self.items = items
        self.mp = mp
        self.magic = magic
        self.df = df
        self.maxhp = hp
        self.atkH = atk + 25
        self.atkL= atk - 10
        self.actions=['Attack',"Magic","Items"]
        self.maxmp = mp

    def gen_dmg(self):
        return random.randrange(self.atkL,self.atkH)


    def get_dmg(self,dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp


    def get_max_mp(self):
        return self.maxmp

    def get_mp(self):
        return self.mp


    def reduce_mp(self,cost):
        self.mp -= cost


    def spell_cost(self, i):
        return self.magic[i]["cost"]


    def chose_action(self):
        print ("Actions")
        print ("===========")
        i = 1
        for item in self.actions:
            print("  " + str(i)+":" + str(item))
            i += 1

    def chose_magic(self):
        print ("Spells")
        print ("===========")
        i = 1
        for spell in self.magic:
            print ("        " + str(i) + ": " + str(spell.name) +  str( " (Cost: " + str ( spell.cost ) +")" ) )
            #the 3rd str helps to print it without the brackets
            i += 1


    def chose_item(self):
        print ("Items")
        print ("===========")
        i = 1
        for item in self.items:
            print("        " + str(i) + ": " +
                  str(item['item'].name) + str(" (" + str(item['item'].desc) + ") ") + " (x"+str(item['quantity'])+")")
            #the 3rd str helps to print it without the brackets
            i += 1


    def heal(self,dmg):
        self.hp += dmg


    def chose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.gen_spell_dmg()
        current_mp = self.get_mp()

        if spell.cost > current_mp:
            print("\nNo Magic Left...")
            self.chose_enemy_spell()
        else:
            return magic_dmg,spell


    def get_stats(self):
        hp_bar = ''
        bar_ticks = ( (self.hp/self.maxhp) * 100 ) / 4

        mp_bar = ''
        mp_bar_ticks = ( (self.mp/self.maxmp) * 100 ) / 10

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += '▒'
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/"+str(self.maxhp)
        mp_string = str(self.mp) +"/"+str(self.maxmp)
        current_hp = ''
        current_mp = ''

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += ' '
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        if len(mp_string) < 7:
            mp_decreased = 7 - len(mp_string)
            while mp_decreased > 0:
                current_mp += ' '
                mp_decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string



        print("                                _________________________           __________")
        print(str(self.name) + "          " + str(current_hp) +
              " |"+ hp_bar+"| " + str(current_mp) + " |"+mp_bar+"|")



    def get_enemy_stats(self):
        hp_bar = ''
        bar_ticks = ( (self.hp/self.maxhp) * 100 ) / 2
        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "


        hp_string = str(self.hp) + "/"+str(self.maxhp)
        current_hp = ''
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += ' '
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                                         __________________________________________________")
        print(str(self.name) + "          " + str(current_hp) +
            " |"+ hp_bar+"| ")


    def chose_target(self,enemies):
        i = 1
        print ("    Target:")
        for enemy in enemies:
            print("        " + str(i) + ": " +    str(enemy.name))
            i += 1
        choice = (int(input("    CHOSE TARGET: ") )  -1 )
        return choice

