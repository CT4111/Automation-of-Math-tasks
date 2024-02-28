import numpy as np
import math
Vector1 = np.zeros(3)
Vector2 = np.zeros(3)
def GetVector():
    for x in range(2):
        for i in range(3):
            if x==0:
                Vector1[i] = float(input(f"input Vector1 {i}: "))
            else:
                Vector2[i] = float(input(f"input Vector2 {i}: "))

def CalculateAngle():
    Angle = math.acos((Vector1[0]*Vector2[0]+Vector1[1]*Vector2[1]+Vector1[2]*Vector2[2])/(math.sqrt(Vector1[0]**2+Vector1[1]**2+Vector1[2]**2)*math.sqrt(Vector2[0]**2+Vector2[1]**2+Vector2[2]**2)))
    print((Vector1[0]*Vector2[0]+Vector1[1]*Vector2[1]+Vector1[2]*Vector2[2])/(math.sqrt(Vector1[0]**2+Vector1[1]**2+Vector1[2]**2)*math.sqrt(Vector2[0]**2+Vector2[1]**2+Vector2[2]**2)))
    return Angle
GetVector()
print((CalculateAngle()/math.pi*360/2))
