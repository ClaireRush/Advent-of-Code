#@title Day 15, Puzzle 1

#Import numpy
import numpy as np

#Take input 
input = '''Sensor at x=2832148, y=322979: closest beacon is at x=3015667, y=-141020
Sensor at x=1449180, y=3883502: closest beacon is at x=2656952, y=4188971
Sensor at x=2808169, y=1194666: closest beacon is at x=3015667, y=-141020
Sensor at x=1863363, y=2435968: closest beacon is at x=2166084, y=2883057
Sensor at x=3558230, y=2190936: closest beacon is at x=3244164, y=2592191
Sensor at x=711491, y=2444705: closest beacon is at x=617239, y=2988377
Sensor at x=2727148, y=2766272: closest beacon is at x=2166084, y=2883057
Sensor at x=2857938, y=3988086: closest beacon is at x=2968511, y=4098658
Sensor at x=1242410, y=2270153: closest beacon is at x=214592, y=2000000
Sensor at x=3171784, y=2523127: closest beacon is at x=3244164, y=2592191
Sensor at x=2293378, y=71434: closest beacon is at x=3015667, y=-141020
Sensor at x=399711, y=73420: closest beacon is at x=1152251, y=-158441
Sensor at x=3677529, y=415283: closest beacon is at x=3015667, y=-141020
Sensor at x=207809, y=2348497: closest beacon is at x=214592, y=2000000
Sensor at x=60607, y=3403420: closest beacon is at x=617239, y=2988377
Sensor at x=3767729, y=3136725: closest beacon is at x=4171278, y=3348370
Sensor at x=3899632, y=3998969: closest beacon is at x=4171278, y=3348370
Sensor at x=394783, y=1541278: closest beacon is at x=214592, y=2000000
Sensor at x=1193642, y=642631: closest beacon is at x=1152251, y=-158441
Sensor at x=122867, y=2661904: closest beacon is at x=214592, y=2000000
Sensor at x=551012, y=3787568: closest beacon is at x=617239, y=2988377
Sensor at x=3175715, y=2975144: closest beacon is at x=3244164, y=2592191
Sensor at x=402217, y=2812449: closest beacon is at x=617239, y=2988377
Sensor at x=879648, y=1177329: closest beacon is at x=214592, y=2000000
Sensor at x=1317218, y=2978309: closest beacon is at x=617239, y=2988377
Sensor at x=3965126, y=1743931: closest beacon is at x=3244164, y=2592191
Sensor at x=2304348, y=3140055: closest beacon is at x=2166084, y=2883057
Sensor at x=3380135, y=3650709: closest beacon is at x=2968511, y=4098658
Sensor at x=49224, y=1914296: closest beacon is at x=214592, y=2000000
Sensor at x=3096228, y=2457233: closest beacon is at x=3244164, y=2592191
Sensor at x=1415660, y=6715: closest beacon is at x=1152251, y=-158441
Sensor at x=2616280, y=3548378: closest beacon is at x=2656952, y=4188971'''

#Split into instructions
instructions = input.split('\n')

#Split each instruction into sensor and beacon
objects = [x.split(':') for x in instructions]

#Split into coordinates
coordinates = [[x.split(',') for x in y] for y in objects]

#Remove the words
coords_string = [[[x[0][0][12:], x[0][1][3:]],[x[1][0][24:], x[1][1][3:]]] for x in coordinates]

#Turn into integers
coords = [[[int(x) for x in y] for y in z] for z in coords_string]

#Calculate the manhatten distances
distances = [abs(x[0][0]-x[1][0]) + abs(x[0][1] - x[1][1]) for x in coords]


#Calculate limits of each sensors range in the order up, down, left, right

#Make empty lists to store limits
up=[]
down=[]
left=[]
right=[]

#Repeat for each sensor
for i in range(len(distances)):

  #Add distance to the coordinates of the sensor and add to list
  up.append(coords[i][0][1]- distances[i])
  down.append(coords[i][0][1]+ distances[i])
  left.append(coords[i][0][0]- distances[i])
  right.append(coords[i][0][0]+ distances[i])

#Define upper, lower, left and right limits
upper_limit = min(up)
lower_limit= max(down)
left_limit = min(left)
right_limit = max(right)

#Create desired row of grid
grid= np.zeros(right_limit - left_limit+1, int)


#Put beacons and sensors in grid
for i in range(len(coords)):

  #Put in sensor ranges as 1
  for j in range(distances[i]+1):


    #Start from location of sensor, only adding it if it's in the desired row
      
    #If you are below target row move up
    if coords[i][0][1]- upper_limit >= 2000000- upper_limit:

      #If you are in target row
      if coords[i][0][1]- upper_limit-j == 2000000- upper_limit:

        #Move along row adding 1's if you are in range
        for k in range(distances[i]+1-j):
          grid[coords[i][0][0]- left_limit-k] = 1
          grid[coords[i][0][0]- left_limit+k] = 1
        
      #When you are now above the target row then break out
      if coords[i][0][1]- upper_limit-j < 2000000- upper_limit:
        break

    #If you are above target row move down
    if coords[i][0][1]- upper_limit < 2000000- upper_limit:

      #If you are in target row
      if coords[i][0][1]- upper_limit+j == 2000000- upper_limit:

        #Move along row adding 1's if you are in range
        for k in range(distances[i]+1-j):
          grid[coords[i][0][0]- left_limit-k] = 1
          grid[coords[i][0][0]- left_limit+k] = 1

      #When you are now below the target row then break out
      if coords[i][0][1]- upper_limit-j > 2000000- upper_limit:
        break


  #Put sensor in grid as 2 if in desired row
  if coords[i][0][1]- upper_limit == 2000000- upper_limit:
    grid[coords[i][0][0]- left_limit]=2

  #Put beacon in grid as 3 if in desired row
  if coords[i][1][1]- upper_limit == 2000000- upper_limit:
    grid[coords[i][1][0]- left_limit]=3


#Count number of spaces in row where you can't have a beacon
number = np.count_nonzero(grid==1)
print(number)
