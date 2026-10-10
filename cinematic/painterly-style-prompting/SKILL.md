---
name: painterly-style-prompting
description: Use whenever creating, revising, or reviewing prompts for painterly images, animation, or video in any project. Translate the project's brief and approved visual references into concrete, repeatable rendering instructions; keep each prompt self-contained and protect project-specific style, character, continuity, camera, and audio rules. Do not impose one house style on every project.
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Painterly Style Prompting

Use this skill for painterly image and video work across projects. Its job is to turn a visual intention or approved reference into clear production language that a generator can follow repeatedly. Treat this as a flexible method, not a single mandatory look.

## 1. Establish the style authority

Before drafting, identify the controlling source in this order:

1. The user's explicit direction and the project's approved style bible.
2. Approved style/reference images for rendering and material treatment.
3. Character sheets for identity and wardrobe.
4. Location, prop, storyboard, composition, and continuity references for their own domains.
5. Prompt prose for shot-specific action and execution.

Keep these roles distinct. A character sheet does not automatically define the rendering style, and a logo or promo image should not be treated as an episode-frame style reference unless the user intends that.

If a project has a locked style or audio rule, preserve it. Do not apply a house palette, a named franchise influence, a particular project's wardrobe, or any other project's lock by default. If the project ships its own style-lock skill (a sibling skill folder), also read that skill and include its exact lock verbatim in every applicable prompt.

## 2. Convert “painterly” into visible choices

Choose only the traits that fit the brief and references. Make them concrete:

- **Form:** flat 2D, dimensional 2.5D, or fully volumetric stylization. Do not assume painterly means flat.
- **Surface:** medium and mark-making (oil, gouache, watercolor, dry brush, impasto, pastel, textured cel paint, or a project-specific mix).
- **Shape language:** graphic value groups, silhouette clarity, shape separation, and level of simplification.
- **Edges:** where contours are crisp, soft, broken, selectively inked, or lost into the environment.
- **Color and light:** palette, contrast, shadow color, key/rim light, and atmosphere, taken from the project's references.
- **Depth:** layered foreground/midground/background, multiplane staging, parallax, and how much background detail stays legible.
- **Motion:** how painted forms, brush marks, particles, cloth, hair, and camera move without losing the authored look.

Do not merely stack style labels. Explain what the image should look and feel like at normal viewing size.

## 3. Build a reusable style lock

When consistency matters across multiple clips or images, write a compact rendering paragraph from the project brief and approved reference. It should state:

- the intended medium and mark-making;
- whether forms stay flat or dimensional;
- how surfaces, color blocks, shadows, and edges are rendered;
- palette and lighting;
- depth treatment and the main cues to avoid.

Keep identity, wardrobe, location, camera, action, continuity, dialogue, and audio in separate prompt sections. A rendering lock should not accidentally dictate unrelated story or sound choices.

For any batch of independently submitted prompts, embed the full applicable style lock inside every prompt. Do not rely on “same style as above,” a shared preamble, or instructions outside the prompt if each clip will be pasted separately. Preserve each project's references and @handles in every prompt that needs them.

## 4. Preserve dimensional painterly rendering

When the requested target is painterly 2.5D, maintain sculpted form, readable volume, and layered depth while making the surfaces look visibly authored with paint. Carry texture onto the focal subject as well as the background; background brushwork alone does not establish a painterly style.

When supported by the reference, use graphic color/value planes, tactile painted shadows, varied edge quality, selective contour accents, and visible brushwork across materials. Reduce conflicting cues such as excessive smooth gradients, uniformly plastic gloss, creamy bokeh, or shallow focus that erases the painted environment. Keep selective highlights and depth where they support form. Do not force a 2.5D treatment if the brief calls for flat 2D or another painterly medium.

## 5. Make each output prompt executable by itself

For each requested still or clip, include only the controls needed for that shot, but keep them complete:

- exact reference handles and what each controls;
- shot duration, aspect ratio, action, framing, and camera movement where known;
- identity, wardrobe, set, object, and continuity constraints;
- dialogue and sound rules as specified by the project;
- the full relevant style lock;
- concise negative constraints for the failure modes that matter.

Do not invent missing references, dialogue, music, safety steps, or exact timing. Ask a focused question only when a missing choice materially blocks a usable prompt; otherwise make and label a reasonable assumption.

## 6. Review outputs without mixing categories

When comparing generations, separate:

- rendering style and material treatment;
- character identity and set continuity;
- motion, acting, camera, and editing;
- dialogue, sync, and sound.

Compare equivalent shots or matched frames when possible. State what evidence was reviewed and avoid claiming a model or platform always performs a certain way based on one clip. Translate findings into one or two prompt changes that directly target the observed mismatch.

## Final check

Before delivering:

- Confirm the selected project's style authority and any locked overrides.
- Check that the prompt's style terms describe visible materials, edges, palette, light, and depth rather than only name-dropping influences.
- For separate clips, verify the full lock and necessary @references occur inside every prompt.
- Keep painterly texture visible on focal subjects and props when requested.
- Preserve each project's language and audio rules.
- Do not generate media or spend credits unless the user separately asks for that action.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
