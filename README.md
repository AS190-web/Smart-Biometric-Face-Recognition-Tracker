# Smart Biometric Face Recognition Tracker

## 📌 Project Overview
The **Automated Biometric Face Tracking System** is an offline computer vision–based application designed to automate attendance tracking using facial recognition. The system captures live video through a webcam, detects faces in real time, recognizes registered individuals, and marks their attendance automatically in both CSV files and a MySQL database. The project is developed using Python and OpenCV and is suitable for academic institutions requiring a contactless and efficient attendance solution.

---

## 🎯 Objectives
- Eliminate manual and proxy attendance
- Provide a contactless biometric attendance system
- Ensure accurate identity verification using facial features
- Store attendance records digitally for easy access and analysis
- Operate completely offline without internet dependency

---

## 🛠️ Technologies Used
- **Programming Language:** Python 3.13  
- **Libraries:** OpenCV, NumPy, MySQL Connector  
- **Database:** MySQL 9.5 command line client 
- **Face Detection:** Haar Cascade Classifier  
- **Face Recognition:** LBPH (Local Binary Pattern Histogram)  
- **Platform:** Windows OS  
- **Hardware:** Webcam  

---

## 📂 Project Structure
```text
Smart-Biometric-Face-Recognition-Tracker/
│
├── 01_face_detection.py        # Camera & face detection test
├── 02_capture_faces.py         # Dataset creation module
├── 03_train_model.py           # LBPH model training
├── 04_face_recognition.py      # Live recognition & attendance
├── mysql_test.py               # Database connectivity test
│
├── haarcascade_frontalface_default.xml
├── attendance.csv              # Sample attendance output
│
├── dataset/                    # Face images (ignored in GitHub)
│
├── README.md
├── LICENSE
├── .gitignore



