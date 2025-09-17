// import React, { useState } from 'react';
// import axios from 'axios';
// import { Card, CardContent } from '@/components/ui/card';
// import { Input } from '@/components/ui/input';
// import { Button } from '@/components/ui/button';
// import { Loader2 } from 'lucide-react';
// import { Bar } from 'react-chartjs-2';
// import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from 'chart.js';

// ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

// const Chatbot = () => {
//   const [query, setQuery] = useState('');
//   const [response, setResponse] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleQuery = async () => {
//     if (!query.trim()) return;
//     setLoading(true);
//     try {
//       const res = await axios.post('http://localhost:8000/query', { query });
//       setResponse(res.data.response);
//     } catch (error) {
//       setResponse({
//         type: 'text',
//         content: '⚠️ Error: Could not fetch response. Please try again later.',
//       });
//     } finally {
//       setLoading(false);
//     }
//   };

//   const renderResponse = () => {
//     if (!response) return null;

//     // Case: Plain Text (string or object)
//     if (typeof response === 'string') {
//       return (
//         <pre className="bg-gray-900 text-green-300 p-4 rounded-md overflow-x-auto">
//           {response}
//         </pre>
//       );
//     }

//     // Case: Text Response with explicit type
//     if (response.type === 'text') {
//       return (
//         <pre className="bg-gray-900 text-green-300 p-4 rounded-md overflow-x-auto whitespace-pre-wrap">
//           {response.content}
//         </pre>
//       );
//     }

//     // Case: Table Output
//     if (response.type === 'table') {
//       return (
//         <div className="overflow-x-auto">
//           <table className="min-w-full border border-gray-300 text-sm text-left">
//             <thead className="bg-gray-200">
//               <tr>
//                 {response.columns.map((col, i) => (
//                   <th key={i} className="px-4 py-2 border font-semibold">{col}</th>
//                 ))}
//               </tr>
//             </thead>
//             <tbody>
//               {response.data.map((row, i) => (
//                 <tr key={i} className={i % 2 === 0 ? 'bg-white' : 'bg-gray-50'}>
//                   {row.map((cell, j) => (
//                     <td key={j} className="px-4 py-2 border">{cell}</td>
//                   ))}
//                 </tr>
//               ))}
//             </tbody>
//           </table>
//         </div>
//       );
//     }

//     // Case: Chart Output
//     if (response.type === 'chart') {
//       const data = {
//         labels: response.labels,
//         datasets: [
//           {
//             label: response.title || 'Data',
//             data: response.values,
//             backgroundColor: 'rgba(75, 192, 192, 0.5)',
//             borderColor: 'rgba(75, 192, 192, 1)',
//             borderWidth: 1,
//           },
//         ],
//       };

//       const options = {
//         responsive: true,
//         plugins: {
//           legend: {
//             display: true,
//             position: 'top',
//           },
//         },
//       };

//       return <Bar data={data} options={options} />;
//     }

//     // Fallback
//     return (
//       <pre className="bg-yellow-100 text-yellow-800 p-4 rounded-md overflow-x-auto">
//         {JSON.stringify(response, null, 2)}
//       </pre>
//     );
//   };

//   const handleKeyPress = (e) => {
//     if (e.key === 'Enter') handleQuery();
//   };

//   return (
//     <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
//       <Card className="w-full max-w-2xl p-6 shadow-xl">
//         <h2 className="text-xl font-semibold mb-4">🛒 E-commerce Chatbot</h2>
//         <Input
//           type="text"
//           value={query}
//           onChange={(e) => setQuery(e.target.value)}
//           onKeyDown={handleKeyPress}
//           placeholder="Ask your query here..."
//           className="mb-4"
//         />
//         <Button onClick={handleQuery} disabled={loading} className="mb-4">
//           {loading ? <Loader2 className="animate-spin" /> : 'Ask'}
//         </Button>
//         <CardContent className="mt-2 bg-white p-4 rounded shadow-inner w-full">
//           <h4 className="font-medium mb-2">📬 Response:</h4>
//           {renderResponse()}
//         </CardContent>
//       </Card>
//     </div>
//   );
// };

// export default Chatbot;


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
      return <pre className="formatted-text">{response}</pre>;
    }

    if (response.type === 'table') {
      return (
        <div className="response-box-scroll">
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
        </div>
      );
    }

    if (response.type === 'chart') {
      const data = {
        labels: response.labels,
        datasets: [
          {
            label: response.title || 'Chart',
            data: response.values,
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
          },
        ],
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
            {renderResponse()}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
