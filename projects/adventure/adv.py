from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = r"projects\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
flip = {"n":"s", "s":"n", "w":"e", "e":"w"}

def traversal(visited=None):
    if visited is None:
        visited = set()

    path = []
    # Loop through exits and move the player through each
    for exit in player.current_room.get_exits():
        print("current room: ", player.current_room.id)
        print("taking exit: ", exit)
        player.travel(exit)
        print("exit room: ", player.current_room.id)

        # Check if the room has been visited
        if player.current_room not in visited:
            # Add if it has not been visited
            visited.add(player.current_room)
            # Add exit to path
            path.append(exit)
            # recurse with visited rooms
            path = path + traversal(visited)

            # Dead end reached, go back to previous room
            player.travel(flip[exit])
            path.append(flip[exit])

        # If Room already was visited then go back to previous room
        else:
            player.travel(flip[exit])


    # Finally, we output the path
    return path

traversal_path = traversal()
print(traversal_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
