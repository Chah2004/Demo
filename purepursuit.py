import math

def pure_pursuit_simulation():
    xb = [80, 90, 99, 108, 116, 125, 133, 141, 151, 160, 169, 179, 180]
    yb = [0, -2, -5, -9, -15, -18, -23, -29, -28, -25, -21, -20, -17]
    
    xf = [0] * 13  
    yf = [0] * 13
    yf[0] = 50
    
    
    vf = 20
    
    print("\nSIMULATION OF PURE PURSUIT PROBLEM IN PYTHON\n")

    for t in range(12):  
        d = math.sqrt((yb[t] - yf[t]) ** 2 + (xb[t] - xf[t]) ** 2)
        
        if d <= 10:
            print(f"\nCaught at {t} mts and {d:.2f} kms\n")
            break
        else:
            xf[t + 1] = xf[t] + (vf * (xb[t] - xf[t]) / d)
            yf[t + 1] = yf[t] + (vf * (yb[t] - yf[t]) / d)

    if t >= 12:
        print("Target Escaped\n")
        
pure_pursuit_simulation()
