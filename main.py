# Import necessary libraries
import cv2  # OpenCV library for image/video processing
from deepface import DeepFace  # DeepFace library for face recognition
import pandas as pd  # Pandas library for data manipulation
from datetime import datetime  # datetime module for working with dates and times
import os  # os module for interacting with the operating system

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Set the model you can change the model as per your need (VGG-Face, Facenet, OpenFace, DeepFace, DeepID, Dlib)
# I have chosen Facenet for this particular case
model = 'Facenet'

# Create a DataFrame to store the attendance data
df = pd.DataFrame(columns=['Name', 'Timestamp'])

# Set the folder for storing unknown faces
unknown_faces_folder = 'unknown_faces'
if not os.path.exists(unknown_faces_folder):
    os.makedirs(unknown_faces_folder)

# Function to recognize a face from a given folder
def recognize_face(frame, folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                result = DeepFace.verify(frame, file_path, model_name=model)
                if result['distance'] < 0.5:
                    return filename.split('.')[0]
    return None

# Set the folder path containing known faces
folder_path = 'MYDB'

# Main loop for face recognition and attendance tracking
while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        face_image = DeepFace.extract_faces(frame)
        if face_image is None:
            continue

        name = recognize_face(frame, folder_path)
        if name:
            df.loc[len(df)] = [name, datetime.now()]  # Saving the attendance data to a CSV file
            df.to_csv('attendance.csv', index=False)
        else:
            print('Unknown face')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            cv2.imwrite(os.path.join(unknown_faces_folder, f'unknown_{timestamp}.jpg'), frame)

    except Exception as e:
        print(e)
        pass

    if cv2.waitKey(1) != -1:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()