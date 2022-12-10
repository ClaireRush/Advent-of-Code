#@title Day 10, Puzzle 1

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

#Create an empty list to store the x values
values=[]

#Repeat for all instructions
for i in instructions:

  #If you get a noop store current x value
  if i == 'noop':
    values.append(x)

  #If you get an addx 
  if 'addx' in i:

    #Store current x for the first cycle
    values.append(x)
    
    #Add the value and then store the new x for the second cycle
    x+= int(i[5:])
    values.append(x)
  
#Store x values for desired cycle
desired=[[values[18 + 40 * i], 20 + 40*i] for i in range(len(values)//40)]

#Calculate signal strength
strength=[x[0]*x[1] for x in desired]

#Calculate total strength
total=sum(strength)
print(total)
