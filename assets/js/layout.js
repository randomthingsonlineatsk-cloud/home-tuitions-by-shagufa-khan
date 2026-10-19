// Renders the shared header + footer into any page that includes a
// <div id="site-header"></div> and <div id="site-footer"></div>.
(function () {
  const bp = SITE_CONFIG.basePath;

  function headerHTML(active) {
    const links = [
      ["index.html", "Home"],
      ["levels.html?band=secondary", "Classes 1-12"],
      ["levels.html?band=neet", "NEET"],
      ["levels.html?band=jee", "JEE"],
      ["levels.html?band=bsc", "B.Sc / M.Sc"],
      ["about.html", "About"],
      ["contact.html", "Contact"],
    ];
    const navItems = links
      .map(([href, label]) => {
        const isActive = active === label;
        return `<a href="${bp}${href}" class="${isActive ? "active" : ""}">${label}</a>`;
      })
      .join("");
    return `
      <div class="bar">
        <a class="brand" href="${bp}index.html">
          <img src="${bp}assets/img/logo.png" alt="logo" onerror="this.style.display='none'">
          <span>Home Tuitions<span class="sub">by Shagufa Khan</span></span>
        </a>
        <nav class="main-nav" id="main-nav">${navItems}</nav>
        <div class="header-social">
          <a class="icon-btn youtube" href="${SITE_CONFIG.youtubeUrl}" target="_blank" rel="noopener" title="YouTube">▶</a>
          <a class="icon-btn insta" href="${SITE_CONFIG.instagramUrl}" target="_blank" rel="noopener" title="Instagram">IG</a>
          <button class="menu-toggle" id="menu-toggle" aria-label="Menu">☰</button>
        </div>
      </div>`;
  }

  function footerHTML() {
    return `
      <div class="container">
        <div class="footer-top">
          <div>
            <h4>Home Tuitions by Shagufa Khan</h4>
            <p style="max-width:320px;color:#a9d9d1;font-size:0.88rem;">
              Free video lessons and downloadable notes for Class 1 to 12, NEET, JEE, B.Sc and M.Sc.
            </p>
          </div>
          <div class="footer-links">
            <h4>Browse</h4>
            <a href="${bp}levels.html?band=secondary">Classes 1-12</a>
            <a href="${bp}levels.html?band=neet">NEET</a>
            <a href="${bp}levels.html?band=jee">JEE</a>
            <a href="${bp}levels.html?band=bsc">B.Sc / M.Sc</a>
          </div>
          <div class="footer-links">
            <h4>Connect</h4>
            <a href="${SITE_CONFIG.youtubeUrl}" target="_blank" rel="noopener">YouTube Channel</a>
            <a href="${SITE_CONFIG.instagramUrl}" target="_blank" rel="noopener">Instagram Page</a>
            <a href="${bp}contact.html">Contact</a>
          </div>
        </div>
        <div class="copyright">© <span id="year"></span> Home Tuitions by Shagufa Khan. Built for students, free, always.</div>
      </div>`;
  }

  window.renderLayout = function (activeLabel) {
    const h = document.getElementById("site-header");
    const f = document.getElementById("site-footer");
    if (h) h.innerHTML = headerHTML(activeLabel);
    if (f) f.innerHTML = footerHTML();
    const y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
    const toggle = document.getElementById("menu-toggle");
    const nav = document.getElementById("main-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", () => nav.classList.toggle("open"));
    }
  };
})();
