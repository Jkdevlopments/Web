const TaskCard = ({ dueDate, completedAtDate, assigneeName, status }) => (
  <div className="task-card">
    {status === "Pending" && (
      <>
        <p>Due Date: {dueDate}</p>
        <p>Assignee: {assigneeName}</p>
      </>
    )}
    {status === "Done" && (
      <>
        <p>Completed On: {completedAtDate}</p>
        <p>Assignee: {assigneeName}</p>
      </>
    )}
  </div>
);
