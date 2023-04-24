# cng-462--AI

Submitted by:
Hevra Petekkaya     2456200
Noor Ul Zain            2528644
Submission contents
Version1.py ->    simple version of UCS and A* 
Version2.py ->   UCS, BFS and A* implemented for Maze read from a .txt file

Read_ME  ->     explanations and output screenshots

maze.txt
maze2.txt           Test cases for Version2.py 
maze3.txt
maze4.txt 


Version2 Details
Constructing the Dictionary Graph Given the Maze

To start with, the maze is represented in a Txt file. The '*' represents a pathway: meaning that one can travel from point A to its neighbor point B. On the other hand, '#' represents a wall: meaning that one can not travel from point A to its neighbor point B. 

E.g. of a Txt file with a maze:

Maze2.txt file
0#1*3#4                            
**#****
6*5#2*3
***##**
9*8#9*3

start: (0,2)
end:   (4,6)


The below figure is the graphical representation of the above maze. Note that the starting point is (0,2). That might appear to be '3' that is on the zeroth row at first sight; however, we are counting the characters '*' and '#' as well so that also take up space.  Hence, '1' is located in the zeroth row, but third column because '0' is in the zeroth column, the wall, '#', is in the second column, and '1' is in the third column, whose index is 2. The same argument holds for the endpoint, which is at (4,6). The row is 4 because, in the zeroth row, there is '0'. In the first row, there is '*' meaning that there is no wall between '0' and '6'. In the second row, there is '6'. In the third row, there is '*' meaning that there is no wall between '6' and '9'. Finally, the fourth row has 
[9*8#9*3]. The sixth column of the fourth row is '3'. 



As another example, the below file and its corresponding graphical visualization can be inspected. In this case, unlike the above one, there are several paths possible to reach from teh start to the end. However, the A* will find the one with the minimum cost, which is Solution Path:   (10, 0)-> (8, 0)-> (6, 0)-> (4, 0)-> (2, 0)-> (2, 2)-> (2, 4)-> (2, 6)-> (2, 8)-> (2, 10)  with total cost 34.0. It is worth emphasizing again that coordinates (10, 0), (8, 0) might not seem to be existent; however, in our implementation, let's keep in mind that the characters also take up space. Hence, the starting point '5', which can be found in the graphical representation below, has coordinates (10, 0).  The solution, which is the optimal path, follows an upward path followed by turning rightwards that is towards the endpoint. All the other possible paths have a cost that is higher than 34.0. 

Maze.txt file
2*3*2#6*8*9
*##********
1*4*8*0*6*2
***********
3*5*8*4*6#1
**#********
4*0#2*3*9#2
*#******#**
6#8*9*1#2*0
***********
5#3*6*2#3*4
******#****
6*3*5*6*9*1

start: (10,0)
end:   (2,10)






