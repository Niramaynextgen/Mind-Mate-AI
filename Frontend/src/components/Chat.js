import React, { useState, useRef, useEffect } from "react";
import { sendText, sendAudio } from "../api";
import "./Chat.css";

export default function Chat({ userId }) {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [loading, setLoading] = useState(false);
  const [recording, setRecording] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  const handleSendText = async () => {
    if (!message.trim()) return;
    const userMsg = message;
    setMessage("");

    setChat((prev) => [...prev, { sender: "user", text: userMsg }]);
    setLoading(true);

    try {
      const res = await sendText(userId, userMsg);
      console.log("Backend response:", res);

      setChat((prev) => [
        ...prev,
        { sender: "bot", text: res.ai_reply, audio: res.audio_base64 },
      ]);

      if (res.audio_base64) {
        const audio = new Audio("data:audio/wav;base64," + res.audio_base64);
        audio.play().catch((err) => console.error("Audio play error:", err));
      }

    } catch (err) {
      console.error("Send Text Error:", err);
    }

    setLoading(false);
  };

  const startRecording = async () => {
    setRecording(true);
    audioChunksRef.current = [];

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);

      mediaRecorderRef.current.ondataavailable = (e) =>
        audioChunksRef.current.push(e.data);

      mediaRecorderRef.current.onstop = sendRecordedAudio;
      mediaRecorderRef.current.start();
    } catch (err) {
      console.error("Microphone access error:", err);
      setRecording(false);
    }
  };

  const stopRecording = () => {
    setRecording(false);
    mediaRecorderRef.current.stop();
  };

  const sendRecordedAudio = async () => {
    const audioBlob = new Blob(audioChunksRef.current, { type: "audio/webm" });

    setChat((prev) => [...prev, { sender: "user", text: "[🎤 Voice message]" }]);
    setLoading(true);

    try {
      const res = await sendAudio(userId, audioBlob);
      console.log("Backend response (audio):", res);

      setChat((prev) => [
        ...prev,
        { sender: "bot", text: res.ai_reply, audio: res.audio_base64 },
      ]);

      if (res.audio_base64) {
        const audio = new Audio("data:audio/wav;base64," + res.audio_base64);
        audio.play().catch((err) => console.error("Audio play error:", err));
      }

    } catch (err) {
      console.error("Send Audio Error:", err);
    }

    setLoading(false);
  };

  return (
    <div className={darkMode ? "chat-container dark" : "chat-container"}>
      {}
      <div className="top-bar-modern">
        <button className="back-btn" onClick={() => (window.location.href = "/")}>
          <span className="material-symbols-outlined">home</span>
        </button>

        <h2 className="chat-header-modern">MindMate Chat</h2>

        <button className="dark-toggle" onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "☀ Light" : "🌙 Dark"}
        </button>
      </div>

      {}
      <div className="chat-box-modern">
        {chat.map((msg, i) => (
          <div
            key={i}
            className={msg.sender === "user" ? "user-row" : "bot-row"}
          >
            {msg.sender === "bot" && <div className="bot-avatar">🤖</div>}

            <div
              className={msg.sender === "user" ? "user-bubble" : "bot-bubble"}
            >
              {msg.text}
            </div>
          </div>
        ))}
        {loading && <p className="loading-text">MindMate is typing...</p>}
        <div ref={chatEndRef} />
      </div>

      {}
      <div className="input-area-modern">
        <input
          className="chat-input-modern"
          type="text"
          placeholder="Say something…"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSendText()}
        />

        <button className="send-btn" onClick={handleSendText}>
          <span className="material-symbols-outlined">send</span>
        </button>

        {recording ? (
          <button className="record-btn-active" onClick={stopRecording}>
            <span className="material-symbols-outlined">mic</span>
          </button>
        ) : (
          <button className="record-btn" onClick={startRecording}>
            <span className="material-symbols-outlined">mic</span>
          </button>
        )}
      </div>
    </div>
  );
}
