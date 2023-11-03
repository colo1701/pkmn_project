import pkmn_classes as pkmn

if __name__ == '__main__':
    player1 = pkmn.Pokemon("Pikachu", 200, 20, 35, "Superzahn", "", "", "")
    player2 = pkmn.Pokemon("Rattfratz", 200, 30, 20, "Biss", "", "", "")

    while player1.active and player2.active:
        player1.do_damage(player2, player1.att1)
        if player1.active and player2.active:
            player2.do_damage(player1, player2.att1)

    if not player1.active:
        print(f"{player1.name} was defeated. {player2.name} wins!")
    if not player2.active:
        print(f"{player2.name} was defeated. {player1.name} wins!")
