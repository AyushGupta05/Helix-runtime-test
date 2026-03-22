import { useState } from "react";
import DashboardPage from "./pages/DashboardPage";
import SettingsPage from "./pages/SettingsPage";
import "./App.css";

const tabs = [
  { id: "dashboard", label: "Dashboard" },
  { id: "settings", label: "Settings" },
];

function App() {
  const [activeTab, setActiveTab] = useState("dashboard");

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div>
          <p className="eyebrow">Internal Tooling</p>
          <h1>Support Ops</h1>
          <p className="sidebar-copy">
            Review incoming customer issues, watch SLA risk, and manage webhook
            delivery settings.
          </p>
        </div>
        <nav className="nav-list" aria-label="Primary">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              className={activeTab === tab.id ? "nav-item active" : "nav-item"}
              onClick={() => setActiveTab(tab.id)}
              type="button"
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </aside>
      <main className="content-panel">
        {activeTab === "dashboard" ? <DashboardPage /> : <SettingsPage />}
      </main>
    </div>
  );
}

export default App;

