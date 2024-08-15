import './TaskCard.css';

const TaskCard = ({ dueDate, completedAtDate, assigneeName, status }) => (
  <div className="task-card">
    {status === "Pending" && (
      <>
        <p className="due-date">Due Date: {dueDate}</p>
        <p className="assignee">Assignee: {assigneeName}</p>
      </>
    )}
    {status === "Done" && (
      <>
        <p className="completed-date">Completed On: {completedAtDate}</p>
        <p className="assignee">Assignee: {assigneeName}</p>
      </>
    )}
  </div>
);
