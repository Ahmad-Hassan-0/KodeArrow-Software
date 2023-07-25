import pyautogui
import keyboard
import os
import sys
import pystray
from PIL import Image
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Define the tray icon image and tooltip
icon_image_path = "icon.ico"
tooltip_text = "arrowTed by Ahmad Hassan"
premium_file_path = "premium.txt"  # File to store premium status

# Load the icon image and resize it to a suitable size for the tray (e.g., 16x16)
icon_image = Image.open(icon_image_path)
icon_image = icon_image.resize((16, 16))

# Function to show a notification popup using tkinter
# def show_tk_notification(title, message):
#     popup = tk.Toplevel()
#     popup.title(title)
#     popup.geometry("300x100")
#     label = tk.Label(popup, text=message)
#     label.pack()
#     popup.after(5000, popup.destroy)  # Close the popup after 5 seconds

# Function to show the initial instructions and key combinations
def show_instructions():
    message = "Thanks for Running ArrowTed: Developed by Ahmad Hassan \n\n\talt + i = Arrow Up(Premiums)\n\talt + k = Arrow Down(Premiums)\n\talt + j = Arrow Left(Free Version)\n\talt + l = Arrow Right(Free Version)\n\nPlease Buy The Paid Version to Unlock the Premiums"
    messagebox.showinfo("Instructions", message)

# Show the initial instructions when the program starts
show_instructions()

# Define the notification function inline
# def show_notification(icon):
#     show_tk_notification("Notification", "Your message goes here.")

# Define the function to open the URL
def open_url(icon, item):
    webbrowser.open("https://bted.000webhostapp.com/")

def open_url_buy(icon, item):
    webbrowser.open("https://bted.000webhostapp.com/HireMe.html")

# Function to create the premium file
def create_premium_file():
    with open(premium_file_path, "w") as file:
        file.write("DONT DELETE THIS FILE \n\n Premium Unlocked \n Developed By Ahmad Hassan")

# Function to delete the premium file
def delete_premium_file():
    if os.path.exists(premium_file_path):
        os.remove(premium_file_path)

# Function to check if the program is running in premium mode
def is_premium():
    return os.path.exists(premium_file_path)

# Define the function to unlock full functionality with a license key
def unlock_functionality(icon, item):
    if is_premium():
        print("Unlock Full Functionality", "Already unlocked (Paid version)")
    else:
        # Create a pop-up window to get the license key from the user
        window = tk.Tk()
        window.title("Enter License Key")
        window.geometry("300x100")
        
        label = tk.Label(window, text="Enter the license key:")
        label.pack()

        entry = tk.Entry(window, show="*")  # Hide entered characters
        entry.pack()

        def submit_key():
            entered_key = entry.get()
            if entered_key == "B-Ted":
                create_premium_file()
                print("Unlock Full Functionality", "Full functionality unlocked (Paid version)")
            else:
                print("Invalid License Key", "Invalid license key. Functionality remains limited (Free version)")
            window.destroy()
            # Recreate the menu and update the icon after the license key is changed
            create_menu()

        submit_button = tk.Button(window, text="Submit", command=submit_key)
        submit_button.pack()

        window.mainloop()

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
        menu.append(pystray.MenuItem('Buy for $2', open_url_buy))
        menu.append(pystray.MenuItem('Enter Key', unlock_functionality))

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
        # Full functionality for the paid version
        pyautogui.press('down')
    else:
        # Limited functionality for the free version
        print("Limited Functionality", "Down arrow (Free version)")

def up_arrow():
    if is_premium():
        # Full functionality for the paid version
        pyautogui.press('up')
    else:
        # Limited functionality for the free version
        print("Limited Functionality", "Up arrow (Free version)")

def right_arrow():
    pyautogui.press('right')

keyboard.add_hotkey('alt+i', up_arrow, suppress=True)
keyboard.add_hotkey('alt+k', down_arrow, suppress=True)
keyboard.add_hotkey('alt+j', left_arrow, suppress=True)
keyboard.add_hotkey('alt+l', right_arrow, suppress=True)

# Run the tray icon application
icon.run()