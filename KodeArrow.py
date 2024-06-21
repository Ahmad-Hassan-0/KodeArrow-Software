import pyautogui
import keyboard
import os
import sys
import pystray
from PIL import Image
import webbrowser
import tkinter as tk
from tkinter import messagebox
import platform
import subprocess
import wmi
import itertools
import firebase_admin
from firebase_admin import credentials, firestore
import requests  # Import requests library for network connectivity check

pyautogui.PAUSE = 0.000

cred = credentials.Certificate('kodearrow-server-firebase-adminsdk-9qxya-d2f88510eb.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_hardware_id():
    system = platform.system()
    if system == "Windows":

        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        return bios.SerialNumber
    elif system == "Darwin":  # macOS
        command = "ioreg -l | grep IOPlatformSerialNumber"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        serial_number = result.stdout.split('=')[-1].strip().strip('"')
        return serial_number
    elif system == "Linux":
        command = "cat /sys/class/dmi/id/product_uuid"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    else:
        raise NotImplementedError(f"Unsupported platform: {system}")

def check_internet_connection():
    # Check internet connectivity using a simple GET request to google.com
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
# Define the tray icon image and tooltip
icon_image_path = "icon.ico"
tooltip_text = "KodeArrow by Ahmad Hassan"
premium_file_path = "systemCompatibility.txt"  # File to store premium status

# Load the icon image and resize it to a suitable size for the tray (e.g., 16x16)
icon_image = Image.open(icon_image_path)
icon_image = icon_image.resize((16, 16))

def is_premium():
    return os.path.exists(premium_file_path)


# Function to show the initial instructions and key combinations
def show_instructions():
    message = "Thank you for using KodeArrow, project by Ahmad Hassan\n\n\n\t\t       Alt + I\n\t\t   (Arrow Up)\n\n     Alt + J \t\t\t       Alt + L \t(Arrow Left) \t\t\t(Arrow Right)\n\n\t\t      Alt + K \n\t\t(Arrow Down)\n\nPlease buy Premium version to unlock ease to access features"
    messagebox.showinfo("Instructions", message)

def show_instructionsPremium():
    message = "Thank you for using KodeArrow, project by Ahmad Hassan\n\n\n\t\t       Alt + I\n\t\t   (Arrow Up)\n\n     Alt + J \t\t\t       Alt + L \t(Arrow Left) \t\t\t(Arrow Right)\n\n\t\t      Alt + K \n\t\t(Arrow Down)\n\n\n\t          ! Premium Unlocked !"
    messagebox.showinfo("Instructions", message)

# Show the initial instructions when the program starts
if not is_premium():
    show_instructions()
else:
    show_instructionsPremium()

# Define the function to open the URL
def open_url(icon, item):
    webbrowser.open("https://bted.000webhostapp.com/")

def open_url_buy(icon, item):
    webbrowser.open("https://kodearrow.000webhostapp.com/")

def create_hidden_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        
        # Try to set the hidden attribute based on the platform
        if platform.system() == "Windows":
            # Windows: Use ctypes to set hidden attribute
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN)
        elif platform.system() == "Darwin":
            # macOS: Prefix file name with a dot to hide it
            os.rename(file_path, f".{file_path}")
        elif platform.system() == "Linux":
            # Linux: Prefix file name with a dot to hide it
            os.rename(file_path, f".{file_path}")
        else:
            raise NotImplementedError(f"Unsupported platform: {platform.system()}")
        
        print(f"Hidden file '{file_path}' created successfully.")
        
    except Exception as e:
        print(f"Failed to create hidden file '{file_path}': {e}")

file_path = "systemCompatibility.txt"
content = """YOUR PREMIUM UNLOCK IS UNLOCKED
                             
                             (((                                                
                             (((((((////                                        
                             (((((((((////                                      
                                   (((((///                                     
                                    ((((((/                                     
                                     (((((((                                    
                                     (((((((                                    
                                     (((((((                                    
                                     (((((((                                    
                                     (((((((                                    
                                     ###((((                                    
                                     #####((                                    
                                     #######                                    
                                      #######                                   
                                      ########            ##((                  
                                        ########          ####(((((((           
      THANKS FOR BUYING KODEARROW         ##########      ####   ((((((((((     
[]][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][      @@@@@@@@@@@ 
                                         ]]#########      &&&&&&&&&&&@@@        
                                        ]]]]]##           &&&&&&&&               
                                      ]]]]]]]             &&&&                    
                                     ]]]]]]%                                    
                                     &]]]]]]                                    
                                     &&&]]]]                                    
                                     &&&&&]]                                    
                                     &&&&&&&                                    
                                     &&&&&&&                                    
                                     &&&&&&&                                    
                                    @@@&&&&                                     
                             @@@@@@@@@@@@@&                                     
                             @@@@@@@@@@@@                                       
                             @@@@@@@@@@@                                       
                                 
CAUTION!
DO NOT MOVE THIS FILE UNDER ANY CIRCUMSTANCES.
DO NOT CHANGE THE DIRECTORY OF THIS FILE.
KEEP THE FILE IN THE SAME FOLDER.
DO NOT SHARE THIS FILE ACROSS ANY OTHER DEVICES.

VIOLATION OF ANY OF THESE INSTRUCTIONS MAY LEAD TO THE USER BEING HELD LIABLE FOR LEGAL ACTION.

CopyrightÂ© 2023. Ahmad Hassan(B-TED)
Project KodeArrow
"""

# Function to check if the program is running in premium mode
def is_premium():
    return os.path.exists(premium_file_path)

# Define the function to unlock full functionality with a license key
# def unlock_functionality(icon, item):
#     if is_premium():
#         print("Unlock Full Functionality", "Already unlocked (Paid version)")
#     else:
#         # Create a pop-up window to get the license key from the user
#         window = tk.Tk()
#         window.title("Enter License Key")
#         window.geometry("300x100")
        
#         label = tk.Label(window, text="Enter the license key:")
#         label.pack()
        
#         # entry = tk.Entry(window, show="*")  # Hide entered characters
#         entry = tk.Entry(window)  # Hide entered characters
#         entry.pack()
        
#         def submit_key():
#             entered_key = entry.get()
#             if entered_key == "BTED-KAKS-P2SE-2023":
#                 create_hidden_file(file_path, content)
#                 messagebox.showinfo("Congratulations", "Premium Unlocked")
#                 #print("Unlock Full Functionality", "Full functionality unlocked (Paid version)")
#             else:
#                 messagebox.showinfo("Invalid License KeY", "Invalid license key. Functionality remains limited (Free version)")
#             window.destroy()
#             # Recreate the menu and update the icon after the license key is changed
#             create_menu()
        
#         submit_button = tk.Button(window, text="Submit", command=submit_key)
#         submit_button.pack()
        
#         window.mainloop()
###########################################################################################################3


# def unlock_functionality(icon, item):
#     if is_premium():
#         print("Unlock Full Functionality", "Already unlocked (Paid version)")
#     else:
#         # Create a pop-up window to get the license key from the user
#         window = tk.Tk()
#         window.title("Email")
#         window.geometry("400x200")
        
#         label = tk.Label(window, text="Enter you Email: \nNote: this process requires internet connectivity)\n")
#         label.pack()
        
#         # entry = tk.Entry(window, show="*")  # Hide entered characters
#         entry = tk.Entry(window)  # Hide entered characters
#         entry.pack()
        
#         def submit_key():
#             hardware_id = get_hardware_id()
#             email = entry.get()

#             if check_and_update(email, hardware_id):
#                 messagebox.showinfo("Congratulations", "Premium Unlocked")
#             else:
#                 messagebox.showinfo("Registration not Found", "Registration not Found: Have you received you conformation email? if not then go and check it out ")
#                 #messagebox.showinfo("Invalid License Key", "Invalid license key. Functionality remains limited (Free version)")
#             window.destroy()
#             # Recreate the menu and update the icon after the license key is changed
#             create_menu()
        
#         submit_button = tk.Button(window, text="Submit", command=submit_key)
#         submit_button.pack()
        
#         window.mainloop()


# def check_and_update(email, hardware_id):
#     # Check if the email exists in Firestore users collection
#     user_ref = db.collection('users').document(email)
#     user_doc = user_ref.get()

#     if user_doc.exists:
#         # User exists, check devices
#         devices_ref = user_ref.collection('devices')
#         devices_query = devices_ref.get()

#         if len(devices_query) >= 4:
#             messagebox.showinfo("Error", "Maximum devices reached")
#         else:
#             # Check if hardware ID already exists
#             hardware_exists = False
#             for device in devices_query:
#                 if device.to_dict().get('id') == hardware_id:
#                     hardware_exists = True
#                     break
            
#             if hardware_exists:
#                 print("Hardware ID already exists. Activating premium.")
#                 #messagebox.showinfo("Congratulations", "Premium Unlocked")
#                 create_hidden_file(file_path, content)
#                 return True
#             else:
#                 # Add hardware ID to Firestore
#                 device_data = {'id': hardware_id}
#                 devices_ref.document(f'device{len(devices_query) + 1}').set(device_data)
#                 print(f"Added hardware ID '{hardware_id}' to Firestore.")
#                 print("Activating premium.")
#                 #messagebox.showinfo("Congratulations", "Premium Unlocked")
#                 create_hidden_file(file_path, content)
#                 return True
#     else:
#         print("Email not registered.")
#         #messagebox.showinfo("Registration not Found", "Registration not Found: Please check your email")
#         return False


def unlock_functionality(icon, item):
    if is_premium():
        print("Unlock Full Functionality", "Already unlocked (Paid version)")
    else:
        # Create a pop-up window to get the email from the user
        window = tk.Tk()
        window.title("Email")
        window.geometry("400x200")
        
        label = tk.Label(window, text="Enter your Email: \n(Note: this process requires internet connectivity)\n")
        label.pack()
        
        entry = tk.Entry(window)
        entry.pack()
        
        def submit_key():
            email = entry.get().strip()
            hardware_id = get_hardware_id()

            if check_and_update(email, hardware_id):
                messagebox.showinfo("Congratulations", "Premium Unlocked")
            
            window.destroy()
            create_menu()
        
        submit_button = tk.Button(window, text="Submit", command=submit_key)
        submit_button.pack()
        
        window.mainloop()

def check_and_update(email, hardware_id):
    # Check internet connectivity
    if not check_internet_connection():
        messagebox.showinfo("Error", "Please check your internet connection again.")
        return False
    
    # Check if the email exists in Firestore users collection
    user_ref = db.collection('users').document(email)
    user_doc = user_ref.get()

    if user_doc.exists:
        # User exists, check devices
        devices_ref = user_ref.collection('devices')
        devices_query = devices_ref.get()

        if len(devices_query) >= 4:
            messagebox.showinfo("Error", "Maximum devices reached")
            return False
        else:
            # Check if hardware ID already exists
            hardware_exists = False
            for device in devices_query:
                if device.to_dict().get('id') == hardware_id:
                    hardware_exists = True
                    break
            
            if hardware_exists:
                print("Hardware ID already exists. Activating premium.")
                create_hidden_file(file_path, content)
                return True
            else:
                # Add hardware ID to Firestore
                device_data = {'id': hardware_id}
                devices_ref.document(f'device{len(devices_query) + 1}').set(device_data)
                print(f"Added hardware ID '{hardware_id}' to Firestore.")
                print("Activating premium.")
                create_hidden_file(file_path, content)
                return True
    else:
        print("Email not registered.")
        messagebox.showinfo("Registration not Found", "Registration not Found: Please check your email")
        return False

############################################################################################################3
# Function to create the tray icon menu
def create_menu():
    global menu, icon
    menu = [
        # pystray.MenuItem('Notification', lambda icon, item: show_tk_notification("Notification", "Your message goes here.")),
        pystray.MenuItem('Created by Ahmad Hassan', open_url),
    ]

    # Check if the program is running in the paid version and adjust the menu accordingly
    if is_premium():
        pass  # If premium, do not show the "Buy for $2" and "Unlock Full Functionality" options
    else:
        menu.append(pystray.MenuItem('Buy here for $2', open_url_buy))
        menu.append(pystray.MenuItem('Already bought? Unlock Here', unlock_functionality))
    
    menu.append(pystray.MenuItem('Exit', lambda icon, item: exit_program()))  # Add the Exit option to the menu
    
    # Update the icon with the new menu
    icon.menu = pystray.Menu(*menu)

# Function to exit the program
def exit_program():
    icon.stop()
    sys.exit()

# Create the initial menu
menu = []  # Define an empty menu
icon = pystray.Icon("arrowTed by Ahmad Hassan", icon=icon_image, title=tooltip_text, menu=menu)
create_menu()

# Define the hotkey event hooks and suppress the default behavior (suppress=True)
def left_arrow():
    pyautogui.press('left')

def down_arrow():
    if is_premium():
        pyautogui.press('down')  # Full functionality for the paid version
    else:
        print("Limited Functionality", "Down arrow (Free version)")   # Limited functionality for the free version

def up_arrow():
    if is_premium():
        pyautogui.press('up')       # Full functionality for the paid version
    else:
        print("Limited Functionality", "Up arrow (Free version)") # Limited functionality for the free version

def right_arrow():
    pyautogui.press('right')

def page_up_key():
    if is_premium():
        pyautogui.press('pageup')  # Full functionality for the paid version
    else:
        print("Limited Functionality", "Down arrow (Free version)")   # Limited functionality for the free version

def page_down_key():
    if is_premium():
        pyautogui.press('pagedown')  # Full functionality for the paid version
    else:
        print("Limited Functionality", "Down arrow (Free version)")   # Limited functionality for the free version

def end_key():
    if is_premium():
        pyautogui.press('end')  # Full functionality for the paid version
    else:
        print("Limited Functionality", "Down arrow (Free version)")   # Limited functionality for the free version

def home_key():
    if is_premium():
        pyautogui.press('home')  # Full functionality for the paid version
    else:
        print("Limited Functionality", "Down arrow (Free version)")   # Limited functionality for the free version


key_actions = {
    'i': up_arrow,
    'j': left_arrow,
    'k': down_arrow,
    'l': right_arrow
}

# Function to handle combinations
def handle_combination(*keys):
    for key in keys:
        key_actions[key]()  # Call the respective function for each key

# Add hotkeys for all combinations
keys = ['i', 'j', 'k', 'l']

# Single key combinations
for key in keys:
    keyboard.add_hotkey(f'alt+{key}', handle_combination, args=(key,), suppress=True)

# Two key combinations
for combo in itertools.permutations(keys, 2):
    keyboard.add_hotkey(f'alt+{combo[0]}+{combo[1]}', handle_combination, args=combo, suppress=True)

# Three key combinations
for combo in itertools.permutations(keys, 3):
    keyboard.add_hotkey(f'alt+{combo[0]}+{combo[1]}+{combo[2]}', handle_combination, args=combo, suppress=True)

# Four key combinations
for combo in itertools.permutations(keys, 4):
    keyboard.add_hotkey(f'alt+{combo[0]}+{combo[1]}+{combo[2]}+{combo[3]}', handle_combination, args=combo, suppress=True)


# keyboard.add_hotkey('alt+shift+i', page_up_key, suppress=True)
# keyboard.add_hotkey('alt+shift+j', page_down_key, suppress=True)
# keyboard.add_hotkey('alt+shift+l', end_key, suppress=True)
# keyboard.add_hotkey('alt+shift+k', home_key, suppress=True)

# Run the tray icon application
icon.run()