import os
import face_recognition
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

image = face_recognition.load_image_file('./Serio.jpg')
face_landmarks = face_recognition.face_landmarks(image)
face_location = face_recognition.face_locations(image)
pil_image = Image.fromarray(image)

# top_lip = 48,49,50,51,52,53,54,64,63,62,61,60
# bot_lip = 54,55,56,57,58,59,48,60,67,66,65,64

# importa = 61,62,63, 67,66,65
# index = [8,9,10][8,9,10]

for face_landmarks in face_landmarks:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # d.line(face_landmarks['top_lip'], fill=(255, 0, 0, 255), width=2)
    # d.line(face_landmarks['bottom_lip'], fill=(255, 0, 0, 255), width=2)
    print(face_location)

    topCornerDiff = face_landmarks['top_lip'][8][1] - \
        face_landmarks['bottom_lip'][10][1]
    midDiff = face_landmarks['top_lip'][9][1] - \
        face_landmarks['bottom_lip'][9][1]
    rightCornerDiff = face_landmarks['top_lip'][10][1] - \
        face_landmarks['bottom_lip'][8][1]

    topRightLip = face_landmarks['top_lip'][8][1]
    topMidLip = face_landmarks['top_lip'][9][1]
    topLeftLip = face_landmarks['top_lip'][10][1]

    if topCornerDiff < 0 and midDiff < 0 and rightCornerDiff < 0:
        if abs((topRightLip - topMidLip) + (topMidLip - topLeftLip)) != 0:
            text = 'Smiling!'
        else:
            text = 'Not smiling!'
    else:
        text = 'Not smiling!'

    for top, right, bottom, left in face_location:
        d.rectangle(((left, top), (right, bottom)), fill=(
            255, 0, 0, 0), outline=(255, 0, 0, 255))
        d.text((left + 6, bottom - 12), text, fill=(255, 0, 0, 255))

    pil_image.show()
