# Compliance
default prevCompliance = 0
default currentCompliance = 0
default brekkiePref = 0
default ateFood = False

# Soundtracks

# Characters
define e = Character("Eileen")
define v = Character("Victim")
define k = Character("Kidnapper")

# Character sprites

label start:
    label day_1:
        scene bg room

        show eileen happy

        "You wake up."

        "Where is this?"

        "Slowly, your senses start to come to you..."

        "You're laying down on a thin mattress in what appears to be a small bedroom? Definitely not your bedroom."

        # add more thoughts, specifcally emotions here

        "Suddenly, you hear footsteps coming down the hall. "

        menu:
            "Pretend to be asleep because they might be dangerous":
                $ currentCompliance -= 1
                "You hide underneath the covers and shiver as you wait for the door to open."
                "Your heart beats faster as the steps get closer..."
                "The door swings open with a creak."
                "Someone steps in and all you can do is hope to not be killed."
                k "Hi~ I know you're awake, by the way. There's no need to pretend."
                #@TODO
            "See who it is":
                $ currentCompliance += 1
                "You get up and wait for the door to open."
                "Your heart beats faster as the steps get closer..."
                "The door swings open with a creak."
                # show the kidnapper
                "A shadowy figure enters the room."
                k "Hello, I see you're up now."
                # how should the kidnapper address the victim other than "you?"
                v "H-hi... you're not going to hurt me, are you?"
                k "Of course not! I brought you here for a reason."
                v "W-what? I-I don't know you..."
                k "That's okay, you'll get to know me eventually."
                "This is very wrong."
                # these are sort of place-holder values and options just to get something down
        menu:
            "Demand to go home":
                $ currentCompliance -= 1
                "You jump off the bed and scream at them."
                v "I want to go home now!"
                k "Go home? This IS your home now. Don't you worry, you'll love it here!"
                "With that, they leave the room and you hear a latch click."
                "All you can do is curl up and start sobbing."
            "Just accept the kidnapper for now":
                $ currentCompliance += 1
                v "Oh.. okay..."
                k "See, you're getting it!"
                k "We're going to have so much fun together!"
                "With that, they leave the room and you hear a latch click."
                "You take a deep breath, grateful to still be alive."
                "At least this person doesn't seem intent on killing you. That means you could escape..."

        # perhaps a bit about looking around the room a la point-and-click adventure

        # WE NEED SOME KIND OF FILLER
        # WE CAN'T HAVE ALL JUST TALKING TO THE KIDNAPPER

        # We need to find stuff for the victim to do in between visits from the kidnapper

        ####
        # breakfast scene, then sleep/sitting around before captor comes to say goodnight and you have option to attack
        ###

        "You hear the click of the door again."
        k "I would be a poor host if I did not provide for my guests."
        "They approach you holding a tray and take a seat beside you on the bed."
        "Oatmeal."
        "Not the most enjoyable of meals, not by a long shot."
        k "I wish I could have made something more appealing, but of course..."
        k "its hard to do so without knowing your preferences."
        # a note-so-nice smile I imagine
        "He waits expectantly."
        menu:
            "Take the oatmeal.":
                $ currentCompliance += 1
                "Unpleasant as your situation may be, it is hard to refuse warm food."
                k "Good."
                k "I wouldn't want you to go hungry."
                "They hand you the bowl with a slight smile of triumph and leave the room."
                "Seeing the food makes you hungry and you begin to eat."
                "A few minutes pass and the bowl is empty."
                
            "Refuse it":
                $ currentCompliance -= 1
                "They continue to smile at you."
                k "If you are not hungry right now, that is fine."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "He puts the bowl beside your bed on a night stand and then leaves the room."
                "Once again, you hear the latch click and you are truly alone."

        # limited exploration scene
        
        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                "You launch yourself at your captor."
                #@TODO
                jump day_1

            "Do nothing":
                $ currentCompliance += 4
                "You drift to sleep, harrowed by the day's events..."
                #@TODO
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway
                $ prevCompliance = currentCompliance
                jump day_2

    label day_2:

        $ currentCompliance = 0
        # you demand to go home or not again
        # and you have breakfast again

        "You wake up."

        "You look out into the room you're in and remember everything from yesterday."

        "Trapped."
        "Lost."
        "Confused."

        "And you can't do a thing about it."

        # add more thoughts, specifcally emotions here
        "You let this thought consume you until you hear the footsteps from yesterday."

        "They calmly walk into the room as if the relationship between the both of you is anything
        other than kidnapper and victim."

        k "Good morning. How are you today?"

        menu:
            "Demand to go home":
                $ currentCompliance -= 1
                "Maybe you could demand to go home again?"
                v "I want to go home now!"
                k "Go home? You forgot already? This is your home now."
                k "But I understand, it'll take you some time to accept that."
                k "I came down to let you know breakfast will be ready soon."
                "With that, they leave the room and you hear a latch click."
                "Once again, you just lay defeated."
                "There is nothing you can do, so you just sit there."
            "Just accept the kidnapper for a little longer":
                $ currentCompliance += 1
                v "So are you going to bring me food soon?"
                k "See, you're getting it!"
                k "Keep this up and maybe I'll even let you out of this room..."
                "With that, they leave the room and you hear a latch click."
                "You take a deep breath, once again grateful to still be alive."
                "If you were let out of this room, you could escape..."
                "That's a thought for later though, so you just quietly wait for them to come back."

        #breakfast scene, pretty much EXACTLY the same as yesterday
        "You hear the click of the door again."
        k "I would be a poor host if I did not provide for my guests."
        "They approach you holding a tray and take a seat beside you on the bed."
        "Oatmeal."
        "Not the most enjoyable of meals, not by a long shot."
        k "I wish I could have made something more appealing, but of course..."
        k "its hard to do so without knowing your preferences."
        # a note-so-nice smile I imagine
        "He waits expectantly."
        menu:
            "Take the oatmeal.":
                $ currentCompliance += 1
                "Unpleasant as your situation may be, it is hard to refuse warm food."
                k "Good."
                k "I wouldn't want you to go hungry."
                k "What I wanted to ask was, what do you prefer on top? On your oatmeal, I mean. I only have so many ingredients."
                k "I could give you banana slices, strawberry, hell, even honey."
                "He looks at you pointedly on that last word."
                menu:
                    "remain silent.":
                        $ currentCompliance -= 1
                        k "You're not talkative today. That's fine. There's always tomorrow."
                    "banana slices":
                        $ currentCompliance += 1
                        $ brekkiePref = 1
                        "He clasps his hands together."
                        k "Wonderful. I will keep this in mind"
                    "strawberry":
                        $ currentCompliance += 1
                        $ brekkiePref = 2
                        "He clasps his hands together."
                        k "Wonderful. I will keep this in mind"
                    "honey":
                        $ currentCompliance += 1
                        $ brekkiePref = 3
                        "He clasps his hands together."
                        k "Wonderful. I will keep this in mind"
                    "watermelon":
                        $ currentCompliance -= 2
                        $ brekkiePref = 4
                        "His smile fades slightly, before he regains composure."
                        k "You'll learn to appreciate what I offer you in time."
            "Refuse it":
                $ currentCompliance -= 1
                "They continue to smile at you."
                k "If you are not hungry right now, that is fine."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "He puts the bowl beside your bed on a night stand."
        
        "He stands up once again."
        k "Before I leave, is there anything more you'd like to speak about?"

        # filler

        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                "You launch yourself at your captor."
                # filler
                jump day_2

            "Do nothing":
                $ currentCompliance += 4
                "You drift to sleep, harrowed by the day's events..."
                # filler
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway
                $ prevCompliance = currentCompliance
                jump day_3

    label day_3:
        $ currentCompliance = 0
        
        "You wake up."

        "It's been... 2 nights now? And you're still here."

        "You're starting to feel unclean. Of course, there's no shower in here."
        "No mirror either, so you can't even check your appearance for sure."

        v "This."
        v "Is."
        v "Hell."

        # add more thoughts, specifcally emotions here
        # filler
        "Like clockwork, the kidnapper starts walking down the hall."

        # demand scene
        menu:
            "Demand to go home again":
                $ currentCompliance -= 1
                "Maybe there's still a chance of going home? They seem like they listen..."
                v "Can I please go home?"
                k "You don't seem so determined anymore. That's good."
                k "But I think you're starting to understand now."
                k "This is your home."
                "With that, they leave the room and you hear a latch click."
                "You pretty much expected that."
                "All you can do is just sit and wait."  
                # filler              
            "Don't anger them":
                $ currentCompliance += 1
                v "Good morning."
                k "Good morning, my dear."
                "They wrinkled their nose"
                k "You might need a shower soon. Not to worry! I'll help you with that later."
                "With that, they leave the room and you hear a latch click."
                "Once again, you're alone in this little room with nothing to do."
                # filler

        #breakfast scene
        "You hear the click of the door again."
        k "I would be a poor host if I did not provide for my guests."
        "They approach you holding a tray and take a seat beside you on the bed."
        "Oatmeal."
        "Not the most enjoyable of meals, not by a long shot."
        k "I wish I could have made something more appealing, but of course..."
        k "its hard to do so without knowing your preferences."
        # a note-so-nice smile I imagine
        "He waits expectantly."
        menu:
            "Take the oatmeal.":
                # remember breakfast choice from before
                $ currentCompliance += 1
                "Unpleasant as your situation may be, it is hard to refuse warm food."
                k "Good."
                k "I wouldn't want you to go hungry."
                # filler
            "Refuse it":
                $ currentCompliance -= 1
                "They continue to smile at you."
                k "If you are not hungry right now, that is fine."
                k "You can eat whenever you like, and I will take your dishes when you sleep."
                "He puts the bowl beside your bed on a night stand."
                # filler
        
        # filler 
        menu:
            "Attack your captor":
                $ currentCompliance -= 4
                "You launch yourself at your captor."
                # filler
                jump day_3

            "Do nothing":
                $ currentCompliance += 4
                "You drift to sleep, harrowed by the day's events..."
                # filler
                # I guess more realistically, someone wouldn't be able to sleep so soundly in a bed that's not theirs
                # what if sleeping soundly is tied to accepting food? that's creepy but anyway
                $ prevCompliance = currentCompliance
                jump day_4
    return
