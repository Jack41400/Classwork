# Bounce calculation

startingHeight = float(input("Enter the starting height: "))
reboundRatio = float(input("Enter the rebound ratio: "))
bounces = int(input("Enter the number of bounces: "))
distance = startingHeight
currentHeight = startingHeight

for i in range(bounces):
    currentHeight *= reboundRatio
    distance += 2 * currentHeight

print(distance)
