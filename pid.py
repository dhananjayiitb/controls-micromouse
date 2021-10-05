import matplotlib.pyplot as plt

TIME_STEP = 0.000001
ONE_SEC = int(1/TIME_STEP)
SET_POINT_INITIAL = 0
PV_INITIAL = 0
print("K_P: ",end="")
K_P = float(input())
print("K_I: ",end="")
K_I = float(input())
print("K_D: ",end="")
K_D = float(input())

max_omega = 0
integral = 0
errors = []
pv_data = []
set_point_data = []
pv = PV_INITIAL
set_point = SET_POINT_INITIAL
for i in range(ONE_SEC):
    errors.append(set_point-pv)
    pv_data.append(pv)
    set_point_data.append(set_point)
    integral += (errors[-1]*TIME_STEP)

# print("Enter new Set Point: ", end="")
# set_point = int(input())
set_point = 90
print("Seconds: ", end="")
seconds = int(input())

for i in range(seconds*ONE_SEC):
    errors.append(set_point-pv)
    pv_data.append(pv)
    set_point_data.append(set_point)
    integral += (errors[-1]*TIME_STEP)
    omega = K_P*errors[-1] + K_I*integral + K_D*(errors[-1] - errors[-2])/TIME_STEP
    max_omega = max(omega, max_omega)
    pv += omega*TIME_STEP

print("Max Omega", max_omega)
print("Final Error",errors[-1])
plt.plot(list(map(lambda x : x*TIME_STEP, range(len(pv_data)))), pv_data)
plt.plot(list(map(lambda x : x*TIME_STEP, range(len(set_point_data)))), set_point_data)
plt.show()
