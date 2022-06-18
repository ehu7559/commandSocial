from argparse import ArgumentParser
from requests import post
from termcolor import colored

#Constants:
SHOW_COLORS = True
KEEP_LOGS = True
  
#Communications Module
class Requester:
    pass


#Displaying Module
class Display:

    def display_message(sender, sender_colors, message_body):
        #Format username
        #Format message_body
        #Format message_body
        pass

    def display_flavor_text():
        pass
    
    def display_gui_text():
        
        pass

    def color_text(text_body, color):
        '''Returns text_body but with color!'''
        pass

#Main method
def main():
    #Start thread listening for updates (to print)
    #Take input and process it
    while True:
        pass

#executable
if __name__ == "__main__":
    parser = ArgumentParser(description="CommandSocial(TM) Client")
    parser.add_argument("--no-color", action="store_true", help="Turns off colorful printing")
    parser.add_argument("--no-logs", action="store_true", help="Turns off message logging")
    args = parser.parse_args()