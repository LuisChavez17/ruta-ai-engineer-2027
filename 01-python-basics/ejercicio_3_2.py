score = input("Enter Score: ")

try:
    s = float(score)
except:
    print("Error: Please enter a numeric value")
    quit()

if s < 0.0 or s > 1.0:
    print("Error: Score is out of range (0.0 - 1.0)")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
