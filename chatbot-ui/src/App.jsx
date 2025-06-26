import { useState } from 'react';
import './App.css';
import Robot from './assets/robot.png';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from 'chart.js';
ChartJS.register(BarElement, CategoryScale, LinearScale);
function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const sendQuery = async () => {
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse({ type: 'text', content: 'Error: Could not reach FastAPI backend.' });
    }
    setLoading(false);
  };
  const renderResponse = () => {
    if (!response) return null;
    if (typeof response === 'string') {
      return <pre>{response}</pre>;
    }
    if (response.type === 'table') {
      return (
        <table className="response-table">
          <thead>
            <tr>
              {response.columns.map((col, i) => (
                <th key={i}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {response.data.map((row, i) => (
              <tr key={i}>
                {row.map((cell, j) => (
                  <td key={j}>{cell}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      );
    }
    if (response.type === 'chart') {
      const data = {
        labels: response.labels,
        datasets: [{
          label: response.title || 'Chart',
          data: response.values,
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
        }],
      };
      return <Bar data={data} />;
    }
    return <pre>{JSON.stringify(response, null, 2)}</pre>;
  };
  return (
    <div className="app-container">
      <div className="left-panel">
        <img src={Robot} alt="Robot" className="robot" />
        <h1>Hi, I'm Robo!</h1>
        <p>Your Ecom Assistant</p>
      </div>
      <div className="right-panel">
        <h1>Ecom Customer Support Chatbot</h1>
        <div className="chat-container">
          <textarea
            rows="3"
            placeholder="Ask your question here..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button onClick={sendQuery} disabled={loading}>
            {loading ? 'Processing...' : 'Send'}
          </button>
          <div className="response-box">
          <h3>Response:</h3>
          <div style={{ overflowX: 'auto' }}>
            {renderResponse()}
          </div>
        </div>
        </div>
      </div>
    </div>
  );
}

export default App;
