import requests, time
import numpy as np

""" A simple keyboard input interface for testing and not to be taken seriously. """


url = 'http://localhost:5000/api/'


def intro():
    print("________________________________________")
    print()
    print("██╗███╗   ██╗ █████╗ ██████╗ ██╗██╗  ██╗\n"\
          "██║████╗  ██║██╔══██╗██╔══██╗██║╚██╗██╔╝\n"\
          "██║██╔██╗ ██║███████║██████╔╝██║ ╚███╔╝ \n"\
          "██║██║╚██╗██║██╔══██║██╔══██╗██║ ██╔██╗ \n"\
          "██║██║ ╚████║██║  ██║██║  ██║██║██╔╝ ██╗\n"\
          "╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝\n"\
          "_______________________________________")
    print()
    print("Welcome to the Inarix model testing interface.")
    print("Please load your model into the wrapper in server.py")
    print("Then, run it.")
    print("Commands:")
    print(" PREDICT [INPUT]")
    print(" CUSTOM_PREDICT [INPUT]")
    print(" EXIT")
    print("_______________________________________")



def main():

    intro()

    flag = True
    while(flag):
        command = input(":")
        # Exit command
        if command == 'EXIT':
            print("Interface Shutdown.")
            print("_______________________________________")
            break

        # Predict command
        command_list = command.split()
        if command_list[0] == 'PREDICT':
            print('...', end='', flush=True)
            query = float(command[8:])
            r = requests.post(url+'predict', json={'x':query,})
            print('> ' + str(r.json()))
        
        # Custom Predict command
        command_list = command.split()
        if command_list[0] == 'CUSTOM_PREDICT':
            print('...', end='', flush=True)
            query = float(command[15:])
            r = requests.post(url+'custom_predict', json={'x':query,})
            print('> ' + str(r.json()))


if __name__ == "__main__":
    main()