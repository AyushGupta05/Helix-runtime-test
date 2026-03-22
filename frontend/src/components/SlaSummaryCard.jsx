function SlaSummaryCard({ label, value, tone }) {
  const colors = {
    warn: { background: "#ffedd5", color: "#9a3412" },
    danger: { background: "#fee2e2", color: "#991b1b" },
    neutral: { background: "#e2e8f0", color: "#0f172a" },
  };

  return (
    <article
      className="panel"
      style={{
        padding: 20,
        borderRadius: 20,
        background: colors[tone].background,
        color: colors[tone].color,
      }}
    >
      <p style={{ margin: 0, fontSize: 14, textTransform: "uppercase", letterSpacing: "0.08em" }}>
        {label}
      </p>
      <p style={{ margin: "8px 0 0", fontSize: 34, fontWeight: 700 }}>{value}</p>
    </article>
  );
}

export default SlaSummaryCard;

