# WELCOME SCREEN
print("--------------------------------------------------")
print("              Python Word Editor")
print("--------------------------------------------------")

print("1) Create a file")
print("2) Open a file")
print("--------------------------------------------------\n")

# import os.path -> Not used here, but for later reference (File validation)

# Accept user input
true = 1
while (true):
  user_input = str(
    input("Enter a number option and press ENTER or type 'q' to quit: "))
  print("\n")

  # ----------------- Create a file /Save a file -------------------------#
  if (user_input != 'q'):
    if (user_input == '1'):
      text_inputted = str(input("Start typing: "))
      print("\n")
      file_name = str(input("Enter file name and press ENTER: ")) + '.txt'
      text_file = open(file_name, 'x')  # Will create a new file with the name

      text_file = open(file_name, 'a')
      text_file = text_file.write(
        text_inputted)  #Write() command is used to write to file

      print("\n")
      print("File created.")
      true = 0

      # ------------------------Open a file-------------------#

    elif (user_input == '2'):
      file_name_inputted = str(input("Enter a file name plus the extension: "))
      print("\n")
      print("\n")

      # File validation - checking file exists or not, "Not used here" so commented out, but for later reference
      # path = './' + file_name_inputted
      # check_file = os.path.isfile(path) # Give True, if file exists and False if no file
      # print(check_file)

      # --------------File validation - checking file exists or not, by TRY-EXCEPT-FINALLY----#

      try:
        with open(file_name_inputted, 'r') as file:
          file = file.read()

      except FileNotFoundError:
        print("                  [Not found] " + file_name_inputted)

      else:
        print("                   [OPEN] " + file_name_inputted)

      finally:
        print("==============================================")

        print("\n")

  else:
    print("Quit \n")
    true = 0
  continue
