##############################
# DTMF Robot car controller
# 2019 Dana Simmons
##############################

from gpiozero import Motor

# Using a 6 pin ribbon cable to span pins 12-22
LeftWheel = Motor(12,16)
RightWheel = Motor(18,22)

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
  "1": None,
  "2": forward(),
  "3": None,
  "4": None,
  "5": stop(),
  "6": None,
  "7": None,
  "8": reverse(),
  "9": None,
}

def main():
  while running:
    data = input().strip()
    directionControls[data]

if __name__ == "__main__":
  main()