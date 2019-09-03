#!/usr/bin/python3
##############################
# DTMF Robot car controller
# 2019 Dana Simmons
##############################

from gpiozero import Motor
import time
from multiprocessing import Queue, Process


# Using a 6 pin ribbon cable to span pins 12-22
LeftWheel = Motor(2,3,enable=4,pwm=False)
RightWheel = Motor(17,27,enable=22,pwm=False)

MOVESIZE = .5 
TURNSIZE = .25

running = True

def stop():
  print("Stoping")
  LeftWheel.stop()
  RightWheel.stop()

def forward():
  print("Moving forward")
  LeftWheel.forward()
  RightWheel.forward()
  time.sleep(MOVESIZE)
  stop()

def reverse():
  print("Moving backwards")
  LeftWheel.backward()
  RightWheel.backward()
  time.sleep(MOVESIZE)
  stop()

def turnRight():
  print("Turning Right")
  RightWheel.forward()
  LeftWheel.backward()
  time.sleep(TURNSIZE)
  stop()

def turnLeft():
  print("Rutning Left")
  RightWheel.backward()
  LeftWheel.forward()
  time.sleep(TURNSIZE)
  stop()

# DTMF KEYS
# 1  2  3 
# 4  5  6
# 7  8  9
# *  0  #
directionControls = {
  "1": lambda : print("doing 1"),
  "2": forward,
  "3": lambda : print("doing 3"),
  "4": turnRight,
  "5": stop,
  "6": turnLeft,
  "7": lambda : print("doing 7"),
  "8": reverse,
  "9": lambda : print("doing 9"),
  "0": lambda : print("doing 0"),
}

def proccess_queue(q):
  while True:
    task = q.get()
    task()

def main():
  Q = Queue()
  #queue processing thread
  p = Process(target=proccess_queue, args=(Q,))
  p.start()

  while running:
    data = input().strip()
    #data = sys.
    if(len(data) > 0):
      if "DTMF:" in data:
          cmd = data.split(" ")[1]
          #directionControls[cmd]()
          Q.put(directionControls[cmd])


if __name__ == "__main__":
  main()
