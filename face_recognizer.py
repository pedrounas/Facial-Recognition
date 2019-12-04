import cv2
import os
import sys
import numpy as np
import face_recognition
import smtplib
import ssl
from datetime import date


def send():

    gmail_user = 'missing.students.cv'
    # problema de segurança, pass do mail do sender em plaintext
    gmail_password = '52S[rheG'

    sent_from = 'missing.students.cv@gmail.com'
    # to = ['saraferreira.p3@gmail.com', 'pedrommunas@gmail.com']
    to = ['missing.students.cv@gmail.com']  # Para testar
    subject = 'Attendence for the class of ' + \
        str(date.today().strftime("%d/%m/%Y"))
    body = None

    with open('./attendance.txt') as fp:
        body = fp.read()

    message = """\
    From: %s
    To: %s
    Subject: %s
    \n\n%s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(
            sent_from,
            sent_from,
            message)
        server.quit()
        print('Email sent!')

    except:
        print('Something went wrong...')


# vid = cv2.VideoCapture('http://192.168.1.4:8080/video')
vid = cv2.VideoCapture(0)

path = './test/'
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
    if file.endswith('.jpg'):
        x = file.split('.')
        file_names.append(path + file)
        names.append(x[0])

for file in file_names:
    if file.endswith('.jpg'):
        temp = face_recognition.load_image_file(file)
        if face_recognition.face_encodings(temp):
            encodings.append(face_recognition.face_encodings(temp)[0])
            print(file)


file = open('students.txt', 'r')
for line in file:
    students.append(line.rstrip('\n'))

cv2.namedWindow('Video', cv2.WINDOW_AUTOSIZE)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

while True:

    ret, frame = vid.read()

    crop = None

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_frame:
        face_names = []
        face_locations = face_recognition.face_locations(
            rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, known_face_locations=face_locations)

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

        cv2.rectangle(frame, (left, top), (right, bottom),
                      (0, 0, 255), 1)

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
        # send()
        break

vid.release()
cv2.destroyAllWindows()
