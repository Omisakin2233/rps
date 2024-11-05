import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper , scissors ]

my_choice = int(input ("what do you want to choose  0 for rock 1 for paper and 2 for scissors " ))

if my_choice == 0 :
    print (" you choose rock")
    print(game[my_choice])
elif my_choice == 1 :
    print (" you choose paper ")
    print (game [my_choice])
elif my_choice == 2:
    print ("you choose scissors ")
    print (game [my_choice])
else:
    print ("wrong number or  invalid ")


computer_choice = random.randint(0,2)
if computer_choice == 0:
    print ("computer choose rock")
    
elif computer_choice == 1:
    print ("computer choice paper ")
    
elif computer_choice == 2:
    print ("computer choice scissors ")

print (game [computer_choice])



if my_choice == computer_choice:
    print ("draw")
elif  my_choice == 0 and computer_choice == 2:
    print ("user win ")
elif my_choice == 1 and computer_choice ==1:
    print ("user_win")
elif my_choice >= 3:
    print ("wrong inpute")
elif  my_choice == 2 and computer_choice == 1 :
    print ("the computer wins loser ")
elif my_choice == 1 and computer_choice == 2 :
    print ("computer wins loser ") 
elif my_choice == 2 and computer_choice == 0 :
    print ("computer wins ")   
elif my_choice == 1 and computer_choice == 0 :
    print ("you win ") 
elif my_choice == 0 and computer_choice == 1 :
    print ("computer wins ")    
else :
    print ("invalid ")    


#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.



