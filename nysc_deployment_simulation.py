import random
import os
import sys
import time

# List of all the 37 states in Nigeria.
# The list is defined as a set to avoid conflicts and enable easy filtering.
nigeria_states = {'abia', 'adamawa', 'akwa ibom', 'anambra', 'bauchi', 'bayelsa', 'benue', 'borno',
                 'cross river', 'delta', 'ebonyi', 'edo', 'ekiti', 'enugu', 'gombe', 'imo', 'jigawa', 'kaduna',
                 'kano', 'katsina', 'kebbi', 'kogi', 'kwara', 'lagos', 'makurdi', 'nassarawa', 'niger',
                 'ogun', 'ondo', 'oyo', 'osun', 'plateau', 'rivers', 'sokoto', 'taraba', 'Abuja', 'zamfara'
                 }

# An empty list to store information about the user's state of origin, residence, and school.
myStates = []

def clearScreen():
    # Clear the terminal screen based on the user's platform.
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def nysc_posting(name, state_of_origin, state_of_residence, state_schooled):
    # Prompt the user to enter states they have visited, separated by commas.
    state_visited = input("Enter states visited separated by comma\n=> ").lower().split(',')
    clearScreen()
    time.sleep(0.5)
    
    if len(state_visited) <= 4:
        myStates.append(state_of_origin)
        myStates.append(state_of_residence)
        myStates.append(state_schooled)
        
        # Combine the lists of states visited and user's states.
        ticked_states = myStates + state_visited
        
        # Convert the list to a set for efficient comparison.
        non_deployment_state = set(ticked_states)
        
        # Find the states in Nigeria not visited by the user.
        possible_deployment_state = nigeria_states.difference(non_deployment_state)
        
        # Choose a random state from the available options and announce it to the user.
        deployed_state = random.choice(list(possible_deployment_state))
        print(f'Congratulations {name.upper()}!\nYou have been posted to  >>[{deployed_state.upper()}]<<')
    else:
        print("Your selections are null or you exceeded the allocated number of visited states."
              f"\nThe system will now choose from all the available states excluding {state_of_origin}, {state_of_residence}, and {state_schooled}.")
        myStates.append(state_of_origin)
        myStates.append(state_of_residence)
        myStates.append(state_schooled)
        
        # Find the states in Nigeria not visited by the user.
        possible_deployment_state = nigeria_states.difference(set(myStates))
        
        # Choose a random state from the available options and announce it to the user.
        deployed_state = random.choice(list(possible_deployment_state))
        print(f'\nCongratulations {name.upper()}!\nYou have been posted to  >>[{deployed_state.upper()}]<<')

def start_process():
    print("\t\tSTAGE ONE")
    print("\tFill in your details appropriately.\n Important Notice: visited states should not be more than 4")
    print("="*60)
    student_name = input("Enter name: ")
    student_origin = input("Enter State of origin: ").lower()
    student_state_residence = input("Enter State of residence: ").lower()
    state_schooled = input("State of school graduated in: ").lower()
    
    while True:
         if (student_origin not in nigeria_states) or (student_state_residence not in nigeria_states) or (state_schooled not in nigeria_states):
         	print("-"*60)
         	print("Please check that the information provided is correct")
         	print("-"*60)
         	try:
         		prompt=input("Choose option\n\tEnter 1: Retry\n\tEnter any key: Quit\n=>")
	         	if prompt != "1":
	         		print("Good bye!")
	         		break
	         	else:
	         		student_name = input("Enter name: ")
	         		student_origin = input("Enter State of origin: ").lower()
	         		student_state_residence = input("Enter State of residence: ").lower()
	         		state_schooled = input("State of school graduated in: ").lower()
         		
         	except:
         		print("invalid input")
         		break
         		
	         
         else:
         	print("success!")
         	print("\n\t\tFINAL STAGE")
         	nysc_posting(student_name, student_origin, student_state_residence, state_schooled)
         	break
	         		
	         	
         	
