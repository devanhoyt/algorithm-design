import time
import random
from random import randint
storytime = random.randint(0, 130)
storytime2 = random.randint(0, 130)
def intro():
    print ("Hello....................")
    time.sleep(2)
    print("Welcome. You are about to engage in the difficult process of decision making. ")
    print("Your choices determine your future. ")
    print(" Indecision is punishable. Mistakes are costly.")
    decision = input("Are you prepared to continue? Y/N\n")
    if decision == "Y" or decision == "y":
        yourstory()
    elif decision == "N" or decision == "n":
        ending3()
    elif decision == "IDK":
        print("Wrong answer. Goodbye.")
    else:
        ending3()
def arc1():
    arc1dec = ""
    print("Its dark outside. The woods around you move slowly around you in the night sky.")
    print("As you are walking forward you see a large shack. There are no windows and you have no way to know what is inside.")
    print("Suddenly you hear a howl close to you. Something is near.")
    arc1dec = input("The choice is yours. Do you KNOCK or RUN?")
    if arc1dec == "KNOCK" or arc1dec == "Knock" or arc1dec == "knock":
        print("KNOCK")
        time.sleep(2)
        print (".. KNOCK")
        time.sleep(2)
        print (".... knock")
        time.sleep(1)
        print ("The last knock cutting off as the door creaks open")
        print ("Inside is a dark room with a wooden bed, and a desk and chair with a book on it. Outside the crunching of leaves underfoot")
        print (" grows louder. You rush inside and shut and lock the door behind you. ")
        arc1dec2 = input("Do you HIDE under the bed or READ the book?")
        if arc1dec2 == "HIDE" or arc1dec2 == "Hide" or arc1dec2 == "hide":
            print("""You hide under the bed. You hear the sound of something banging against the door and then all of a sudden
            it slams wide open! A scarred man stumbles inside falling down at eye level to you and looks up. He sees you.""")
            ending2()
        elif arc1dec2 == "READ" or arc1dec2 == "Read" or arc1dec2 == "read":
            print("You try and read the book at the table, but the light inside is almost nonexistent and you can hardly see the words")
            print("You sit quietly at the desk, waiting, and hardly breathing. You hear nothing but the echoing silence around you. The")
            print(" very trees outside have gone silent. Your heart thumps in your chest growing louder and louder. You have to do something!")
            arc1dec3 = input("Do you OPEN the door, BARRACADE the door, or try to start a FIRE?")
            if arc1dec3 == "OPEN" or arc1dec3 == "Open" or arc1dec3 == "open":
                print("The overwhelming curiosity takes control of you and you have to know whats outside.")
                print("You open the door to see a man standing in front of the door. Your last thought is ")
                time.sleep(2)
                print("its so cold\n\n\n\n")
                ending2()



            elif arc1dec3 == "BARRACADE" or arc1dec3 == "Barracade" or arc1dec3 == "barracade":
                print("You barracade the door with the desk and chair. Just as you do a large pounding shakes the shack violently.")
                print('"Let me in!" a loud voice shouts from the other side. You frantically reach into your pocket to call for help.')
                print("As you dial 911 into your phone the table bounces off the door with the shock of the door swinging open.")
                print("You scream and back into the shack. A large man stumbles forward into the shack, off balance from the door suddenly")
                print(" opening. You race out of the shack, running as fast as you can away from the shack and the man.")
                ending1()
            elif arc1dec3 == "FIRE" or arc1dec3 == "Fire" or arc1dec3 == "fire":
                print("You break the chair up and push the pieces into the fireplace on the side of the shack. The cobwebs")
                print(" make excellent kindling to start the fire with your trusty lighter. As the light begins to enter the shack")
                print(" you look at the book laying on the table and read.")
                print(" Journal")
                print("On the front cover. You thumb through the pages reading about a man who lost his mother and father when he was a child")
                print(" and how he never forgave them for abandoning him. The man was the reason they died and it left him scarred and unable his new")
                print(" reality. He was driven mad with rage and hatred. Blaming everyone else for their death, he vowed to get his revenge.\n")
                print(" As you finish reading the journal, the door slams open. A scarred man stands in the doorway.")
                ending2()
            else:
                print("Indecision is punishable. Mistakes are costly. You get to try again this time but you might not always be lucky.")
                arc1()
        else:
            print("Indecision is punishable. Mistakes are costly. An intruder breaks through the door and this is the end for you.")

    elif arc1dec == "RUN" or arc1dec == "Run" or arc1dec == "run":
        print ("You take off running away from the shack and the noise you heard. The sound of your footsteps crunching")
        print (" against the leaves sends chills down your spine. The howling you heard earlier gets louder and you recognise it for")
        print("What it is. Someone screaming in the night. Begging for help. ")
        dec4 = input("Do you HELP or HIDE or RUN?")
        if dec4 == "HELP" or dec4 == "Help" or dec4 == "help":
            print("You turn and search for the source of the noise. You rush towards it, but loose your footing and fall, twisting your ankle.")
            print(" As you cry out in pain, a dark figure walks out from behind a tree. Its a scarred man.")
            print(" You don't say a word. Just watch, frozen in terror as he walks towards you.\n\n\n\n")
            ending2()
        elif dec4 == "HIDE" or dec4 == "Hide" or dec4 == "hide":
            print("You hide behind a tree. As you hide there you see a scarred man walking. He stops and cries out for help.")
            print("You stop and hold your breath wondering if he sees you. ")
            dec5 = input("Do you RUN or HIDE?")
            if dec5 == "RUN" or dec5 == "Run" or dec5 == "run":
                print("You run thinking you were spotted. The man sees you run and chases after you. But he's quicker.")
                ending2()
            if dec5 == "HIDE" or dec5 == "Hide" or dec5 == "hide":
                print("You stay silent and don't move. The man stays still and appears to be listening. After a few moments he")
                print("Continues walking. After a hundred feet or so he cries out for help again. You continue watching him for")
                print(" a few minutes til he goes out of sight. Then you quietly run the other way, towards saftey.")
                ending1()
        elif dec4 == "RUN" or dec4 == "Run" or dec4 == "run":
            print("You keep running. You can hear the pounding of someone elses footsteps behind you but it is faint")
            print(" and getting quieter the farther you go. You look over your shoulder and see a scarred man stop chasing you and turn around.")
            print("But All you care about though is how far you can go. You keep running for what feel like hours until you come across a road.")
            print(" You follow the road and see a town in the distance. As you get closer, you hear the rumbling of a truck behind you. ")
            print("You feel a sense of relief until you see the driver. Its the same man that was chasing you. ")
            ending2()
        else:
            print("Try again.")
            arc1()
    elif decision == "IDK":
        print("Wrong answer. You die.")
    else:
        print("Try again.")
        arc1()


def arc2():
    print("The sun is bright and everything is right! You are walking with your....")
    companion = input("MOM   DAD   FRIEND")
    if companion == "MOM" or companion == "Mom" or companion == "mom":
        print("You are with your mom. While walking on the neighborhood street you come upon an ice cream truck")
        print('Overcome by memories of your childhood, you ask your mom one more time for a ')
        x = input("SPIDERMAN popscicle or a CHOCO taco?")
        if x == "SPIDERMAN" or x == "Spiderman" or x == "spiderman":
            print("You get a Spiderman popscicle, the one with the lemon and strawberry ice cream and bubble gum eyes.")
            print("Life is going simple and great. The sun feels nice out as you eat your ice cream while walking with your mother.")
        elif x == "CHOCO" or x == "Choco" or x == "choco":
            print("""Popsaicles jusat aren't for you anymore. You've progressed onto the finer things of life and want to enjoy 
            that delectable choco taco. Life is going good and you are on top of the world. As you are walking you see a large dog
            in the road. Do you PET him or WALK away? """)
            y = input("PET or WALK")
            if y == "PET" or y == "Pet" or y == "pet":
                print("""You aproach slowly and stick your hand out for him to smell. He sniffs you curiously and nudges closer 
                and you start petting him. Ice cream and a dog... doesn't get much better. """)
            else:
                print(""" You keep walking and the dog continues on his way. You don't want to risk it, dogs can be scary even if 
                they do look like clifford. """)
    if companion == "DAD" or companion == "Dad" or companion == "dad":
        print("""You are with your dad. As you are walking he is telling a story about a time you both went ice fishing that you've heard
        a million times. do you not say anything and LISTEN or CHANGE the topic? """)
        z = input("LISTEN or CHANGE the topic?")
        if z == "LISTEN" or z == "Listen" or z == "listen":
            print(""" You continue listening patiently as he continues his story. You don't get to see him often anymore and its
            nice to hear him so excited. After he finishes his recounting he reaches out and hugs you. He appreciates you listening
            and tells you that he knows you've heard it a million times. You feel closer than ever before with your dad. """)
        else:
            print(""" You interrupt him and tell him that you've heard that story a million times. He looks sad but agrees. You feel
            guilty for interuppting him when he was getting so excited and suggest you try and find a time to go out and find a new 
            spot around your college town that you could go fishing. He perks up at this and you both begin planning it out.""" )
    
    if companion == "FRIEND" or companion == "Friend" or companion == "Friend":
        print("""You are with your friend. You're walking down the road after getting lunch at the local taco bellery and hear another friend 
        call out from a car. "Hey do you guys want a ride?" do you RIDE or WALK """)
        a == input("RIDE or WALK")
        if a == "RIDE" or a == "Ride" or a == "ride":
            print(""" You yell out "Sure!" and hop in their car. Theres only one seat open so your friend has to keep walking. You ride 
            home and as you get dropped off at your apartment you get a call from your friend and he seems frustrated. You tell him you're sorry 
            but you didn't want to walk anymore. To make up for it you do all the dishes and take out the trash while you wait. """)
        else:
            print(""" "I'm good, we'll walk!" you yell to the friend in the car. As you continue walking your friend tells you thanks, he only saw
            one seat open in his car. As you walk you talk about all the stuff that is going on and how excited you are about an upcoming event
            that you didn't think anyone there knew about. You find out that your friend is also interested in it and make plans to get tickets for it!""")




def arc3():
    print("Lucky you, Sometimes life is simple. Heres a few short stories and you decide how they end!")
    print("Once a 5 year old boy was standing in shallow water.")
    x = input("Next line? HAPPY      SAD      TWIST\n")
    if x == "HAPPY" or x == "Happy" or  x == "happy":
        print("His mother splashed him as they played in the pool")
        ss2()
    elif x == "SAD" or x == "Sad" or x == "sad":
        print("He looked out to the lake, watching as the waves took his ball away")
        ss2()
    elif x== "TWIST" or x== "TWIST" or x== "TWIST":
        print('He kept repeating the same sentance to the waves. "I can never forgive you for taking away my parents" ')
        ss2()
    else:
        ending3()

def ss2():
    print("Everyone goes with the flow… but the one who goes against it becomes someone remarkable.")
    x = input("Next line? HAPPY      SAD      TWIST\n")
    if x == "HAPPY" or x == "Happy" or  x == "happy":
        print("She thought as she prepared for her award acceptance speech.")
        ss3()
    elif x == "SAD" or x == "Sad" or x == "sad":
        print("He thought wishing his ball could go against the flow of the river")
        ss3()
    elif x== "TWIST" or x== "TWIST" or x== "TWIST":
        print('Before I could explain this to the traffic police, the man issued me a ticket')
        ss3()
    else:
        ending3()

def ss3():
    print(" The little kid had to stay in jail for quite some time, only to see his home stolen after his release.")
    x = input("Next line? HAPPY      SAD      TWIST\n")
    if x == "HAPPY" or x == "Happy" or  x == "happy":
        print('"You are so dramatic" his mother said after letting him out of time out and seeing his fort knocked over')
    elif x == "SAD" or x == "Sad" or x == "sad":
        print("The bank took everything when he couldn't pay back his debts.")
    elif x== "TWIST" or x== "TWIST" or x== "TWIST":
        print('The Monopoly board game got a little tricky at times')
    else:
        ending3()

def ending1():
    print("Whew! you made it! want to try again?")
    x = input("Y/N?\n")
    if x == "Y" or x == "y":
        yourstory()


def ending2():
    print("Well that was an untimely ending for you! Want to try and live this time?")
    x = input("Y/N?\n")
    if x == "Y" or x == "y":
        arc1()

def ending3():
    print("So in the end you give up. How predictable. Maybe if you try again things will turn out differently? ")
    end = input("Y/N?\n")
    if end == "Y" or end == "y":
        if storytime2 > 80:
            arc1()
        elif storytime2 > 40:
            arc2()
        else:
            arc3()
    else:
        print("Thanks for playing!")  
    
def yourstory():
    x = input("Would you like to choose your story or go random? CHOOSE or RANDOM\n")
    if x == "CHOOSE" or x == "Choose" or x == "choose":
        print("1. Scary, 2. Happy, 3. Short")
        y = input("1 or 2 or 3?\n")
        if y == "1":
            arc1()
        elif y == "2":
            arc2()
        elif y == "3":
            arc3()
        else:
            print("Try again")
            yourstory()
    else:
        whichstory()

def whichstory():
    if storytime > 80:
        arc1()
    elif storytime > 40:
        arc2()
    else:
        arc3()

#Starting point
print (storytime)
intro()