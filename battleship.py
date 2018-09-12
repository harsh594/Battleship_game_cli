import winsound
fname = "F:\\Spit.wav"
y=1
while(y==1):
 print('''welcome to Batlleship game 
      Choose game mode:
      Easy -Press:1(1 battle ship in sea :3 chances to sink it)
      Medium -Press:3(3 battle ships in sea :5 chances to sink it)
      Hard -Press:5(5 battle ships in sea:7 chances to sink it)
      ''')
 u=True   
 while u:
     try:
      n=int(input("Enter your Choice\n"))
      u=False
     except ValueError:
      print("wrong entry choice : enter 1(easy),3(medium) or 5(hard) and try again")
      continue
     if n==3 or n==1 or n==5:
         break
     else:
      print("wrong entry choice : enter 1(easy),3(medium) or 5(hard) and try again")    
      u=True
 print("TIP:1 Sink the battleship hidden in the sea by entering values\nTIP:2 Enter values ranging from 0 to 4 for guessing the row and column")    
 u=True
 while(u):
    try:
      o=input("Press enter to continue:")
      u=False
    except ValueError:
       print("Error! Press only enter please")
       continue
    if o=="":
      break
    else:
       print("Error!Press only enter please") 
       u=True
 q=n+3
 from random import randint

 board = []

 for x in range(0, 5):
    board.append(["O"] * 5)
 #print(board)
 def print_board(board):
    for row in board:
        
        print((" ".join(row).center(70)))
        
 print("\t \t \t INITIAL BATTLEFIELD")
 print_board(board)

 def random_row(board):
    return randint(0, len(board) - 1)

 def random_col(board):
    return randint(0, len(board[0]) - 1)
 def check_already_sinked(z):
    for e in a:
         if z==e:
            print("OOPS!you Already sank that ship.Turn not counted")
            return True
    return False     

 l=[]
 for i in range(0,n):   
    ship_row = random_row(board)
    ship_col = random_col(board)
    for j in l:
        while([ship_row,ship_col]==j):#tuple  can have only one argument thtas wwhy multiple brackets
           ship_row = random_row(board)
           ship_col = random_col(board)
            
    l.append([ship_row,ship_col])
# print(l)    
 a=[]    
 x=1
 while(x<q):
     
     print(" \tChance no. %s" % (x))
     t=True
     while(t):
      try:         
       guess_row = int(input("guess_row"))
       
       guess_col = int(input("guess_col"))
       t=False
      except ValueError:
       print("Wrong entry choice : Guess Row And Column Again")
       continue
     if(guess_row not in range(len(board)) or guess_col not in range(len(board[0]))): 
      print("OOPS! SHIP NOT EVEN IN THE OCEAN! Turn not counted\n")
      continue
     if check_already_sinked([guess_row,guess_col])==True:
      continue
    
         
     for k,p in enumerate(l,1): 
       # print(p)
      
      
        if[guess_row,guess_col]!=p and k<len(l):
          continue
          
        if(k<=len(l) and [guess_row,guess_col]==p):
    
             
         x+=1
         board[guess_row][guess_col] = "X"
         a.append([guess_row,guess_col])
        # print(a)
         print_board(board)
         print("Congratulations! You sank NO. %s battleship! \n"%(k))
      
         break 
        else: 
         x+=1   
         print_board(board)
         print("You missed my battleship!\n \n")
         winsound.PlaySound(fname, winsound.SND_FILENAME)
         break
 print("FINAL RESULT:")
 print("you sank %s ships out of %s ships"%(len(a),n))
 print_board(board) 
 print(" WANT TO PLAY AGAIN???? PRESS 1 if yes or 2 to exit")
 s=True
 while s:
  try: 
     y=int(input())
     s=False
  except ValueError:
      print("ERROR! press 1 to play again AND 2 to Exit")
      continue
  if y==1 or y==2:
      break 
  else:
      print("ERROR! press 1 to play again AND 2 to Exit")
      s=True
  
      
print("Thanks for playing") 
         
          
     
    