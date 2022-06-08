from itertools import count
import time, sys
def readfile():
  try:
    x=input("file:> ")
    fp=open(f"{x}", "r")
    for count, xx in enumerate(fp, start=1):
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
  try:
    lines=0
    x=input("file:> ")
    fp=open(f"{x}", "r")

    for xx in fp:
      print(xx)
      lines+=1

    print(f"Your file has {lines} line(s)")

  except FileNotFoundError:
    print("The file you have entered is not found.")

def detectlanguage():
  languages = {
    ".txt":"text file",
    ".c":"c",
    ".cpp":"c++",
    ".css":"css",
    ".go":"golang",
    ".html":"html",
    ".java":"java",
    ".js":"javascript",
    ".kt":"kotlin",
    ".py":"python",
    ".rs":"rust",
    ".vala":"vala",
  }
  x=input("file:> ")
  xx=x.split(".")
  try:
    print(languages[f".{xx[1]}"])
  except:
    print("It seems like the language is not yet supported.")
