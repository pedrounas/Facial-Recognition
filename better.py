import cv2, os, sys
import numpy as np
import face_recognition

vid = cv2.VideoCapture('http://192.168.1.4:8080/video')

path = './known'
files = os.listdir(path)
names = []
file_names = []
encodings = []

for file in files:
    x = file.split('.')
    file_names.append('./known/' + file)
    names.append(x[0])

for file in file_names:
    temp = face_recognition.load_image_file(file)
    encodings.append(face_recognition.face_encodings(temp)[0])

process_frame = True
face_locations = []
face_names = []
face_encodings = []

while True:

    ret, frame = vid.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []

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

        cv2.rectangle(frame, (left, top), (right, bottom),
                      (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_DUPLEX
        name_ = name.replace("_", " ")
        cv2.putText(frame, name_, (left + 6, bottom-6),
                    font, 1.0, (0, 0, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
