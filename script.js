document.addEventListener("DOMContentLoaded", () => {
  const path = window.location.pathname.toLowerCase();
  const pageClassMap = [
    { key: "services", className: "page-services", textMode: "impact-wave" },
    { key: "about", className: "page-about", textMode: "impact-glow" },
    { key: "projects", className: "page-projects", textMode: "impact-wave" },
    { key: "contact", className: "page-contact", textMode: "impact-glow" }
  ];
  const matchedPage = pageClassMap.find((entry) => path.includes(entry.key));
  if (matchedPage) {
    document.body.classList.add(matchedPage.className);
  } else {
    document.body.classList.add("page-home");
  }

  const fileName = path.split("/").pop() || "index.html";
  const guideLinks = [
    { href: "index.html", label: "Home", match: ["index.html", ""] },
    { href: "services.html", label: "Services", match: ["services.html"] },
    { href: "about.html", label: "About", match: ["about.html"] },
    { href: "projects.html", label: "Gallery", match: ["projects.html"] },
    { href: "contact.html", label: "Contact", match: ["contact.html"] }
  ];
  const serviceLinks = [
    { href: "painting.html", label: "Painting" },
    { href: "carpentry.html", label: "Carpentry" },
    { href: "handyman.html", label: "Handyman" },
    { href: "demolition-cleanup.html", label: "Demolition & Cleanup" },
    { href: "flooring-tile.html", label: "Flooring & Tile" },
    { href: "doors-trim-small-projects.html", label: "Doors & Trim" },
    { href: "interior-painting.html", label: "Interior Painting" },
    { href: "exterior-painting.html", label: "Exterior Painting" },
    { href: "millwork.html", label: "Millwork" },
    { href: "cabinetry.html", label: "Cabinetry" },
    { href: "baseboard.html", label: "Baseboard" },
    { href: "trim.html", label: "Trim Work" }
  ];

  const isActiveHref = (href, matchList = [href]) =>
    matchList.some((item) => fileName === item || path.endsWith(`/${item}`));

  const sidebar = document.createElement("aside");
  sidebar.className = "site-guide";
  sidebar.setAttribute("aria-label", "Site guide");
  sidebar.innerHTML = `
    <button class="site-guide-toggle" type="button" aria-expanded="false" aria-controls="site-guide-panel">
      Menu
    </button>
    <div class="site-guide-panel" id="site-guide-panel">
      <p class="site-guide-title">Site Guide</p>
      <nav class="site-guide-nav" aria-label="Main pages">
        ${guideLinks
          .map(
            (link) =>
              `<a href="${link.href}" class="${isActiveHref(link.href, link.match) ? "is-active" : ""}">${link.label}</a>`
          )
          .join("")}
      </nav>
      <p class="site-guide-title site-guide-title-sub">Services</p>
      <nav class="site-guide-nav site-guide-services" aria-label="Service pages">
        ${serviceLinks
          .map(
            (link) =>
              `<a href="${link.href}" class="${isActiveHref(link.href) ? "is-active" : ""}">${link.label}</a>`
          )
          .join("")}
      </nav>
      <a class="btn btn-primary site-guide-cta" href="contact.html#estimate-form">Free Estimate</a>
    </div>
  `;
  document.body.prepend(sidebar);
  document.body.classList.add("has-site-guide");

  const guideToggle = sidebar.querySelector(".site-guide-toggle");
  if (guideToggle) {
    guideToggle.addEventListener("click", () => {
      const open = document.body.classList.toggle("guide-open");
      guideToggle.setAttribute("aria-expanded", open ? "true" : "false");
      guideToggle.textContent = open ? "Close" : "Menu";
    });
  }

  const isMobileGuide = () => window.matchMedia("(max-width: 960px)").matches;
  let guideCloseTimer = null;

  const openGuide = () => {
    if (isMobileGuide()) {
      return;
    }
    clearTimeout(guideCloseTimer);
    document.body.classList.add("guide-open");
  };

  const scheduleCloseGuide = () => {
    if (isMobileGuide()) {
      return;
    }
    clearTimeout(guideCloseTimer);
    guideCloseTimer = setTimeout(() => {
      document.body.classList.remove("guide-open");
    }, 160);
  };

  document.addEventListener(
    "pointermove",
    (event) => {
      if (isMobileGuide()) {
        return;
      }
      const guideOpen = document.body.classList.contains("guide-open");
      const nearLeftEdge = event.clientX <= 28;
      const insideGuide = event.clientX <= (guideOpen ? 250 : 28);
      if (nearLeftEdge || insideGuide) {
        openGuide();
      } else {
        scheduleCloseGuide();
      }
    },
    { passive: true }
  );

  sidebar.addEventListener("pointerenter", openGuide);
  sidebar.addEventListener("pointerleave", scheduleCloseGuide);

  document.body.classList.add("is-entering");

  const textTargets = document.querySelectorAll("h1, h2, .badge");
  textTargets.forEach((element, groupIndex) => {
    if (element.children.length > 0) {
      return;
    }

    const originalText = element.textContent || "";
    const trimmed = originalText.trim();
    if (!trimmed) {
      return;
    }

    element.classList.add("text-reveal");
    element.classList.add(matchedPage?.textMode || "impact-rise");
    element.classList.add("impact-hover");
    element.setAttribute("aria-label", trimmed);
    element.textContent = "";

    const hiddenText = document.createElement("span");
    hiddenText.className = "sr-only";
    hiddenText.textContent = trimmed;
    element.appendChild(hiddenText);

    const words = trimmed.split(" ");
    let charCounter = 0;

    words.forEach((word, wordIndex) => {
      const wordSpan = document.createElement("span");
      wordSpan.className = "word";
      wordSpan.setAttribute("aria-hidden", "true");

      [...word].forEach((character) => {
        const charSpan = document.createElement("span");
        charSpan.className = "char";
        charSpan.style.setProperty("--char-index", String(charCounter));
        charSpan.style.setProperty("--char-base-delay", `${groupIndex * 110}ms`);
        charSpan.textContent = character;
        charSpan.setAttribute("aria-hidden", "true");
        wordSpan.appendChild(charSpan);
        charCounter += 1;
      });

      element.appendChild(wordSpan);

      if (wordIndex < words.length - 1) {
        const spaceSpan = document.createElement("span");
        spaceSpan.className = "word-space";
        spaceSpan.textContent = "\u00A0";
        spaceSpan.setAttribute("aria-hidden", "true");
        element.appendChild(spaceSpan);
      }
    });
  });

  requestAnimationFrame(() => {
    document.body.classList.remove("is-entering");
    document.body.classList.add("is-ready");
  });

  document.addEventListener("pointermove", (event) => {
    const x = (event.clientX / window.innerWidth) * 100;
    const y = (event.clientY / window.innerHeight) * 100;
    document.body.style.setProperty("--mx", `${x}%`);
    document.body.style.setProperty("--my", `${y}%`);
  });

  const yearNodes = document.querySelectorAll("[data-year]");
  const currentYear = String(new Date().getFullYear());
  yearNodes.forEach((node) => {
    node.textContent = currentYear;
  });

  const serviceName = document.body.dataset.serviceName;
  if (serviceName) {
    const mailtoLinks = document.querySelectorAll("[data-service-mailto]");
    const subject = encodeURIComponent(`${serviceName} Project Request`);
    const body = encodeURIComponent(
      `Hello Elite Craft Honor,\n\nI would like a quote for ${serviceName}.` +
        "\nProject details:\nLocation:\nPreferred schedule:\n\nThank you."
    );

    mailtoLinks.forEach((link) => {
      link.href = `mailto:gmonsalve@elitecrafthonor.com?subject=${subject}&body=${body}`;
    });
  }

  const trackEvent = (eventName, details = {}) => {
    const payload = {
      event: eventName,
      page: window.location.pathname,
      timestamp: new Date().toISOString(),
      ...details
    };

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(payload);
    try {
      const existing = JSON.parse(localStorage.getItem("ech_events") || "[]");
      existing.push(payload);
      localStorage.setItem("ech_events", JSON.stringify(existing.slice(-50)));
    } catch (error) {
      // Ignore storage errors and keep site behavior uninterrupted.
    }
  };

  const trackedCtas = document.querySelectorAll("[data-track]");
  trackedCtas.forEach((cta) => {
    cta.addEventListener("click", () => {
      trackEvent(cta.dataset.track, { label: cta.textContent?.trim() || "" });
    });
  });

  const estimateForm = document.querySelector("[data-estimate-form]");
  if (estimateForm instanceof HTMLFormElement) {
    estimateForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const formData = new FormData(estimateForm);
      const fullName = String(formData.get("fullName") || "");
      const phone = String(formData.get("phone") || "");
      const email = String(formData.get("email") || "");
      const service = String(formData.get("service") || "");
      const city = String(formData.get("city") || "");
      const details = String(formData.get("details") || "");

      const subject = encodeURIComponent(`Free Estimate Request - ${service}`);
      const body = encodeURIComponent(
        `Name: ${fullName}\nPhone: ${phone}\nEmail: ${email}\nService: ${service}\nCity/Town: ${city}\n\nProject Details:\n${details}`
      );

      trackEvent("estimate-form-submit", { service, city });

      const successMessage = estimateForm.querySelector("[data-form-success]");
      if (successMessage instanceof HTMLElement) {
        successMessage.hidden = false;
      }

      window.location.href = `mailto:gmonsalve@elitecrafthonor.com?subject=${subject}&body=${body}`;
    });
  }

  const revealItems = document.querySelectorAll(".is-reveal");
  if (revealItems.length) {
    revealItems.forEach((item, index) => {
      item.style.transitionDelay = `${Math.min(index * 70, 420)}ms`;
    });

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.2 }
    );

    revealItems.forEach((item) => observer.observe(item));
  }

  const interactiveCards = document.querySelectorAll(
    ".card, .service-item, .plan-step, .tile, .contact-card"
  );

  interactiveCards.forEach((card) => {
    card.classList.add("is-interactive");

    card.addEventListener("mousemove", (event) => {
      const rect = card.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const rotateY = ((x / rect.width) - 0.5) * 6;
      const rotateX = (0.5 - (y / rect.height)) * 6;
      card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener("mouseleave", () => {
      card.style.transform = "perspective(900px) rotateX(0deg) rotateY(0deg)";
    });
  });

  const magneticButtons = document.querySelectorAll(".btn");
  magneticButtons.forEach((button) => {
    button.classList.add("magnetic");
    button.addEventListener("mousemove", (event) => {
      const rect = button.getBoundingClientRect();
      const dx = event.clientX - (rect.left + rect.width / 2);
      const dy = event.clientY - (rect.top + rect.height / 2);
      button.style.transform = `translate(${dx * 0.12}px, ${dy * 0.12}px)`;
    });
    button.addEventListener("mouseleave", () => {
      button.style.transform = "translate(0, 0)";
    });
  });

  const header = document.querySelector(".site-header");
  let lastScrollY = window.scrollY;
  if (header) {
    window.addEventListener("scroll", () => {
      const currentY = window.scrollY;
      if (currentY > 130 && currentY > lastScrollY) {
        header.classList.add("nav-hidden");
      } else {
        header.classList.remove("nav-hidden");
      }
      lastScrollY = currentY;
    }, { passive: true });
  }

  const toTopButton = document.createElement("button");
  toTopButton.className = "to-top-btn";
  toTopButton.type = "button";
  toTopButton.setAttribute("aria-label", "Back to top");
  toTopButton.textContent = "↑";
  document.body.appendChild(toTopButton);

  const toggleToTopButton = () => {
    if (window.scrollY > 320) {
      toTopButton.classList.add("show");
    } else {
      toTopButton.classList.remove("show");
    }
  };

  window.addEventListener("scroll", toggleToTopButton, { passive: true });
  toggleToTopButton();

  toTopButton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});
