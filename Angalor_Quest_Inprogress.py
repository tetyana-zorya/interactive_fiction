#The Quest begins...
import turtle
print("Welcome to 'The Quest of Angalor'")
print("Note that if you are not asked for an input and the cursor blinks, simply press enter on your keyboard to continue...")
print()
print()
print("Let's begin...")
three = input("")
print("CHAPTER ONE: RUMORS")
four = input("")
print()
print("It's been a long day on horseback. Every part of you aches, and Ganandorf, your horse is begining to slow his pace...")
print("You see a nearby village and decide to stop by the local inn...")
print("You tie up Ganandorf at the horse post, and walk into the inn...")
print("You can either grab a drink and some stew at the bar, or you can get a room for the night.")
print()
while True:
    choice_1 = input("Choose either 'drink' or 'room': ")
    if choice_1.lower() == "drink" or choice_1.lower() == "room":
        break
    else:
        print("invalid choice sire, try your hand again")
print()

def quest_hunt_vill_trav():
   print("The rumors are true...the darkness is real...and its closer than you think. Those in Arelon, or Kandor have heard merely whispers and could not imagine that it is here...yes it is here")
   five = input("")
   print("We can all feel it...the evil of Ruin...its malicious essence...mmmmmmmmm....yes...yes,yes,yes...it radiates from the caves of Angalor...")
   six = input("")
   print("There have been stories...of those who wander too close...those that disapear, or come back as husks of themselves...bodies intact but heads...thoughts...not theirs...")
   seven = input("")
   print("Ruin is here...Kae feels it...and suffers it...as year by year the crops wither...")
   eight = input('')
   print("Here take this...")
   print()
   print("You look at the scrap of parchment handed to you, and see it's a map of sorts...")



def room_night():
    print("You walk into the inn, and approach the innkeeper.")
    print()
    print("She is an older woman, plump, and jolly, which contrasts severely with the rest of the inn.")
    print("She sees that you're not from these parts and begins to tell you all about Kae...as she energetically rants...")
    print("She gives you a room key and says she'll bring up some stew as soon as she gets a chance...")
    one = input("")
    print("You go to your room and minutes later she knocks at your door holding a bowl of stew, and still telling you all about the village.")
    print()
    print("And then she mentions something...something you have heard rumors about all the way in Arelon. But this is Kae, thousands of miles away, why would I be hearing about this here?")
    print()
    print("You intervene, 'tell me, what do they say in these parts about the Ruin?'")
    print()
    print("She looks you in the eye and furrows her brows, and says: ")
    ent = input("")
    quest_hunt_vill_trav()
    print("You look up from the map and ralize the woman has left.")

def bar():
    print("You walk up to the barkeep. He looks old...not just old, skin sagging and greying hair, but old in his eyes.")
    print()
    print("There is a sort of hopelessness in him you haven't seen in a long while, even though this is your 12th village this month")
    print()
    while True:
        bar_choice = input("You ask the barkeep for a drink. Do you spark a conversation with him or find a seat? ('speak' or 'sit') ")
        if bar_choice.lower() == 'sit' or bar_choice.lower() == 'speak':
            break
        else:
            print("you know that's not a choice my leige...try again")
    if bar_choice == 'speak':
        print('You look at the old barkeep and say: "Ive been traveling for days now and havent run into a village, would you let me join you and hear about all of the news of this little part of the world?"')
        print()
        print("Oh my sir, he says in his creaky voice, 'there been some bad things happening in Kae...and then he says something...something you have heard rumors about all the way in Arelon. But this is Kae, thousands of miles away, why would I be hearing about this here? you think to yourself.'")
        nine = input("")
        print("You intervene, 'tell me, what do they say in these parts about the Ruin?' ")
        print()
        print("The  old man looks at you with beady eyes, and furrowed brow, and says: ")
        ten = input("")
        quest_hunt_vill_trav()
        print("You look up from the map and see the barkeep has moved on to cleaning the bar")
    if bar_choice == 'sit':
        print("You take a look around...there are what look like a couple village regulars at the leftmost table, and lone traveler in the corner, and a group of what look like hunters on the right.")
        print()
        print("You take a deep breath and decide....")
        while True:
            hunt_reg_trav = input("'traveler', 'hunters' or 'villagers'? ")
            if hunt_reg_trav.lower() == 'hunters' or hunt_reg_trav.lower() == 'traveler' or hunt_reg_trav.lower() == 'villagers':
                break
            else:
                print("Oh my sir, getting greedy with your choices again, there are only three...try it again")


        if hunt_reg_trav == 'hunters':
            print("You walk up the group of hunters. They hush their energetic conversation and turn to look at you.")
            two = input("")
            print("""You say: "hello there my good fellows, I've been traveling for days now and haven't run into a village, would you let me join you and hear about all of the news of this little part of the world? """)
            eleven = input('')
            print("They all smile, and offer you a seat, and resume their conversation. You realize they're talking about something...something you have heard rumors about all the way in Arelon. But this is Kae, thousands of miles away, why would I be hearing about this here?")
            twelve = input("")
            print("You intervene, 'tell me, what do they say in these parts about the Ruin?'")
            print()
            print("The man with the large orange beard turns to you and with a gleam in his eye says: ")
            thirteen = input("")
            quest_hunt_vill_trav()
            print("You look up from the map and see the conversation has resumed without you")
        if hunt_reg_trav == 'traveler':
            print("You walk up the traveler. You say 'Hello there good fellow, would you mind if I sit?'")
            fourteen = input("")
            print('The young man waves his hand as to say "go ahead"...')
            print("Tell me of your travels, good sir, for I have traveled many days and nights and have not heard any news from this part of the world for very long")
            fifteen = input("")
            print("He begins to tell you about his travels, and then he mentions something...something you have heard rumors about all the way in Arelon. But this is Kae, thousands of miles away, why would I be hearing about this here? you think to yourself.")
            sixteen = input("")
            print("You intervene, 'tell me, what do they say in these parts about the Ruin?'")
            print()
            print("He looks into your eyes, the green in his turning from a dark olive to a spring leaf, and says: ")
            seventeen = input("")
            quest_hunt_vill_trav()
            print("You look up from the map and see that the traveler is getting up to retire for the night.")
        if hunt_reg_trav == 'villagers':
            print("You walk up the group of villagers. They hush their already quiet conversation and turn to look at you.")
            eighteen = input("")
            print("""You say: "hello there my good fellows, I've been traveling for days now and haven't run into a village, would you let me join you and hear about all of the news of this little part of the world? """)
            nineteen = input("")
            print("They all grumble a bit, but offer you a seat, and resume their conversation. You realize they're talking about something...something you have heard rumors about all the way in Arelon. But this is Kae, thousands of miles away, why would I be hearing about this here?")
            print()
            print("You intervene, 'tell me, what do they say in these parts about the Ruin?'")
            print()
            print("The man with the large nose and beady eyes turns to you and with a serious look in his eye says: ")
            twenty = input("")
            quest_hunt_vill_trav()
            print("You look up from the map and realize the villagers have resumed their conversation without you.")


print()
if choice_1 == "drink":
    bar()
if choice_1 == "room":
    room_night()
print()
print("You shove the map into you pocket, and retire for the night.")
enter = input("")
print()
print("CHAPTER 2: THE QUEST BEGINS")
print()
print("You wake up...beads of sweat roll down your face as you try to clam your heart rate.")
print('"Ruin...Ruin...Ruin" echoes through your head.')
print()
print("Angalor.")
print("Angalor is where you must go.")
print()
twentyone = input("")
print("You pull out the map that you got last night. Its hard to read...it there are two routes, one west through the steppes, and one east through the mountains...")
print()
print("You decide to get ready to go, and that you will decide which route to take by your gut when it is time...")
print()
print("You step out of the inn. The sun is still behind the mountains to your east, the air feels cold, and mist covers the ground.")
twenty_one = input("")
print("You prepare Ganandorf, and begin down the King's Road, North for now.")
print(".....")
print("The road splits. You must make a choice...")

while True:
    east_west = input("'east' or 'west'? ")
    if east_west.lower() == 'east' or east_west.lower() == 'west':
        break
    else:
        print("Hmm, seems like there are only two ways to go...choose again")

if east_west.lower() == 'east':
    print("'Mountains it is then...its going to get much colder very soon' you mutter to yourself.")
    print()
if east_west.lower() == 'west':
    print("'The steppes it is then...I wonder if Dimitri still lives in Tramdyr' you mutter to yourself.")
    print()
