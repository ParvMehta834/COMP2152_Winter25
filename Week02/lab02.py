import random

#define the choices array
choices = [ "Rock" , "Paper" , "Scissors"]

def main():
    try:
        user_input = input("Enter your chioce (Rock, Paper, Scissors): ").capitalize()
    
        #validate user input
        if user_input not in choices:
            raise ValueError("Invalid choice! Please enter 'Rock', 'Paper', 'Sciessors'")
    
        #Convert the user inout to an index
        player_choice = choices.index(user_input)
    
    
        #Randomly select the computer choice 
        computer_choice = random.randint(0,2)

        print(f"Player choose {choices [player_choice]}")
        print(f"Computer choose {choices [computer_choice]}")
    
        # Determine the winer
        if player_choice == computer_choice:
            print("It is a tie!")
        elif (player_choice == 0 and computer_choice == 2) or \
            (player_choice==1 and computer_choice== 0) or \
            (player_choice==2 and computer_choice==1):
                print ("Player Wins!")
        else:
            print("Computer Wins!")    

    except ValueError as e:
         print(f"Error {e}")
         
    
    return True
# Run the game
if __name__ == "__main__":
        main()      