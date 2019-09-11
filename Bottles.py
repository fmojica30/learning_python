#  File: Bottles.py 

#  Description:  

#  Student Name:  Fernando Martinez Mojica  

#  Student UT EID: fmm566

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 5/6/2019

#  Date Last Modified: 5/6/2019

def bottles_dp(v):
  sv = []
  bv = []
  vol = 0 
  for i in range(len(v)):
    if (i == 0):
      sv.append(v[i]) #initializing the s(v) list
      bv.append(i)
    elif (i == 1): #initializing the s(v) list 
      if (len(sv) == 1):
        if (v[i] > v[i - 1]):
          sv.append(v[i])
          bv.append(i)
        else:
          sv.append(sv[i - 1])
          bv.append(-1)
    else:
      vol_add = v[i]
      compare = [] #where to store the comparison values
      compare_idx = [] #storage for comparison indices
      for j in range(len(sv) - 1):
        vol_add += sv[j]
        compare.append(vol_add)
        vol_add -= sv[j]
      item = compare.index(max(compare))
      if (compare[item] > sv[i - 1]):
        sv.append(compare[item])
        bv.append(i)
      else:
        sv.append(sv[i - 1])
        bv.append(-1)

  return sv, bv

def find_bottles(sv,bv,v):
  bottles_used = []
  final_max = sv.index(max(sv))
  minus = -1
  while (minus >= -len(bv)):
    if (bv[minus] != -1):
      bottles_used.append(v[bv[minus]])
      minus -= 2
    else:
      minus -= 1
  return bottles_used

def main():
  # create empty list of bottles
  v = []

  # open file bottles.txt for reading
  inf = open ("./bottles.txt", "r")

  # read the number of bottles
  num_bottles = int(inf.readline())
  # populate the list v with bottles
  for i in range(num_bottles):
    bottle = int(inf.readline())
    v.append(bottle)

  # close the file
  inf.close()

  # find the greatest sum
  s_v, b_v = bottles_dp (v)

  # print the list s_v
  for i in range(len(s_v)):
    print(s_v[i],end = "  ")
  print()

  # print the list b_v
  for i in range(len(b_v)):
    print(b_v[i],end = "  ")
  print()


  # print the greatest sum
  print(s_v[-1])

  # print the bottles contributing to the largest sum
  bot_used = find_bottles(s_v,b_v,v)
  bot_used.reverse()
  for i in range(len(bot_used)):
    print(bot_used[i], end = "  ")
  print()


if __name__ == "__main__":
  main()
