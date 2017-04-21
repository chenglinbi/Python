from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(0,0) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit", "back"]

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        # ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # depending on whether or not it's been visited before,
        #   print either full description (first time visit) or brief description (every subsequent visit)

        print('Game menu')
        print(menu)
        print('Game action')
        print('GoNorth, GoSouth, GoEast, GoWest')
        choice = input("\nEnter action: ")
        choice = choice.lower()

        if choice == "gonorth":
            print(location)
        elif choice == 'gosouth':
            PLAYER.move_south()
            location = WORLD.get_location(PLAYER.x,PLAYER.y)
            print(location)
        elif choice == 'goeast':
            Player.move_east()
        elif choice == 'gowest':
            Player.move_west()



        # CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON USER'S CHOICE
        #    REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if the
        #               choice the user made was just a movement, so only updating player's position is enough to change
        #               the location to the next appropriate location
        # Possibilities: a helper function do_action(WORLD, PLAYER, location, choice)
        # OR A method in World class WORLD.do_action(PLAYER, location, choice)
        # OR Check what type of action it is, then modify only player or location accordingly
        # OR Method in Player class for move or updating inventory
        # OR Method in Location class for updating location item info, or other location data
        # etc....

