import { useEffect, useState } from "react";
import { fetchSettings, saveSettings } from "../lib/api";

const initialSettings = {
  webhook_url: "",
  retry_enabled: true,
  retry_delay_seconds: 30,
  max_retries: 3,
};

function SettingsPage() {
  const [settings, setSettings] = useState(initialSettings);
  const [savedState, setSavedState] = useState("idle");
  const [error, setError] = useState("");

  useEffect(() => {
    async function load() {
      try {
        const response = await fetchSettings();
        setSettings(response);
      } catch (loadError) {
        setError(loadError.message);
      }
    }

    load();
  }, []);

  async function handleSubmit(event) {
    event.preventDefault();
    setSavedState("saving");
    setError("");

    try {
      const response = await saveSettings(settings);
      setSettings(response);
      setSavedState("saved");
    } catch (saveError) {
      setError(saveError.message);
      setSavedState("idle");
    }
  }

  function updateField(field, value) {
    setSettings((current) => ({ ...current, [field]: value }));
  }

  return (
    <section>
      <div className="page-header">
        <div>
          <h2>Webhook Settings</h2>
          <p>
            Configure how support events are pushed to internal systems when
            ticket activity changes.
          </p>
        </div>
        <div className="status-pill">
          {savedState === "saved" ? "Saved" : "Unsaved changes"}
        </div>
      </div>

      <form className="panel" onSubmit={handleSubmit}>
        <div style={{ display: "grid", gap: 18 }}>
          <label>
            Webhook URL
            <input
              style={{ width: "100%", marginTop: 8 }}
              type="url"
              value={settings.webhook_url}
              onChange={(event) => updateField("webhook_url", event.target.value)}
            />
          </label>

          <label>
            Retry delay (seconds)
            <input
              style={{ width: "100%", marginTop: 8 }}
              type="number"
              min="1"
              value={settings.retry_delay_seconds}
              onChange={(event) =>
                updateField("retry_delay_seconds", Number(event.target.value))
              }
            />
          </label>

          <label>
            Max retries
            <input
              style={{ width: "100%", marginTop: 8 }}
              type="number"
              min="1"
              max="10"
              value={settings.max_retries}
              onChange={(event) =>
                updateField("max_retries", Number(event.target.value))
              }
            />
          </label>

          <label style={{ display: "flex", gap: 10, alignItems: "center" }}>
            <input
              type="checkbox"
              checked={settings.retry_enabled}
              onChange={(event) =>
                updateField("retry_enabled", event.target.checked)
              }
            />
            Retry failed webhook deliveries
          </label>
        </div>

        <div style={{ marginTop: 20, display: "flex", gap: 12, alignItems: "center" }}>
          <button type="submit">Save settings</button>
          {savedState === "saving" ? <span>Saving...</span> : null}
          {savedState === "saved" ? <span>Changes saved.</span> : null}
          {error ? <span role="alert">{error}</span> : null}
        </div>
      </form>
    </section>
  );
}

export default SettingsPage;

