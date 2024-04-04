# Attendance System using Face Recognition

This project is an attendance system that uses face recognition to identify individuals and record their attendance with timestamps. It utilizes the OpenCV and DeepFace libraries for video capture, image processing, and face recognition.

## Features

- Captures video from the default camera.
- Extracts faces from the captured frames.
- Compares the extracted faces with a database of known faces.
- Records the attendance data (name and timestamp) for recognized faces.
- Saves unknown faces in a separate folder.
- Saves the attendance data to a CSV file (`attendance.csv`).

Install the required packages using the following command:
pip install requirements.txt

**Warning:** DeepFace is compatible with TensorFlow version 2.15. Make sure you have the correct version of TensorFlow installed.

## Usage

1. Clone the repository or download the source code.
2. Place the images of known faces in the `MYDB` folder (modify the folder path in the code if needed).
3. Run the `main.py` script.
4. The application will start capturing video from the default camera.
5. Recognized faces will be recorded in the `attendance.csv` file with their names and timestamps.
6. Unknown faces will be saved in the `unknown_faces` folder with a timestamp as the filename.
7. Press any key to exit the application.

## Configuration

You can modify the following settings in the code:

- Change the `model` variable to use a different face recognition model (e.g., VGG-Face, OpenFace, DeepFace, DeepID, Dlib).
- Modify the `folder_path` variable to point to the folder containing known faces.
- Adjust the distance threshold in the `recognize_face` function to change the sensitivity of face recognition.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.