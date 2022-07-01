import csv
file = open("Participant_List.csv", "r+")
number_of_participants = None

def display_main_menu():
    print("""
1.) Sign up 
2.) Cancel Sign Up 
3.) View Participants
4.) Save Changes
5.) Exit""")

def display_title(title): #title plue = signs
    this_list =[]
    print(title)
    for i in title:
        print("=", end="")

def get_input(display): # take display phrase (string) displays it and returns input
    the_input = input(display)
    return the_input

def start_up():
    number_of_participants = get_input("Enter the number of participants")
    display_title("Welcome to the Tournaments R Us")
    print(f"\nThere are {number_of_participants} participant slots ready for sign up.")

def view_participants():# this needs to display the 5 up 5 down for view participants
    #for loop -5 to number +5
    print()

def confirm_deny(input, confirm, deny): # checks for y/n anything else reprimand and repeat
    if input == "y":
        return confirm
    if input == "n":
        return deny
    else:
        print("Not a valid entry!")
        return confirm_deny(input,confirm, deny)

def error_check(): #error check for matching position
    print()
    
def main_menu(): # "switch case" for main menu
    display_title("Participant menu")
    x = get_input(display_main_menu())
    
    global number_of_participants
    name = None
    starting_slot = None
    leave = None

    if x == "1":
        display_title("Participant Sign up")
        name = get_input("\nParticipant Name:")
        starting_slot = get_input(f"Desired starting slot #[1-{number_of_participants}]:")
    elif x == "2":
        display_title("Participant Cancelation")
        starting_slot = get_input(f"Starting slot #[1-{number_of_participants}]:")
        name = get_input("Participant Name:")
    elif x == "3":
        display_title("View Participants")
        starting_slot = get_input(f"Starting slot #[1-{number_of_participants}]:")
    elif x == "4":
        display_title("Save Changes")
        save = confirm_deny(get_input("Save your changes to CSV? [y/n]"), "Changes have been saved.", "Changes have not been saved")
        main_menu()
    elif x == "5":
        display_title("Exit")
        leave = confirm_deny(get_input("Any unsaved changes will be lost.\nAre you sure you want to exit? [y/n]"), "Goodbye!", "Going back to main menu.")
        if leave == "Going back to main menu.":
            main_menu()
        else:
            file.close()
            quit()
    else:
        print("Incorrect Value.")
        main_menu()

start_up()
main_menu()
        



    



    