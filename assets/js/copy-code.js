document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("pre").forEach((pre) => {
    const code = pre.querySelector("code");
    if (!code || pre.closest(".mcix-code-snippet")) return;

    const wrapper = document.createElement("div");
    wrapper.className = "mcix-code-snippet cds--snippet cds--snippet--multi";

    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);

    const button = document.createElement("button");
    button.className = "mcix-copy-button cds--copy-btn";
    button.type = "button";
    button.setAttribute("aria-label", "Copy code");
    button.setAttribute("title", "Copy code");

    button.innerHTML = `
      <svg
        class="mcix-copy-icon"
        focusable="false"
        preserveAspectRatio="xMidYMid meet"
        fill="currentColor"
        width="16"
        height="16"
        viewBox="0 0 32 32"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg">
        <path d="M28,10V28H10V10H28M28,8H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z"></path>
        <path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z"></path>
      </svg>
    `;

    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(code.innerText);

        button.classList.add("mcix-copy-button--copied");
        button.setAttribute("aria-label", "Copied");
        button.setAttribute("title", "Copied");

        setTimeout(() => {
          button.classList.remove("mcix-copy-button--copied");
          button.setAttribute("aria-label", "Copy code");
          button.setAttribute("title", "Copy code");
        }, 2000);
      } catch (err) {
        button.setAttribute("aria-label", "Copy failed");
        button.setAttribute("title", "Copy failed");
      }
    });

    wrapper.appendChild(button);
  });
});