from flask import Flask
app = Flask(__name__)
app.debug = True

TIME_STEP = 0.000001
MAX = 40
ONE_SEC = int(1/TIME_STEP)
OMEGA_ERROR = 20
RADIUS = 2
CIRCUMFERENCE = 32
K_P_L = 2.5
K_P_A = 0.43

x_current = 0 # X of bot
theta_current = 0 # Angle of bot
left_set = 0
right_set = 0

@app.route('/')
def run():
    return str(int(255.0*left_set/MAX)) + "," + str(int(255.0*right_set/MAX))

app.run(host="192.168.0.177")

x_set = 16
theta_set = 0

while(True):
    left_set = K_P_L*(x_set-x_current) + K_P_A*(theta_set-theta_current) if K_P_L*(x_set-x_current) + K_P_A*(theta_set-theta_current) < MAX else MAX
    right_set = K_P_L*(x_set-x_current) - K_P_A*(theta_set-theta_current) if K_P_L*(x_set-x_current) - K_P_A*(theta_set-theta_current) < MAX else MAX
    v_set = 1.0*RADIUS*(left_set + right_set)/2
    omega_set = 180.0*RADIUS*(left_set - right_set)/CIRCUMFERENCE
    x_current = (x_current+v_set*TIME_STEP)
    theta_current = (theta_current+omega_set*TIME_STEP)