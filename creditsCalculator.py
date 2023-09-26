# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W19474591 
# Date: 18/11/2022

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

# Reference:
# https://westminster.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=04181dcc-b079-4824-8774-af470063c474

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

# Reference:
# https://pythonexamples.org/python-if-not/
# https://www.w3schools.com/python/ref_string_isdigit.asp

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

# Reference:
# https://www.w3schools.com/python/python_variables_global.asp

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

# Reference:
# https://www.programiz.com/python-programming/methods/built-in/len

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

# Reference:
# https://bobbyhadz.com/blog/python-input-validation-while-loop#:~:text=To%20validate%20input%20in%20a,break%20out%20of%20the%20loop.


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

# Reference:
# apayangkamu.com/how-to-remove-square-brackets-from-nested-list-in-python

# -----Part 3 - Text File-----
time.sleep(0.7)
print("\nPart 3 - Text File:")
results = open('savedResults.txt', 'w')
results.write(str(list()))
results.close()

# Reference:
# https://westminster.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4613272e-2798-4cdc-8309-add7011205f2