import matplotlib.pyplot as plt


TIME_STEP = 0.000001
ONE_SEC = int(1/TIME_STEP)
OMEGA_ERROR = 20
RADIUS = 2
CIRCUMFERENCE = 32
# print("K_P_Linear: ",end="")
# K_P_L = float(input())
# print("K_P_Angular: ",end="")
# K_P_A = float(input())
K_P_L = 2.5
K_P_A = 0.43

x_set = [0] # X to be reached
x_current = [0] # X of bot
theta_set = [0] # Angle to be reached
theta_current = [0] # Angle of bot
left_set = [0] # Left Omega
right_set = [0] # Right Omega


# for i in range(1*ONE_SEC): # Still 
#     left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]))
#     right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]))
#     v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
#     omega_set = 1.0*RADIUS*(left_set[-1]-right_set[-1])/2
#     x_set.append(x_set[-1])
#     x_current.append(x_current[-1]+v_set*TIME_STEP)
#     theta_set.append(theta_set[-1])
#     theta_current.append(theta_current[-1]+omega_set*TIME_STEP)

x_set.append(16)

for i in range(int(0.5*ONE_SEC)): 
    left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
    omega_set = 180.0*RADIUS*(left_set[-1]-right_set[-1])/CIRCUMFERENCE
    x_set.append(x_set[-1])
    x_current.append(x_current[-1]+v_set*TIME_STEP)
    theta_set.append(theta_set[-1])
    theta_current.append(theta_current[-1]+omega_set*TIME_STEP)
 
theta_set.append(90)

for i in range(int(0.4*ONE_SEC)): 
    left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
    omega_set = 180.0*RADIUS*(left_set[-1]-right_set[-1])/CIRCUMFERENCE
    x_set.append(x_set[-1])
    x_current.append(x_current[-1]+v_set*TIME_STEP)
    theta_set.append(theta_set[-1])
    theta_current.append(theta_current[-1]+omega_set*TIME_STEP)

x_set.append(16*10)

for i in range(int(3*ONE_SEC)): 
    left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
    omega_set = 180.0*RADIUS*(left_set[-1]-right_set[-1])/CIRCUMFERENCE
    x_set.append(x_set[-1])
    x_current.append(x_current[-1]+v_set*TIME_STEP)
    theta_set.append(theta_set[-1])
    theta_current.append(theta_current[-1]+omega_set*TIME_STEP)

theta_set.append(0)

for i in range(int(0.25*ONE_SEC)): 
    left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
    omega_set = 180.0*RADIUS*(left_set[-1]-right_set[-1])/CIRCUMFERENCE
    x_set.append(x_set[-1])
    x_current.append(x_current[-1]+v_set*TIME_STEP)
    theta_set.append(theta_set[-1])
    theta_current.append(theta_current[-1]+omega_set*TIME_STEP)


theta_set.append(-90)

for i in range(int(0.25*ONE_SEC)): 
    left_set.append(K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) + K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    right_set.append(K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) if K_P_L*(x_set[-1]-x_current[-1]) - K_P_A*(theta_set[-1]-theta_current[-1]) < 40 else 40)
    v_set = 1.0*RADIUS*(left_set[-1] + right_set[-1])/2
    omega_set = 180.0*RADIUS*(left_set[-1]-right_set[-1])/CIRCUMFERENCE
    x_set.append(x_set[-1])
    x_current.append(x_current[-1]+v_set*TIME_STEP)
    theta_set.append(theta_set[-1])
    theta_current.append(theta_current[-1]+omega_set*TIME_STEP)

plt.figure(1)
plt.plot(x_set)
plt.plot(x_current)

plt.figure(2)
plt.plot(theta_set)
plt.plot(theta_current)

plt.figure(3)
plt.plot(left_set)
plt.plot(right_set)

plt.show()