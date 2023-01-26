while True:

     import random
     def hangman():
          word_list=['dictionary','advertisement','ambulance','refrigerator','televisoion','computer',
                     'development','employmet','imagination','independence','measurement','opportunity',
                     'philosophy','percentage','recommendation','transportation','significance','improvement','equipment','atmosphere']
     #randomly chooses something from the list
          word = random.choice(word_list)
          print ("\n" + "You Have",len(word),"turns")
          print("\n" + "You Have",len(word),"turns" , file = open("history.txt","a"))
          turns= len(word)
          user_letter = ""
          correct_word=""
          guessed=[]
          entry = set('abcdefghijklmnopqrstuvwxyz')                                                                                                                         


     #what the user has guessed     
          while True:
               turns>0      
               correct_word=""
               missed = 0
               for letter in word:
                    if letter in guessed:
                         correct_word = correct_word + letter
                    else:
                         correct_word = correct_word + "_ "
               if correct_word == word:
                   
                    print(correct_word)
                    print("\n"+ correct_word, file = open("history.txt","a"))
                    print("You Are Won...")
                    print("\n" + "You Are Won..." , file = open("history.txt","a"))
                    break
               else:
                    print("guess the correct word", correct_word)
                   
     #Ask the user input                    
                    guess = input()
                    if guess == "exit":
                         exit()
                    

                    if guess in entry:
                         user_letter=''
                         user_letter = user_letter + guess
                    else:
                         print("Enter the valid items")
                        
                         guess= input()
                         if guess == "exit":
                              exit()
     #if the guess is wrong display the message ,You guess wrong and display turns                   
                    if user_letter not in word:
                         turns -= 1
                         print("You Guess Wrong")
                         print("You have only ",+ turns,"turns now")
                         print("\n" + "You have only ",+ turns,"turns now", file = open("history.txt","a"))
     #if the guess is correct display the message , You guess correctly and display turns                   
                    elif user_letter in word :
                         print("You have guessed correctly")
                         guessed.append(user_letter)
                         print ("You have ", turns,"turns")
     #if turns become zero display ,You are loose and print correct word                        
                    if turns == 0:
                         print("You Are Looes...")
                         print("\n" +"You Are Looes..." , file = open("history.txt","a"))
                         print("Word is ",(word))
                         print("\n" +"Word is ",(word) , file = open("history.txt","a"))
                         break
            
                     
               

     #input name and welcome
     name=input ("Enter Your Name-")
     print ("Welcome",name,"!!!")
     #open a text document and getting game history to text document
     print("\n" + "Welcome",name,"!!!", file = open("history.txt","a+"))


     #rules of the game
     print("\n" + "try to guess the word...")
     print("...use only simple letters...")
     print("You want to exit at any time type -> exit")
     hangman()


     next_chance = input("\nDo you want play again? (yes(or any key)/no)")
     if next_chance == "no":
          break
     else:
          continue
         






