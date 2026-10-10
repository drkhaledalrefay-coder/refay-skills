---
name: cinematic-hero
description: "Build a full-viewport scroll-driven cinematic hero for a website: two-video crossfade (ambient loops, mobile-safe muted playsinline, 8-bit H.264) or canvas frame-sequence scrubbing. Use for 'cinematic hero', 'scroll video hero', 'video crossfade on scroll', 'frame sequence hero', or any scroll-driven video hero."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Cinematic Hero — Scroll-Driven Video & Canvas Techniques

**Version:** 1.1  
**Built for:** any website that needs a scroll-driven cinematic hero  
**Status:** Production-verified — desktop + mobile + tablet + landscape  
**Also covers:** Canvas frame-sequence pattern (Rodrigo Olivares / Dynamo Sites SOP)

---

## Two Patterns — When to Use Which

| | **Pattern A: Two-Video Crossfade** | **Pattern B: Canvas Frame Sequence** |
|---|---|---|
| **Best for** | Ambient loops, portal heroes, continuous background | Product showcases, "scrubbing" through an action |
| **Scroll behavior** | Smooth opacity crossfade between 2 looping videos | Step-by-step through 60-90 still frames |
| **Mobile autoplay** | Works with `muted playsinline` + 8-bit codec | No autoplay needed — user-driven via scroll |
| **Codec risk** | ⚠️ 10-bit H.264 = black screen → must re-encode | None — just images (WebP/JPEG) |
| **Asset size** | 1–2 MP4 files, <2MB each | 60–90 WebP frames, ~15–30KB each |
| **This project** | ✅ Built & live | Use for future product demos |

---

## What This Skill Builds

A full-viewport cinematic hero with:
- **Two ambient background videos** that crossfade as the user scrolls
- **Two copy sections** (welcome message → call-to-action) that fade in sequence with the videos
- **Mobile-first stacked layout** — face in upper band, copy at bottom
- **Desktop side-by-side layout** — copy on left, model/face on right
- **Scroll-driven animation** — no autoplay restrictions, no jank, no audio

---

## Architecture

```
<main class="flow" id="flow">        ← tall div (300vh) creates the scroll space
  <div class="stage">                ← position:sticky, stays in viewport while flow scrolls
    <video id="v1" class="v">        ← Video 1: hero/welcome scene
    <video id="v2" class="v">        ← Video 2: training/action scene
    <section class="copy one" id="c1">  ← Copy for V1 (welcome back)
    <section class="copy two" id="c2">  ← Copy for V2 (your next move)
  </div>
</main>
```

**Key principle:** `.stage` is `position: sticky` inside `.flow`. JS reads `scrollY / flow.offsetHeight` to compute a 0→1 progress value `p`, then uses smoothstep (`ss()`) to drive opacity/transform on both videos and both copy sections.

---

## CSS — Core

```css
:root {
  --n: #0d1825;   /* dark navy background */
  --l: #a8dc36;   /* lime accent */
  --m: #8fa3b8;   /* muted text */
}

/* ─── FLOW / STAGE ─── */
.flow { height: 300vh; }
.flow[data-no-training] { height: 100svh; }   /* no scroll when single-video */

.stage {
    height: calc(100svh - 52px);   /* 52px = navbar height */
    position: sticky;
    top: 52px;
    overflow: hidden;
    background: var(--n);
}

/* Gradient overlay — always on top of videos, pointer-events:none */
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
#v1 { object-position: 70% 0; }
#v2 { object-position: 50% 0; opacity: 0; }

/* ─── COPY SECTIONS ─── */
.copy {
    position: absolute;
    z-index: 3;
    left: 7vw;
    bottom: 12vh;
    width: min(470px, 40vw);
    transition: opacity .15s, transform .15s;
}
/* CRITICAL: c2 must start with pointer-events:none — otherwise it blocks
   taps on c1's button even when invisible (opacity:0 ≠ pointer-events:none) */
.copy.two { opacity: 0; transform: translateY(28px); pointer-events: none; }
```

---

## CSS — Mobile Portrait (≤700px)

```css
@media (max-width: 700px) {
    .flow:not([data-no-training]) { height: 280vh; }

    /* Bottom-only gradient — stacked layout (face up, text down) */
    .stage::after {
        background: linear-gradient(180deg,
            rgba(13,24,37,.05), rgba(13,24,37,.16) 30%,
            rgba(13,24,37,.9) 57%, var(--n) 76%);
    }

    /* object-position: ~70% horizontal to show face (usually right-of-center in frame) */
    /* object-position: 12% vertical to push face into upper band */
    #v1 { object-position: 72% 12%; }
    #v2 { object-position: 50% 20%; }

    /* Full-width copy at bottom — no side-by-side */
    .copy, .copy.two {
        left: 7vw;
        right: 7vw;
        width: auto;
        bottom: 6vh;
    }
    .copy h1 { font-size: clamp(2.2rem, 10vw, 3.6rem); margin: 10px 0; line-height: 1.05; }
}
```

**Why stacked, not side-by-side on mobile:**  
At 400px wide, a side-by-side layout (text left, face right) leaves the face cropped to a sliver AND the text too wide — they fight each other. Stacking gives the face the upper 55% of the screen and the copy the lower 45% over the gradient.

**Face crop rule:**  
`object-position: X% Y%` — X positions the horizontal crop. If the model's face is at ~70% from the left edge of the video frame, set X to ~70-75%. Test by adjusting in DevTools responsive mode.

---

## CSS — Landscape (≤450px height)

```css
@media (max-height: 450px) and (orientation: landscape) {
    .flow:not([data-no-training]) { height: 100svh; }  /* no scroll on tiny landscape */
    #v1 { object-position: 65% 30%; }
    #v2 { object-position: 55% 30%; }
    .copy, .copy.two { bottom: 5vh; left: 7vw; right: auto; width: min(44vw, 340px); }
    .copy h1 { font-size: clamp(1.6rem, 4.5vw, 2.4rem); margin: 6px 0; line-height: 1.05; }
    .copy p, .copy-stats, .copy-progress { display: none; }  /* hide secondary copy on tiny landscape */
    .copy .btn { margin-top: 10px; padding: 10px 14px; font-size: .9rem; }
}
```

**Do NOT add `display:none` or `opacity:1 !important` on videos in mobile/landscape CSS.**  
Both videos must run on all screen sizes — the crossfade works on mobile. Forcing opacity/display breaks the JS-driven animation.

---

## JavaScript — Scroll-Driven Crossfade

```javascript
var reduce  = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var f       = document.getElementById('flow');
var a       = document.getElementById('v1');
var b       = document.getElementById('v2');
var c1      = document.getElementById('c1');
var c2      = document.getElementById('c2');
var hasTraining = !!(f && !f.hasAttribute('data-no-training'));

/* ─── VIDEO PLAY ─── */
function play(v) {
    if (!v) return;
    v.muted = true;                     // belt-and-suspenders: enforce mute in JS too
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
}

play(a);

var v2ready = false;
function ensureV2() {
    if (!v2ready) { v2ready = true; play(b); }
}

/* Start v2 on first user interaction (touchstart on mobile, click on desktop) */
['click', 'touchstart', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, function () { play(a); ensureV2(); }, { once: true, passive: true });
});

/* ─── SMOOTHSTEP MATH ─── */
function clamp(n, lo, hi) { return Math.max(lo, Math.min(hi, n)); }
function ss(e0, e1, x) {
    var t = clamp((x - e0) / (e1 - e0), 0, 1);
    return t * t * (3 - 2 * t);
}

/* ─── TICK (runs on every scroll event) ─── */
function tick() {
    if (!f || !hasTraining) return;
    var max = f.offsetHeight - innerHeight;
    var p   = max > 0 ? clamp(scrollY / max, 0, 1) : 0;
    var x, y;

    if (reduce) {
        x = p > 0.4 ? 1 : 0;
        y = p > 0.55 ? 1 : 0;
    } else {
        x = ss(0.14, 0.58, p);   /* video crossfade range: 14%→58% of scroll */
        y = ss(0.48, 0.73, p);   /* copy crossfade range: 48%→73% of scroll */
    }

    if (a) { a.style.opacity = String(1 - x); a.style.transform = 'scale(' + (1 + 0.03 * x) + ')'; }
    if (b) {
        if (x > 0.1) ensureV2();   /* lazy-start v2 when crossfade begins */
        b.style.opacity = String(x);
        b.style.transform = 'scale(' + (1.03 - 0.03 * x) + ')';
    }
    if (c1) {
        var op1 = 1 - Math.min(1, x * 2);
        c1.style.opacity      = String(op1);
        c1.style.transform    = 'translateY(' + (-x * 24) + 'px)';
        c1.style.pointerEvents = op1 < 0.05 ? 'none' : 'auto';  /* CRITICAL */
    }
    if (c2) {
        c2.style.opacity      = String(y);
        c2.style.transform    = 'translateY(' + (28 - y * 28) + 'px)';
        c2.style.pointerEvents = y < 0.05 ? 'none' : 'auto';    /* CRITICAL */
        c2.setAttribute('aria-hidden', y < 0.05 ? 'true' : 'false');
    }
}

addEventListener('scroll', tick, { passive: true });
addEventListener('resize', tick, { passive: true });

/* Reset scroll to top on load, then run tick */
requestAnimationFrame(function () {
    requestAnimationFrame(function () {
        window.scrollTo(0, 0);
        tick();
    });
});
```

---

## Video Specs — Required for Mobile Compatibility

| Property | Requirement | Why |
|---|---|---|
| Codec | H.264 (libx264) | Runway AI exports 10-bit H.264 which Safari/iOS rejects |
| Pixel format | `yuv420p` (8-bit) | `yuv420p10le` (10-bit) = black screen on mobile |
| Profile | `main` or `baseline` | Not `high` for best mobile compat |
| Audio | None / stripped | No audio track = no mute battles |
| Moov atom | `faststart` | Starts playing before full download |
| Resolution | Max 1080p | Larger = unnecessary bandwidth |
| Size target | <2MB per video | Ambient loops: aim 1–2MB |

**FFmpeg re-encode command (run when Runway video is black on mobile):**
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -profile:v main -pix_fmt yuv420p \
  -movflags +faststart -an \
  -crf 23 -preset slow \
  output-web.mp4
```

**Check codec before deploying:**
```bash
ffprobe -v quiet -print_format json -show_streams input.mp4 | grep pix_fmt
# Should be: "pix_fmt": "yuv420p"  (NOT yuv420p10le)
```

---

## Known Bugs & Fixes (Documented)

### Bug 1: Button blocked by invisible overlay
**Symptom:** CTA button in first copy section (c1) doesn't respond to taps on mobile.  
**Root cause:** c2 is `position: absolute` at the same coordinates as c1. CSS `opacity: 0` does NOT disable `pointer-events` — the invisible c2 intercepts all taps.  
**Fix:** `pointer-events: none` in CSS for `.copy.two` initial state + toggle in `tick()` based on opacity threshold.

### Bug 2: Video black on mobile (codec)
**Symptom:** v2 shows as black/blank on iOS Safari or Android Chrome.  
**Root cause:** 10-bit H.264 (`yuv420p10le`) — generated by Runway AI and some export tools. Mobile browsers only support 8-bit.  
**Fix:** Re-encode with FFmpeg command above. The `-web` suffix convention (`hero-ambient-web.mp4`) marks web-safe re-encodes.

### Bug 3: Face completely cropped on mobile portrait
**Symptom:** Model's face barely visible — only the right edge showing.  
**Root cause:** `object-position: 50%` centers the crop on the middle of the video frame. If the face is at 70% horizontal, centering at 50% crops it off.  
**Fix:** Set `object-position: 70-75% 12%` on mobile to shift the crop rightward toward the face.

### Bug 4: Two mobile fixes that are WRONG
**Never do these:**
- `#v2 { display: none }` on mobile — breaks crossfade entirely
- `#v1 { opacity: 1 !important }` on mobile — fights JS animation, freezes v1

Both videos should play on all screen sizes. Mobile autoplay of 2 muted `playsinline` videos works if both have `muted` HTML attribute AND `v.muted = true` in JS.

### Bug 5: RTL page flip from Blade `$lesson` variable leak
**Symptom:** If any Blade view that extends a layout containing `@if(isset($lesson) && $lesson->isArabic()) dir="rtl"` uses a loop variable named `$lesson`, the last iteration leaks into layout scope, silently flipping the entire page to RTL.  
**Fix:** Never name loop variables `$lesson` in views that extend such layouts. Use `$courseLesson`, `$topLesson`, etc.

---

## Customization Guide

| Variable | Where | What to change |
|---|---|---|
| Scroll height | `.flow { height: 300vh }` | Increase for slower crossfade; decrease for quicker |
| Crossfade start/end | `ss(0.14, 0.58, p)` | First two numbers = % of scroll where crossfade begins/ends |
| Copy transition | `ss(0.48, 0.73, p)` | When second copy section appears |
| Navbar height | `top: 52px` / `height: calc(100svh - 52px)` | Match your actual navbar height |
| Face crop desktop | `#v1 { object-position: 70% 0 }` | Horizontal % = where in frame the face lives |
| Face crop mobile | `#v1 { object-position: 72% 12% }` | Second value = vertical — 12% keeps face in upper band |
| Copy width desktop | `width: min(470px, 40vw)` | Max copy block width |
| Flow height mobile | `.flow { height: 280vh }` | Shorter than desktop — mobile scroll is faster |

---

## Poster Images

Each video needs a poster JPEG — shown before video loads and on slow connections.

- `poster="{{ asset('Videos/<section>/hero-welcome-poster.jpg') }}"` for v1
- `poster="{{ asset('Videos/<section>/second-ambient-poster.jpg') }}"` for v2

**Poster size:** 1280×714 (16:9, 720p equivalent). Compress to <50KB with ImageMagick or PowerShell `System.Drawing`.

**PowerShell resize command:**
```powershell
Add-Type -AssemblyName System.Drawing
$src = [System.Drawing.Image]::FromFile("C:\path\to\input.jpg")
$dst = New-Object System.Drawing.Bitmap(1280, 714)
$g = [System.Drawing.Graphics]::FromImage($dst)
$g.DrawImage($src, 0, 0, 1280, 714)
$dst.Save("C:\path\to\poster.jpg", [System.Drawing.Imaging.ImageFormat]::Jpeg)
$g.Dispose(); $dst.Dispose(); $src.Dispose()
```

---

## Pattern B: Canvas Frame-Sequence (Rodrigo Olivares / Dynamo Sites SOP)

Source: *Crea Webs Animadas Increíbles en Minutos* + *Así Creo Webs Animadas con Gemini Omni Flash 1.1 y Antigravity*

### Concept

Instead of a video that the user watches passively, you pre-render 60–90 frames from a video and draw them on a `<canvas>` — advancing forward/backward in sync with scroll position. This gives "video scrubbing" without any autoplay restriction or codec issue.

### Asset Preparation (done OUTSIDE the code agent)

1. **Hero image** — subject offset (right or left) to create negative space for headline + CTA
2. **Ambient loop video** — 3–5s seamless loop, subtle camera, fixed position → use as `<video autoplay loop muted playsinline>` background
3. **Scroll sequence video** — subject CENTERED (for mobile crop safety), subtle camera orbit, fluid motion → export as frame sequence

**Framing rule:**
- Hero section: subject RIGHT-aligned → headline on left, CTA on left
- Scroll animation scene: subject CENTERED → safe on all viewports without cropping

### Frame Export (FFmpeg)

```bash
# Export 80 WebP frames from a video (adjust -r for frame count relative to video length)
ffmpeg -i input.mp4 -vf "fps=25,scale=1920:-1" -q:v 80 assets/frames/frame_%03d.webp

# Or JPEG if WebP not supported
ffmpeg -i input.mp4 -vf "fps=25,scale=1920:-1" -q:v 3 assets/frames/frame_%03d.jpg
```

Target: 60–90 frames, each ~15–30KB (WebP). Total frame folder: <2MB.

### HTML Structure

```html
<section class="canvas-section" id="canvas-section">
  <div class="canvas-sticky">
    <canvas id="product-canvas"></canvas>
    <div class="canvas-copy" id="copy-phase-1">
      <h2>Two-line</h2>
      <h2>editorial headline.</h2>
    </div>
    <div class="canvas-copy" id="copy-phase-2" style="opacity:0">
      <p>Feature callout at mid-scroll</p>
    </div>
    <div class="canvas-copy canvas-cta" id="copy-phase-3" style="opacity:0">
      <a href="#buy" class="btn">Buy now →</a>
    </div>
  </div>
</section>
```

### CSS

```css
.canvas-section {
    height: 300vh;  /* scroll space — adjust for desired scrub speed */
    position: relative;
}
.canvas-sticky {
    position: sticky;
    top: 0;
    height: 100vh;
    overflow: hidden;
    background: #000;
}
canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.canvas-copy {
    position: absolute;
    z-index: 3;
    left: 7vw;
    bottom: 20vh;
    color: #fff;
    transition: opacity .3s;
}
```

### JavaScript — Canvas Scroll Engine

```javascript
(function () {
    var TOTAL_FRAMES = 80;         // must match your frame count
    var FRAME_PATH   = 'assets/frames/frame_%03d.webp';  // adjust extension
    var canvas       = document.getElementById('product-canvas');
    var ctx          = canvas.getContext('2d');
    var section      = document.getElementById('canvas-section');
    var frames       = [];
    var loaded       = 0;
    var currentFrame = 0;

    function pad(n) { return String(n).padStart(3, '0'); }

    // Preload all frames
    for (var i = 1; i <= TOTAL_FRAMES; i++) {
        (function (idx) {
            var img = new Image();
            img.src = FRAME_PATH.replace('%03d', pad(idx));
            img.onload = function () {
                loaded++;
                frames[idx - 1] = img;
                if (loaded === 1) drawFrame(0);  // show first frame immediately
            };
        })(i);
    }

    function drawFrame(idx) {
        if (!frames[idx]) return;
        canvas.width  = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
        // Cover-fit the image on canvas
        var img = frames[idx];
        var scale = Math.max(canvas.width / img.width, canvas.height / img.height);
        var w = img.width * scale;
        var h = img.height * scale;
        var x = (canvas.width - w) / 2;
        var y = (canvas.height - h) / 2;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, x, y, w, h);
    }

    function getProgress() {
        var rect = section.getBoundingClientRect();
        var total = section.offsetHeight - window.innerHeight;
        return Math.max(0, Math.min(1, -rect.top / total));
    }

    function tick() {
        var p = getProgress();
        var frame = Math.min(TOTAL_FRAMES - 1, Math.floor(p * TOTAL_FRAMES));
        if (frame !== currentFrame) { currentFrame = frame; drawFrame(frame); }

        // Fade copy phases at scroll milestones
        var p1 = document.getElementById('copy-phase-1');
        var p2 = document.getElementById('copy-phase-2');
        var p3 = document.getElementById('copy-phase-3');
        if (p1) p1.style.opacity = p < 0.25 ? '1' : p < 0.35 ? String(1 - (p - 0.25) / 0.1) : '0';
        if (p2) p2.style.opacity = p >= 0.35 && p < 0.65 ? String(Math.min(1, (p - 0.35) / 0.1)) : p >= 0.65 ? '0' : '0';
        if (p3) p3.style.opacity = p >= 0.75 ? String(Math.min(1, (p - 0.75) / 0.1)) : '0';
    }

    window.addEventListener('scroll', function () { requestAnimationFrame(tick); }, { passive: true });
    window.addEventListener('resize', function () { drawFrame(currentFrame); });
    requestAnimationFrame(tick);
})();
```

### Anti-Slop Audit Checklist

Before shipping any AI-generated page, remove all of these:
- [ ] Pill badges / eyebrow chips (`<span class="badge">NEW</span>` etc.)
- [ ] Floating tag counters / metric bubbles
- [ ] Decorative rounded cards with icons just for decoration
- [ ] Generic section dividers (wavy SVGs, gradient bars)
- [ ] Font sizes that are all the same — enforce editorial scale (large title, small body)
- [ ] Dark overlay boxes placed over the product/subject in the canvas
- [ ] Verbose text (more than 2 lines per callout in scroll sections)

### Rodrigo SOP — 4-Prompt Agent Script

When instructing an AI coding agent to build this pattern from scratch:

**Prompt 1 — Hero only:**
> "Create a modern minimal HTML/CSS/JS landing page for [Brand]. Build ONLY the hero section using `assets/hero-bg.jpg` as background. Left side: brand name, 2-line editorial headline, short subheading, primary CTA. Right side: empty for the background focal subject. No secondary sections. Clean typography."

**Prompt 2 — Canvas scroll engine:**
> "Add a full-screen sticky canvas section below the hero. Height: 300vh. Preload 80 frames from `/assets/frames/frame_%03d.webp`. Bind rendering to scroll progress — forward scroll advances frames, backward reverses, stopping freezes the frame. Use requestAnimationFrame. Cover-fit frames to fill viewport."

**Prompt 3 — Copy overlays:**
> "Add editorial text that fades in/out at scroll milestones over the canvas: 0–25% scroll: headline 1. 35–65%: headline 2 + feature point. 75–100%: final CTA. Use progressive background darkening toward the section end — no dark boxes over the center subject."

**Prompt 4 — Anti-slop:**
> "Do an anti-slop audit: remove all pill badges, eyebrow chips, tag counters, decorative cards. Ensure font sizing has clear editorial scale. Check canvas stays centered on mobile without cropping the subject."

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
