!pip install mediapipe

from google.colab import files

uploaded = files.upload()

import cv2
from google.colab.patches import cv2_imshow
import math
import numpy as np

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480
def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  cv2_imshow(img)

# Read images with OpenCV.
images = {name: cv2.imread(name) for name in uploaded.keys()}
# Preview the images.
for name, image in images.items():
  print(name)   
  resize_and_show(image)
  
import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
help(mp_hands.Hands)

# Run MediaPipe Hands.
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
  for name, image in images.items():
    # Convert the BGR image to RGB, flip the image around y-axis for correct 
    # handedness output and process it with MediaPipe Hands.
    results = hands.process(cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1))

    # Print handedness (left v.s. right hand).
    print(f'Handedness of {name}:')
    print(results.multi_handedness)

    if not results.multi_hand_landmarks:
      continue
    image_hight, image_width, _ = image.shape
    annotated_image = cv2.flip(image.copy(), 1)
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    resize_and_show(cv2.flip(annotated_image, 1))
    
# Run MediaPipe Hands and plot 3d hands world landmarks.
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
  for name, image in images.items():
    # Convert the BGR image to RGB and process it with MediaPipe Hands.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # Draw hand world landmarks.
    print(f'Hand world landmarks of {name}:')
    if not results.multi_hand_world_landmarks:
      continue
    for hand_world_landmarks in results.multi_hand_world_landmarks:
      # finger states
      thumbIsOpen = False
      firstFingerIsOpen = False
      secondFingerIsOpen = False
      thirdFingerIsOpen = False
      fourthFingerIsOpen = False

      fingerOpenCount = 0

      landmarkList = hand_world_landmarks.landmark[:]
      pseudoFixKeyPoint = landmarkList[2].x
      if landmarkList[3].x < pseudoFixKeyPoint and landmarkList[4].x < pseudoFixKeyPoint:
        thumbIsOpen = True
        fingerOpenCount += 1
        
      pseudoFixKeyPoint = landmarkList[6].y
      if landmarkList[7].y < pseudoFixKeyPoint and landmarkList[8].y < pseudoFixKeyPoint:
        firstFingerIsOpen = True
        fingerOpenCount += 1

      pseudoFixKeyPoint = landmarkList[10].y
      if landmarkList[11].y < pseudoFixKeyPoint and landmarkList[12].y < pseudoFixKeyPoint:
        secondFingerIsOpen = True
        fingerOpenCount += 1

      pseudoFixKeyPoint = landmarkList[14].y
      if landmarkList[15].y < pseudoFixKeyPoint and landmarkList[16].y < pseudoFixKeyPoint:
        thirdFingerIsOpen = True
        fingerOpenCount += 1

      pseudoFixKeyPoint = landmarkList[18].y
      if landmarkList[19].y < pseudoFixKeyPoint and landmarkList[20].y < pseudoFixKeyPoint:
        fourthFingerIsOpen = True
        fingerOpenCount += 1

      if not thumbIsOpen and firstFingerIsOpen and secondFingerIsOpen and not thirdFingerIsOpen and not fourthFingerIsOpen:
        fingerOpenCount = 'V'
      elif not thumbIsOpen and firstFingerIsOpen and not secondFingerIsOpen and not thirdFingerIsOpen and fourthFingerIsOpen:
        fingerOpenCount = 'Peace'
      elif thumbIsOpen and firstFingerIsOpen and not secondFingerIsOpen and not thirdFingerIsOpen and fourthFingerIsOpen:
        fingerOpenCount = 'SpiderMan'
      
      resize_and_show(cv2.flip(image, 1))
      print(f'finger count: {fingerOpenCount}')