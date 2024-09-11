place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
else:
    cave_action = input("light a torch or proceed in the dark?")
    if cave_action == "light a torch":
        print("You find a hidden treasure!")
    else:
        print("You stumbled and fell.")