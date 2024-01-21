# Example 5.3
import cv2
for i in range(5):
  print ("Checking camera #{0}...".format(i))
  cap = cv2.VideoCapture(i)
  if cap.isOpened():
    print ("Camera found!")
  if not cap.isOpened():
    print ("Camera not found!")