import time, sys
def readfile():
  try:
    count=0
    x=input("file:> ")
    bow=open(f"{x}.txt", "r")
    for xx in bow:
      count += 1
      if count == 300: #hmmm
        print("The file is too big to read in a short amount of time.")
        sys.exit()
      else:
        start=time.time()
        print(bow.read())
        end=time.time()
    timetaken=end-start
    print(f"It took {timetaken} seconds to read your file.")
  except FileNotFoundError:
    print("The file you have entered is not found.")
