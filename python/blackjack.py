import random

#                                        J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(cards) # To see the list before being shuffled

random.shuffle(cards)

print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player card: ' + str(player_card1))
print('Computer card:  ' + str(computer_card1))

print(cards) # To see the list after two cards have been popped off.
#decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if (str(decision )== 'h'):
    player_card2 = cards.pop()
    print( "player card : " + str(player_card1) + "," + str(player_card2))
elif (str(decision) == 's'):
    player_card2 = 0;
    print( "player card : " + str(player_card1) + "," + str(player_card2))
else:
    print("enter the valid decison")

computer_card2 = cards.pop()

print ("Computer card: " + str(computer_card1) + "," + str(computer_card2))

decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

# Round 3

if( str(decision) == 'h'):
    player_card3 = cards.pop()
    print( "player card : " + str(player_card1) + "," + str(player_card2) + "," + str(player_card3))
elif (str(decision) == 's'):
    player_card3 = 0
    print( "player card : " + str(player_card1) + "," + str(player_card2) + "," + str(player_card3))
else:
    print("Enter a valid decision")

computer_total = computer_card1 + computer_card2
if(computer_total < 16):
    computer_card3 = cards.pop()
else:
    computer_card3 = 0
print( "computer card : " + str(computer_card1) + "," + str(computer_card2) + "," + str(computer_card3))

#Results

print("Game Over!!!")

player_sum = player_card1 + player_card2 + player_card3
computer_sum = computer_card1 + computer_card2 + computer_card3

if((player_sum > 21) and (computer_sum > 21)):
    print("Tie , Both Player and Computer got busted")
elif(player_sum == computer_sum):
    print("Tie!!!")
elif(computer_sum > 21):
    print("Player Won !!! Computer Busted")
elif(player_sum > 21):
    print("Computer won !!! Player Busted")
elif( player_sum > computer_sum):
    print("Player Won , Closer to 21")
else:
    print("Computer Won , Closer to 21")
