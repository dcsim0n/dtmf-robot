#!/usr/bin/python3
##############################
# DTMF Robot car controller
# 2019 Dana Simmons
##############################

from gpiozero import Motor

# Using a 6 pin ribbon cable to span pins 12-22
LeftWheel = Motor(2,3,enable=4,pwm=False)
RightWheel = Motor(17,27,enable=22,pwm=False)

running = True
def forward():
  print("Moving forward")
  LeftWheel.forward()
  RightWheel.forward()

def reverse():
  print("Moving backwards")
  LeftWheel.backward()
  RightWheel.backward()

def stop():
  print("Stoping")
  LeftWheel.stop()
  RightWheel.stop()

# DTMF KEYS
# 1  2  3 
# 4  5  6
# 7  8  9
# *  0  #
directionControls = {
  "1": lambda : print("doing 1"),
  "2": forward,
  "3": lambda : print("doing 3"),
  "4": lambda : print("doing 4"),
  "5": stop,
  "6": lambda : print("doing 6"),
  "7": lambda : print("doing 7"),
  "8": reverse,
  "9": lambda : print("doing 9"),
  "0": lambda : print("doing 0"),
}

def main():
  while running:
    data = input().strip()
    #data = sys.
    if(len(data) > 0):
      if "DTMF:" in data:
          cmd = data.split(" ")[1]
          directionControls[cmd]()

if __name__ == "__main__":
  main()
