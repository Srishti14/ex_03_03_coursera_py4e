score_str = input("Enter a score between 0 and 1:")

try:
    score_no = float(score_str)

except:
    print("Error, enter a numeric input.")

if (score_no >= 0.0 and score_no <= 1.0):
    if (score_no >= 0.9 ):
        print("A")
    elif (score_no >= 0.8):
        print("B")
    elif (score_no >= 0.7):
        print("C")
    elif (score_no >= 0.6):
        print("D")
    elif (score_no < 0.6):
        print("F")
else:
    print("Please, enter a number between 0 and 1.")
