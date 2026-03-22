export function formatDate(value) {
  return new Date(value).toLocaleString("en-GB", {
    dateStyle: "medium",
    timeStyle: "short",
  });
}
