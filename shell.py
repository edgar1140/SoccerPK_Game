import core, disk
from termcolor import cprint
import os


def welcome_message():
    cprint(disk.get_field(), 'yellow')


def shoot(player):

    cprint(r'''
     ,
     -   \O                                     ,  .-.___
   -     /\                                   O/  /xx\XXX\
  -   __/\ `                                  /\  |xx|XXX|
     `    \, ()                              ` << |xx|XXX|
  ^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ''', 'green')

    cprint('{} PRESS ENTER TO SHOOT'.format(player.name), attrs=['blink'])
    input('')
    os.system('clear')
    player.shoot()
    print(player)


def main():
    welcome_message()
    player_one = core.Futbol(
        input('Player one name:\n'), input('Player one team:\n'))
    print(player_one)
    os.system('clear')
    welcome_message()
    player_two = core.Futbol(
        input('Player two name:\n'), input('Player two team:\n'))
    print(player_two)
    os.system('clear')

    game = core.Game(player_one, player_two)
    while game.keep_game_going():
        shoot(player_one)
        shoot(player_two)

    print(game.winner())
    cprint(r'''
                _\\\_
                /^  ^\
               | *| * |
           __  |      |   __
           \ \ |  \/  |  / /
            \ \ \____/  / /
             \ \__||__ / /
              \         /
               \  GT   /
                \     |
                 \    |     ====
                 /    \    / /
                /  /\  \  / /
    _____      /  /  \  \/ /
   / \_/ \    /  /    \___/
  |\_/ \_/|   \ \
  |/ \_/ \|    \ \       
   \_/_\_/     _\ \
              ====/
    ''', 'blue')


if __name__ == '__main__':
    main()