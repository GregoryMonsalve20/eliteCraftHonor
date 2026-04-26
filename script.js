document.addEventListener("DOMContentLoaded", () => {
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
    element.setAttribute("aria-label", trimmed);
    element.textContent = "";

    const hiddenText = document.createElement("span");
    hiddenText.className = "sr-only";
    hiddenText.textContent = trimmed;
    element.appendChild(hiddenText);

    [...trimmed].forEach((character, charIndex) => {
      const charSpan = document.createElement("span");
      charSpan.className = "char";
      charSpan.style.setProperty("--char-index", String(charIndex));
      charSpan.style.setProperty("--char-base-delay", `${groupIndex * 110}ms`);
      charSpan.textContent = character === " " ? "\u00A0" : character;
      charSpan.setAttribute("aria-hidden", "true");
      element.appendChild(charSpan);
    });
  });

  requestAnimationFrame(() => {
    document.body.classList.remove("is-entering");
    document.body.classList.add("is-ready");
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
    // Keeps a lightweight local trail for future optimization.
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
