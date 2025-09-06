# "https://media.giphy.com/media/YWf50NNii3r4k/giphy.gif"

import time
import pandas as pd
from threading import Timer
import random
import discord
import datetime
import discord.ext
from discord.ext import commands, tasks

current_date = datetime.datetime.now()

botID = 79  # <------ change this to your BOT ID

# "https://blog.xrds.acm.org/wp-content/uploads/2018/07/kermit-gif.gif "

#Timetable array holders
timetable = []
timetable2 = []
timetable3 = []
timetable4 = []
timetable5 = []
timetable6 = []
timetable7 = []
timetable8 = []
timetable9 = []
timetable10 = []

#Message Counter for visitors (if offcial)#
visitors = {}
messageCounter = 0

#Timetable Name Variables#
timetable_Name = "Timetable 1"
timetable2_Name = "Timetable 2"
timetable3_Name = "Timetable 3"
timetable4_Name = "Timetable 4"
timetable5_Name = "Timetable 5"
timetable6_Name = "Timetable 6"
timetable7_Name = "Timetable 7"
timetable8_Name = "Timetable 8"
timetable9_Name = "Timetable 9"
timetable10_Name = "Timetable 10"


#Not Timetable relateed#
glonkerPointsCounter = 0
glonkerHelloFlag = 0
brainRotFlag = 0
brainRotMessageFlag = 0
skibidimessage = ""
glonkerState = 0
glonkerKingFlag = 0
timer = 0
timerCheck = True
timerState = 0

print("Glonker points counter: " + str(glonkerPointsCounter))
print("Brain Rot Flag counter: " + str(brainRotFlag))
print("Timer: " + str(timer))

def setup():
    return (":wave: Hello! I am your personal Timetable bot! To see what I can do, please type '=help_page_1'! Please note I cannot"
            " understand what you say if you don't include my '=' prefix and a dedicated command!")

#End of method setup

#= is the prefix. Make sure to remember that. Return to documentation to ensure you hit all the things you said you would

def overheard(message, user, nameDisplay):
    print(" (Logger) " + user + " said " + message)

    global brainRotFlag

    if user in visitors:
        visitors[user] = visitors[user] + 1

#==================Show All Timetables===============#
    if "=show_all_timetables" in message:
        return showAllTimetablesCommand(message, user, nameDisplay)

#==================Timetable 10 Code==================#

    if "=reset_timetable_10" in message:
        return resetManualTimetable10(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_10" in message:
        return removeManualTimetable10ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_10" in message:
        return addManualTimetable10(message, user, nameDisplay)

    if "=show_timetable_10" in message:
        return showManualTimetable10(message, user, nameDisplay)

    if "=display_timetable_10_name" in message:
        return showTimetable10Name(message, user, nameDisplay)

    if "=reset_timetable_10_name" in message:
        return clearTimetable10Name(message, user, nameDisplay)

    if "=name_timetable_10" in message:
        return nameTimetable10(message, user, nameDisplay)

#==================End Of Timetable 10 Code==================#

#==================Timetable 1 Code==================#

    if "=reset_timetable_1" in message:
        return resetManualTimetable(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_1" in message:
        return removeManualTimetableItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_1" in message:
        return addManualTimetable(message, user, nameDisplay)

    if "=show_timetable_1" in message:
        return showManualTimetable(message, user, nameDisplay)

    if "=display_timetable_1_name" in message:
        return showTimetableName(message, user, nameDisplay)

    if "=reset_timetable_1_name" in message:
        return clearTimetableName(message, user, nameDisplay)

    if "=name_timetable_1" in message:
        return nameTimetable(message, user, nameDisplay)

#==================End Of Timetable 1 Code==================#

#==================Timetable 2 Code==================#

    if "=reset_timetable_2" in message:
        return resetManualTimetable2(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_2" in message:
         return removeManualTimetable2ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_2" in message:
        return addManualTimetable2(message, user, nameDisplay)

    if "=show_timetable_2" in message:
        return showManualTimetable2(message, user, nameDisplay)

    if "=display_timetable_2_name" in message:
        return showTimetable2Name(message, user, nameDisplay)

    if "=reset_timetable_2_name" in message:
        return clearTimetable2Name(message, user, nameDisplay)

    if "=name_timetable_2" in message:
        return nameTimetable2(message, user, nameDisplay)

#==================End Of Timetable 2 Code==================#

#==================Timetable 3 Code==================#

    if "=reset_timetable_3" in message:
        return resetManualTimetable3(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_3" in message:
        return removeManualTimetable3ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_3" in message:
        return addManualTimetable3(message, user, nameDisplay)

    if "=show_timetable_3" in message:
        return showManualTimetable3(message, user, nameDisplay)

    if "=display_timetable_3_name" in message:
        return showTimetable3Name(message, user, nameDisplay)

    if "=reset_timetable_3_name" in message:
        return clearTimetable3Name(message, user, nameDisplay)

    if "=name_timetable_3" in message:
        return nameTimetable3(message, user, nameDisplay)

#==================End Of Timetable 3 Code==================#

#==================Timetable 4 Code==================#

    if "=reset_timetable_4" in message:
        return resetManualTimetable4(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_4" in message:
        return removeManualTimetable4ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_4" in message:
        return addManualTimetable4(message, user, nameDisplay)

    if "=show_timetable_4" in message:
        return showManualTimetable4(message, user, nameDisplay)

    if "=display_timetable_4_name" in message:
        return showTimetable4Name(message, user, nameDisplay)

    if "=reset_timetable_4_name" in message:
        return clearTimetable4Name(message, user, nameDisplay)

    if "=name_timetable_4" in message:
        return nameTimetable4(message, user, nameDisplay)

#==================End Of Timetable 4 Code==================#

#==================Timetable 5 Code==================#

    if "=reset_timetable_5" in message:
        return resetManualTimetable5(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_5" in message:
        return removeManualTimetable5ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_5" in message:
        return addManualTimetable5(message, user, nameDisplay)

    if "=show_timetable_5" in message:
        return showManualTimetable5(message, user, nameDisplay)

    if "=display_timetable_5_name" in message:
        return showTimetable5Name(message, user, nameDisplay)

    if "=reset_timetable_5_name" in message:
        return clearTimetable5Name(message, user, nameDisplay)

    if "=name_timetable_5" in message:
        return nameTimetable5(message, user, nameDisplay)

#==================End Of Timetable 5 Code==================#

#==================Timetable 6 Code==================#

    if "=reset_timetable_6" in message:
        return resetManualTimetable6(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_6" in message:
        return removeManualTimetable6ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_6" in message:
        return addManualTimetable6(message, user, nameDisplay)

    if "=show_timetable_6" in message:
        return showManualTimetable6(message, user, nameDisplay)

    if "=display_timetable_6_name" in message:
        return showTimetable6Name(message, user, nameDisplay)

    if "=reset_timetable_6_name" in message:
        return clearTimetable6Name(message, user, nameDisplay)

    if "=name_timetable_6" in message:
        return nameTimetable6(message, user, nameDisplay)

#==================End Of Timetable 6 Code==================#

#==================Timetable 7 Code==================#

    if "=reset_timetable_7" in message:
        return resetManualTimetable7(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_7" in message:
        return removeManualTimetable7ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_7" in message:
        return addManualTimetable7(message, user, nameDisplay)

    if "=show_timetable_7" in message:
        return showManualTimetable7(message, user, nameDisplay)

    if "=display_timetable_7_name" in message:
        return showTimetable7Name(message, user, nameDisplay)

    if "=reset_timetable_7_name" in message:
        return clearTimetable7Name(message, user, nameDisplay)

    if "=name_timetable_7" in message:
        return nameTimetable7(message, user, nameDisplay)

#==================End Of Timetable 7 Code==================#

#==================Timetable 8 Code==================#

    if "=reset_timetable_8" in message:
        return resetManualTimetable8(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_8" in message:
        return removeManualTimetable8ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_8" in message:
        return addManualTimetable8(message, user, nameDisplay)

    if "=show_timetable_8" in message:
        return showManualTimetable8(message, user, nameDisplay)

    if "=display_timetable_8_name" in message:
        return showTimetable8Name(message, user, nameDisplay)

    if "=reset_timetable_8_name" in message:
        return clearTimetable8Name(message, user, nameDisplay)

    if "=name_timetable_8" in message:
        return nameTimetable8(message, user, nameDisplay)

#==================End Of Timetable 8 Code==================#

#==================Timetable 9 Code==================#

    if "=reset_timetable_9" in message:
        return resetManualTimetable9(message, user, nameDisplay)

    if "=remove_last_item_from_timetable_9" in message:
        return removeManualTimetable9ItemCommand(message, user, nameDisplay)

    if "=add_to_timetable_9" in message:
        return addManualTimetable9(message, user, nameDisplay)

    if "=show_timetable_9" in message:
        return showManualTimetable9(message, user, nameDisplay)

    if "=display_timetable_9_name" in message:
        return showTimetable9Name(message, user, nameDisplay)

    if "=reset_timetable_9_name" in message:
        return clearTimetable9Name(message, user, nameDisplay)

    if "=name_timetable_9" in message:
        return nameTimetable9(message, user, nameDisplay)

#==================End Of Timetable 9 Code==================#

#==================User Code==================#

    if "=add_me_as_a_user" in message:
        return visitorAddCommand(message, user, nameDisplay)

    if "=remove_me_as_a_user" in message:
        return visitorRemoveCommand(message, user, nameDisplay)

    if "=show_users" in message:
        return visitorMessageCommand(message, user, nameDisplay)

#==================End Of User Code==================#

#==================Misc Code==================#

    if "=help_page_1" in message:
        return helpMessageCommand(message, user, nameDisplay)

    if "=help_page_2" in message:
        return helpMessageCommand2(message, user, nameDisplay)

    if "=what_is_the_date" in message:
        return dateMessageCommand(message, user, nameDisplay)

    if "=more_info" in message:
        return moreInfomationMessageCommand(message, user, nameDisplay)

    if "=debug" in message:
        return debugMessageCommand(message, user, nameDisplay)

    if "=timetable_tutorial" in message:
        return mttutorialMessageCommand(message, user, nameDisplay)

    if "=credits" in message:
        return creditMessageCommand(message, user, nameDisplay)

#==================End Of Misc Code==================#

#==================Other Code==================#

    if "yippie" in message.lower():
        return secretYippieMessage(message, user, nameDisplay)

    if "=activate_brain_rot" in message and brainRotFlag == 1:
        global skibidimessage

        for i in range(10):
            skibidimessage += "Skibidi Toilet https://media1.tenor.com/m/YzseE_-j48QAAAAd/skibidi-toilet.gif \n\n Skibidi Toilet"
        return skibidimessage

    elif "=activate_brain_rot" in message and brainRotFlag == 0:
        return "You have not unlocked this mode yet!"

    if "=send_a_random_cat" in message:
        return catSenderCommand(message, user, nameDisplay)

    if "feet" in message.lower():
        return "Ew, behave yourself!"

#===================================Glonker Code start===================================#

    if "hi glonker" in message.lower() or "hello glonker" in message.lower():
        brainRotFlag = + 1
        print("Brain rot flag = " + str(brainRotFlag))
        return glonkerHello(message, user, nameDisplay)

    if "glonker is king" in message.lower():
        return glonkerKing(message, user, nameDisplay)

    if "=what_are_glonker_points" in message:
        return glonkerPointsMessageCommand(message, user, nameDisplay)

    if "=show_glonker_points" in message:
        print(glonkerPointsCounter)
        return glonkerPointsShowCommand(message, user, nameDisplay)

#===================================Glonker Code End===================================#

#==========================================================#
                    #Start of debug messages#
    if "=1" in message:
        return debugMessageOne(message, user, nameDisplay)

    if "=2" in message:
        return debugMessageTwo(message, user, nameDisplay)


                    #End of debug messages#
#==========================================================#

    if "Sorry CodeWrangleBot10, I didn't understand that!" in message:
        return easterEggMessageCommand(message, user, nameDisplay)

    if "classtest" in message:
        return f"The gunner has {Gunner.speed} units of speed!"

    if "changespeed" in message:
        message = Gunner.speed
        return f"The gunner now has a speed of {Gunner.speed}"

    return messageNotUnderstood(message, user, nameDisplay)

    #if "what is the date" in message:
        #return f"The date is {current_date.strftime('%A: %d/%m/%Y')}"

# END of  method overheard

#Example Class Below

class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

Gunner = Character(100, 100, 100)
Sniper = Character(50, 200, 150)

#End of example class

#================Show All Timetables Function=========#
def showAllTimetablesCommand(message, user, nameDisplay):

    global timetable_Name #Gets the name variable assigned to each Timetable (well, it allows it to be accessed)
    global timetable2_Name
    global timetable3_Name
    global timetable4_Name
    global timetable5_Name
    global timetable6_Name
    global timetable7_Name
    global timetable8_Name
    global timetable9_Name
    global timetable10_Name

    full_timetable = "" #Place to store all items
    full_timetable2 = ""
    full_timetable3 = ""
    full_timetable4 = ""
    full_timetable5 = ""
    full_timetable6 = ""
    full_timetable7 = ""
    full_timetable8 = ""
    full_timetable9 = ""
    full_timetable10 = ""

    for item in timetable:                       #For every item (or instance) of full timetable, it'll print it out
        full_timetable += f"{item}\n"
    for item2 in timetable2:
        full_timetable2 += f"{item2}\n"
    for item3 in timetable3:
        full_timetable3 += f"{item3}\n"
    for item4 in timetable4:
        full_timetable4 += f"{item4}\n"
    for item5 in timetable5:
        full_timetable5 += f"{item5}\n"
    for item6 in timetable6:
        full_timetable6 += f"{item6}\n"
    for item7 in timetable7:
        full_timetable7 += f"{item7}\n"
    for item8 in timetable8:
        full_timetable8 += f"{item8}\n"
    for item9 in timetable9:
        full_timetable9 += f"{item9}\n"
    for item10 in timetable10:
        full_timetable10 += f"{item10}\n"

    return (f"Hey {nameDisplay}, here are all your Timetables!\n\n"
            f"Timetable 1 ({timetable_Name}):\n{full_timetable}\n\n"
            f"Timetable 2 ({timetable2_Name}):\n{full_timetable2}\n\n"
            f"Timetable 3 ({timetable3_Name}):\n{full_timetable3}\n\n"
            f"Timetable 4 ({timetable4_Name}):\n{full_timetable4}\n\n"
            f"Timetable 5 ({timetable5_Name}):\n{full_timetable5}\n\n"
            f"Timetable 6 ({timetable6_Name}):\n{full_timetable6}\n\n"
            f"Timetable 7 ({timetable7_Name}):\n{full_timetable7}\n\n"
            f"Timetable 8 ({timetable8_Name}):\n{full_timetable8}\n\n"
            f"Timetable 9 ({timetable9_Name}):\n{full_timetable9}\n\n"
            f"Timetable 10 ({timetable10_Name}):\n{full_timetable10}\n\n")

#================End Of Show All Timetables Function=========#

#================Timetable 10 Functions================#

def resetManualTimetable10(message, user, nameDisplay):
    if not timetable10:
        return f"{nameDisplay}, Timetable 10 has already been cleared! Nothing has changed."

    if timetable10:
        timetable10.clear()
    return f"{nameDisplay}, Timetable 10 has been successfully reset!"


def removeManualTimetable10ItemCommand(message, user, nameDisplay):
    if len(timetable10) > 0:
        item = timetable10.pop()
        return f"{item} has been successfully removed from Timetable 10!"
    return f"{nameDisplay}, Timetable 10 is already empty! Nothing was removed."


def addManualTimetable10(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_10")
    message = message[new_message:]
    msglen = len("=add_to_timetable_10") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable10.append(new_item)
    return(f"{new_item} has been added to Timetable 10!")


def showManualTimetable10(message, user, nameDisplay):
    global timetable10_Name
    full_timetable10 = ""
    if not timetable10:
         return f"{nameDisplay}, Timetable 10 is empty!"
    else:
        for item in timetable10:
            full_timetable10 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 10 ({timetable10_Name}):\n{full_timetable10}"


def showTimetable10Name(message, user, nameDisplay):
    global timetable10_Name
    return f"{nameDisplay}, Timetable 10 has a custom name of: {timetable10_Name}!"


def clearTimetable10Name(message, user, nameDisplay):
    global timetable10_Name
    if timetable10_Name == "Timetable 10":
        return f"{nameDisplay}, Timetable 10 is already set to the default name!"

    if timetable10_Name:
        timetable10_Name = "Timetable 10"
        return f"{nameDisplay}, Timetable 10 name has been successfully reset to the default name of {timetable10_Name}!"


def nameTimetable10(message, user, nameDisplay):
    global timetable10_Name
    timetable10_Name = message.index("=name_timetable_10") #Checks for this specific string
    message = message[timetable10_Name:]
    msglen = len("=name_timetable_10") + 1
    timetable10_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable10_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable10_Name = "Timetable 10"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 10 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable10_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 10 has been successfully named to: {message}!"

#================End Of Timetable 10 Functions================#

#================Timetable 9 Functions================#

def resetManualTimetable9(message, user, nameDisplay):
    if not timetable9:
        return f"{nameDisplay}, Timetable 9 has already been cleared! Nothing has changed."

    if timetable9:
        timetable9.clear()
    return f"{nameDisplay}, Timetable 9 has been successfully reset!"


def removeManualTimetable9ItemCommand(message, user, nameDisplay):
    if len(timetable9) > 0:
        item = timetable9.pop()
        return f"{item} has been successfully removed from Timetable 9!"
    return f"{nameDisplay}, Timetable 9 is already empty! Nothing was removed."


def addManualTimetable9(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_9")
    message = message[new_message:]
    msglen = len("=add_to_timetable_9") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable9.append(new_item)
    return(f"{new_item} has been added to Timetable 9!")


def showManualTimetable9(message, user, nameDisplay):
    global timetable9_Name
    full_timetable9 = ""
    if not timetable9:
         return f"{nameDisplay}, Timetable 9 is empty!"
    else:
        for item in timetable9:
            full_timetable9 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 9 ({timetable9_Name}):\n{full_timetable9}"


def showTimetable9Name(message, user, nameDisplay):
    global timetable9_Name
    return f"{nameDisplay}, Timetable 9 has a custom name of: {timetable9_Name}!"


def clearTimetable9Name(message, user, nameDisplay):
    global timetable9_Name
    if timetable9_Name == "Timetable 9":
        return f"{nameDisplay}, Timetable 9 is already set to the default name!"

    if timetable9_Name:
        timetable9_Name = "Timetable 9"
        return f"{nameDisplay}, Timetable 9 name has been successfully reset to the default name of {timetable9_Name}!"


def nameTimetable9(message, user, nameDisplay):
    global timetable9_Name
    timetable9_Name = message.index("=name_timetable_9") #Checks for this specific string
    message = message[timetable9_Name:]
    msglen = len("=name_timetable_9") + 1
    timetable9_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable9_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable9_Name = "Timetable 9"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 9 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable9_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 9 has been successfully named to: {message}!"

#================End Of Timetable 9 Functions================#

#================Timetable 8 Functions================#

def resetManualTimetable8(message, user, nameDisplay):
    if not timetable8:
        return f"{nameDisplay}, Timetable 8 has already been cleared! Nothing has changed."

    if timetable8:
        timetable8.clear()
    return f"{nameDisplay}, Timetable 8 has been successfully reset!"


def removeManualTimetable8ItemCommand(message, user, nameDisplay):
    if len(timetable8) > 0:
        item = timetable8.pop()
        return f"{item} has been successfully removed from Timetable 8!"
    return f"{nameDisplay}, Timetable 8 is already empty! Nothing was removed."


def addManualTimetable8(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_8")
    message = message[new_message:]
    msglen = len("=add_to_timetable_8") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable8.append(new_item)
    return(f"{new_item} has been added to Timetable 8!")


def showManualTimetable8(message, user, nameDisplay):
    global timetable8_Name
    full_timetable8 = ""
    if not timetable8:
         return f"{nameDisplay}, Timetable 8 is empty!"
    else:
        for item in timetable8:
            full_timetable8 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 8 ({timetable8_Name}):\n{full_timetable8}"


def showTimetable8Name(message, user, nameDisplay):
    global timetable8_Name
    return f"{nameDisplay}, Timetable 8 has a custom name of: {timetable8_Name}!"


def clearTimetable8Name(message, user, nameDisplay):
    global timetable8_Name
    if timetable8_Name == "Timetable 8":
        return f"{nameDisplay}, Timetable 8 is already set to the default name!"

    if timetable8_Name:
        timetable8_Name = "Timetable 8"
        return f"{nameDisplay}, Timetable 8 name has been successfully reset to the default name of {timetable8_Name}!"


def nameTimetable8(message, user, nameDisplay):
    global timetable8_Name
    timetable8_Name = message.index("=name_timetable_8") #Checks for this specific string
    message = message[timetable8_Name:]
    msglen = len("=name_timetable_8") + 1
    timetable8_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable8_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable8_Name = "Timetable 8"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 8 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable8_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 8 has been successfully named to: {message}!"

#================End Of Timetable 8 Functions================#

#================Timetable 7 Functions================#

def resetManualTimetable7(message, user, nameDisplay):
    if not timetable7:
        return f"{nameDisplay}, Timetable 7 has already been cleared! Nothing has changed."

    if timetable7:
        timetable7.clear()
    return f"{nameDisplay}, Timetable 7 has been successfully reset!"


def removeManualTimetable7ItemCommand(message, user, nameDisplay):
    if len(timetable7) > 0:
        item = timetable7.pop()
        return f"{item} has been successfully removed from Timetable 7!"
    return f"{nameDisplay}, Timetable 7 is already empty! Nothing was removed."


def addManualTimetable7(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_7")
    message = message[new_message:]
    msglen = len("=add_to_timetable_7") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable7.append(new_item)
    return(f"{new_item} has been added to Timetable 7!")


def showManualTimetable7(message, user, nameDisplay):
    global timetable7_Name
    full_timetable7 = ""
    if not timetable7:
         return f"{nameDisplay}, Timetable 7 is empty!"
    else:
        for item in timetable7:
            full_timetable7 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 7 ({timetable7_Name}):\n{full_timetable7}"


def showTimetable7Name(message, user, nameDisplay):
    global timetable7_Name
    return f"{nameDisplay}, Timetable 7 has a custom name of: {timetable7_Name}!"


def clearTimetable7Name(message, user, nameDisplay):
    global timetable7_Name
    if timetable7_Name == "Timetable 7":
        return f"{nameDisplay}, Timetable 7 is already set to the default name!"

    if timetable7_Name:
        timetable7_Name = "Timetable 7"
        return f"{nameDisplay}, Timetable 7 name has been successfully reset to the default name of {timetable7_Name}!"


def nameTimetable7(message, user, nameDisplay):
    global timetable7_Name
    timetable7_Name = message.index("=name_timetable_7") #Checks for this specific string
    message = message[timetable7_Name:]
    msglen = len("=name_timetable_7") + 1
    timetable7_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable7_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable7_Name = "Timetable 7"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 7 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable7_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 7 has been successfully named to: {message}!"

#================End Of Timetable 7 Functions================#

#================Timetable 6 Functions================#

def resetManualTimetable6(message, user, nameDisplay):
    if not timetable6:
        return f"{nameDisplay}, Timetable 6 has already been cleared! Nothing has changed."

    if timetable6:
        timetable6.clear()
    return f"{nameDisplay}, Timetable 6 has been successfully reset!"


def removeManualTimetable6ItemCommand(message, user, nameDisplay):
    if len(timetable6) > 0:
        item = timetable6.pop()
        return f"{item} has been successfully removed from Timetable 6!"
    return f"{nameDisplay}, Timetable 6 is already empty! Nothing was removed."


def addManualTimetable6(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_6")
    message = message[new_message:]
    msglen = len("=add_to_timetable_6") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable6.append(new_item)
    return(f"{new_item} has been added to Timetable 6!")


def showManualTimetable6(message, user, nameDisplay):
    global timetable6_Name
    full_timetable6 = ""
    if not timetable6:
         return f"{nameDisplay}, Timetable 6 is empty!"
    else:
        for item in timetable6:
            full_timetable6 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 6 ({timetable6_Name}):\n{full_timetable6}"


def showTimetable6Name(message, user, nameDisplay):
    global timetable6_Name
    return f"{nameDisplay}, Timetable 6 has a custom name of: {timetable6_Name}!"


def clearTimetable6Name(message, user, nameDisplay):
    global timetable6_Name
    if timetable6_Name == "Timetable 6":
        return f"{nameDisplay}, Timetable 6 is already set to the default name!"

    if timetable6_Name:
        timetable6_Name = "Timetable 6"
        return f"{nameDisplay}, Timetable 6 name has been successfully reset to the default name of {timetable6_Name}!"


def nameTimetable6(message, user, nameDisplay):
    global timetable6_Name
    timetable6_Name = message.index("=name_timetable_6") #Checks for this specific string
    message = message[timetable6_Name:]
    msglen = len("=name_timetable_6") + 1
    timetable6_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable6_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable6_Name = "Timetable 6"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 6 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable6_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 6 has been successfully named to: {message}!"

#================End Of Timetable 6 Functions================#

#================Timetable 5 Functions================#

def resetManualTimetable5(message, user, nameDisplay):
    if not timetable5:
        return f"{nameDisplay}, Timetable 5 has already been cleared! Nothing has changed."

    if timetable5:
        timetable5.clear()
    return f"{nameDisplay}, Timetable 5 has been successfully reset!"


def removeManualTimetable5ItemCommand(message, user, nameDisplay):
    if len(timetable5) > 0:
        item = timetable5.pop()
        return f"{item} has been successfully removed from Timetable 5!"
    return f"{nameDisplay}, Timetable 5 is already empty! Nothing was removed."


def addManualTimetable5(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_5")
    message = message[new_message:]
    msglen = len("=add_to_timetable_5") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable5.append(new_item)
    return(f"{new_item} has been added to Timetable 5!")


def showManualTimetable5(message, user, nameDisplay):
    global timetable5_Name
    full_timetable5 = ""
    if not timetable5:
         return f"{nameDisplay}, Timetable 5 is empty!"
    else:
        for item in timetable5:
            full_timetable5 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 5 ({timetable5_Name}):\n{full_timetable5}"


def showTimetable5Name(message, user, nameDisplay):
    global timetable5_Name
    return f"{nameDisplay}, Timetable 5 has a custom name of: {timetable5_Name}!"


def clearTimetable5Name(message, user, nameDisplay):
    global timetable5_Name
    if timetable5_Name == "Timetable 5":
        return f"{nameDisplay}, Timetable 5 is already set to the default name!"

    if timetable5_Name:
        timetable5_Name = "Timetable 5"
        return f"{nameDisplay}, Timetable 5 name has been successfully reset to the default name of {timetable5_Name}!"


def nameTimetable5(message, user, nameDisplay):
    global timetable5_Name
    timetable5_Name = message.index("=name_timetable_5") #Checks for this specific string
    message = message[timetable5_Name:]
    msglen = len("=name_timetable_5") + 1
    timetable5_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable5_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable5_Name = "Timetable 5"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 5 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable5_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 5 has been successfully named to: {message}!"

#================End Of Timetable 5 Functions================#

#================Timetable 4 Functions================#

def resetManualTimetable4(message, user, nameDisplay):
    if not timetable4:
        return f"{nameDisplay}, Timetable 4 has already been cleared! Nothing has changed."

    if timetable4:
        timetable4.clear()
    return f"{nameDisplay}, Timetable 4 has been successfully reset!"


def removeManualTimetable4ItemCommand(message, user, nameDisplay):
    if len(timetable4) > 0:
        item = timetable4.pop()
        return f"{item} has been successfully removed from Timetable 4!"
    return f"{nameDisplay}, Timetable 4 is already empty! Nothing was removed."


def addManualTimetable4(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_4")
    message = message[new_message:]
    msglen = len("=add_to_timetable_4") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable4.append(new_item)
    return(f"{new_item} has been added to Timetable 4!")


def showManualTimetable4(message, user, nameDisplay):
    global timetable4_Name
    full_timetable4 = ""
    if not timetable4:
         return f"{nameDisplay}, Timetable 4 is empty!"
    else:
        for item in timetable4:
            full_timetable4 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 4 ({timetable4_Name}):\n{full_timetable4}"


def showTimetable4Name(message, user, nameDisplay):
    global timetable4_Name
    return f"{nameDisplay}, Timetable 4 has a custom name of: {timetable4_Name}!"


def clearTimetable4Name(message, user, nameDisplay):
    global timetable4_Name
    if timetable4_Name == "Timetable 4":
        return f"{nameDisplay}, Timetable 4 is already set to the default name!"

    if timetable4_Name:
        timetable4_Name = "Timetable 4"
        return f"{nameDisplay}, Timetable 4 name has been successfully reset to the default name of {timetable4_Name}!"


def nameTimetable4(message, user, nameDisplay):
    global timetable4_Name
    timetable4_Name = message.index("=name_timetable_4") #Checks for this specific string
    message = message[timetable4_Name:]
    msglen = len("=name_timetable_4") + 1
    timetable4_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable4_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable4_Name = "Timetable 4"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 4 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable4_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 4 has been successfully named to: {message}!"

#================End Of Timetable 4 Functions================#

#================Timetable 3 Functions================#

def resetManualTimetable3(message, user, nameDisplay):
    if not timetable3:
        return f"{nameDisplay}, Timetable 3 has already been cleared! Nothing has changed."

    if timetable3:
        timetable3.clear()
    return f"{nameDisplay}, Timetable 3 has been successfully reset!"


def removeManualTimetable3ItemCommand(message, user, nameDisplay):
    if len(timetable3) > 0:
        item = timetable3.pop()
        return f"{item} has been successfully removed from Timetable 3!"
    return f"{nameDisplay}, Timetable 3 is already empty! Nothing was removed."


def addManualTimetable3(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_3")
    message = message[new_message:]
    msglen = len("=add_to_timetable_3") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable3.append(new_item)
    return(f"{new_item} has been added to Timetable 3!")


def showManualTimetable3(message, user, nameDisplay):
    global timetable3_Name
    full_timetable3 = ""
    if not timetable3:
         return f"{nameDisplay}, Timetable 3 is empty!"
    else:
        for item in timetable3:
            full_timetable3 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 3 ({timetable3_Name}):\n{full_timetable3}"


def showTimetable3Name(message, user, nameDisplay):
    global timetable3_Name
    return f"{nameDisplay}, Timetable 3 has a custom name of: {timetable3_Name}!"


def clearTimetable3Name(message, user, nameDisplay):
    global timetable3_Name
    if timetable3_Name == "Timetable 3":
        return f"{nameDisplay}, Timetable 3 is already set to the default name!"

    if timetable3_Name:
        timetable3_Name = "Timetable 3"
        return f"{nameDisplay}, Timetable 3 name has been successfully reset to the default name of {timetable3_Name}!!"


def nameTimetable3(message, user, nameDisplay):
    global timetable3_Name
    timetable3_Name = message.index("=name_timetable_3") #Checks for this specific string
    message = message[timetable3_Name:]
    msglen = len("=name_timetable_3") + 1
    timetable3_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable3_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable3_Name = "Timetable 3"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 3 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable3_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 3 has been successfully named to: {message}!"

#================End Of Timetable 3 Functions================#

#================Timetable 2 Functions================#

def resetManualTimetable2(message, user, nameDisplay):
    if not timetable2:
        return f"{nameDisplay}, Timetable 2 has already been cleared! Nothing has changed."

    if timetable2:
        timetable2.clear()
    return f"{nameDisplay}, Timetable 2 has been successfully reset!"


def removeManualTimetable2ItemCommand(message, user, nameDisplay):
    if len(timetable2) > 0:
        item = timetable2.pop()
        return f"{item} has been successfully removed from Timetable 2!"
    return f"{nameDisplay}, Timetable 2 is already empty! Nothing was removed."


def addManualTimetable2(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_2")
    message = message[new_message:]
    msglen = len("=add_to_timetable_2") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable2.append(new_item)
    return(f"{new_item} has been added to Timetable 2!")


def showManualTimetable2(message, user, nameDisplay):
    global timetable2_Name
    full_timetable2 = ""
    if not timetable2:
         return f"{nameDisplay}, Timetable 2 is empty!"
    else:
        for item in timetable2:
            full_timetable2 += f"{item}\n"
    return f"Hey {nameDisplay}, here is your Timetable 2 ({timetable2_Name}):\n{full_timetable2}"


def showTimetable2Name(message, user, nameDisplay):
    global timetable2_Name
    return f"{nameDisplay}, Timetable 2 has a custom name of: {timetable2_Name}!"


def clearTimetable2Name(message, user, nameDisplay):
    global timetable2_Name
    if timetable2_Name == "Timetable 2":
        return f"{nameDisplay}, Timetable 2 is already set to the default name!"

    if timetable_Name:
        timetable2_Name = "Timetable 2"
        return f"{nameDisplay}, Timetable 2 name has been successfully reset to the default name of {timetabl2_Name}!!"


def nameTimetable2(message, user, nameDisplay):
    global timetable2_Name
    timetable2_Name = message.index("=name_timetable_2") #Checks for this specific string
    message = message[timetable2_Name:]
    msglen = len("=name_timetable_2") + 1
    timetable2_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable2_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable2_Name = "Timetable 2"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 2 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable2_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 2 has been successfully named to: {message}!"

#================End Of Timetable 2 Functions================#

def showTimetableName(message, user, nameDisplay):
    global timetable_Name
    return f"{nameDisplay}, Timetable 1 has a custom name of: {timetable_Name}!"

#End of showTimetableName Function

def clearTimetableName(message, user, nameDisplay):
    global timetable_Name
    if timetable_Name == "Timetable 1":
        return f"{nameDisplay}, Timetable 1 is already set to the default name!"

    if timetable_Name:
        timetable_Name = "Timetable 1"
        return f"{nameDisplay}, Timetable 1 name has been successfully reset to the default name of {timetable_Name}!"

#End of clearTimetableName Function

def nameTimetable(message, user, nameDisplay):
    global timetable_Name
    timetable_Name = message.index("=name_timetable_1") #Checks for this specific string
    message = message[timetable_Name:]
    msglen = len("=name_timetable_1") + 1
    timetable_Name = message[msglen:] #This takes out =name_manual_timetable plus one extra character
    if not timetable_Name: #If nothing is in it, it'll say you can't add nothing.
        timetable_Name = "Timetable 1"
        return f"You cannot leave your custom Timetable name blank {nameDisplay}! The custom Timetable 1 name will now revert back to default. Please type in the desired name after the command."
    else:
        message = timetable_Name #uses the message as the name for the time table
        return f"{nameDisplay}, your Timetable 1 has been successfully named to: {message}!"

#End of nameTimetable function

def mttutorialMessageCommand(message, user , nameDisplay):
    return ("To use the =add_to_timetable_1 (and its alterations such as =add_to_timetable_2) command, you must include your information in the same message you use the command, ensuring that their is a **space** between the command and your input message. "
            "It is recommended that you plan your information out methodically and keep consistency to minimise confusion. It'll also help you keep your Timetable neat! :smile:\n\n "
            "Here is an example of how you can lay out your information:\n**=add_to_timetable_1 [Name of Teacher] | [Class being taught] | [Date] | [Start and end time]**\n\n"
            "Here is what it would look like using example input information.\n"
            "**=add_to_timetable_1 John Snow | Medical Science | 05/04/2024 | 9:00AM - 2:00PM**\n\n"
            "After you have sent this message, the bot will send a message back confirming that the information has been set into your Timetable, and would look like so:\n"
            "**John Snow | Medical Science | 05/04/2024 | 9:00AM - 2:00PM has been added to your manual timetable!**\n\n"
            "You can then use the =show_timetable_1 command to show all the items you have added to your Timetable! Here is an example:\n"
            "**[User] =show_timetable_1**\n"
            "**[Bot] Here is your timetable:**\n"
            "**[Bot] John Snow | Medical Science | 05/04/2024 | 9:00AM - 2:00PM**\n\n"
            "If you have followed these steps correctly, you have successfully added to your Timetable! :smile: Remember that there are **multiple Timetables**, so if you add items to Timetable 2 and use the '=show_timetable_1' command, it won't show Timetable 2's! Always keep track of that!")

#End of function mttutorialMessageCommand


def debugMessageCommand(message, user, nameDisplay):
    return (f":wave:Hello {nameDisplay}! Looks like you've used my debug command! Please choose one of the following commands that relate to your problem! (To choose a command, type in the prefix and the corresponding "
            f"number e.g '=1' for issue one)\n\n"
            f"**=1** - I can't understand my manual Timeatable. It looks messy, why?!"
            f"**=2** - When I use the '=show_all_timetables' command, nothing is there!")

#End of function debugMessageCommand

#=================================#
    #Start of debug functions
def debugMessageOne(message, user, nameDisplay):
    return "As the user, you are fully in control of your manual timetable! If you are having issues with organisation, use the '=mt_tutorial' command, it can give you some examples! :smile:"

def debugMessageTwo(message, user, nameDisplay):
    return "If there is no data/items showing when using the '=show_all_timetables' command, then that means you have not added any data in yet! Be sure to check the '=help_page_1' command to see how I work!"

    #End of debug functions
#=================================#

def removeManualTimetableItemCommand(message, user, nameDisplay):
    if len(timetable) > 0:
        item = timetable.pop()
        return f"{item} has been successfully removed from Timetable 1!"
    return f"{nameDisplay}, Timetable 1 is already empty! Nothing was removed."

#End of function removeManualTimetableItemCommand

def resetManualTimetable(message, user, nameDisplay):
    if not timetable:
        return f"{nameDisplay}, Timetable 1 has already been cleared! Nothing has changed."

    if timetable:
        timetable.clear()
    return f"{nameDisplay}, Timetable 1 has been successfully reset!"

#End of function resetManualTimetable

def showManualTimetable(message, user, nameDisplay):
    global timetable_Name
    full_timetable = ""
    if not timetable:
         return f"{nameDisplay}, Timetable 1 is empty!"
    else:
        for item in timetable:
            full_timetable += f"{item}\n"

    return f"Hey {nameDisplay}, here is your Timetable 1 ({timetable_Name}):\n{full_timetable}"

#End of function showManualTimetable

def addManualTimetable(message, user, nameDisplay):
    new_message = message.index("=add_to_timetable_1")
    message = message[new_message:]
    msglen = len("=add_to_timetable_1") + 1
    new_item = message[msglen:]
    if not new_item:
        return "You cannot add nothing to your Timetable! Please input information after the command. Use ='timetable_tutorial' for more information!"
    timetable.append(new_item)
    return(f"{new_item} has been added to your Timetable!")

#End of fucntion addManualTimetable

def messageNotUnderstood(message, use, nameDisplay):
    return f"Sorry {nameDisplay}, I didn't understand that!"

#End of method messageNotUnderstood

def helpMessageCommand(message, user, nameDisplay):
    return f"""```Here are my commands and their features, {nameDisplay}! (Help page 1)\n
    Main Commands
    '=help_page_1' - Shows page 1 of all the commands I can perform.
    '=help_page_2' - Shows page 2 of all the commands I can perform.
    '=add_to_timetable_1 [Your input here]' - Adds items you create to Timetable 1. 
    '=show_timetable_1' - Shows Timetable 1's items.
    '=remove_last_item_from_timetable_1' - Removes the last item you added to Timetable 1.
    '=reset_timetable_1' - Clears all items in Timetable 1.
    '=name_timetable_1 [Your input here]' - Give your Timetable a custom name.
    '=display_timetable_1_name' - Shows the custom name of your Timetable 1.
    '=reset_timetable_1_name' - Resets the name you gave to your Timetable 1.
    
    '=add_to_timetable_2 [Your input here]' - Adds items you create to Timetable 2. 
    '=show_timetable_2' - Shows Timetable 2's items.
    '=remove_last_item_from_timetable_2' - Removes the last item you added to Timetable 2.
    '=reset_timetable_2' - Clears all items in Timetable 2.
    '=name_timetable_2 [Your input here]' - Give your Timetable a custom name.
    '=display_timetable_2_name' - Shows the custom name of your Timetable 2.
    '=reset_timetable_2_name' - Resets the name you gave to your Timetable 2.
    
    '=timetable_tutorial' - Demonstrates how to use the '=add_to_timetable_2' command.
    '=show_all_timetables' - Displays all Timetable data.
    ```
    """

#End of function helpMessageCommand

def helpMessageCommand2(message, user, nameDisplay):
    return f"""```Here are my commands and their features, {nameDisplay}! (Help page 2)\n

    Misc and Debug Commands
    '=what_is_the_date' - Displays the current date and time by days, months, years and clock time.   
    '=debug' - Sends a list of all possible fixes to issues you may be having.
    '=more_info' - Explains how to use this bot in more depth and in more detail.
    '=show_users' - Shows all the users who have used this bot.
    '=add_me_as_a_user' - Adds you as an official user. (Also counts how many times you send message)
    '=remove_me_as_a_user' - Remove you from the user list. (No long tracks how many times you send a message)\n

    Fun Commands
    '=send_a_random_cat' - Sends a random cat gif incase you need some cute animals in your day.
    '=show_glonker_points' - Shows how many glonker points you have!
    '=what_are_glonker_points' - Explains what glonker points are and how to get them.
    '=activate_brain_rot' - Activates the secret brain rot mode! I wonder what it does. :thinking:
    '=credits' - Provides the credits of who made this bot.
    ```
    """

#=====================================glonker fucntions=====================================#

def glonkerPointsMessageCommand(message, user, nameDisplay):
    return ("Glonker points are points you get for pleasing **Glonker**.\n\nHow do you please **Glonker** you ask? "
           "Well it is secret! \n\nUse all commands to find out! There are also some **secret messages** you can say to gains points!")

#End of glonkerPointsMessageCommand

def glonkerKing(message, user, nameDisplay):
    global glonkerKingFlag
    global glonkerPointsCounter

    if glonkerKingFlag == 0:
        glonkerKingFlag =+ 1
        glonkerPointsCounter += 2
        print("Glonker points Counter: " + str(glonkerPointsCounter))
        return "Glonker is indeed king! You have gained two glonker points!"
    elif glonkerKingFlag == 1:
        return "You have already praised the king!"

def glonkerHello(message, user, nameDisplay):
    global glonkerHelloFlag
    global glonkerPointsCounter

    if glonkerHelloFlag == 0:
        glonkerHelloFlag = + 1
        glonkerPointsCounter += 1
        print("Glonker points Counter: " + str(glonkerPointsCounter))
        return "You have pleased Glonker. You have gained a Glonker point!"
    elif glonkerHelloFlag == 1:
        return "You've already said hello to Glonker!"

#End of glonkerHello function.

def glonkerPointsShowCommand(message, user, nameDisplay):
    global glonkerPointsCounter
    global brainRotMessageFlag
    global glonkerState

    if glonkerPointsCounter <= 0:
        return f"You have {glonkerPointsCounter} Glonker points! Glonker is not pleased with you."

    elif glonkerPointsCounter <= 2:
        return f"You have {glonkerPointsCounter} Glonker points! Glonker is somewhat pleased with you."

    elif glonkerPointsCounter <= 3:
        glonkerState += 1
        glonkerPointsCounter = 4
        print("Glonker Points are now at :" + str(glonkerPointsCounter))
        return f"You have collected all the glonker points! Glonker is very pleased with you! You have unlocked __**Brain Rot Mode!**__ :smiling_imp:"

    if glonkerState == 1:
        return f"You have collected all the Glonker points! Glonker is very pleased with you!"


#=====================================End of glonker Functions=====================================#

def visitorMessageCommand(message, user, nameDisplay):
    v = "Official users and their message count: "
    for who in visitors:
        v = v + "\n" + "- " + who + " with " + str(visitors[who]) + " messages!"
        return v
    if not visitors:
        return f"{nameDisplay}, there are no current users right now!"

#End of function visitorMessageCommand

def Test(message, user, nameDisplay):
    return "TEST FUNCTION"

#End of function Test. This is used to test parts of code that are not working correctly. [FOR BUG TESTING ONLY]

def visitorAddCommand(message ,user ,nameDisplay):

    global visitors
    if user not in visitors:
        visitors[user] = 1
        return f"Hi {nameDisplay}! You are now listed as an official user! I will now keep track of how many messages you send! :smile:"
    else:
        return "You are already an official user!"

#End of function visitorAddCommand

def visitorRemoveCommand(message, user, nameDisplay):
    global visitors
    if user not in visitors:
        return f"{nameDisplay}, you aren't listed as an official user yet! Nothing changed."
    else:
        visitors.pop(user)
        return f"Hi {nameDisplay}! Sorry to see you go, you are now removed from from the user list! I will no longer track your messages."

#End of function visitorRemoveCommand

def catSenderCommand(message, user, nameDisplay):
    global choice
    choice = 0 #Variable that holds an number

    choice = random.randint(1, 6) #Picks a number between 1 and 6 at random
    if choice == 1:
        return "Here is a random cat! He is sleepy! https://media1.tenor.com/m/47qpxBq_Tw0AAAAd/cat-cat-meme.gif"
    elif choice == 2:
        return "Here is a random cat! He's so happy! https://media.tenor.com/CnP64S7lszwAAAAi/meme-cat-cat-meme.gif"
    elif choice == 3:
        return "Here is a random cat! Looks like he's giving you a side eye :eyes: https://media1.tenor.com/m/yNMGjXsoYGUAAAAd/cat-cats.gif"
    elif choice == 4:
        return "Here is a random cat! She does not look very impressed right now. https://media1.tenor.com/m/-tquk_v-Y_YAAAAC/emy-d%C3%A9part.gif"
    elif choice == 5:
        return "Here is a random cat! She is working overtime! https://media1.tenor.com/m/m811ZEJkb9UAAAAC/kfc-cat.gif"
    elif choice == 6:
        return "Here is a random cat! Say hello! https://media1.tenor.com/m/Onl8JXpfN3QAAAAC/hi-glonker-glonker.gif"

#End of function catSenderCommand

def dateMessageCommand(message, user, nameDisplay):
    global current_date
    return f"The date is {current_date.strftime('%A: %d/%m/%Y %H:%M')}"

#End of function dateMessageCommand

def easterEggMessageCommand(message, user, nameDisplay):
    return "Hey! Stop copying me!"

#End of function easterEggMessageCommand

def creditMessageCommand(message, user, nameDisplay):
    return f"Timetable bot made by {user}!"

#End of function creditMessageCommand

def moreInfomationMessageCommand(message, user, nameDisplay):
    return ("This Timetable bot can provide a Timetable handling service!\n\n"
            "You have 10 Timetables at your disposal! You may give a custom name each Timetable, whilst also being able add things to them! \n\nBe sure to check out the '=timetable_tutorial' command to see how to add items to your Timetables!")

#End of moreInformationMessageCommand Function

def secretYippieMessage(message, user, nameDisplay):
    return "**Yippie!!!** https://media1.tenor.com/m/yqxW6xzgR6UAAAAC/cat-jumpy.gif"

#End of secretYippieMessage Function

###OLD CODE BELOW###

#def visitorAddCommand(message, user, nameDisplay):
#    global visitors
#    if user in visitors:
#        visitors[user] = visitors[user] + 1
#    else:
#        visitors[user] = 1
#        return f"Hi {nameDisplay}! It appears that you're new here, I hope you enjoy your stay! :smile:"

#Test Code#
#x = 0
#y = 0
#z = 0

#def testFunctionCalculator():
#    x = input("First number: ")
#    y = input("Second number: ")
#    result = int(x) + int(y)
#    print(result)
#testFunctionCalculator()

    #print("Timer default", str(timer))

    #while timer < 100 and timerState == 0:
    #    time.sleep(0.2)
    #    timer += 1  # While timer is less than 100, it will count it's way to 100 in intervals of 0.2 seconds.
    #    print("Timer: ", str(timer))

    #if timer == 100:  # Once the timer has reached 100, it will send a message.
    #    print("Timer Complete")
    #    timer = 0
    #    print("Timer reset check: ", str(timer))
    #    return "It appears you have been inactive for awhile, if you are stuck, please use '=help_page1'!"

##END OF OLD CODE##

#####INGORE EVERYTHING BELOW FOR NOW ################
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

botChannel = "bot" + str(botID)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! <')
    # print out serve name and id
    for guild in client.guilds:
        print("Server/Guild", guild.name, guild.id)
        # print out the members on this server.
        for member in guild.members:
            print("Member", member)

    time.sleep(3)

    for guildServer in client.guilds:
        chn = discord.utils.get(guildServer.text_channels, name=botChannel)
        print(f'{botChannel} found ', chn)
        message = setup() # "I have arrived on " + botChannel
        if not (chn is None):
            await chn.send(content=message)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message: discord.Message):
    # print( '***TELLS', message.author.name , client.user.name   )
    if message.author == client.user:
        return
    if message.author.name in client.user.name:
        return
    if message.channel.name != botChannel:
        return




# The main tokens have been removed for security and safety

    if "CodeWrangleBot" in message.author.name or "CodeWranglingBot" in message.author.name:
        return

    # print(  "** OK ", message.author.name , client.user.name  , ";", message.content, ":")

    response = overheard(message.content, message.author.name, message.author.display_name)  # "I hear what you say"
    await message.channel.send(response)

client.run(TOKEN)


