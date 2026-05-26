# 🛡️ Face Guard Mac — AI Smart Security System

An AI-based MacBook security system that uses face recognition to:

- Detect authorized user
- Detect unknown person
- Lock Mac automatically
- Detect user return after lock
- Show smart notifications

---

## 🚀 Features

✔ Real-time face recognition  
✔ Auto lock on unknown detection  
✔ Smart “welcome back” detection  
✔ Works with MacBook built-in camera  
✔ Fully offline (no cloud API)

---

## 🧠 How It Works

1. System learns your face from `myface.jpg`
2. Webcam continuously scans faces
3. If unknown person detected → timer starts
4. If unknown persists → Mac locks
5. If you return → system detects and welcomes you

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/yourusername/face-guard-mac.git
cd face-guard-mac

```
### 2. Create virtual environment
```bash
python3 -m venv faceenv
source faceenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 📦 requirements.txt
```bash
opencv-python
face_recognition
numpy
pillow
```
### 📸 Setup Face Recognition
Capture a clear image of your face
Save it as:
myface.jpg

### Place it inside project folder
▶️ Run Project
```bash
python face_guard.py
```

### 🔐 macOS Permissions Required

Enable:

Camera access for Terminal
Accessibility permissions

Path:
System Settings → Privacy & Security

### ⚠️ Notes
Works best in good lighting
Uses MacBook built-in camera
iPhone Continuity Camera may interfere
First run may require permissions

### 🛠️ Future Improvements
Face unlock system (TouchID-style simulation)
Multi-user recognition
Telegram alerts for intruders
Background daemon mode
Invisible security mode
### 👨‍💻 Author

Built by Vishal using Python, OpenCV, and face_recognition AI library.
