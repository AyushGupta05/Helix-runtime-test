const statuses = ["all", "open", "pending", "resolved"];
const priorities = ["all", "low", "medium", "high", "urgent"];

function FilterBar({ filters, onChange }) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
        gap: 16,
      }}
    >
      <label>
        Status
        <select
          style={{ width: "100%", marginTop: 8 }}
          value={filters.status}
          onChange={(event) =>
            onChange((current) => ({ ...current, status: event.target.value }))
          }
        >
          {statuses.map((status) => (
            <option key={status} value={status}>
              {status}
            </option>
          ))}
        </select>
      </label>

      <label>
        Priority
        <select
          style={{ width: "100%", marginTop: 8 }}
          value={filters.priority}
          onChange={(event) =>
            onChange((current) => ({ ...current, priority: event.target.value }))
          }
        >
          {priorities.map((priority) => (
            <option key={priority} value={priority}>
              {priority}
            </option>
          ))}
        </select>
      </label>
    </div>
  );
}

export default FilterBar;

