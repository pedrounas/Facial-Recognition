import cv2
import os
import sys
import numpy as np
import face_recognition
import send_mail

# vid = cv2.VideoCapture('http://192.168.1.4:8080/video')
vid = cv2.VideoCapture(0)

path = './known'
files = os.listdir(path)
names = []
file_names = []
encodings = []
process_frame = True
face_locations = []
face_names = []
face_encodings = []
found_names = []
students = []

for file in files:
    x = file.split('.')
    file_names.append('./known/' + file)
    names.append(x[0])

for file in file_names:
    temp = face_recognition.load_image_file(file)
    encodings.append(face_recognition.face_encodings(temp)[0])


file = open('students.txt', 'r')
for line in file:
    students.append(line.rstrip('\n'))


while True:

    ret, frame = vid.read()

    crop = None

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []

        # if len(face_locations) == 2:
        #     temp = face_locations[0]
        #     face_locations[0] = face_locations[1]
        #     face_locations[1] = temp

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(
                encodings, face_encoding)
            best_match = np.argmin(face_distances)
            if matches[best_match]:
                name = names[best_match]

            face_names.append(name)

    process_frame = not process_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # print(name, top, bottom, left, right)
        # crop = frame[top:bottom, left:right]

        # cv2.rectangle(frame, (left, top), (right, bottom),
        #               (0, 0, 255), 1)

        font = cv2.FONT_HERSHEY_DUPLEX
        name_ = name.replace("_", " ")
        if name_ not in found_names and name_ != "Unknown":
            found_names.append(name_)

        cv2.putText(frame, name_, (left + 6, bottom-6),
                    font, 1.0, (0, 0, 255), 1)

    cv2.imshow('Video', frame)

    # cv2.imshow('Crop', crop)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        fp = open('attendance.txt', 'w+')

        fp.write('In class:\n')

        for student in found_names:
            if student in students:
                fp.write(student + '\n')
                students.remove(student)

        fp.write('\nNot here:\n')

        for student in students:
            fp.write(student + '\n')
        fp.close()
        send_mail.send()
        break

vid.release()
cv2.destroyAllWindows()
