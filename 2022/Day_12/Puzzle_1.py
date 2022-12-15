#@title Day 12, Puzzle 1

#In theory this works but it took too long to run so I just hand drew the best route on the map


#Import numpy
import numpy as np

#Take input
input = '''abcccccccccaaaaaaaaaaccccccccccccaaaaaaaaccaaccccccccccccccccccccccccccccccccccccccccccccaaaaaa
abccccccccccaaaaaaaaaccccccccccccaaaaaaaaaaaacccccccccccaacccacccccccccccccccccccccccccccaaaaaa
abcccccccccccaaaaaaacccccccccccccaaaaaaaaaaaaaacccccccccaaacaacccccccccaaaccccccccccccccccaaaaa
abccccccccccaaaaaaccccccccccccccaaaaaaaaaaaaaaaccccccccccaaaaaccccccccccaaacccccccccccccccccaaa
abccccccccccaaaaaaaccccccccccccaaaaaaaaaaaaaacccccccccccaaaaaacccccccccaaaacccccccccccccccccaac
abaaccaaccccaaccaaaccccccccaaaaaaaaaaaaaaacaaccccccccccaaaaaaaacccccccccaaalcccccccccccccccaaac
abaaaaaacccccccccaaccccccccaaaaaacccaaaacccaaccccccccccaaaaaaaaccccccccalllllllcccccccccccccccc
abaaaaaacccccccaaacccccccccaaaaccccccaaaccccaaaaacccccccccaacccccccaaaakllllllllcccccccaacccccc
abaaaaaacccccccaaaacccccccccaacccccccaaaccccaaaaacccccccccaacccccccaakkklllpllllccccacaaacccccc
abaaaaaaaccccccaaaaccccaaccccccccccccccccccaaaaaaccccccccccccccccccckkkkpppppplllcccaaaaaaacccc
abaaaaaaacaaaccaaaaccaaaaaaccccccccccccccccaaaaaacccccccaaaccccckkkkkkkpppppppplllcddaaaaaacccc
abcaaaacccaacccccccccaaaaaacccccaaaccccccccaaaaaacccccccaaaaccjkkkkkkkpppppuppplmmdddddaaaccccc
abccaaaaaaaaaccccccccaaaaaaccccaaaaaacccccccaaacccccccccaaaajjjkkkkkrpppuuuuupppmmmdddddacccccc
abccccaaaaaaaacccccccaaaaacccccaaaaaacccccccccccccccccccaaacjjjjrrrrrrppuuuuupqqmmmmmddddaccccc
abccccaaaaaaaaacccccccaaaacccccaaaaaaccccccccccccccccccccccjjjrrrrrrrrpuuuxuvvqqqmmmmmddddccccc
abccccaaaaaaaaacccccccccccccccccaaaaaccccaacccaccccccccaaccjjjrrrruuuuuuuxxyvvqqqqqmmmmmdddcccc
abccccaaaaaaaacccccccccaaaccccccaacaaccccaaacaacccaaacaaaccjjjrrrtuuuuuuuxxyvvvqqqqqmmmmdddcccc
abccaaaaaaaacccccccccccaaaaaccccccccccccccaaaaacccaaaaaaaccjjjrrttttxxxxxxyyvvvvvqqqqmmmmdeeccc
abccaaaccaaaccccccccaacaaaaacccccccccccccaaaaaacccaaaaaacccjjjrrtttxxxxxxxyyvvvvvvvqqqmmmeeeccc
abaaaaaaaaaacccaaaccaaaaaaaaaaaccaaaccccaaaaaaaacccaaaaaaaajjjqqrttxxxxxxxyyyyyyvvvqqqnnneeeccc
SbaaaaaaaaccccaaaaccaaaaaaaaaaaaaaaaacccaaaaaaaaccaaaaaaaaacjjjqqtttxxxxEzzyyyyvvvvqqqnnneeeccc
abcaaaaaacccccaaaaccccaaaaaaaccaaaaaaccccccaaccccaaaaaaaaaaciiiqqqtttxxxyyyyyyvvvvrrrnnneeecccc
abcaaaaaacccccaaaacccaaaaaaaaccaaaaaaccccccaaccccaaacaaacccciiiqqqqttxxyyyyyywvvvrrrnnneeeecccc
abcaaaaaaccccccccccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqtttxxyyyyyywwrrrrnnnneeeccccc
abcaaacaacccccaacccccaaaaaaaaacaaaaacccccccccccccccccaaaccccciiiqqttxxxywwyyywwrrrnnnneeecccccc
abccccccccaaacaaccccccccccacccccccccccccccccccccccccccccccccciiqqqttxxwwwwwwywwrrrnnneeeccccccc
abccaacccccaaaaaccccccccccccccccccccccccccccccccccccccccaacaaiiqqqttwwwwsswwwwwrrrnnfffeccccccc
abaaaaccccccaaaaaacccccccccccccccccccccccccccccaaaccccccaaaaaiiqqqttssssssswwwwrrronfffaccccccc
abaaaaaacccaaaaaaacccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqssssssssssswrrrooofffaaaacccc
abaaaaaaccaaaaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiiqqqppssspppssssrrrooofffaaaacccc
abaaaaaaccaacaaacccccccccccccccccccccccccccccaaaaaacccccaaaaaiihpppppppppppossrrooofffaaaaacccc
abaaaaccccccccaacccccccccccccccccccccccccccccaaaaaccccccccaaahhhhppppppppppoooooooofffaaaaccccc
abaaaaccccccccccaacccccccccccccccccaaacccccccaaaaacccccccccccchhhhhhhhhhggpoooooooffffaaaaccccc
abccaacccccccacaaaccccccccccccccccaaaaacccccccccccccccccccccccchhhhhhhhhggggoooooffffaacaaacccc
abccccccccccaaaaacaaccccccccccccccaaaaaccccccccccccccccccccccccchhhhhhhhggggggggggffcaacccccccc
abccccccccccaaaaaaaaccccccccccccccaaaacccaacccccccccccaccccccccccccccaaaaaggggggggfcccccccccccc
abccccccccccccaaaaaccccaacccccccccaaaacaaaaccccccccaaaaccccccccccccccaaaacaaagggggcccccccccaccc
abcccccccccccaaaaacccccaacccccccccaaaaaaaaaccccccccaaaaaaccccccccccccaaaccaaaacccccccccccccaaac
abcccccccccccaacaaccaaaaaaaacccaaaaaaaaaaaccccccccccaaaaccccccccccccccaccccaaacccccccccccccaaaa
abccccccccccccccaaccaaaaaaaaccaaaaaaaaaaaccccccccccaaaaacccccccccccccccccccccacccccccccccccaaaa
abccccccccccccccccccccaaaaacccaaaaaaaaaaaacccccccccaacaacccccccccccccccccccccccccccccccccaaaaaa'''

#Split input into a grid of numbers corresponding to height
rows=input.split('\n')
grid=np.array([[ord(x)-ord('a')+1 for x in y] for y in rows])

#Identify start and end positions
start= np.where(grid == ord('S')-ord('a')+1)
end= np.where(grid == ord('E')-ord('a')+1)

#Set start and end points to have values 1 and 26
grid[start[0][0]][start[1][0]]= 1
grid[end[0][0]][end[1][0]]= 26

#Create variable for min path length (shortened for run)
#min_path = grid.shape[0] * grid.shape[1]
min_path = 421
iteration = 0

#Define function to find paths
def find(s,path):

  #Make min_path a global variable
  global min_path
  global iteration
  iteration = iteration + 1
  if ((iteration % 1000000) == 0):
    print(iteration, min_path, s, len(path) , path)
  
  #If current point is end point and path length is less than min_path
  if s == [end[0][0],end[1][0]] and len(path)<min_path:

    #Update min_path
    min_path = len(path)
    return

  #If current path longer than min_path stop
  if len(path) >= min_path:
    return

  #If current position already in path then stop
  if s in path:
    return

  #If you can move up move up
  if s[0]>0 and grid[s[0]-1][s[1]] <= grid[s[0]][s[1]]+1:

    #Make copies of path and s
    new_path=[x for x in path]
    new_s = [x for x in s ]

    #Add elements of new_s to new_path
    new_path.append([x for x in new_s])

    #Update new_s
    new_s[0]= new_s[0]-1

    #Repeat from new position
    find(new_s,new_path)

  #If you can move right move right
  if s[1]< grid.shape[1]-1 and grid[s[0]][s[1]+1] <= grid[s[0]][s[1]]+1:

    #Make copies of path and s
    new_path=[x for x in path]
    new_s = [x for x in s ]

    #Add elements of new_s to new_path
    new_path.append([x for x in new_s])

    #Update new_s
    new_s[1]= new_s[1]+1

    #Repeat from new position
    find(new_s,new_path)

  #If you can move down move down
  if s[0]< grid.shape[0]-1 and grid[s[0]+1][s[1]] <= grid[s[0]][s[1]]+1:

    #Make copies of path and s
    new_path=[x for x in path]
    new_s = [x for x in s ]

    #Add elements of new_s to new_path
    new_path.append([x for x in new_s])

    #Update new_s
    new_s[0]= new_s[0]+1

    #Repeat from new position
    find(new_s,new_path)

  #If you can move left move left
  if s[1]>0 and grid[s[0]][s[1]-1] <= grid[s[0]][s[1]]+1:

    #Make copies of path and s
    new_path=[x for x in path]
    new_s = [x for x in s ]

    #Add elements of new_s to new_path
    new_path.append([x for x in new_s])

    #Update new_s
    new_s[1]= new_s[1]-1

    #Repeat from new position
    find(new_s,new_path)


#Run function with starting values and an empty path
find([start[0][0],start[1][0]],[])

#Print the minimum path length
print(min_path)
