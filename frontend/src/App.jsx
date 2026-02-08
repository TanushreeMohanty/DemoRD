import { useState, useEffect } from 'react';
import axios from 'axios';

// Change this from localhost to your new Render URL
const API_URL = "https://demord-xg4s.onrender.com/api/todos/";
function App() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    axios.get(API_URL).then(res => setTodos(res.data));
  }, []);

  const addTodo = () => {
    axios.post(API_URL, { title: input, completed: false })
      .then(res => setTodos([...todos, res.data]));
    setInput("");
  };

  return (
    <div>
      <h1>Simple To-Do</h1>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={addTodo}>Add</button>
      <ul>
        {todos.map(t => <li key={t.id}>{t.title}</li>)}
      </ul>
    </div>
  );
}
export default App;