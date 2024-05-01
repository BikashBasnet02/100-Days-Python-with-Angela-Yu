print('''
____________________________________________________________________
/ \-----     ---------  -----------     -------------- ------    ----\\
\_/__________________________________________________________________/
|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
|  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
| | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
|  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
|~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
|  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
|~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
|    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
| ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
|  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
|~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
| ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
|~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
| ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
|~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
| ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
/ \----- ----- ------------  ------- ----- -------  --------  -------\\
\_/__________________________________________________________________/ 
''')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure. \n')

print("You are on a mystical island, standing in front of a crossroad.")

stage1 = input('Where do you want to go (left or right)? ').lower()
if stage1 == 'right':
    print('You chose the right path.')
    print('You arrive at a river.')
    stage2 = input('Do you want to swim or wait for a boat? ').lower()

    if stage2 == 'swim':
        print('You decide to swim across the river.')
        print('A strong current drags you under, and you drown. Game over.')
    else:
        print('You wait for a boat and safely cross the river.')
        print('You come across three doors: one red, one blue, and one yellow.')
        door_choice = input('Which door do you choose (red/blue/yellow)? ').lower()

        if door_choice == 'red':
            print('You open the red door and are engulfed in flames. Game over.')
        elif door_choice == 'blue':
            print('You open the blue door and are attacked by a beast. Game over.')
        elif door_choice == 'yellow':
            print('You open the yellow door and find the treasure! Congratulations, you win!')
        else:
            print('You cannot make up your mind and stand there forever. Game over.')
else:
    print('You chose the left path.')
    print('You fall into a pit of snakes. Game over.')
