import { render, screen } from "@testing-library/react";
import App from "./App";

describe("App", () => {
  it("renders the dashboard navigation", () => {
    render(<App />);
    expect(screen.getByText("Support Ops")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Dashboard" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Settings" })).toBeInTheDocument();
  });
});
