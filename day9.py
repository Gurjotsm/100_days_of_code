" Day 9
Hunt a new Apartment:
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. 
You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question.
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.
Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

sample output:
3 
Explanation
At index 3, the farthest you'd have to walk to reach a gym, school, or a store is 1 block; at any other index, you'd have to walk farther

"

import numpy as np
true = True
false = False

def apartmentHunting(blocks, reqs):
  # converting true/ false to 0 and inf
  distance = []
  for block in blocks:
    block_d = []
    for building in block:
      if block[building] == True:
        block_d.append(0)
      else:
        block_d.append(np.inf)
    distance.append(block_d)
    
  
  # converting inf values using 0's present to some smaller no
  # which is basically distance btw blocks
  for i, block in enumerate(distance):
    for j, building in enumerate(block):
      if building == np.inf:

        x = i - 1
        y = i + 1
        min_left = np.inf
        min_right = np.inf
        left_index = x
        right_index = y
        
        while x > -1:
          left = distance[x][j]
          if left < min_left:
            min_left = left
            left_index = x
            
          x -= 1
        
        while y < len(distance):
          right = distance[y][j]
          if right < min_right:
            min_right = right
            right_index = y
            
          y += 1

        
        val = min(min_left,min_right)
        
        # here tricky part, if left = right, check for closer 1
        
        if min_right == min_left and min_left == 0:
          inc = min(abs(left_index-i), abs(right_index-i))
        elif val == min_left:
          inc = abs(left_index- i)
        else:
          inc = abs(right_index - i )
        
        # if some value found, otherwise it means no block has this building
        if val != np.inf:
          distance[i][j] = inc
  
  
  # this would return optimal block if user requires everything or nothing
  # return farthest_dist.index(min(farthest_dist))
  # but we have to customize it according to user
   
  # user requirements     
  reqd_j = [ list(blocks[0]).index(x) for x in reqs]
  dup = distance[:]
  # setting the value 0 for the buildings user doesn't require as it's distance doesn't matter
  for i,x in enumerate(dup):
    for j in range(len(x)):
      if j not in reqd_j:
        distance[i][j] = 0
        
  # farthest dist 1 has to travel if he gets a house in particular block
  farthest_dist = []   
  for x in distance:
    farthest_dist.append(max(x))
  
  # returning index with minimum farthest distance, ## our answer
  return farthest_dist.index(min(farthest_dist))



blocks = [
  {"gym": true, "pool": false, "school": true, "store": false},
  {"gym": false, "pool": false, "school": false, "store": false}, 
  {"gym": false, "pool": false, "school": true, "store": false},
  {"gym": false, "pool": false, "school": false, "store": false},
  {"gym": false, "pool": false, "school": false, "store": true},
  {"gym": true, "pool": false, "school": false, "store": false},
  {"gym": false, "pool": false, "school": false, "store": false},
  {"gym": false, "pool": false, "school": false, "store": false},
  {"gym": false, "pool": false, "school": false, "store": false},
  {"gym": false, "pool": false, "school": true, "store": false},
  {"gym": false, "pool": true, "school": false, "store": false},


]
reqs = ["gym", "pool", "school", "store"]

print(apartmentHunting(blocks, reqs))
