# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# William Min
# wkmin1@uci.edu
# 51528316

from Profile import Profile
from ds_client import send

# print a dictionary of commands and theri prompts on a single line in parentheses
def print_command_dict_on_line(command_dict:dict):
    command_list = list()

    for command in command_dict.keys():
        prompt = command_dict[command][0]
        command_list.append(" " + command + " -> " + prompt + " ")

    return "(" + "|".join(command_list) + ")"

# ask continously for a valid command basec on dictionary of commands
def get_valid_command(command_dict:dict, prompt:str) -> str:
    command = input(prompt)

    while command not in command_dict:
        command = input(f"Invalid command. Please try again {print_command_dict_on_line(command_dict)}: ")

    return command

# set profile username and password
def set_profile_usr_pwd(profile:Profile):

    has_right_input = False
    old_usr = profile.username
    old_pwd = profile.password

    while not has_right_input:
        
        print()
        username = input("Enter profile username: ")
        password = input("Enter profile password: ")
        print()

        # currently logging in
        if (old_usr == None or len(old_usr) <= 0) and (old_pwd == None or len(old_pwd) <= 0):
            profile.username = username
            profile.password = password
            has_right_input = True

        # changing to new profile
        else:

            # checking for same profile info
            if username == old_usr and password == old_pwd:
                retry_dict = {"R" : ["retry prompt"],
                                "CA" : ["cancel"],
                                }
                command_input = get_valid_command(retry_dict.keys(), f"You're making the same current profile. Please try again or exit prompt {print_command_dict_on_line(retry_dict)}: ")

                if command_input == "CA":
                    has_right_input = True
            
            # confirm if you want this new profile
            else:
                usr_pwd_command_dict = {"C" : ["confirm inputs"],
                                        "R" : ["retry prompt"],
                                        "CA" : ["cancel"],
                                        }

                print(f"{old_usr} -> {username}, {old_pwd} -> {password}")
                command_input = get_valid_command(usr_pwd_command_dict, f"Confirm new profile? {print_command_dict_on_line(usr_pwd_command_dict)}: ")
                
                # command functionality
                if command_input != "R":

                    if command_input == "C":
                        profile.username = username
                        profile.password = password
                        has_right_input = True
                    elif command_input == "CA":
                        has_right_input = True

                    print()

# set profile bio
def set_profile_bio(profile:Profile):
    
    confirmed_new_bio = False
    bio_command_dict = {"C" : "confirm bio",
                        "R" : "retry bio",
                        "CA" : "cancel",
                        }

    while not confirmed_new_bio:
        
        # input new bio
        bio = input("\nEnter bio below:\n")
        old_bio = profile.bio

        # fill profile bio if empty
        if len(old_bio) <= 0 or old_bio.isspace():
            profile.bio = bio
            confirmed_new_bio = True

        # confirm to change bio
        else:
            print(f"\nOLD:\n{profile.bio}\n\nNEW:\n{bio}\n")
            command_input = get_valid_command(bio_command_dict, f"Confirm new bio? {print_command_dict_on_line(bio_command_dict)}: ")

            # command functionality
            if command_input == "C":
                profile.bio = bio
                confirmed_new_bio = True
            elif command_input == "CA":
                confirmed_new_bio = True

# send message
def send_message(profile:Profile):

    message = input("\nEnter message below:\n")
    print()

    if send(profile.dsuserver[0], profile.dsuserver[1], profile.username, profile.password, message, profile.bio):
        print(f"Your message \"{message}\" was sent successfully.\n")
    else:
        print("An error occurred when sending your message.\n")

# main program
def main():
    server = ("168.235.86.101", 3021)
    print("Welcome to the DSU online post service!")
    print("Please enter your profile username and password below to begin.")

    current_profile = Profile(dsuserver = server)
    set_profile_usr_pwd(current_profile)

    is_using_program = True
    interface_dict = {"UP" : ("change username or password", set_profile_usr_pwd),
                    "M" : ("message to DSU server", send_message),
                    "B" : ("change profile bio", set_profile_bio),
                    "Q" : ["quit program"]
                    }

    while is_using_program:
        command_input = get_valid_command(interface_dict, f"What do you wish to do? {print_command_dict_on_line(interface_dict)}: ")

        if command_input == "Q":
            is_using_program = False
        else:
            interface_dict[command_input][1](current_profile)

    print("\nThe program has ended. Thank you for using our services!")

if __name__ == "__main__":
    main()