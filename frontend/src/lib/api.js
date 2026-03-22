const API_BASE_URL = "http://127.0.0.1:8000";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return response.json();
}

export function fetchTickets() {
  return request("/tickets");
}

export function fetchTicketSummary(filters) {
  const params = new URLSearchParams();
  if (filters.status && filters.status !== "all") {
    params.set("status", filters.status);
  }
  if (filters.priority && filters.priority !== "all") {
    params.set("priority", filters.priority);
  }

  return request(`/tickets/summary?${params.toString()}`);
}

export function fetchSettings() {
  return request("/settings");
}

export function saveSettings(payload) {
  return request("/settings", {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

