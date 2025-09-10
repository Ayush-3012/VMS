# Video Management System (VMS) with AI Integration

## 📖 Project Overview

This project is a lightweight **Video Management System (VMS)** designed to handle multiple video inputs and perform AI-based inferences such as face and person detection in real-time. The backend is built using **FastAPI**, while the frontend uses **React (Vite)** to display video streams, detection results, and alerts. The system is designed to be scalable and efficient without relying on heavy external AI models.

---

## ✅ Features

- ✅ Handles multiple video inputs simultaneously
- ✅ Performs face and person detection using OpenCV Haar cascades
- ✅ Real-time frame processing and inference results
- ✅ Dynamic alerts based on detected objects
- ✅ Simple and responsive dashboard built with React
- ✅ CORS-enabled for seamless frontend-backend communication
- ✅ Easy-to-deploy architecture using AWS services

---

## 📂 Project Structure

root/
├── backend/
│ ├── app/
│ │ └── api_video_results.py
│ ├── data/
│ │ ├── sample_video.mp4
│ │ ├── sample_video2.mp4
│ │ ├── sample_video3.mp4
│ │ └── sample_video4.mp4
│ └── venv/
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ └── VideoStream.jsx
│ │ └── services/
│ │ └── api.js
│ └── vite.config.js
└── README.md

## 🚀 Setup Instructions

### 🟠 Backend Setup (FastAPI)

1. Install Python (version 3.8 or later) from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv\Scripts\activate
   pip install -r requirements.txt
   ```
Install the required dependencies:
bash
Copy code

```bash
pip install fastapi uvicorn python-multipart opencv-python
```

Place your sample video files inside the backend/data/ directory.

Run the backend server:

Copy code

```bash
uvicorn app.api_video_results:app --reload
```

Verify the API by visiting:

Copy code

```bash
http://127.0.0.1:8000/results
```

### 🟠 Frontend Setup (React with Vite)

Install Node.js (version 16 or later) from https://nodejs.org/en/download/

Initialize the project:

Copy code

```bash
npm create vite@latest my-vms --template react
cd my-vms
npm install
```

Create the API service in src/services/api.js:

javascript
Copy code

```bash
export async function getResults() {
const response = await fetch("http://127.0.0.1:8000/results");
return await response.json();
}
```

Implement the VideoStream.jsx component inside src/components/ and import it in App.jsx.

Run the development server:

Copy code

```bash
npm run dev
```

Open the app in your browser:

```bash
http://localhost:5173
```
