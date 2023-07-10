def constboard(board):
  print("Current state of board: \n\n")
  for i in range(0,9):
    if ((i>0) and (i%3==0)):
      print("\n");
    if (board[i]==0):
      print("_",end=" ");
    if (board[i]==-1):
      print("X ",end=" ");
    if (board[i]==1):
      print("O ",end=" ");
  print("\n\n");
def user1turn(board):
  pos=input("Enter X position from 1 to 9");
  pos=int(pos);
  if (board[pos-1]!=0):
    print("Wrong move!")
    exit(0);
  board[pos-1]=-1;
def user2turn(board):
  pos=input("Enter O position from 1 to 9");
  pos=int(pos);
  if (board[pos-1]!=0):
    print("Wrong move!")
    exit(0);
  board[pos-1]=1;
def analyzeboard(board):
  cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in range(0,8):
    if (board[cb[i][0]!=0] and board[cb[i][0]]==board[cb[i][1]] and
        board[cb[i][0]]==board[cb[i][2]]):
      return board[cb[i][0]];
  return 0;
def minmax(board,player):
  x=analyzeboard(board);
  if (x!=0):
    return (x*player);
  pos=-1;
  value=-2;
  for i in range(0,9):
    if (board[i]==0):
      board[i]=player;
      score=-minmax(board,player*-1);
      board[i]=0;
      if (score>value):
        value=score;
        pos=i;
  if (pos==-1):
      return 0;
  return value;

def compturn(board):
  pos=-1;
  value=-2;
  for i in range(0,9):
    if (board[i]==0):
      board[i]=1;
      score=-minmax(board,-1);
      board[i]=0;
      if (score>value):
        value=score;
        pos=i;
  board[pos]=1;



def main():
  choice=input("Enter 1 for single player and 2 for multiplayer:")
  choice=int(choice);
  board=[0,0,0,0,0,0,0,0,0]
  if (choice==1):
    print("computer:0 vs you: 1");
    player=input("Enter to play 1(1st) or 2(2nd)");
    player=int(player);
    for i in range(0,9):
      if (analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        compturn(board);
      else:
        constboard(board);
        user1turn(board);
  else:
     for i in range(0,9):
      if (analyzeboard(board)!=0):
        break;
      if(i%2==0):
        compturn(board);
      else:
        constboard(board);
        user1turn(board);
  x=analyzeboard(board);
  if (x==0):
    constboard(board);
    print("Draw!")
  if (x==-1):
    constboard(board);
    print("Player X Wins O loses!")
  if (x==1):
    constboard(board);
    print("Player O wins Player X loses!")


