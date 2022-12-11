#@title Day 10, Puzzle 2

#import numpy
import numpy as np

#Take input
input = '''noop
noop
noop
addx 6
addx -1
addx 5
noop
noop
noop
addx 5
addx -8
addx 9
addx 3
addx 2
addx 4
addx 3
noop
addx 2
noop
addx 1
addx 6
noop
noop
noop
addx -39
noop
addx 5
addx 2
addx -2
addx 3
addx 2
addx 5
addx 2
addx 2
addx 13
addx -12
noop
addx 7
noop
addx 2
addx 3
noop
addx -25
addx 30
addx -10
addx 13
addx -40
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 3
addx -2
addx 3
addx -1
addx 7
noop
noop
addx 5
addx -1
addx 6
noop
noop
noop
noop
addx 9
noop
addx -1
noop
addx -39
addx 2
addx 33
addx -29
addx 1
noop
addx 4
noop
noop
noop
addx 3
addx 2
noop
addx 3
noop
noop
addx 7
addx 2
addx 3
addx -2
noop
addx -30
noop
addx 40
addx -2
addx -38
noop
noop
noop
addx 5
addx 5
addx 2
addx -9
addx 5
addx 7
addx 2
addx 5
addx -18
addx 28
addx -7
addx 2
addx 5
addx -28
addx 34
addx -3
noop
addx 3
addx -38
addx 10
addx -3
addx 29
addx -28
addx 2
noop
noop
noop
addx 5
noop
addx 3
addx 2
addx 7
noop
addx -2
addx 5
addx 2
noop
addx 1
addx 5
noop
noop
addx -25
noop
noop'''

#Split input into instrcutions
instructions = input.split('\n')

#Set x=1
x=1

#Create a grid to store output
grid = np.zeros((6,40),int)

#Set row to 0
row = 0

#Create counter to count which pixel you can draw
pixel=0

#Repeat for all instructions
for i in instructions:

  #If you get a noop 
  if i == 'noop':

    #If sprite is over pixel, colour it in
    if pixel== x or pixel == x-1 or pixel==x+1:
      grid[row][pixel]=1

    #Move pixel along
    pixel+= 1

    #If you reach the end of the row move to the beginning of the next
    if pixel ==40:
      pixel=0
      row+=1

  #If you get an addx 
  if 'addx' in i:

    #If sprite is over pixel, colour it in
    if pixel== x or pixel == x-1 or pixel==x+1:
      grid[row][pixel]=1

    #Move pixel along
    pixel+= 1

    #If you reach the end of the row move to the beginning of the next
    if pixel ==40:
      pixel=0
      row+=1

    #If sprite is over pixel, colour it in
    if pixel== x or pixel == x-1 or pixel==x+1:
      grid[row][pixel]=1

    #Move pixel along
    pixel+= 1

    #If you reach the end of the row move to the beginning of the next
    if pixel ==40:
      pixel=0
      row+=1

    #Add the value
    x+= int(i[5:])

#Print grid
print(grid)
