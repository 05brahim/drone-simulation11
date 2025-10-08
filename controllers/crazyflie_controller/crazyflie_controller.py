from controller import Robot
import sys

robot = Robot()
timestep = int(robot.getBasicTimeStep())

candidates = [
  "propeller1","propeller2","propeller3","propeller4",
  "m1_motor","m2_motor","m3_motor","m4_motor",
  "motor1","motor2","motor3","motor4",
  "rotor1","rotor2","rotor3","rotor4",
  "rotor_0","rotor_1","rotor_2","rotor_3"
]

motors = []
found = []

for name in candidates:
    try:
        dev = robot.getDevice(name)
        if dev:
            dev.setPosition(float('inf'))
            dev.setVelocity(0.0)
            motors.append(dev)
            found.append(name)
    except:
        pass

print("*** Motor detection ***")
print("Found motors:", found)
sys.stdout.flush()

while robot.step(timestep) != -1:
    for m in motors:
        m.setVelocity(30.0)
