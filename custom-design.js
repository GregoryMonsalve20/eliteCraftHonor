(() => {
  const root = document.querySelector(".custom-design-page");
  if (!root) {
    return;
  }

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hero = root.querySelector(".cd-hero");
  const spine = root.querySelector("[data-cd-spine]");
  const progress = root.querySelector("[data-cd-progress]");
  const stages = [...root.querySelectorAll("[data-cd-stage]")];
  const railLinks = [...root.querySelectorAll(".cd-rail a, .cd-progress__dots a")];
  const mudLabels = ["Bare Sheetrock", "Taped", "Mud", "Sanded"];

  const readyHero = () => {
    if (hero) {
      hero.classList.add("is-ready");
    }
  };

  if (reduce) {
    readyHero();
  } else if (hero) {
    requestAnimationFrame(readyHero);
  }

  const setActiveStage = (id) => {
    railLinks.forEach((link) => {
      const active = link.getAttribute("href") === `#${id}`;
      link.classList.toggle("is-active", active);
    });
  };

  const observers = [];

  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            const id = entry.target.id;
            if (id && railLinks.some((link) => link.getAttribute("href") === `#${id}`)) {
              setActiveStage(id);
            }
          }
        });
      },
      { threshold: 0.38, rootMargin: "-10% 0px -30% 0px" }
    );

    stages.forEach((stage) => io.observe(stage));
    root.querySelectorAll("[data-cd-layout], [data-cd-framing], [data-cd-sheet]").forEach((el) => io.observe(el));
    observers.push(io);
  } else {
    root.querySelectorAll("[data-cd-layout], [data-cd-framing], [data-cd-sheet], .cd-stage").forEach((el) => {
      el.classList.add("is-in");
    });
  }

  let ticking = false;
  const updateScrollChrome = () => {
    ticking = false;
    const doc = document.documentElement;
    const max = Math.max(doc.scrollHeight - window.innerHeight, 1);
    const ratio = Math.min(Math.max(window.scrollY / max, 0), 1);
    if (progress) {
      progress.style.width = `${ratio * 100}%`;
    }
    if (spine) {
      spine.style.strokeDashoffset = String(1 - ratio);
    }
  };

  const onScroll = () => {
    if (ticking) {
      return;
    }
    ticking = true;
    requestAnimationFrame(updateScrollChrome);
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  updateScrollChrome();

  const hotspots = root.querySelectorAll("[data-hotspot]");
  const links = root.querySelectorAll(".cd-overlay-lines [data-link]");
  hotspots.forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.getAttribute("data-hotspot");
      hotspots.forEach((item) => item.setAttribute("aria-pressed", item === button ? "true" : "false"));
      links.forEach((link) => link.classList.toggle("is-on", link.getAttribute("data-link") === key));
    });
  });

  const xray = root.querySelector("[data-cd-xray]");
  const xrayBtn = root.querySelector("[data-cd-xray-toggle]");
  if (xray && xrayBtn) {
    xrayBtn.addEventListener("click", () => {
      const open = xray.classList.toggle("is-open");
      xrayBtn.setAttribute("aria-pressed", open ? "true" : "false");
      xrayBtn.textContent = open ? "Close the Wall" : "Reveal Behind the Wall";
    });
  }

  const mudRange = root.querySelector("[data-cd-mud-range]");
  const mudImgs = [...root.querySelectorAll("[data-mud]")];
  const mudLabel = root.querySelector("[data-cd-mud-label]");
  const setMud = (value) => {
    mudImgs.forEach((img) => img.classList.toggle("is-on", img.getAttribute("data-mud") === String(value)));
    if (mudLabel) {
      mudLabel.textContent = mudLabels[value] || mudLabels[0];
    }
    if (mudRange) {
      mudRange.setAttribute("aria-valuetext", mudLabels[value] || mudLabels[0]);
    }
  };
  if (mudRange) {
    mudRange.addEventListener("input", () => setMud(Number(mudRange.value)));
    setMud(0);
  }

    const primerRange = root.querySelector("[data-cd-primer-range]");
  const primerAfter = root.querySelector(".cd-primer-after");
  const setPrimer = (value) => {
    if (primerAfter) {
      primerAfter.style.clipPath = `inset(0 ${100 - value}% 0 0)`;
    }
  };
  if (primerRange) {
    primerRange.addEventListener("input", () => setPrimer(Number(primerRange.value)));
    setPrimer(Number(primerRange.value));
  }
  if (reduce && primerAfter) {
    primerAfter.style.clipPath = "inset(0 0 0 0)";
  }

  const lightFrame = root.querySelector("[data-cd-light]");
  const lightBtns = root.querySelectorAll("[data-light]");
  lightBtns.forEach((button) => {
    button.addEventListener("click", () => {
      const mood = button.getAttribute("data-light");
      if (lightFrame) {
        lightFrame.setAttribute("data-cd-light", mood);
      }
      lightBtns.forEach((item) => item.setAttribute("aria-pressed", item === button ? "true" : "false"));
    });
  });

  const finale = root.querySelector("[data-cd-finale]");
  const finaleBtns = root.querySelectorAll("[data-finale]");
  const setFinale = (key) => {
    if (!finale) {
      return;
    }
    finale.setAttribute("data-show", key);
    finale.querySelectorAll("img[data-finale]").forEach((img) => {
      img.classList.toggle("is-on", img.getAttribute("data-finale") === key);
    });
    finale.querySelectorAll("button[data-finale]").forEach((btn) => {
      btn.setAttribute("aria-pressed", btn.getAttribute("data-finale") === key ? "true" : "false");
    });
  };
  finaleBtns.forEach((button) => {
    if (button.tagName === "BUTTON") {
      button.addEventListener("click", () => setFinale(button.getAttribute("data-finale")));
    }
  });
  setFinale("finished");

  window.addEventListener(
    "pagehide",
    () => {
      observers.forEach((io) => io.disconnect());
      window.removeEventListener("scroll", onScroll);
    },
    { once: true }
  );
})();
