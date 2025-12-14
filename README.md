<h1>🧠 Mind Mate – AI</h1>

**Mind Mate – AI** is an emotion-aware voice AI companion designed for students and young adults.

Unlike traditional chatbots that only respond to text, Mind Mate listens to *how* a user speaks — detecting emotional cues and intent — and responds with a natural, human-like voice. The goal is not productivity or automation, but **emotional understanding and short, supportive interventions**.

This project is built for the **Google Cloud + ElevenLabs Hackathon** and focuses on simplicity, creativity, and real-world impact.

---

<h2>🚀 What Problem Are We Solving?</h2> 

Students often experience stress, anxiety, and mental overload but hesitate to open full apps or type long messages.

Mind Mate reduces friction by allowing users to simply **speak** and receive:

* Emotion-aware responses
* Calm and adaptive voice feedback
* Short guided resets (breathing, focus, affirmation)

No long conversations. No data overload. Just quick, human-centered support.

---

## ✨ Key Features

* 🎙️ **Voice-first interaction** (no typing required)
* 🧠 **Emotion & intent detection** using Google Gemini
* 🔊 **Natural voice responses** powered by ElevenLabs
* 🌬️ **One-minute reset rituals** (breathing, grounding, focus)
* 📊 **Optional emotion timeline** (stores only emotion labels, not audio)
* 🔐 **Privacy-first design** (no raw voice storage)

---

## 🏗️ Tech Stack

* **Google Cloud**

  * Gemini (emotion & intent understanding)
  * Speech-to-Text
  * Cloud Run (deployment)

* **ElevenLabs**

  * Text-to-Speech (emotion-matched voice output)

* **Backend**

  * Python
  * FastAPI

* **Frontend**

  * HTML / CSS / JavaScript (simple voice UI)

---

## 🔁 High-Level Architecture

1. User speaks via the web interface
2. Audio is converted to text
3. Google Gemini analyzes emotion & intent
4. Gemini generates an empathetic response
5. ElevenLabs converts the response to voice
6. Voice reply is played back to the user

---

## 👥 Team Members

### **Niramay Shrivastava** *(Research, Backend  Developer & API Integrator)*

* Designed the backend project structure
* Implemented FastAPI application flow
* Integrated Google Gemini APIs
* Integrated ElevenLabs APIs
* Managed request–response lifecycle between services

### **Sachin Rajak** *(Frontend Developer)*

* Designed and developed the frontend user interface
* Implemented voice interaction UI components
* Connected frontend with backend APIs
* Focused on usability and smooth user experience

### **Rishita Chouksey** *(Cloud Deployment & Documentation)*

* Handled cloud deployment setup (Google Cloud / Cloud Run)
* Managed environment configuration and deployment workflow
* Created and maintained project documentation
* Assisted with submission-ready README and Devpost content

### **Yash Sahu** *(API Fetching, Testing & Error Handling)*

* Integrated and tested API calls between frontend and backend
* Handled API response validation and error handling
* Performed end-to-end testing of voice workflows
* Assisted in debugging and quality assurance

---

## 🛠️ Project Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd mind-mate-ai
```

### 2️⃣ Environment Variables

Create a `.env` file using `.env.example` as reference.

```env
GEMINI_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here
```

> ⚠️ Never commit your `.env` file to GitHub.

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Backend

```bash
uvicorn main:app --reload
```

The API will start locally at:

```
http://127.0.0.1:8000
```

---

## 🎥 Demo

A short demo video (≤ 3 minutes) demonstrates:

* Voice input
* Emotion detection
* Adaptive voice response

(Video link will be added after submission.)

---

## 🌱 Learning Outcomes

* Hands-on experience with Google Cloud AI services
* Integrating third-party AI APIs (ElevenLabs)
* Designing emotion-aware AI systems
* Building and deploying a real hackathon-ready application

---

## 📜 License

This project is open-source and intended for educational and hackathon use.

---

## 🙌 Acknowledgements

* Google Cloud
* ElevenLabs
* Devpost Hackathon Platform

---

**Mind Mate – AI**

> *An AI that listens to how you feel — not just what you say.*
