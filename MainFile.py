# -*- coding: utf-8 -*-
from game_class.invin import Item
from game_class.game import player
from game_class.magic import Spell
import time
import random


# Player and Enemies magic create
Fire_Shot = Spell('Fire Shot', 15, 350, "Black Magic")
Thunder_Storm = Spell("Thunder Storm", 25, 550, "Black Magic")
Ninja_Summon = Spell("Ninja Summon", 30, 800, "Ninjustu")
The_End = Spell("THE END", 60, 3500, "Finisher")
Heal = Spell("HEAL ME", 50, 750, 'Heal')


player_magic = [Fire_Shot, Thunder_Storm, Ninja_Summon, Heal, The_End]

Shock = Spell('Electric Shock', 20, 350, "Black Magic")
DarkSlap = Spell('Dark Slap', 20, 350, "Black Magic")
RockShower = Spell('Rock Shower', 20, 350, "Black Magic")
EHeal = Spell("Dark Heal", 40, 2500, 'Heal')

enemy_magic = [Shock, DarkSlap, RockShower, EHeal]


LightingStorm = Spell('Dark Lighting Storm', 20, 450, "Black Magic")
BackBite = Spell('Dark Back Biting', 10, 250, "Black Magic")
Devine = Spell('Devine Darkness', 40, 550, "Black Magic")
DarkHeal = Spell("Divine Darkness Heal", 30, 4500, 'Heal')

boss_magic = [LightingStorm, BackBite, Devine]


# Items create
potion = Item("Potion", 'Potion', 'Heals Nigga for 50 HP', 50)
high_potion = Item("Potion+", 'Potion', 'Heals Nigga for 120 HP', 120)
super_potion = Item("Ultra Potion", 'Potion', 'Heal nigga for 250 HP', 250)
elixir = Item("Elixir", 'Elixir', 'Give 1 Nigga EVERYTHING BACK', 1000)
high_elixir = Item("Omega Elixir", 'Elixir',
                   'Give all Niggas EVERYTHING BACK', 1000)
bomb = Item("Bomb", 'Attack', 'Deals 350 Damage', 350)

player_items = [{"item": potion, "quantity": 3},
                {'item': high_potion, "quantity": 2}, {"item": super_potion, "quantity": 1}, {'item': elixir, "quantity": 2}, {'item': high_elixir, "quantity": 1}, {"item": bomb, "quantity": 2}]


# PLAYER CREATE
Player1 = player('Night-Man  ', 3200, 120, 4065, 40, player_magic, player_items)
Player2 = player('Ray-Wills  ', 3200, 120, 3185, 35, player_magic, player_items)
Player3 = player("Randy-Orton", 3200, 120, 4180, 20, player_magic, player_items)

Enemy1 = player("Left-Keeper       ", 10000, 200, 250, 50, enemy_magic, None)
Boss = player("Nito-The-Gravelord", 18000, 350, 350, 60, boss_magic, None)
Enemy2 = player("Right-Keeper      ", 8000, 200, 250, 50, enemy_magic, None)

enemies = [Enemy1, Boss, Enemy2]
players = [Player1, Player2, Player3]


# Game starts

run = True
i = 1

while run:
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")
    print("\n")

    print("  NAME                           HP                                 MP\n")

    for player in players:
        player.get_stats()
    print("\n┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬")
    print("┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴")

    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:

        print("\n")
        player.chose_action()
        print("--------------------------")
        print(player.name)
        print("--------------------------")
        choice = input("CHOSE ACTION: ")
        index = (int(choice)) - 1

        if index == 0:
            dmg = player.gen_dmg()
            enemy = player.chose_target(enemies)
            if len(enemies)>0:
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", '') + " killed")
                    del enemies[enemy]
                else:

                    enemies[enemy].get_dmg(dmg)
                    print("\n"+player.name.replace(" ", '').replace(" ", '') + ' attacked ' +
                        enemies[enemy].name.replace(" ", '').replace(" ", '') + ' for ' + str(dmg) + ' damage points\n')
            else:
                print ("WIN")
                run = False

        elif index == 1:
            player.chose_magic()
            magic_choice = (int(input("Chose Spell: ")) - 1)

            spell = player.magic[magic_choice]
            magic_dmg = spell.gen_spell_dmg()
            current_mp = player.get_mp()
            if magic_choice == -1:
                continue

            if spell.cost > current_mp:
                print("\nNOT ENOUGH MANA")
                continue

            if spell.stype == "Heal":
                player.heal(magic_dmg)
                player.reduce_mp(spell.cost)
                print(str(magic_dmg) + ' HP restored')
                print("HP:", player.get_hp())

            elif spell.stype == "Black Magic" or spell.stype == "Ninjustu" or spell.stype == "Finisher":
                player.reduce_mp(spell.cost)
                enemy = player.chose_target(enemies)
                enemies[enemy].get_dmg(magic_dmg)
                print(str(spell.name) + ' did damage of ' + str(magic_dmg) +
                      " points against " + enemies[enemy].name.replace(" ", ''))
                print("Remaining Magic Points: " +
                      str(player.get_mp()) + "/" + str(player.get_max_mp()))
                if len(enemies)>0:
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name.replace(" ", '') + " killed")
                        del enemies[enemy]
                    else:
                        enemies[enemy].get_dmg(magic_dmg)

                else:
                    print ("WIN")
                    run = False


        elif index == 2:
            player.chose_item()
            item_choice = (int(input("Chose Item: ")) - 1)
            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']
            if player.items[item_choice]['quantity'] == 0:
                print("No Item...")
                continue
            player.items[item_choice]['quantity'] -= 1

            if item.itype == 'Potion':
                player.heal(item.prop)
                print(str(item.name) + " used and healed NIGGA for " +
                      str(item.prop) + " HP")
            elif item.itype == "Elixir":
                if item.name == "Omega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print("\n"+"STATS RESTORED BECASUE OF " + str(item.name))
            elif item.itype == "Attack":
                enemy = player.chose_target(enemies)
                enemies[enemy].get_dmg(item.prop)
                print("You used a 'Bomb!!!' MAN & that dealt damage of " +
                      str(item.prop) + " against " + enemies[enemy].name.replace(" ", '')+"\n")

                if enemies[enemy].get_hp() == 0:
                    del enemies[enemy]
                    print(enemies[enemy].name.replace(" ", '') + " killed")


# check if game is over
    defeated_enemies = 0
    defeated_heros = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            print('')
            print('ENEMY DEAD')
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            print('')
            print('You are DEAD')
            defeated_heros += 1

    if defeated_enemies == 3:
        print("YOU WIN")
        time.sleep(1)
        run = False
    elif defeated_heros == 3:
        print("YOU LOST")
        time.sleep(1)
        run = False

    elif index == 3:
        print("Arigato Gozaimasu for playing")
        time.sleep(1)
        print("BYE BYE")
        run = False

    for enemy in enemies:
        enemy_choice = random.randrange(0, 3)
        if len(players) == 0:
            print ("GAMEOVER"*1)
            run = False
        else:
            target = random.randrange(0,len(players))
            if enemy_choice == 0:
                enemy_dmg = enemy.gen_dmg()
                players[target].get_dmg(enemy_dmg)
                print(
                    "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")
                print(enemy.name+" attacked " +     str(players[target].name)+" for " + str(enemy_dmg))

                if players[target].get_hp() == 0:
                    print(players[target].name + " died")
                    del players[target]


            elif enemy_choice == 1:
                magic_dmg, spell = enemy.chose_enemy_spell()
                print(
                    "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")

                if spell.stype == "Heal":
                    enemy.heal(magic_dmg)
                    enemy.reduce_mp(spell.cost)
                    print(str(magic_dmg) + ' HP restored')
                    print("HP:", enemy.get_hp())

                elif spell.stype == "Black Magic":
                    enemy.reduce_mp(spell.cost)
                    print(enemy.name + " attacked " + str(players[target].name) + " for " + str(magic_dmg) + " HP Points")
                    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n")

                    players[target].get_dmg(magic_dmg)
                    if players[target].get_hp() == 0:
                        print(players[target].name + " died")
                        del players[target]


