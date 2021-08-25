# Import Dependencies =
import random

# Define all my global functions 
def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)





# The question 
def TheCyberKingQuestion1():
    # At this point we will be requesting for the player to enter the source of the games data in a text file(.txt) format.
    file_name = input("Give the name of the words and their meanings file:")

    # After entering the filename, I can now read the file.
    # Note that -  The file must be in the same folder as the python file. 
    read_file = open(file_name, 'r')

    # Take the read file and convert to a key value pair.
    answer = {}
    for line in read_file:
        k, v = line.strip().split(',')
        answer[k.strip()] = v.strip()

    #Define some initial variables
    yes = "yes"
    no = "no"
    user_entered_value = ""
    question_mark = "?"

    # I will start an infinite loop here.
    while True:
        # if user input is empty
        if(user_entered_value == ""):
            # select a list from the key value pair answer 
            word, meaning = random.choice(list(answer.items()))
            # declare more variable 
            the_word = word
            the_meaning = meaning
            # Create a scrambled word
            scrambled_word = scramble(the_word)
            # User Input 
            user_entered_value = input("Unscramble the following letters to form a word. Type ? for the meaning of the unscambled word:{}\n\nEnter the answer [or ? for the meaning]:".format(scrambled_word))
            # User Input if equals to question mark
            if(user_entered_value == question_mark):
                print("\n\nThe word means:" + the_meaning)
                user_entered_value = input("Enter the answer [or ? for the meaning]:")
        # User Input if equals to question mark
        elif (user_entered_value == question_mark):
            print("\n\nThe word means:" + the_meaning)
            user_entered_value = input("Enter the answer [or ? for the meaning]:")
        # User Input if equals to no
        elif (user_entered_value == no):
            user_entered_value = "no"
            print("Goodbye!")
            break
        # User Input if equals to yes
        elif (user_entered_value == "yes"):
            user_entered_value = ""
        # User Input if equals to wrong 
        elif (user_entered_value != the_word):
            print("\n\nWrong, try again")
            user_entered_value = input("Enter the answer [or ? for the meaning]:")
        # User Input if equals to right answer
        elif (user_entered_value == the_word):
            user_entered_value = input("You got it! Do you want to continue[yes or no]")








# Call function 
TheCyberKingQuestion1()