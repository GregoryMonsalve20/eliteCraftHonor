(function () {
  document.documentElement.classList.add("js-enabled");

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const initReveal = () => {
    const items = [...document.querySelectorAll(".ech-reveal, .photo-card")];
    items.forEach((el, i) => {
      if (!el.classList.contains("ech-reveal")) {
        const modes = ["", "ech-reveal-left", "ech-reveal-right", "ech-reveal-mask"];
        el.classList.add("ech-reveal");
        const mode = modes[i % modes.length];
        if (mode) el.classList.add(mode);
      }
      el.style.transitionDelay = `${Math.min(i % 4, 3) * 0.12}s`;
    });

    if (reduced || !("IntersectionObserver" in window)) {
      items.forEach((el) => el.classList.add("is-in"));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-in");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.16, rootMargin: "0px 0px -8% 0px" }
    );

    items.forEach((el) => observer.observe(el));
  };

  const initBeforeAfter = () => {
    document.querySelectorAll("[data-ech-ba]").forEach((root) => {
      const range = root.querySelector("input[type='range']");
      const after = root.querySelector(".ech-before-after__after");
      const handle = root.querySelector(".ech-before-after__handle");
      if (!range || !after || !after.getAttribute("src")) return;

      const setValue = (value) => {
        const pct = Math.max(0, Math.min(100, Number(value)));
        after.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
        if (handle) handle.style.left = `${pct}%`;
        range.value = String(pct);
      };

      range.addEventListener("input", () => setValue(range.value));
      setValue(range.value || 50);
    });
  };

  const initServiceCards = () => {
    document.querySelectorAll(".ech-service-card, .page-services .service-item").forEach((card) => {
      card.classList.add("ech-service-card");
      let extra = card.querySelector(".ech-service-extra");
      const link = card.querySelector(".service-link, a[href]");
      if (!extra && link) {
        extra = document.createElement("div");
        extra.className = "ech-service-extra";
        extra.innerHTML = `<div class="ech-service-actions"><a class="btn btn-ghost" href="${link.getAttribute("href")}">Learn More</a><a class="btn btn-primary" href="${link.getAttribute("href").includes("../") ? "../contact.html#estimate-form" : "contact.html#estimate-form"}">Request an Estimate</a></div>`;
        card.appendChild(extra);
      }
      let toggle = card.querySelector(".ech-service-toggle");
      if (!toggle) {
        toggle = document.createElement("button");
        toggle.type = "button";
        toggle.className = "ech-service-toggle";
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "More about this service";
        card.appendChild(toggle);
      }
      toggle.addEventListener("click", () => {
        const open = card.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", String(open));
      });
    });
  };

  const initProjectSelector = () => {
    const root = document.querySelector("[data-ech-selector]");
    if (!root) return;
    const panel = root.querySelector("[data-ech-selector-panel]");
    const buttons = [...root.querySelectorAll("[data-plan]")];
    const copy = {
      painting: {
        title: "Painting",
        text: "Interior and exterior painting with a clean, even finish. Start with a visit so we can see the surfaces and scope.",
        explore: "services/painting.html",
        cta: "Request a Painting Estimate"
      },
      builtin: {
        title: "Custom Built-In",
        text: "Vanities, TV walls, shelves, and LED ceiling features designed around the room you already have.",
        explore: "services/custom-built-ins.html",
        cta: "Start Your Design"
      },
      repair: {
        title: "Home Repair",
        text: "Carpentry, drywall, doors, trim, and everyday repairs handled with the same finish standard as larger work.",
        explore: "services/handyman.html",
        cta: "Get a Free Estimate"
      },
      unsure: {
        title: "Not Sure Yet",
        text: "Tell us what you want the space to feel like. We will help you choose painting, built-ins, or repairs.",
        explore: "services.html",
        cta: "Get a Free Estimate"
      }
    };

    buttons.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        event.preventDefault();
        buttons.forEach((b) => b.setAttribute("aria-pressed", "false"));
        btn.setAttribute("aria-pressed", "true");
        const key = btn.getAttribute("data-plan");
        const item = copy[key];
        if (!item || !panel) return;
        panel.hidden = false;
        panel.innerHTML = `<h3>${item.title}</h3><p>${item.text}</p><div class="home-hero-actions"><a class="btn btn-primary" href="${item.explore}">Explore this service</a><a class="btn btn-secondary" href="contact.html">${item.cta}</a></div>`;
      });
    });
  };

  const initFinishExplorer = () => {
    const root = document.querySelector("[data-ech-finish]");
    if (!root) return;
    const stage = root.querySelector(".ech-finish-explorer__stage");
    root.querySelectorAll("[data-finish]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const group = btn.getAttribute("data-group");
        root.querySelectorAll(`[data-group="${group}"]`).forEach((b) => b.setAttribute("aria-pressed", "false"));
        btn.setAttribute("aria-pressed", "true");
        const map = {
          "wall-warm": ["--ech-wall", "#ece6da"],
          "wall-soft": ["--ech-wall", "#d8cfc0"],
          "trim-light": ["--ech-trim", "#f7f3ec"],
          "trim-dark": ["--ech-trim", "#2a241c"],
          "wood-light": ["--ech-wood", "#d8b57a"],
          "wood-dark": ["--ech-wood", "#6b4a2b"],
          "led-warm": ["--ech-led", "rgba(232,196,120,.55)"],
          "led-neutral": ["--ech-led", "rgba(232,224,200,.45)"],
          "led-cool": ["--ech-led", "rgba(186,214,232,.45)"],
          modern: ["--ech-floor", "#b9b3a8"],
          classic: ["--ech-floor", "#cbb89a"],
          minimal: ["--ech-floor", "#d7d2c8"]
        };
        const pair = map[btn.getAttribute("data-finish")];
        if (pair && stage) stage.style.setProperty(pair[0], pair[1]);
      });
    });
  };

  const initGalleryFilters = () => {
    const root = document.querySelector("[data-ech-filters]");
    if (!root) return;
    const buttons = [...root.querySelectorAll("[data-filter]")];
    const items = [...document.querySelectorAll("[data-category]")];
    const empty = document.querySelector("[data-ech-empty]");

    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        buttons.forEach((b) => b.setAttribute("aria-pressed", "false"));
        btn.setAttribute("aria-pressed", "true");
        const filter = btn.getAttribute("data-filter");
        let visible = 0;
        items.forEach((item) => {
          const match = filter === "all" || item.getAttribute("data-category").split(" ").includes(filter);
          item.classList.toggle("is-filtered-out", !match);
          if (match) visible += 1;
        });
        if (empty) empty.hidden = visible > 0;
      });
    });
  };

  const initJourney = () => {
    document.querySelectorAll("[data-ech-journey]").forEach((root) => {
      const buttons = [...root.querySelectorAll("[data-step]")];
      const panel = root.querySelector("[data-ech-journey-panel]");
      const text = {
        1: "We walk the space, listen to what you want, and confirm what is realistic for the room.",
        2: "We measure openings, walls, and clearances so built-ins and finishes fit the existing structure.",
        3: "You review a concept so you can see the idea before we commit to materials and schedule.",
        4: "You receive a written estimate based on the agreed scope. No work starts until you approve it.",
        5: "We build and finish on site with protection for the rest of the home.",
        6: "We walk the completed work with you and address punch-list items before close-out."
      };

      buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
          const id = btn.getAttribute("data-step");
          const open = btn.getAttribute("aria-expanded") !== "true";
          buttons.forEach((b) => b.setAttribute("aria-expanded", "false"));
          btn.setAttribute("aria-expanded", String(open));
          if (panel) {
            panel.hidden = !open;
            panel.textContent = open ? text[id] : "";
          }
        });
      });
    });
  };

  const initStageTabs = () => {
    document.querySelectorAll("[data-ech-stages]").forEach((root) => {
      const tabs = [...root.querySelectorAll("[role='tab']")];
      const panels = [...root.querySelectorAll("[role='tabpanel']")];

      const activate = (index) => {
        tabs.forEach((tab, i) => {
          const selected = i === index;
          tab.setAttribute("aria-selected", String(selected));
          tab.tabIndex = selected ? 0 : -1;
          panels[i].hidden = !selected;
        });
        tabs[index].focus();
      };

      tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => activate(index));
        tab.addEventListener("keydown", (event) => {
          if (event.key === "ArrowRight") activate((index + 1) % tabs.length);
          if (event.key === "ArrowLeft") activate((index - 1 + tabs.length) % tabs.length);
        });
      });
    });
  };

  const initHeader = () => {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const onScroll = () => {
      header.classList.toggle("is-solid", window.scrollY > 24);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  };

  const initTeam = () => {
    document.querySelectorAll(".ech-team-card .ech-profile-toggle").forEach((btn) => {
      btn.addEventListener("click", () => {
        const card = btn.closest(".ech-team-card");
        const open = card.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", String(open));
      });
    });
  };

  const initSmartForm = () => {
    const form = document.querySelector("#estimate-form");
    if (!form) return;
    const steps = [...form.querySelectorAll(".ech-step")];
    if (!steps.length) return;
    let current = 0;
    const progress = form.querySelector("[data-ech-progress]");
    const back = form.querySelector("[data-ech-back]");
    const next = form.querySelector("[data-ech-next]");
    const submit = form.querySelector('button[type="submit"]');
    const review = form.querySelector("[data-ech-review]");

    const show = () => {
      steps.forEach((step, i) => step.classList.toggle("is-active", i === current));
      if (progress) progress.textContent = `Step ${current + 1} of ${steps.length}`;
      if (back) back.hidden = current === 0;
      if (next) next.hidden = current === steps.length - 1;
      if (submit) submit.hidden = current !== steps.length - 1;
      if (review && current === steps.length - 1) {
        const data = new FormData(form);
        review.textContent = ["fullName", "phone", "email", "service", "city", "details"]
          .map((key) => `${key}: ${data.get(key) || "—"}`)
          .join(" · ");
      }
    };

    next?.addEventListener("click", () => {
      const fields = [...steps[current].querySelectorAll("[required]")];
      const invalid = fields.find((field) => !field.checkValidity());
      if (invalid) {
        invalid.reportValidity();
        return;
      }
      current = Math.min(steps.length - 1, current + 1);
      show();
    });

    back?.addEventListener("click", () => {
      current = Math.max(0, current - 1);
      show();
    });

    show();
  };

  const initTestimonials = () => {
    const root = document.querySelector("[data-ech-testimonials]");
    if (!root) return;
    const slides = [...root.querySelectorAll("[data-review]")];
    if (!slides.length) return;
    let index = 0;
    const show = () => {
      slides.forEach((slide, i) => {
        slide.hidden = i !== index;
      });
    };
    root.querySelector("[data-prev]")?.addEventListener("click", () => {
      index = (index - 1 + slides.length) % slides.length;
      show();
    });
    root.querySelector("[data-next]")?.addEventListener("click", () => {
      index = (index + 1) % slides.length;
      show();
    });
    show();
  };

  const initAreaMap = () => {
    const select = document.querySelector("[data-ech-city]");
    const panel = document.querySelector("[data-ech-city-panel]");
    if (!select || !panel) return;
    select.addEventListener("change", () => {
      const option = select.selectedOptions[0];
      if (!option || !option.value) {
        panel.hidden = true;
        return;
      }
      panel.hidden = false;
      panel.innerHTML = `<p>We serve ${option.textContent}. Review the local page or request an estimate for work in this city.</p><p><a href="${option.value}">Open ${option.textContent} page</a> · <a href="contact.html">Get a Free Estimate</a></p>`;
    });
  };

  const splitFallingTitle = (title) => {
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const full = title.textContent.replace(/\s+/g, " ").trim();
    title.setAttribute("aria-label", full);
    const lines = title.innerHTML.split(/<br\s*\/?>/i);
    title.textContent = "";
    const visible = document.createElement("span");
    visible.setAttribute("aria-hidden", "true");
    title.appendChild(visible);
    let index = 0;
    lines.forEach((line, lineIndex) => {
      const text = line.replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").trim();
      const words = text.split(" ");
      words.forEach((word, wordIndex) => {
        const wordSpan = document.createElement("span");
        wordSpan.className = "word";
        [...word].forEach((character) => {
          const char = document.createElement("span");
          char.className = "char";
          char.style.setProperty("--i", String(index));
          char.textContent = character;
          wordSpan.appendChild(char);
          index += 1;
        });
        visible.appendChild(wordSpan);
        if (wordIndex < words.length - 1) {
          const space = document.createElement("span");
          space.className = "char";
          space.style.setProperty("--i", String(index));
          space.textContent = "\u00A0";
          visible.appendChild(space);
          index += 1;
        }
      });
      if (lineIndex < lines.length - 1) {
        visible.appendChild(document.createElement("br"));
      }
    });
    if (reduced) {
      title.querySelectorAll(".char").forEach((char) => {
        char.style.opacity = "1";
        char.style.animation = "none";
      });
      return;
    }
    requestAnimationFrame(() => title.classList.add("is-falling"));
  };

  const initHeroFall = () => {
    document.querySelectorAll("h1.ech-hero-title").forEach(splitFallingTitle);
  };

  document.addEventListener("DOMContentLoaded", () => {
    initHeroFall();
    initReveal();
    initBeforeAfter();
    initServiceCards();
    initProjectSelector();
    initFinishExplorer();
    initGalleryFilters();
    initJourney();
    initStageTabs();
    initHeader();
    initTeam();
    initSmartForm();
    initTestimonials();
    initAreaMap();
  });
})();
