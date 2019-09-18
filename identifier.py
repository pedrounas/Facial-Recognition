import face_recognition
import os
import sys
from PIL import Image, ImageDraw

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
    
# Load test image to find faces in
test_image = face_recognition.load_image_file(sys.argv[1])

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(encodings, face_encoding)

    name = "Unknown Person"

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = names[first_match_index]
        name_ = name.replace("_", " ")
        break

if name != "Unknown Person":
    print("Found a match by the name of " + name_)

    # Draw box
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))

    # Draw label
    text_width, text_height = draw.textsize(name_)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
                fill=(255, 0, 0), outline=(255, 0, 0))
    draw.text((left + 6, bottom - text_height - 5), name_, fill=(0, 0, 0))

    del draw

    # # Display image
    pil_image.show()

    # Save image
    pil_image.save('result.jpg')

else:
    print("No match found!")
