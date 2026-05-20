function showToast({
  kind = "success",
  title = "Success",
  subtitle = "",
  caption = "Now",
  timeout = 3000
} = {}) {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("cds-toast-notification");

  toast.setAttribute("kind", kind);
  toast.setAttribute("title", title);
  toast.setAttribute("subtitle", subtitle);
  toast.setAttribute("caption", caption);
  toast.setAttribute("close-button-label", "Close notification");
  toast.setAttribute("low-contrast", "");

  container.prepend(toast);

  if (timeout > 0) {
    setTimeout(() => {
      toast.remove();
    }, timeout);
  }
}

function showInlineNotification({
  kind = "info",
  title = "Information",
  subtitle = "",
  lowContrast = true
} = {}) {

  const container = document.getElementById(
    "mcix-inline-notification"
  );

  if (!container) return;

  container.innerHTML = `
    <cds-inline-notification
      kind="${kind}"
      title="${title}"
      subtitle="${subtitle}"
      ${lowContrast ? "low-contrast" : ""}
      hide-close-button>
    </cds-inline-notification>
  `;
}
