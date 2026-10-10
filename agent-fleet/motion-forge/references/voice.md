# Voice-over

## When
Only after picture lock (or at least beat lock). Timings come from the EDL, not guesses.
Ask the director once: one recording for the whole video, or per section? Which voice for which
video? (Two videos may use two narrators — never mix them inside one video.)

## Prompt (ElevenLabs v3/v4 style) — paste inline in chat
- Settings line: voice name, model, Language Override, Speed 1.0, Stability ~50, Similarity ~75, no Enhance.
- One paste-ready block, one paragraph per line, blank line between, `[pause]` between sections.
- Tags per paragraph only (not mid-sentence): historical/opening `[calm] [thoughtful] [slow]`;
  explanation `[warm] [clear]`; claims `[confident]`.
- Light diacritics on Arabic where pronunciation matters. Copy approved script text exactly — find the
  CURRENT approved script (versions get renamed: VO-SCRIPT-v2 etc.); ask the owner if unsure.
- Duration table: words ÷ ~2.1 words/s vs window. Say what to do if long (drop `[slow]`, regenerate).
- Tell the director the exact save path and file name.

## Split + placement (fleet)
- Copy the take unchanged first. Split with **whisper word timestamps** (faster-whisper
  large-v3-turbo) — silencedetect alone splits inside slow sentences. No faster-whisper → try
  whisper.cpp or openai-whisper; none installed → ask the director for paragraph timestamps and mark
  the word-order proof as "director/manual" (do not block silently).
- Export per paragraph WAV 48 kHz mono, 50 ms fades, ≤120 ms edge silence, **+300 ms tail on the last
  line**; check every cut: voice energy in the 150 ms after a cut ⇒ re-export (cut-off words are the
  most common complaint).
- Place lines **sequentially, never overlapping**, 0.25–0.4 s gaps; if a line overruns, re-time the
  PICTURE first, then atempo max 1.05× faster / 0.95× slower (beat visible while its key word is spoken).
- Limiter −1.5 dBTP → loudnorm two-pass → −16 LUFS integrated, TP ≤ −1 dBTP.
- SRT from actual placements; whisper the final audio to prove words and order.
