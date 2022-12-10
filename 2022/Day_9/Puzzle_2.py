#@title Day 9, Puzzle 2

#Import numpy
import numpy as np

#Take input
input = '''D 2
U 1
D 2
R 2
L 1
U 2
L 1
U 2
D 1
R 1
D 2
R 1
D 1
U 2
D 2
R 1
U 1
R 1
U 2
R 1
L 1
U 2
R 1
L 2
U 1
R 1
U 1
R 1
L 2
U 2
D 1
U 1
D 2
L 1
U 1
L 1
R 1
D 1
R 1
D 1
U 2
D 1
R 1
U 1
L 1
U 2
L 1
D 1
U 1
D 1
L 1
U 2
L 1
D 2
R 2
L 1
R 2
D 1
L 2
D 2
U 2
R 1
L 1
D 2
U 2
L 1
D 2
U 1
L 2
R 2
U 1
D 1
U 1
D 1
R 1
D 1
U 2
D 1
R 1
D 1
L 1
D 1
L 2
U 2
D 1
R 1
D 1
L 1
D 2
R 2
U 2
D 1
U 2
D 1
U 1
L 1
R 2
D 2
R 1
D 2
L 2
D 2
R 1
L 1
U 1
D 2
R 2
U 2
R 2
L 1
R 1
L 3
U 3
L 3
D 2
U 1
D 1
U 2
D 1
R 1
D 1
R 2
D 3
U 1
L 2
U 1
D 2
R 1
D 1
L 2
R 2
U 1
L 2
D 2
L 1
U 2
D 3
L 1
U 1
R 2
U 3
D 1
L 3
U 1
L 3
D 1
R 2
L 3
U 2
L 2
U 1
L 1
R 3
D 3
L 1
R 2
D 3
R 2
L 3
D 1
U 2
R 3
U 2
R 3
L 2
U 1
L 1
D 3
U 1
D 1
U 2
D 3
U 3
R 1
U 2
L 1
D 1
L 2
U 1
D 1
L 1
R 3
U 3
L 3
D 3
L 2
D 1
U 1
L 1
U 3
L 1
D 3
R 1
L 1
R 2
U 1
R 2
U 3
R 1
D 3
L 3
U 2
L 3
R 1
D 2
U 3
R 3
D 3
U 1
R 3
D 2
R 3
U 1
D 1
U 3
R 1
L 1
U 2
L 1
U 1
L 1
R 1
D 1
R 3
D 4
L 2
R 4
U 3
D 1
R 4
L 4
R 1
D 2
U 3
R 2
D 2
U 3
R 4
L 2
D 3
L 4
D 4
U 4
R 2
U 1
L 3
D 4
U 2
R 1
L 3
D 3
R 4
D 2
R 2
D 4
U 4
L 4
D 4
R 2
D 2
U 3
D 3
R 3
L 2
D 2
L 2
U 3
L 4
U 2
R 4
D 4
L 3
R 1
U 1
R 2
L 1
D 1
U 2
D 3
L 4
U 3
L 1
U 3
R 2
U 3
R 1
U 1
R 2
U 2
R 1
D 4
U 4
L 2
U 2
D 4
U 1
R 4
L 4
D 4
U 3
D 4
L 4
U 3
L 1
R 4
L 3
D 3
U 1
R 4
D 3
U 4
L 2
U 4
D 3
R 2
D 3
U 4
R 4
L 4
R 3
U 1
R 4
D 1
L 3
U 3
L 3
D 1
L 4
R 2
U 1
L 3
R 2
U 4
L 1
U 5
R 2
L 2
U 2
L 2
R 4
D 4
L 5
D 1
R 4
U 5
L 1
D 4
U 1
L 4
U 3
L 1
R 3
D 1
R 2
L 5
U 3
L 5
U 4
D 3
L 5
D 2
R 4
U 2
L 1
R 4
L 5
R 3
L 1
U 2
L 4
D 1
R 2
L 5
U 3
D 2
R 5
L 4
D 2
R 3
D 2
R 4
D 3
U 1
D 1
U 4
D 2
L 2
R 1
U 5
D 5
U 3
R 2
U 3
L 5
R 1
U 3
L 4
R 2
U 3
D 1
U 2
D 2
L 5
R 5
D 3
L 1
R 3
U 2
D 5
U 1
D 5
R 3
U 1
L 5
R 1
D 4
L 4
D 1
U 2
L 4
R 5
U 5
L 4
D 2
R 5
U 1
L 5
D 1
L 1
U 5
R 1
L 2
R 5
L 5
R 2
L 1
D 2
U 1
L 3
R 1
U 5
D 1
U 1
L 5
U 6
R 6
U 5
D 5
R 3
U 1
R 1
L 6
R 6
D 5
R 6
D 4
L 3
R 6
U 5
D 6
L 2
R 1
D 5
R 3
D 2
L 1
R 5
U 5
D 4
U 3
R 5
U 5
R 3
D 5
R 3
U 3
R 2
D 5
L 6
D 3
U 3
D 6
R 5
U 4
L 4
D 3
U 6
L 2
R 1
U 4
D 1
L 2
U 1
L 3
D 4
U 1
L 5
D 1
R 2
U 3
L 1
R 1
U 1
L 4
U 6
R 6
D 3
U 4
R 2
D 5
L 6
D 2
R 4
D 2
U 5
D 3
U 2
R 6
L 5
R 6
U 1
L 5
U 1
L 6
U 1
D 4
R 3
D 3
L 1
D 3
R 2
L 1
R 3
D 4
L 6
U 2
D 5
U 3
R 6
U 2
R 6
L 5
R 1
U 2
R 3
U 1
R 6
L 2
U 6
R 5
U 1
R 4
L 1
R 3
U 3
L 5
D 7
R 2
D 4
R 5
L 3
R 6
U 7
L 7
U 6
L 2
D 2
R 7
D 7
U 3
R 1
U 7
L 2
D 3
L 5
R 4
U 7
R 3
L 7
D 2
R 7
D 5
L 7
D 1
U 7
R 5
U 4
D 4
U 4
D 4
U 1
R 7
L 3
D 3
U 2
L 3
U 1
D 7
L 6
R 3
U 6
D 1
R 6
D 1
R 1
D 7
U 4
R 1
L 4
U 3
L 7
R 2
D 2
L 6
U 2
R 2
U 7
R 5
L 6
R 5
D 1
R 4
U 2
L 1
D 4
U 5
R 4
D 7
U 7
R 1
U 3
R 4
L 1
R 6
L 4
U 4
L 2
U 3
D 2
L 2
U 2
L 6
R 5
D 7
L 2
U 5
L 6
R 7
L 7
D 2
U 6
D 3
R 1
U 1
D 4
L 7
D 7
U 5
L 6
D 1
L 4
D 1
U 1
L 5
U 1
R 5
D 8
R 7
L 5
U 3
D 2
R 2
L 6
R 1
L 4
R 8
U 8
L 5
R 7
D 7
L 2
R 5
L 6
D 2
L 7
U 3
R 2
D 3
U 3
L 6
U 5
D 3
L 6
U 5
D 5
L 1
U 4
L 8
D 3
L 3
R 2
U 6
D 8
U 7
L 6
D 2
U 4
D 1
U 3
L 6
R 2
D 2
U 4
R 8
D 3
R 6
D 6
U 1
L 4
U 3
L 6
D 8
U 7
D 5
L 3
U 4
D 2
R 7
L 8
U 1
R 3
D 5
U 5
D 6
R 3
L 2
R 8
L 3
U 5
L 3
U 5
L 7
U 7
L 2
U 1
L 5
D 7
U 7
D 8
R 2
D 7
U 4
R 4
U 6
L 2
U 8
D 1
U 1
D 4
L 4
U 1
L 5
R 8
U 5
D 4
R 2
D 6
L 1
D 8
U 4
D 5
L 8
U 3
L 5
D 1
U 3
R 1
D 7
R 9
U 8
R 7
L 3
D 8
U 9
D 1
U 7
L 6
U 4
R 8
U 1
D 6
R 3
L 5
D 3
U 1
L 3
U 2
L 3
U 2
R 7
D 2
R 7
D 8
R 1
D 4
R 1
D 6
R 8
U 8
L 2
U 8
L 5
D 1
U 7
R 4
L 9
U 2
L 3
U 4
L 2
D 3
L 4
U 9
D 2
R 2
U 9
R 1
L 4
D 5
R 9
U 3
L 3
U 8
R 5
U 7
D 5
U 9
R 3
D 9
R 1
D 7
R 3
D 6
L 6
D 5
U 9
D 8
U 4
L 5
R 6
D 7
R 6
L 8
R 3
U 3
R 9
U 8
R 6
L 9
U 2
R 9
L 8
U 1
R 9
L 5
D 5
U 9
L 6
D 7
U 3
D 3
R 4
D 1
L 4
D 5
L 4
U 2
R 9
U 7
L 4
D 7
U 9
R 4
D 7
R 7
D 4
L 1
D 2
L 1
U 7
R 8
D 2
U 9
D 6
L 7
R 5
L 3
R 5
D 8
L 3
R 8
L 6
U 6
L 6
U 5
R 7
L 9
U 1
R 3
D 7
U 10
D 1
U 8
D 8
L 5
U 6
D 5
U 9
R 8
D 8
R 9
D 2
L 1
D 8
R 2
D 6
L 10
R 1
U 3
L 8
U 7
R 7
U 7
D 6
L 7
U 3
L 4
R 9
D 8
U 4
D 3
L 8
R 7
U 1
L 9
D 10
U 2
L 5
U 3
L 4
R 10
L 2
D 6
L 6
D 2
U 5
D 3
R 9
D 2
U 1
D 5
U 9
D 7
R 2
U 5
R 4
D 9
U 6
L 10
D 3
U 1
L 1
D 9
U 2
L 8
U 3
R 5
U 7
D 8
R 5
L 8
U 9
L 1
D 5
U 8
R 4
D 7
U 4
R 10
U 9
R 9
U 7
R 3
U 10
R 5
U 7
R 6
U 10
R 9
U 8
D 8
L 1
U 2
D 1
R 9
U 10
D 6
L 3
D 4
R 11
D 11
R 7
U 3
L 3
U 11
D 11
U 5
R 9
U 3
R 4
D 1
U 11
R 2
L 7
R 8
L 2
D 4
U 4
L 9
R 10
L 3
R 7
D 7
L 9
U 6
L 5
D 8
U 4
D 4
L 4
D 2
U 8
R 4
D 4
U 10
D 5
R 5
D 5
U 8
D 2
L 6
U 8
L 2
D 8
R 5
D 5
U 1
D 1
L 9
R 7
U 2
L 7
R 1
L 1
U 2
R 10
D 2
U 8
L 1
R 6
L 3
R 4
D 6
L 2
D 11
R 8
D 11
L 3
R 4
L 10
U 7
L 9
U 4
L 8
D 6
U 8
R 7
L 5
R 8
L 4
U 6
R 5
U 7
D 3
L 8
U 2
R 7
D 3
R 4
D 11
L 8
U 6
D 1
R 11
L 7
D 4
R 4
L 4
U 5
L 8
R 7
U 8
D 12
R 9
D 8
R 7
L 9
R 2
D 1
L 7
D 3
L 1
R 5
U 1
D 12
R 4
U 1
D 4
L 9
U 10
R 5
D 11
R 2
L 3
U 8
R 5
D 8
U 12
D 6
R 2
D 5
R 12
U 7
L 2
U 4
D 5
U 8
R 12
U 1
L 11
U 7
D 10
L 6
D 6
R 1
L 6
D 2
U 5
R 6
D 8
R 4
L 7
D 2
L 7
D 8
U 10
R 1
U 6
R 5
L 4
R 8
D 9
R 5
U 11
D 4
U 11
R 8
L 8
U 2
R 11
L 12
U 7
L 12
U 10
R 3
D 11
R 1
L 8
D 2
L 5
R 4
U 3
D 9
R 8
D 11
L 12
R 11
L 4
R 10
D 6
U 4
R 6
D 6
U 9
R 12
U 5
R 8
L 10
D 1
U 7
D 12
L 3
U 10
D 2
U 6
D 12
R 3
U 2
D 2
U 3
D 11
R 2
U 2
D 9
R 11
D 4
U 6
R 11
L 9
R 10
D 13
L 2
D 2
L 4
D 13
R 7
L 3
U 8
D 5
R 7
D 7
U 13
D 5
U 5
L 12
D 9
L 2
D 6
U 13
R 2
D 10
L 9
D 7
R 2
U 3
D 2
L 3
R 9
U 3
L 12
U 4
R 1
U 13
R 4
U 1
D 10
R 10
D 10
U 5
L 7
D 8
R 1
D 12
L 13
R 10
D 6
R 9
U 4
R 9
U 1
L 3
R 3
D 8
U 6
L 11
R 8
D 5
U 2
L 9
R 7
L 7
D 8
L 12
R 12
U 9
D 9
U 7
D 10
L 3
R 3
D 8
L 11
U 8
D 7
U 11
L 4
D 4
R 3
U 4
R 6
D 5
U 5
L 8
U 4
L 9
U 6
L 8
D 3
U 12
D 5
L 8
D 11
U 4
R 12
U 7
L 5
D 4
R 4
U 7
R 9
L 5
U 2
L 3
D 2
R 6
U 2
R 8
D 10
U 14
L 3
R 4
U 10
R 7
L 11
R 7
U 4
R 8
L 14
D 11
U 12
R 10
L 8
R 11
L 4
U 1
L 2
R 7
U 13
D 5
U 2
L 6
D 7
R 5
U 4
D 10
U 5
D 2
R 9
U 13
L 10
U 1
R 10
D 14
L 5
R 12
L 7
D 2
L 2
D 5
R 4
U 6
D 7
R 12
U 9
D 9
R 6
U 1
D 14
U 14
D 14
L 7
R 10
U 3
D 2
R 10
L 14
R 7
D 5
U 1
L 8
U 2
D 3
U 6
L 11
R 13
L 10
D 9
U 5
R 6
U 2
D 7
U 5
L 6
R 8
D 11
R 14
D 5
R 10
L 13
R 1
U 4
L 9
R 2
D 1
U 10
D 6
U 3
R 13
L 9
R 2
D 3
R 14
L 2
R 14
U 1
R 7
L 1
U 6
D 6
R 10
L 12
D 10
R 11
D 13
L 3
R 2
L 1
R 10
U 1
L 7
R 5
D 6
U 11
L 8
R 7
D 10
U 13
R 12
D 8
L 7
U 8
R 14
U 10
L 6
D 15
R 8
L 10
U 13
L 3
U 13
L 9
R 4
D 6
R 12
L 12
R 4
U 12
D 6
R 2
L 11
R 7
D 1
U 4
R 14
U 6
D 1
U 15
D 14
R 3
D 14
L 1
R 9
L 2
D 11
R 11
D 10
R 1
L 9
U 6
R 8
L 4
R 9
U 13
D 15
L 2
D 2
L 2
D 6
R 10
U 10
L 8
D 11
L 8
R 10
U 3
R 7
U 15
R 11
L 10
U 2
R 8
L 8
D 5
R 11
U 7
L 13
D 15
U 4
D 10
R 11
D 6
L 2
U 3
R 2
L 1
D 14
U 5
L 14
D 13
R 12
U 8
R 1
L 14
U 6
D 10
R 3
U 8
L 2
R 6
D 10
U 9
L 2
D 13
L 13
D 9
L 10
U 14
R 11
L 14
U 10
L 6
D 14
L 11
R 4
L 9
U 3
D 13
L 5
R 16
U 3
L 9
D 6
R 15
U 6
L 4
R 10
D 12
R 4
D 2
U 11
D 13
R 6
U 15
R 14
D 14
U 8
R 9
L 5
D 16
U 9
R 15
D 13
R 3
L 2
R 3
U 14
D 9
U 2
D 6
U 9
D 7
L 13
D 7
L 5
R 3
U 2
L 13
R 9
D 1
L 16
D 8
R 12
U 15
R 4
D 15
L 12
D 13
R 4
L 2
U 5
R 13
L 15
D 12
L 3
D 13
L 5
D 16
L 11
D 13
U 1
D 9
L 10
U 11
D 12
U 11
D 14
U 16
D 14
U 10
R 7
L 11
R 14
U 11
R 5
U 1
D 16
R 16
L 9
U 7
D 7
R 8
D 7
U 10
L 7
D 6
U 4
D 2
L 3
D 3
L 2
R 3
L 9
D 2
R 12
D 11
U 11
L 14
U 4
L 12
R 13
L 9
D 11
R 12
L 15
R 15
L 15
R 16
U 17
D 4
L 9
U 9
D 17
L 8
U 15
D 17
U 9
R 4
U 6
L 1
D 7
R 3
D 11
L 10
R 1
U 14
D 13
R 7
L 8
U 16
L 16
U 12
D 3
R 4
D 8
R 8
D 1
L 12
R 16
D 3
R 7
D 16
U 11
R 6
D 13
R 4
L 3
R 6
U 1
R 4
D 4
U 13
L 7
D 17
R 4
D 6
L 1
U 17
L 16
U 12
L 11
R 1
L 11
D 8
U 15
D 6
L 5
U 16
R 6
D 11
L 17
D 7
L 1
D 8
L 16
U 8
R 4
L 17
D 2
L 1
U 16
D 8
L 17
U 12
D 4
R 1
D 12
U 2
L 11
U 17
L 3
R 7
L 10
U 16
R 8
U 6
L 3
D 15
L 11
R 7
U 14
R 8
L 9
D 6
L 3
U 17
R 1
D 13
U 15
L 18
U 11
R 3
U 16
D 12
R 1
D 6
L 17
R 9
L 6
U 2
D 2
U 16
D 12
R 1
U 17
R 16
D 12
U 3
D 11
L 13
U 11
R 15
U 13
D 11
U 8
L 3
D 1
L 7
R 9
D 18
R 17
U 2
L 16
D 8
L 14
D 11
R 4
D 12
U 5
D 6
U 2
D 4
L 1
R 11
D 3
U 10
L 1
R 16
U 10
L 17
D 5
R 16
U 18
R 1
D 16
R 14
D 11
U 13
D 13
R 5
L 9
U 11
R 18
L 14
U 14
L 18
R 15
D 10
U 10
R 17
U 12
L 2
D 11
R 15
U 3
R 17
L 1
R 1
U 1
L 8
U 15
R 15
L 12
U 2
R 1
L 9
R 3
L 6
R 18
D 9
R 12
U 6
L 17
R 11
D 8
R 17
D 12
L 2
R 9
U 4
D 17
R 18
D 12
L 9
R 16
U 5
R 1
L 12
R 9
L 8
U 8
R 2
U 9
L 2
D 18
U 11
L 17
U 3
L 11
R 3
L 5
D 1
R 4
U 10
D 18
R 10
D 10
L 5
R 7
D 2
R 2
L 18
U 4
D 10
U 16
D 1
L 2
U 17
D 5
U 9
R 13
D 6
R 14
D 10
L 15
R 13
L 6
U 11
R 6
L 4
R 19
L 4
D 13
R 1
L 9
D 4
R 12
U 18
D 3
U 17
R 19
L 6
R 6
D 8
R 12
L 10
R 3
U 5
L 2
D 7
L 9
D 16
L 16
U 14
L 12
R 2
L 17
R 18
D 12
R 16
D 19
U 6
D 19
U 13
R 4
D 18
L 14
U 14
D 12
R 10
L 13
D 10
U 10
D 2
U 18
L 19
R 15
D 6
L 1
D 10
R 7
D 2
R 19
D 5
U 19
L 13
U 17
L 3
R 19
U 9
L 7
D 6
R 12
L 10
R 9
D 9
U 13
R 7
L 1
U 1
D 17'''

import numpy as np

#Split input into list of instructions
instructions = input.split('\n')


#Find size of array needed

#Set initial distances to 0
width=0
max_r=0
max_l=0
height=0
max_u=0
max_d=0

#Repeat for each instruction
for i in instructions:

  #If it moves right
  if 'R' in i:
    
    #Add the number of steps to right
    width += int(i[2:])

    #If that's the max width reached update accordingly
    if width> max_r:
      max_r = width

  #If it moves up
  if 'U' in i:
    
    #Add the number of steps to height
    height += int(i[2:])

    #If that's the max height reached update accordingly
    if height> max_u:
      max_u = height

  #If it moves left
  if 'L' in i:
    
    #Subtract the number of steps from width
    width += - int(i[2:])

    #If that's the min width reached update accordingly
    if width< max_l:
      max_l = width

  #If it moves down
  if 'D' in i:
    
    #Subtract the number of steps from height
    height += -int(i[2:])

    #If that's the max height reached update accordingly
    if height< max_d:
      max_d = height

total_width = max_r - max_l
total_height = max_u - max_d

#Make 11 zero arrays, one for the head, 9 for the 9 knot tail and one for where knot 9 has been with an extra border of 0
head = np.zeros((total_height+3,total_width+3),int)
tail_1 = np.zeros((total_height+3,total_width+3),int)
tail_2 = np.zeros((total_height+3,total_width+3),int)
tail_3 = np.zeros((total_height+3,total_width+3),int)
tail_4 = np.zeros((total_height+3,total_width+3),int)
tail_5 = np.zeros((total_height+3,total_width+3),int)
tail_6 = np.zeros((total_height+3,total_width+3),int)
tail_7 = np.zeros((total_height+3,total_width+3),int)
tail_8 = np.zeros((total_height+3,total_width+3),int)
tail_9 = np.zeros((total_height+3,total_width+3),int)
trail = np.zeros((total_height+3,total_width+3),int)

#Put head and tails where theres max_l columns to the left and max_u rows above and then the buffer
head[max_u+1][- max_l+1]=1
tail_1[max_u+1][- max_l+1]=1
tail_2[max_u+1][- max_l+1]=1
tail_3[max_u+1][- max_l+1]=1
tail_4[max_u+1][- max_l+1]=1
tail_5[max_u+1][- max_l+1]=1
tail_6[max_u+1][- max_l+1]=1
tail_7[max_u+1][- max_l+1]=1
tail_8[max_u+1][- max_l+1]=1
tail_9[max_u+1][- max_l+1]=1
trail[max_u+1][- max_l+1]=1

#Define a function to move the tail
def move_tail(head,tail):

  #Check if you need to move tail
  new_position = np.where(head == 1)
  x=new_position[1][0]
  y=new_position[0][0]
  
  if tail[y][x]==0 and tail[y][x+1]==0 and tail[y][x-1]==0 and tail[y+1][x]==0 and tail[y+1][x+1]==0\
  and tail[y+1][x-1]==0 and tail[y-1][x]==0 and tail[y-1][x+1]==0 and tail[y-1][x-1]==0:
    
    #Increase move by 1 to indicate it moved
    global move
    move += 1

    #If tail not touching head then figure out which corner is touching and move there
    tail_position = np.where(tail == 1)
    p=tail_position[1][0]
    q=tail_position[0][0]
       
    #If differncee in x direction is positive and y direction is negative, then move up and right
    if x - p >0 and  y - q <0:
      tail[q][p]=0
      tail[q-1][p+1]=1

    #If differncee in x direction is positive and y direction is positive, then move down and right
    if x - p >0 and  y - q >0:
      tail[q][p]=0
      tail[q+1][p+1]=1

    #If differncee in x direction is negative and y direction is positive, then move down and left
    if x - p <0 and  y - q >0:
      tail[q][p]=0
      tail[q+1][p-1]=1
  
    #If differncee in x direction is negative and y direction is negative, then move up and left
    if x - p <0 and  y - q<0:
      tail[q][p]=0
      tail[q-1][p-1]=1

    #If differncee in x direction is 0 and y direction is negative, then move up
    if x - p ==0 and  y - q <0:
      tail[q][p]=0
      tail[q-1][p]=1

    #If differncee in x direction is 0 and y direction is positive, then move down
    if x - p ==0 and  y - q >0:
      tail[q][p]=0
      tail[q+1][p]=1

    #If differncee in x direction is positive and y direction is 0, then move right
    if x - p >0 and  y - q ==0:
      tail[q][p]=0
      tail[q][p+1]=1
  
    #If differncee in x direction is negative and y direction is 0, then move left
    if x - p <0 and  y - q==0:
      tail[q][p]=0
      tail[q][p-1]=1


#Repeat for each instruction
for i in instructions:

  #Check number of steps
  steps = int(i[2:])

  #Repeat for each step
  for s in range(steps):

    #Find current position of head
    position = np.where(head == 1)

    #Move head one step in correct direction
    if 'R' in i:
      head[position[0][0]][position[1][0]]=0
      head[position[0][0]][position[1][0]+1]=1

    if 'L' in i:
      head[position[0][0]][position[1][0]]=0
      head[position[0][0]][position[1][0]-1]=1

    if 'U' in i:
      head[position[0][0]][position[1][0]]=0
      head[position[0][0]-1][position[1][0]]=1

    if 'D' in i:
      head[position[0][0]][position[1][0]]=0
      head[position[0][0]+1][position[1][0]]=1
    
    #Set move = 0
    move=0

    #Move tail 1
    move_tail(head,tail_1)

    #If tail 1 moved, move tail 2 
    if move==1:
      move_tail(tail_1,tail_2)

    #If tail 2 moved, move tail 3
    if move==2:
      move_tail(tail_2,tail_3)

    #If tail 3 moved, move tail 4
    if move==3:
      move_tail(tail_3,tail_4)

    #If tail 4 moved, move tail 5
    if move==4:
      move_tail(tail_4,tail_5)

    #If tail 5 moved, move tail 6
    if move==5:
      move_tail(tail_5,tail_6)

    #If tail 5 moved, move tail 7
    if move==6:
      move_tail(tail_6,tail_7)

    #If tail 7 moved, move tail 8
    if move==7:
      move_tail(tail_7,tail_8)

    #If tail 8 moved, move tail 9
    if move==8:
      move_tail(tail_8,tail_9)

      #Update trail
      position = np.where(tail_9==1)
      trail[position[0][0]][position[1][0]]=1


#Find number of positions in trail
columns = sum(trail)
total=sum(columns)
print(total)
