import numpy as np
def NormalenForm(vectors):
    normalV = ([vectors[1][1]-vectors[2][2]],[vectors[1][2]-vectors[2][0]],[vectors[1][0]-vectors[2][1]])
Punkte = np.zeros((3,3))
vector = np.zeros((3,3))
for i in range(3):
    for c in range(3):
        Punkte[i][c] = float(input("input value {} {}:".format(i,c)))
for i in range(2):
    vector[i+1]=Punkte[i+1]-Punkte[0]
vector[0]=Punkte[0]
print(Punkte)
print(vector)
print("{} + a * {} + b * {}".format(vector[0],vector[1],vector[2]))
print(f"normalen Vektor = {NormalenForm(vector)}")
#Ziel output
#   x10 + a*x11 + b*x12
#   x10 + a*x11 + b*x12
#   x10 + a*x11 + b*x12

#Normalenform
