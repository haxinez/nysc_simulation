import time
import os
import nysc_deployment_simulation
import sys


nysc=nysc_deployment_simulation

def clear_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For macOS and Linux


def loading_simulation(duration, interval=0.1):
    logo="\t\t\t🇳 🇾 🇸 🇨 \n"
    strt="░𝕊░░𝕋░░𝔸░░ℝ░░𝕋"
    text="\t \tstate deployment simulation \n"
    shadow="░"*20
    display= f"{logo}{text}{shadow}{strt}{shadow}"
    print(display)
    
    total_ticks = int(duration / interval)
    for tick in range(total_ticks + 1):
        percent_complete = (tick / total_ticks) * 100
        progress_bar = "|" * tick
        spaces = " " * (total_ticks - tick)
        
        print(f"\twait:[{progress_bar}{spaces}] {percent_complete:.1f}%", end="\r")
        time.sleep(interval)
        
    print("\n\t\t\t[Done]")
    time.sleep(0.8)
    # Call the function to clear the terminal
    clear_terminal()
    nysc.start_process()
    
    
    

# Usage example: Run the loading simulation for 5 seconds with a 0.2-second interval.
loading_simulation(5, 0.2)
