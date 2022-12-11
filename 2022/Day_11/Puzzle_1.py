#@title Day 11, Puzzle 1

#Take input
input='''Monkey 0:
  Starting items: 56, 56, 92, 65, 71, 61, 79
  Operation: new = old * 7
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 7

Monkey 1:
  Starting items: 61, 85
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 2:
  Starting items: 54, 96, 82, 78, 69
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 3:
  Starting items: 57, 59, 65, 95
  Operation: new = old + 4
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 1

Monkey 4:
  Starting items: 62, 67, 80
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 6

Monkey 5:
  Starting items: 91
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 4

Monkey 6:
  Starting items: 79, 83, 64, 52, 77, 56, 63, 92
  Operation: new = old + 6
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 7:
  Starting items: 50, 97, 76, 96, 80, 56
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 5'''

#Split input into rows
instructions= input.split('\n')

#Make lists for storing data
items_list = [x[18:].split(',') for x in instructions if "Starting" in x]
items = [[int(x)for x in y] for y in items_list]
operations = [x[23:] for x in instructions if "Operation" in x]
test = [int(x[21:]) for x in instructions if "Test" in x]
true = [int(x[29:]) for x in instructions if "true" in x]
false= [int(x[30:]) for x in instructions if "false" in x]

#Make list to store how many items each monkey inspects
monkey=[0 for x in items]


#Repeat for 20 rounds
for i in range(20):

  #Go through each monkey
  for j in range(len(test)):
    

    #Repeat for each item the monkey has
    for k in items[j]:

      #Add one to the count of items the monkey has inspected
      monkey[j]+=1


      #Perform operation

      #Check if its +
      if '+' in operations[j]:
        
        #Add required amount
        new = k + int(operations[j][2:])

      #Check if its *
      if '*' in operations[j]:

        #Check if its * old
        if 'old' in operations[j]:

          #Multiply by itself 
          new = k * k
  
        #Otherwise multiply by required amount
        else:
          new = k * int(operations[j][2:])

      
      #Adjust for relief
      new = new // 3


      #Perform test

      #If test true throw to relevant monkey
      if new% test[j]==0:
        items[true[j]].append(new)

      #If test false throw to other monkey
      else:
        items[false[j]].append(new)

      #Empty items list as all items thrown
      items[j]=[]

#Sort monkeys with most items handled first
monkey.sort(reverse = True)

#Calculate monkey business
business= monkey[0] * monkey[1]
print(business)
