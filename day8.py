" Day 8
Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.
The Longest Peak consists of elements that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the sub-array are in decreasing order.

Input: arr = [2, 2, 2] 
Output: 0 
Explanation: 
No sub-array exists that shows the behaviour of a mountain sub-array.

Input: arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 
Output: 11 

Explanation: 
There are two sub-arrays that can be considered as mountain sub-arrays. The first one is from index 0 – 2 (3 elements) and next one is from index 2 – 12 (11 elements).  As 11 > 2, our answer is 11.
"

def LongestPeak(a): 
  prev_peak , peak = 0, 0
  inc = 0
  dec = 0
  
  if len(a) < 3:
    return 0
  
  for i in range(len(a) - 1):
    # print("inc : {} dec: {}".format(inc, dec))
    
    # since equal element is also a deal breaker for both the value of inc,dec
    if a[i] == a[i+ 1]:
      if dec != 0:
        peak = inc + dec
      inc = 0
      dec = 0  
      
    # first mountain
    if a[i] < a[i+1] and dec == 0:
      inc += 1
      
    # new mointain has started if elif is true
    elif a[i] < a[i+ 1] and dec != 0:
      peak = inc + dec
      dec = 0
      inc = 1

    # decreasing order only if increasing order was present before
    if a[i] > a[i+ 1] and inc != 0:
      # peak is left behind, so this makes sure peak is also counted
      if dec == 0:
          inc += 1
      dec += 1

    if prev_peak < peak:
      prev_peak = peak
    
      
  # since peak is only evaluated if new mountain comes
  # for last mountain we have to evaluate again
  if dec != 0:
    # case of all increments
    peak = inc + dec 
  if prev_peak < peak:
    prev_peak = peak 
  return prev_peak
      

if __name__ == "__main__":
  # d = [ 1, 3, 1, 4, 5, 6,  
        # 7, 8, 9, 8, 7, 6, 5 ]
  d = list(map(int, input().split(",")))
  print(LongestPeak(d)) 
      