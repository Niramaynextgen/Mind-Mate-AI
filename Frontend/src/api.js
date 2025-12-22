const BASE_URL = process.env.REACT_APP_API_URL || "https://mind-mate-ai-production-51a0.up.railway.app";

export const sendText = async (userId, text) => {
  try {
    const res = await fetch(`${BASE_URL}/mindmate`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_id: userId, text }),
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`Backend error: ${errText}`);
    }

    const data = await res.json(); 
    return data;
  } catch (err) {
    console.error("Error in sendText:", err);
    throw err;
  }
};

export const sendAudio = async (userId, audioBlob) => {
  try {
    const textFromAudio = "[🎤 Voice message]";
    return sendText(userId, textFromAudio);
  } catch (err) {
    console.error("Error in sendAudio:", err);
    throw err;
  }
};
