# -----Part 1 - Main Version-----

# A - Outcomes
import time
passCredits = 0
deferCredits = 0
failCredits = 0

progressList = []
moduleTrailerList = []
moduleRetrieverList = []
excludeList = []

def outcome(passCredits, deferCredits, failCredits):
  if passCredits == 120:
    print("Progress")
    progressList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 100:
    print("Progress (module trailer)")
    moduleTrailerList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 80:
    print("Do not progress - module retriever")
    moduleRetrieverList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 60:
    print("Do not progress - module retriever")
    moduleRetrieverList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 40 and deferCredits >= 20:
    print("Do not progress - module retriever")
    moduleRetrieverList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 40 and deferCredits == 0:
    print("Exclude")
    excludeList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 20 and failCredits <= 60:
    print("Do not progess - module retriever")
    moduleRetrieverList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 20 and failCredits >= 80:
    print("Exclude")
    excludeList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 0 and deferCredits >= 60:
    print("Do not progress - module retriever")
    moduleRetrieverList.append([passCredits, deferCredits, failCredits])
  elif passCredits == 0 and deferCredits >= 80:
    print("Exclude")
    excludeList.append([passCredits, deferCredits, failCredits])

# B - Validation
def get_credits(prompt):
  validCredits = [0, 20, 40, 60, 80, 100, 120]
  while True:
    userInput = input("Please enter your credits at " + prompt + ": ")
    if not userInput.isdigit():
      print("Integer required\n")
      continue
    credits = int(userInput)
    if credits in validCredits:
      break
    print("Out of range")
  return credits
print("-" * 12, "Progression Outcomes", "-" * 12)
print("Part 1 - Main Version")
print()

def validation():
  global passCredits, deferCredits, failCredits
  while True:
    passCredits = get_credits("pass")
    deferCredits = get_credits("defer")
    failCredits = get_credits("fail")
    total = passCredits + deferCredits + failCredits
    if total == 120:
      break
    print("Total Incorrect")
  print("\nProgression Outcome: ", end= '')
  outcome(passCredits, deferCredits, failCredits)
  histogram(passCredits, deferCredits, failCredits)
  multiple()

# D - Histogram
progress = []
moduleTrailer = []
moduleRetriever = []
exclude = []

def histogram(passCredits, deferCredits, failCredits):
  if passCredits == 120:
    progress.append(0)
  elif passCredits == 100:
    moduleTrailer.append(0)
  elif passCredits == 80:
    moduleRetriever.append(0)
  elif passCredits == 60:
    moduleRetriever.append(0)
  elif passCredits == 40 and deferCredits >= 20:
    moduleRetriever.append(0)
  elif passCredits == 40 and deferCredits == 0:
    exclude.append(0)
  elif passCredits == 20 and failCredits <= 60:
    moduleRetriever.append(0)
  elif passCredits == 20 and failCredits >= 80:
    exclude.append(0)
  elif passCredits == 0 and deferCredits >= 60:
    moduleRetriever.append(0)
  elif passCredits == 0 and deferCredits >= 80:
    exclude.append(0)

def displayHistogram():
    print()
    print("-" * 60)
    print("Histogram:\n")
    print("Progress", len(progress), " :", "*" * len(progress))
    print("Trailer", len(moduleTrailer), "  :", "*" * len(moduleTrailer))
    print("Retriever", len(moduleRetriever), ":", "*" * len(moduleRetriever))
    print("Excluded", len(exclude), " :", "*" * len(exclude))
    print()
    total = len(progress) + len(moduleTrailer) + len(moduleRetriever) + len(exclude)
    print(total, "outcomes in total.")
    print("-" * 60)
    print("")

# C - Multiple Outcomes
def multiple():
    global moreData
    while True:
        print("")
        try:
            moreData = input("Would you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ")
        except ValueError:
            print("Please Enter 'y' or 'q'")
        else:
            if moreData == "q":
                displayHistogram()
                time.sleep(0.7)
                break

            elif moreData == "y":
                validation()
                print()
                pass
                break

    return moreData

validation()
histogram(passCredits, deferCredits, failCredits)

# -----Part 2 - List-----
time.sleep(0.7)
print("Part 2 - List:")
def list():
  for i in progressList:
    print("Progress -", str(i)[1:-1])

  for i in moduleTrailerList:
    print("Progress (module trailer) -", str(i)[1:-1])
  
  for i in moduleRetrieverList:
    print("Module retriever -", str(i)[1:-1])

  for i in excludeList:
    print("Exclude -", str(i)[1:-1])
list()

# -----Part 3 - Text File-----
time.sleep(0.7)
print("\nPart 3 - Text File:")
results = open('savedResults.txt', 'w')
results.write(str(list()))
results.close()
