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

### 1. Create virtual environment

```bash
python3 -m venv faceenv
source faceenv/bin/activate
