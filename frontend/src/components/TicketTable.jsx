import { formatDate } from "../lib/format";

function TicketTable({ tickets }) {
  return (
    <div className="panel" style={{ overflowX: "auto" }}>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th align="left">Ticket</th>
            <th align="left">Customer</th>
            <th align="left">Status</th>
            <th align="left">Priority</th>
            <th align="left">First response due</th>
            <th align="left">Owner</th>
          </tr>
        </thead>
        <tbody>
          {tickets.map((ticket) => (
            <tr key={ticket.id}>
              <td style={{ padding: "12px 0" }}>{ticket.id}</td>
              <td>{ticket.customer}</td>
              <td style={{ textTransform: "capitalize" }}>{ticket.status}</td>
              <td style={{ textTransform: "capitalize" }}>{ticket.priority}</td>
              <td>{formatDate(ticket.first_response_due_at)}</td>
              <td>{ticket.assigned_to}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TicketTable;

