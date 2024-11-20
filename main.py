
import os

#input from user
# Password prompt
password = input("Enter the password: ")
while password != "OnLoad":
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")
print("Password accepted.")

#Menu
def menu():
  print("*******************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("*******************************")
  print("Plese enter the following number bellow from the following menu: ")
  print("[1] PRINT all Authorized Vehicles")
  print("[2] SEARCH for Authorized Vehicle")
  print("[3] ADD Authorized Vehicle")
  print("[4] DELETE Authorized Vehicle")
  print("[5] Exit")
  print("*******************************")

#Print menu
menu()

#Give option to choose
option = int(input("Enter your option: "))

#Array of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Load vehicles from file (if it exists)
if os.path.exists("vehicle.txt"):
    with open("vehicle.txt", "r") as file:
        AllowedVehiclesList = file.read().splitlines()

#While loop to keep the program running
while option != 5:
  if option == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    #Prints the array
    for AllowedVehicles in AllowedVehiclesList:
      print(AllowedVehicles)
    #Gives menu option to choose
    menu()
    option = int(input("Enter your option: "))

  #option 2 is chosen
  elif option == 2:
    #prompt to choose the vehicle
    print("Please Enter the full Vehicle name: ")
    #input for the vehicle
    vehicle = input()
    #if statement to check if the vehicle is in the list
    if vehicle in AllowedVehiclesList:
      print(f"The {vehicle} is an authorized vehicle") 
      #Gives menu option to choose
      menu()
      option = int(input("Enter your option: ")) #Get user's next choise
    else:
      print(f"The {vehicle} is not an authorized vehicle") 
      #Gives menu option to choose
      menu()
      option = int(input("Enter your option: ")) #Get user's next choise

  #opition 3 is chosen
  elif option == 3:
    print("Please enter the full Vehicle name you would like to add: ")
    #input for the vehicle
    vehicle = input()
    #check if the vehicle is already in the list
    if vehicle in AllowedVehiclesList:
        print(f"The {vehicle} is already in the list")
        menu()
        option = int(input("Enter your option: "))
    else:
      #add vehicle to the end of the list
      AllowedVehiclesList.append(vehicle)
      print(f"You have added \"{vehicle}\" as an authorized vehicle")
      #save updated list to file
      with open("vehicles.txt", "w") as file:
          file.write("\n".join(AllowedVehiclesList))
      #Gives menu option to choose
      menu()
      option = int(input("Enter your option: "))

#option 4 is chosen
  elif option == 4:
    print("Please enter the full Vehicle name you would like to REMOVE: ")
    #input for the vehicle
    vehicle = input()
    #check if the vehicle is in the list
    if vehicle in AllowedVehiclesList:
      print(f"Are you sure you watn to remove \"{vehicle}\" from the list Authourized Vehicle List?")
      #input for the user to confirm
      confirm = input("Enter yes or no: ")
      #if statement to check if the user confirms
      if confirm.lower() == "yes":
        #remove vehicle from the list
        AllowedVehiclesList.remove(vehicle)
        print(f"You have removed \"{vehicle}\" from the list")

        #save updated list to file
        with open("vehicle.txt", "w") as file:
            file.write("\n".join(AllowedVehiclesList))

        #menu option
        menu()
        option = int(input("Enter your option: "))
      else:
        menu()
        option = int(input("Enter your option: "))
    else:
      print(f"The {vehicle} is not in the list of authorized vehicles")
      menu()
      option = int(input("Enter your option: "))

#option 5 is chosen
#exit the program
#saves the updated list to file
def save_vehicles_to_file():
  """Saves the AllowedVehiclesList to a file named "vehicles.txt"."""
  with open("vehicles.txt", "w") as file:
      file.write("\n".join(AllowedVehiclesList))
save_vehicles_to_file()
#Thank you 
print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
