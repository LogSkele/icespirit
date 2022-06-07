from itertools import count
import time, sys
def readfile():
  try:
    count=0
    x=input("file:> ")
    fp=open(f"{x}", "r")
    for xx in fp:
      count += 1
      if count == 300: #hmmm
        print("The file is too big to read in a short amount of time.")
        sys.exit()
      else:
        start=time.time()
        print(fp.read())
        end=time.time()
    timetaken=end-start
    print(f"It took {timetaken} seconds to read your file.")
  except FileNotFoundError:
    print("The file you have entered is not found.")

def countlines():
  cnt=0
  x=input("file:> ")
  fp=open(f"{x}", "r")

  for xx in fp:
    print(xx)
    cnt+=1

  print(f"Your file has {cnt} line(s)")
