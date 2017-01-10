"""
A simple text adventure designed as a learning experience for new programmers.
""" # looks like the main script to run the game from
__author__ = 'Phillip Johnson' # in every file so far. Must add something
import world # The world module is standalone. Maybe I'll start here...
from player import Player #imports the world and the player class


def play():
    world.load_tiles() #loads the tiles for the world and stores them in world._world
    player = Player() #player is the instance of the Player class
    room = world.tile_exists(player.location_x, player.location_y) #player already received start location
    print(room.intro_text()) #only used for starting room
    while player.is_alive() and not player.victory: #this is the loop that keeps the game going
        room = world.tile_exists(player.location_x, player.location_y) #checks if tile exists and populates room
        room.modify_player(player) #runs the modify player method that every room has. Can be from an enemy attack
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n") #prompts for action
            available_actions = room.available_actions() #from the tiles.py that is
            # imported into the _world dictionary with the getattr in world.py
            for action in available_actions: #prints the action list, different in different room types
                print(action)
            action_input = raw_input('Action: ') #changed this to raw_input
            for action in available_actions: #checks action list for input action hotkey
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs) #uses the mysterious do_action method
                    break #breaks the for loop and returns to start of while loop


if __name__ == "__main__":
    play()
