
#Program for tic tac toe

import random
import sys

wins = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
biased = [[4, 7, 8], [4, 6, 7], [2, 4, 5], [0, 1, 4], [0, 3, 4], [1, 2, 4], [3, 4, 6], [0, 2, 8], [0, 2, 6], [0, 6, 8], [2, 6, 8], [4, 6, 8], [2, 4, 8], [0, 4, 6], [0, 2, 4]]

index_available = [0, 1, 2, 3, 4, 5, 6, 7, 8]
index_human = []
index_bot = []

turn = int(random.randrange(0, 2))

for i in range(9):
	if turn%2==0:
		#human

		print("Your Turn - ")
		option = int(input("Choose an index - \n0 1 2\n3 4 5\n6 7 8\n"))
		index_available.remove(option)
		index_human.append(option)

		#Checking for the win
		for i in range(len(wins)):
			count = 0
			for j in range(3):
				for k in range(len(index_human)):
					if(index_human[k] == wins[i][j]):
						count += 1
						break
				if count==0:
					break
				elif j==2 and count==3:
					print("User wins.")
					sys.exit(1)

		turn += 1
	else:
		#bot
		option = -1
		#the last winning move
		if len(index_bot)>1:
			track = 0
			for i in range(len(wins)):
				count = 0
				notin = -1
				if track==1:
					break		
				for j in range(len(wins[i])):
					count1 = 0
					count2 = 0
					for k in range(len(index_bot)):
						if index_bot[k]==wins[i][j]:
							count1 +=1
					if count1!=0:
						count += 1
					for k in range(len(index_available)):
						if index_available[k]==wins[i][j]:
							count2 +=1
					if count1==0 and count2!=0:
						notin = wins[i][j]
					elif j==2 and count==2 and notin!=-1:
						option = notin
						track = 1
						break
			print("Option is"  +str(option))
		if option==-1:
			#Preventing the win			
			check_list = {}
			for i in range(len(wins)):
				count = 0
				for j in range(len(wins[i])):
					for k in range(len(index_human)):
						if wins[i][j] == index_human[k]:
							count += 1

				check_list[str(wins[i])] = count

			check_list_keys = list(check_list.keys())
			check_list_values = list(check_list.values())
			new_list = []
			for i in range(len(check_list_keys)):
				if check_list_values[i] == max(check_list_values):
					for j in check_list_keys[i]:						
						try:
							new_list.append(eval(str(j)))
							#print(new_list)
						except:
							pass
			new_list = list(set(new_list))
			for i in index_human:
				try:				
					new_list.remove(i)
				except:
					pass
			
			for i in index_bot:
				try:			
					new_list.remove(i)
				except:
					pass

			if len(new_list)!=0:
				option = random.choice(new_list)
			else:
				option = random.choice(index_available)
		
		print("Computer's Turn - " + str(option))
		index_available.remove(option)			
		index_bot.append(option)

		#Checking for the win
		for i in range(len(wins)):
			for j in range(3):
				if index_bot.count(wins[i][j])==0:
					break
				elif j==2:
					print("Cpu win")
					sys.exit(1)
		turn += 1
