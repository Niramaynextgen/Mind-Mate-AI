import React from "react";
import { useNavigate } from "react-router-dom";
import "./Landing.css";

export default function Landing() {
  const navigate = useNavigate();

  return (
    <div className="landing-container">
      <div className="overlay"></div>

      <div className="content">
        <h1 className="title">MindMate</h1>
        <p className="subtitle">
          Your AI-powered emotional wellness companion ❤
        </p>

        <button
          className="start-btn"
          onClick={() => navigate("/chat")}
        >
          Start Chatting 🚀
        </button>
      </div>
    </div>
  );
}