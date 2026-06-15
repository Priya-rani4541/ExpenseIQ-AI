import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>ExpenseIQ AI</h1>

      <p>
        AI Powered Expense Management System
      </p>

      <hr />

      <h2>Features</h2>

      <ul>
        <li>CSV Expense Upload</li>
        <li>Expense Tracking</li>
        <li>Smart Analytics</li>
        <li>AI Insights</li>
      </ul>

      <hr />

      <h2>Backend APIs</h2>

      <a
        href="https://expenseiq-ai.onrender.com/api/expenses/"
        target="_blank"
      >
        View Expenses
      </a>

      <br />
      <br />

      <a
        href="https://expenseiq-ai.onrender.com/api/imports/upload/"
        target="_blank"
      >
        Upload CSV
      </a>
    </div>
  );
}

export default App;