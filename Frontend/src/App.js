import { BrowserRouter, Routes, Route } from "react-router-dom";
import Chat from "./components/Chat";
import Landing from "./pages/Landing";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/chat" element={<Chat userId="user123" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;