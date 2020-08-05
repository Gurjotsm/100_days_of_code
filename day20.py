" Day 20
Write a  program to remove leading zeros following "." from an IP address.
Sample Input -> Output
remZero("216.08.094.196") → "216.8.94.196" 
remZero("016.08.0904.96") → "016.8.904.96"
"

import re
def remZero(ip_addr):

  # without regex

  # result = ""
  # for i in ip_addr:
  #   if len(result) != 0:
  #     if i == "0" and result[-1] == ".":
  #       continue
  #   result += i
  # return result
  
  # with regex

  result = re.sub("\.0", ".", ip_addr)
  return result
  
if __name__ == "__main__":
  ip = "016.08.0904.96"
  print(remZero(ip))


