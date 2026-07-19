player1 = input("rock ,paper or scissors: ")
player2 = input("rock,paper or scissors: ")

if(player1 == 'rock'  and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper' or player1 == 'paper' and player2 == 'rock'):
	print("player1 wins")

elif(player2 == 'rock'  and player1 == 'scissors' or player2 == 'scissors' and player1 == 'paper' or player2 == 'paper' and player1 == 'rock'):
	print("player2 wins")

elif(player1 == player2):
	print("tie")


