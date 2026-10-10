# Cinematic Hero — Handoff Prompt

Copy and send this to any AI tool when starting a new cinematic hero feature.

**Two patterns available — pick one before sending:**
- **Pattern A** (Two-Video Crossfade): ambient portal heroes, background loops → send Section A below
- **Pattern B** (Canvas Frame Sequence): product showcases, scroll-scrubbing → send Section B below

---

## PATTERN A HANDOFF PROMPT (copy everything below this line)

---

Build a scroll-driven cinematic hero with two crossfading ambient background videos. This is a production-verified pattern — follow the architecture exactly.

---

### HTML Structure

```html
<main class="flow" id="flow">
  <div class="stage">
    <video class="v" id="v1" autoplay loop muted playsinline preload="auto" aria-hidden="true"
           poster="[V1_POSTER_URL]">
      <source src="[V1_VIDEO_URL]" type="video/mp4">
    </video>
    <video class="v" id="v2" autoplay loop muted playsinline preload="auto" aria-hidden="true"
           poster="[V2_POSTER_URL]">
      <source src="[V2_VIDEO_URL]" type="video/mp4">
    </video>
    <section class="copy one" id="c1">
      <!-- Welcome / hero copy + CTA button -->
    </section>
    <section class="copy two" id="c2" aria-hidden="true">
      <!-- Second copy (training / next move) -->
    </section>
  </div>
</main>
```

---

### CSS (paste verbatim, adjust tokens)

```css
/* ─── TOKENS ─── */
:root {
  --n: #0d1825;   /* dark background */
  --l: #a8dc36;   /* accent color */
  --m: #8fa3b8;   /* muted text */
  --nav-h: 52px;  /* your navbar height */
}

/* ─── FLOW / STAGE ─── */
.flow { height: 300vh; }
.flow[data-no-training] { height: 100svh; }

.stage {
    height: calc(100svh - var(--nav-h));
    position: sticky;
    top: var(--nav-h);
    overflow: hidden;
    background: var(--n);
}

.stage::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(13,24,37,.85) 0%, rgba(13,24,37,.5) 42%, transparent 65%),
        linear-gradient(0deg, rgba(13,24,37,.9), transparent 58%);
    pointer-events: none;
    z-index: 2;
}

/* ─── VIDEOS ─── */
.v {
    position: absolute;
    inset: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    z-index: 1;
}
/* Set object-position based on where the model's face sits in each video frame */
#v1 { object-position: 70% 0; }
#v2 { object-position: 50% 0; opacity: 0; }

/* ─── COPY ─── */
.copy {
    position: absolute;
    z-index: 3;
    left: 7vw;
    bottom: 12vh;
    width: min(470px, 40vw);
    transition: opacity .15s, transform .15s;
}
/* CRITICAL: pointer-events:none on c2 — opacity:0 does NOT disable pointer events.
   Without this, the invisible c2 overlay blocks all taps on c1's buttons on mobile. */
.copy.two { opacity: 0; transform: translateY(28px); pointer-events: none; }

/* ─── MOBILE PORTRAIT (≤700px) ─── */
@media (max-width: 700px) {
    .flow:not([data-no-training]) { height: 280vh; }

    /* Bottom gradient only — stacked layout: face up, text down */
    .stage::after {
        background: linear-gradient(180deg,
            rgba(13,24,37,.05), rgba(13,24,37,.16) 30%,
            rgba(13,24,37,.9) 57%, var(--n) 76%);
    }

    /* Adjust X% to match where the face sits in each video frame.
       Rule: if face is at 70% horizontal in frame → set object-position X to ~70-75%.
       Y at 12% keeps face in the upper band of a portrait screen. */
    #v1 { object-position: 72% 12%; }
    #v2 { object-position: 50% 20%; }

    /* Full-width stacked copy — no side-by-side */
    .copy, .copy.two { left: 7vw; right: 7vw; width: auto; bottom: 6vh; }
    .copy h1 { font-size: clamp(2.2rem, 10vw, 3.6rem); margin: 10px 0; line-height: 1.05; }
}

/* ─── LANDSCAPE (phones sideways, height ≤450px) ─── */
@media (max-height: 450px) and (orientation: landscape) {
    .flow:not([data-no-training]) { height: 100svh; }
    #v1 { object-position: 65% 30%; }
    #v2 { object-position: 55% 30%; }
    .copy, .copy.two { bottom: 5vh; left: 7vw; right: auto; width: min(44vw, 340px); }
    .copy h1 { font-size: clamp(1.6rem, 4.5vw, 2.4rem); margin: 6px 0; line-height: 1.05; }
    .copy p, .copy-stats { display: none; }
}

/* ─── REDUCED MOTION ─── */
@media (prefers-reduced-motion: reduce) {
    .v, .copy { transition: none !important; }
}
```

---

### JavaScript (paste verbatim)

```javascript
var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var f      = document.getElementById('flow');
var a      = document.getElementById('v1');
var b      = document.getElementById('v2');
var c1     = document.getElementById('c1');
var c2     = document.getElementById('c2');
var hasTraining = !!(f && !f.hasAttribute('data-no-training'));

function play(v) {
    if (!v) return;
    v.muted = true;   // enforce mute in JS as belt-and-suspenders
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
}

play(a);

var v2ready = false;
function ensureV2() { if (!v2ready) { v2ready = true; play(b); } }

// Start v2 on first user gesture (mobile autoplay policy)
['click', 'touchstart', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, function () { play(a); ensureV2(); }, { once: true, passive: true });
});

function clamp(n, lo, hi) { return Math.max(lo, Math.min(hi, n)); }
function ss(e0, e1, x) { var t = clamp((x - e0) / (e1 - e0), 0, 1); return t * t * (3 - 2 * t); }

function tick() {
    if (!f || !hasTraining) return;
    var max = f.offsetHeight - innerHeight;
    var p   = max > 0 ? clamp(scrollY / max, 0, 1) : 0;
    var x, y;
    if (reduce) {
        x = p > 0.4 ? 1 : 0;
        y = p > 0.55 ? 1 : 0;
    } else {
        x = ss(0.14, 0.58, p);   // video crossfade: starts at 14% scroll, ends at 58%
        y = ss(0.48, 0.73, p);   // copy crossfade: starts at 48% scroll, ends at 73%
    }

    if (a) { a.style.opacity = String(1 - x); a.style.transform = 'scale(' + (1 + 0.03 * x) + ')'; }
    if (b) {
        if (x > 0.1) ensureV2();
        b.style.opacity = String(x);
        b.style.transform = 'scale(' + (1.03 - 0.03 * x) + ')';
    }
    if (c1) {
        var op1 = 1 - Math.min(1, x * 2);
        c1.style.opacity      = String(op1);
        c1.style.transform    = 'translateY(' + (-x * 24) + 'px)';
        c1.style.pointerEvents = op1 < 0.05 ? 'none' : 'auto'; // CRITICAL: prevent ghost blocking
    }
    if (c2) {
        c2.style.opacity      = String(y);
        c2.style.transform    = 'translateY(' + (28 - y * 28) + 'px)';
        c2.style.pointerEvents = y < 0.05 ? 'none' : 'auto';   // CRITICAL: enable when visible
        c2.setAttribute('aria-hidden', y < 0.05 ? 'true' : 'false');
    }
}

addEventListener('scroll', tick, { passive: true });
addEventListener('resize', tick, { passive: true });
requestAnimationFrame(function () {
    requestAnimationFrame(function () { window.scrollTo(0, 0); tick(); });
});
```

---

### Video Requirements — MUST FOLLOW

Videos MUST be 8-bit H.264 (`yuv420p`). Runway AI and other AI video generators often output 10-bit H.264 (`yuv420p10le`) which renders as a **black screen** on iOS Safari and Android Chrome.

**Re-encode command (run before deploying any new video):**
```bash
ffmpeg -i input.mp4 -c:v libx264 -profile:v main -pix_fmt yuv420p -movflags +faststart -an -crf 23 -preset slow output-web.mp4
```

**Check codec:**
```bash
ffprobe -v quiet -show_streams input.mp4 | grep pix_fmt
# Must show: pix_fmt=yuv420p
```

**Size target:** under 2MB per video for ambient loops. Use `-crf 28` for aggressive compression.

---

### Things to NEVER Do

1. `#v2 { display: none }` on mobile — breaks the crossfade. Both videos play on ALL screen sizes.
2. `opacity: 1 !important` on videos in mobile CSS — fights JS, freezes animation.
3. `isMobile` guard that nulls out v2 — mobile autoplay works with `muted playsinline`.
4. Assuming DevTools responsive mode = real mobile autoplay behavior — it does NOT enforce mobile autoplay policy. Test on a real device.
5. `pointer-events` not set on hidden copy section — invisible elements still block taps.

---

### Customization Checklist

- [ ] Replace `[V1_VIDEO_URL]`, `[V2_VIDEO_URL]`, poster URLs
- [ ] Set `--nav-h` to match your navbar height
- [ ] Adjust `#v1 { object-position: X% Y% }` based on face position in video frame
- [ ] Choose two visually DISTINCT videos (different action, different mood — not two similar shots of same person)
- [ ] Re-encode both videos with FFmpeg before deploying
- [ ] Test on real mobile device at 390px, portrait AND landscape

---

*Pattern A documented from production use. Verified: desktop, mobile portrait, mobile landscape, tablet.*

---

## PATTERN B HANDOFF PROMPT — Canvas Frame Sequence (copy everything below this line)

---

Build a scroll-driven cinematic product showcase using an HTML5 canvas bound to scroll progress. This is a production-verified pattern from Rodrigo Olivares (Dynamo Sites SOP).

---

### Two-Phase Asset Setup (you must prepare these BEFORE starting code)

**Phase 1: Hero**
- Hero image: subject **offset right** (or left) with empty space on the other side for headline + CTA
- Optional ambient loop video: 3–5s seamless loop, subtle movement, fixed camera → plays as `autoplay loop muted playsinline` background

**Phase 2: Scroll sequence**
- Video with subject **centered** (for mobile safety — no cropping of focal point)
- Camera: smooth orbit or slow linear motion — avoid fast jerky moves (they degrade when stepped frame-by-frame)
- Export to 60–90 WebP frames named `frame_001.webp` through `frame_080.webp` in `/assets/frames/`

**FFmpeg frame export command:**
```bash
ffmpeg -i input.mp4 -vf "fps=25,scale=1920:-1" -q:v 80 assets/frames/frame_%03d.webp
```
Target: each frame ~15–30KB, total folder <2MB.

---

### Prompt 1 — Hero Section

Send this first. Agent builds ONLY the hero, nothing else.

> "Create a modern, minimal, high-impact HTML/CSS/JS landing page for [BRAND NAME]. First, build ONLY the hero section.
>
> Use `assets/hero-bg.jpg` as a full-viewport background image (or `assets/hero-loop.mp4` as an autoplay muted looping video if provided).
>
> Left side: brand name, a 2-line high-contrast editorial headline, a short subheading (max 10 words), and a primary CTA button.
> Right side: left clear — the background focal subject occupies that space.
>
> Typography: large editorial scale, clean and minimal. No pill badges. No decorative cards. No eyebrow chips.
> Do NOT build any secondary sections yet."

---

### Prompt 2 — Canvas Scroll Engine

Send after hero is approved.

> "Now add the interactive scroll-driven showcase section directly below the hero.
>
> Requirements:
> - Full-screen sticky container, height: 300vh (creates scroll space for the animation)
> - An HTML5 `<canvas>` inside that covers 100% of the viewport (cover-fit logic like `object-fit: cover`)
> - Preload all 80 frames from `/assets/frames/frame_%03d.webp` (pad index to 3 digits: frame_001 through frame_080)
> - Bind canvas rendering to scroll progress: scrolling down advances frames forward; scrolling up reverses; stopping freezes the exact frame
> - Use `requestAnimationFrame` — zero lag, no jumpiness
> - Show the first frame immediately on page load before any scrolling"

---

### Prompt 3 — Narrative Copy Overlays

Send after canvas engine is working.

> "Add editorial text callouts that fade in and out at specific scroll milestones over the canvas:
>
> - 0%–25% scroll: Headline 1 fades in, then fades out
> - 35%–65% scroll: Headline 2 + one-line feature callout fades in, then out
> - 75%–100% scroll: Final product spec + purchase CTA appears and stays
>
> Rules:
> - Use progressive background darkening toward section end to blend into the next section
> - Do NOT place any dark overlay box over the center of the canvas (where the subject is)
> - Max 2 lines of text per phase — punchy, editorial, no sentences
> - Use `pointer-events: none` on all copy overlays so they never block canvas interaction"

---

### Prompt 4 — Anti-Slop Audit

Send as the final cleanup pass before shipping.

> "Perform a complete anti-slop visual audit across the entire page:
>
> 1. Remove all pill badges, eyebrow chips, category tags, and floating metric counters
> 2. Strip decorative rounded cards and icon boxes that contain only text
> 3. Enforce editorial font scale: titles should be dramatically larger than body text — no uniform sizing
> 4. Verify canvas stays centered on mobile (375px) without horizontally clipping the subject
> 5. Check that all copy phases use `pointer-events: none` so taps/clicks reach the canvas or underlying elements
> 6. Remove any generic section dividers (wave SVGs, gradient bars) that look template-generated"

---

### Things to NEVER Do (Pattern B)

1. Bind `video.currentTime` to scroll — it stutters badly on mobile. Always use canvas + image frames.
2. Generate frames from a video with fast/jerky motion — stepped frames look choppy.
3. Use the same framing for hero and scroll sequence — hero = offset subject, scroll = centered subject.
4. Skip the anti-slop audit — AI agents always add badges and cards that break the editorial look.
5. Use dark overlay boxes over the canvas subject area — darken the background progressively instead.

---

*Pattern B documented from production use, based on the Rodrigo Olivares / Dynamo Sites methodology.*
