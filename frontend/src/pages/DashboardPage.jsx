import { useEffect, useMemo, useState } from "react";
import FilterBar from "../components/FilterBar";
import SlaSummaryCard from "../components/SlaSummaryCard";
import TicketTable from "../components/TicketTable";
import { fetchTicketSummary, fetchTickets } from "../lib/api";

function DashboardPage() {
  const [tickets, setTickets] = useState([]);
  const [summary, setSummary] = useState(null);
  const [filters, setFilters] = useState({ status: "all", priority: "all" });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError("");

      try {
        const [ticketData, summaryData] = await Promise.all([
          fetchTickets(),
          fetchTicketSummary({
            status: filters.status === "all" ? null : filters.status,
            priority: filters.priority === "all" ? null : filters.priority,
          }),
        ]);
        setTickets(ticketData);
        setSummary(summaryData);
      } catch (loadError) {
        setError(loadError.message);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [filters]);

  const filteredTickets = useMemo(() => {
    return tickets.filter((ticket) => {
      const matchesStatus =
        filters.status === "all" || ticket.status === filters.status;
      const matchesPriority =
        filters.priority === "all" || ticket.priority === filters.priority;
      return matchesStatus && matchesPriority;
    });
  }, [filters, tickets]);

  return (
    <section>
      <div className="page-header">
        <div>
          <h2>Support Queue</h2>
          <p>
            Monitor first-response commitments, triage urgent work, and keep an
            eye on the ticket mix for the current shift.
          </p>
        </div>
        <div className="status-pill">
          {filteredTickets.length} visible ticket
          {filteredTickets.length === 1 ? "" : "s"}
        </div>
      </div>

      <div className="panel" style={{ marginBottom: 20 }}>
        <FilterBar filters={filters} onChange={setFilters} />
      </div>

      {error ? <p role="alert">{error}</p> : null}
      {loading ? <p>Loading support queue...</p> : null}

      {!loading && summary ? (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))",
            gap: 16,
            marginBottom: 20,
          }}
        >
          <SlaSummaryCard label="At risk" value={summary.at_risk} tone="warn" />
          <SlaSummaryCard label="Overdue" value={summary.overdue} tone="danger" />
          <SlaSummaryCard
            label="Open workload"
            value={summary.open_tickets}
            tone="neutral"
          />
        </div>
      ) : null}

      {!loading ? <TicketTable tickets={filteredTickets} /> : null}
    </section>
  );
}

export default DashboardPage;

