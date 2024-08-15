import React from 'react';
import './TaskCard.css'; // Import the CSS specific to TaskCard

function TaskCard({ title, description }) {
  return (
    <div className="task-card">
      <h2 className="task-card-title">{title}</h2>
      <p className="task-card-description">{description}</p>
    </div>
  );
}

export default TaskCard;
