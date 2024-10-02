import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSpeechRecognition = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/recognize-speech', {
        method: 'POST',
      });
      const data = await response.json();
      setText(data.text);
      handleGeminiResponse(data.text);
    } catch (error) {
      console.error('Error recognizing speech:', error);
      setOutput('Error recognizing speech.');
    }
    setLoading(false);
  };

  const handleGeminiResponse = async (prompt) => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/gemini-response', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });
      const data = await response.json();
      if (data.response) {
        setOutput(data.response);
      } else {
        setOutput('No response from Gemini.');
      }
    } catch (error) {
      console.error('Error getting Gemini response:', error);
      setOutput('Error getting Gemini response.');
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Voice to Chat</h1>
      <button onClick={handleSpeechRecognition} disabled={loading}>
        {loading ? 'Processing...' : 'Start Speech Recognition'}
      </button>

      {text && <div className="output"><h3>Recognized Speech:</h3><p>{text}</p></div>}
      
      {output && (
        <div className="output">
          <h3>Gemini Response:</h3>
          <ReactMarkdown>{output}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;
