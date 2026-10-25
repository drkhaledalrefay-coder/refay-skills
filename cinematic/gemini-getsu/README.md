# gemini-getsu: Google Flow prompt pack

## بالعربي: السكيل دي بتعمل إيه؟

**بتكتب لك برومبتات جاهزة للنسخ واللصق في Google Flow.** مش بتولّد فيديو، ومش بتصرف كريدت، ومش بتتصل بأي أداة. شغلها إنها تحوّل فكرتك وملفاتك لخطة صغيرة وبرومبتات مظبوطة، بحيث ما تصرفش كريدت على محاولات مكررة.

**الفكرة اللي بتتبعها (نفس اللي اتعمل في الفيديو):** تاخد **مقطع واحد أصلي** وتطلع منه أكتر من نسخة، كل نسخة بشخصية مختلفة، والأداء والحركة والتوقيت والكاميرا فاضلين زي ما هما. شبه فيديوهات Higgsfield Genjutsu، بس بتتعمل في Google Flow.

### بتاخد منك إيه
1. **مقطع أصلي واحد** (الملف وطوله ونسبة الشاشة).
2. **صورة مرجعية لكل شخصية** (صورة واحدة لكل شخصية).
3. **الكلام بالنص** لو حد بيتكلم (باللهجة واللغة زي ما هو).
4. عدد المقاطع ونسبة الشاشة والستايل (اختياري).

لو ناقص حاجة، بتسألك سؤال واحد قصير بس لو الإجابة هتغيّر النتيجة.

### بتطلّع لك إيه
1. **خريطة الملفات:** سطر لكل نسخة، مثلاً `نسخة 1 = المقطع الأصلي + صورة المحارب`.
2. **برومبت مستقل لكل نسخة** في خمس أجزاء بالترتيب: إيه اللي بيتغيّر بس، وإيه اللي بيفضل زي ما هو، وهوية الشخصية والملابس، والكلام بالنص، وقايمة ممنوعات (مفيش ترجمة، ولا نص على الشاشة، ولا لوجو، ولا ناس زيادة، ولا موبايل ظاهر).
3. **قايمتين فحص:** قبل التوليد (ملف أصلي واحد، صورة واحدة لكل برومبت، الكلام اتنسخ حرف بحرف) وبعد التوليد (نص محروق، لوجو، موبايل في الانعكاس، الحركة مطابقة، الشخصية ثابتة).

### القواعد اللي ما بتتغيّرش
- **كل نسخة بتتعمل من المقطع الأصلي نفسه**، مش من نتيجة نسخة قبلها. ده اللي بيمنع الانحراف.
- ما بتخترعش شخصيات ولا مقاطع ولا نص كلام.
- بدون أسعار أو ادعاءات سرعة أو جودة. النتايج بتختلف من مقطع لمقطع.
- استبدل شخص بس لو هو موافق، وفي لقطات من حقك تستخدمها.

### إزاي تستخدمها
- **في Claude Code أو Codex أو أي أداة بتدعم السكيلز:** حط فولدر السكيل في مجلد السكيلز بتاع الأداة، واكتب مثلاً «اكتب لي برومبتات Google Flow لتلات نسخ من المقطع ده» وارفق الملفات.
- **في أي شات (ChatGPT، Gemini...):** افتح `portable-prompt.md`، انسخه كله، والصق تحته فكرتك وملفاتك.
- بعد ما تاخد البرومبتات، **انت اللي بتشغّلها** في Google Flow وتراجع النتيجة بقايمة الفحص.

### مثال سريع (بدون تخمين)
المقطع الأصلي: 8 ثواني في كافيه، شخص بيشرب شاي. التلات نسخ: محارب، جندي، أرنب بنفسجي. الكلام: «الشاي ده مش مظبوط» في الأربعة.

```
نسخة 1 = SOURCE.mp4 + warrior.png → المحارب
نسخة 2 = SOURCE.mp4 + soldier.png → الجندي
نسخة 3 = SOURCE.mp4 + bunny.png  → الأرنب البنفسجي
```
وبعدها برومبت لكل نسخة بالشكل ده:
```
Replace only the person performing in the attached video with the attached character, a medieval warrior. Keep the same cafe setting, framing, camera, action, timing, props and lighting as the source video, frame for frame.
Dialogue: الشاي ده مش مظبوط at the same moment as in the source. No other speech.
No subtitles, no text, no logos, no extra people, no phone or recording device visible anywhere, including reflections.
```

### لازم تعرف
- دي **مش** سكيل ALTER الأصلية، دي مستوحاة منها (ALTER by Scenario، ترخيص MIT). ومش تابعة لـ Google ولا Scenario ولا Higgsfield.
- السكيل بتكتب البرومبتات، ومكتوب فيها بالنص إنها ما تدّعيش إن فيديو اتولّد إلا لو اتولّد فعلاً.

---

## English: what does this skill do?

**It writes copy-ready prompts for Google Flow.** It does not generate video, spend credits or connect to any tool. It turns your idea and files into a small plan and tight prompts so you do not waste credits on duplicate attempts.

**The method (the same one used in the video):** take ONE original clip and make several versions of it, each with a different character, while performance, motion, timing and camera stay the same, like Higgsfield Genjutsu videos but made in Google Flow.

**Inputs:** one source clip, one reference image per character, the exact dialogue if anyone speaks, and optionally clip count, aspect ratio and style. It asks at most one short question, only when the answer changes the result.

**Outputs:** (1) an asset map, one line per version; (2) one standalone prompt per version (what changes, what stays, character identity, verbatim dialogue, negatives); (3) a pre-generation checklist and a post-generation QA checklist.

**Fixed rules:** every version comes from the SAME original clip, never from another version's output; no invented characters, clips or dialogue; no price, speed or quality claims; recast only people who agreed, in footage you may use.

**How to use it:** drop the folder into your agent's skills folder (Claude Code, Codex and similar) and ask for Google Flow prompts with your files attached; or paste `portable-prompt.md` into any chat. You run the prompts in Google Flow yourself and review results with the QA checklist.

**Credit:** not the original ALTER skill: inspired by ALTER by Scenario (MIT). Not affiliated with Google, Scenario or Higgsfield.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Inspired by ALTER by Scenario (scenario-alter, MIT)*
