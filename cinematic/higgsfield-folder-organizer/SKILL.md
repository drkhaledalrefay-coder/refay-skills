---
name: higgsfield-folder-organizer
description: "Use when reorganizing assets (images/videos/character sheets) inside a Higgsfield.ai project via the browser UI — drag-and-drop into folders, multi-select, bulk download. Never use to trigger generation."
author: Khaled Al Refay
license: CC-BY-4.0
source: https://github.com/drkhaledalrefay-coder
---

# Higgsfield Project Folder Organizer

A reusable technique for organizing assets inside any Higgsfield.ai project canvas using browser automation (Claude's built-in browser or Claude in Chrome). This works at the UI/folder level — completely separate from the Higgsfield MCP tools, which can only list/create assets and cannot rename, delete, or move them into folders.

## HARD SAFETY RULE — NEVER VIOLATE

Never trigger any AI generation action inside Higgsfield during an organizing session. Forbidden buttons/menus/actions include (but are not limited to):
- Generate / Recreate / Regenerate
- Create Video / Create Image / Create Element / Create Character
- Turn to video
- Upscale
- Any model-selector dropdown or "Run" button

Only these actions are permitted: Select / multi-select, drag-and-drop between folders, Add folder / rename folder, Download, and viewing an asset in the lightbox (always close via X or Escape, never click action buttons inside the lightbox).

**Recovery procedure**: If a generation-related menu or dialog is accidentally opened, immediately press Escape or click the X to close it, then tell the user exactly what happened (what was clicked, what opened, and that it was closed without running).

## Background facts about the Higgsfield UI

- Each project has a flat "All assets" pool plus custom folders. Folder tags are non-exclusive — an asset can appear in multiple folders and still shows in "All assets".
- Some thumbnails that look like video/scene tiles are actually static images. Verify by opening the lightbox and checking for "Edit Image" (image) vs playback/video controls (video), and by reading the prompt text shown.
- The workspace-level Elements/Souls library (Soul characters, reference elements) is separate from a project's Canvas folders — it's a shared pool across ALL of the user's projects, not project-specific.
- Each project has a Project Brief doc that may still be the default empty template and worth checking/filling in.

## Technique: drag-and-drop a single asset into a folder

1. Take a screenshot to see current state.
2. Hover over the source tile first (required immediately before the drag — the hover state must be freshly triggered).
3. Use left_click_drag from the source tile to the target folder row in the sidebar (folder rows are typically around x=135).
4. Take a fresh screenshot before each subsequent drag — the view re-renders after every move, so coordinates from a prior screenshot are not reliable for the next drag.

## Technique: multi-select

1. Hover over a tile to reveal its "..." icon (typically around x=479–517).
2. Click "..." then click "Select".
3. Checkboxes appear on tiles; click additional tiles to add them to the selection.
4. A bottom toolbar shows "{n} selected" with actions: Download / Move to / Copy to / Delete.

## Technique: bulk download

1. Multi-select the desired assets (see above).
2. Click Download in the bottom toolbar.
3. This produces a client-side zip. If the browser is running on the user's own machine (via the Claude desktop app / built-in browser), the zip lands in their real Downloads folder.

## Organizing principles for film/video projects

- Group all character sheets together in one folder regardless of which character they depict (e.g. `01_Character_Sheets`), rather than splitting by character.
- Numbered scene folders should contain only actual scene content — no character-sheet turnarounds mixed in.
- Audit every folder via screenshot before declaring a reorganization pass complete — don't assume a move succeeded without visually confirming folder contents/counts.
- Conventions vary by project — always explicitly confirm the proposed organizing structure with the user before doing a large reorganization. Never assume a structure and start moving assets without sign-off.

## Suggested workflow

1. List existing folders and their current item counts (screenshot the project canvas / sidebar).
2. Open each folder to identify what's actually inside (use the lightbox-check technique above to distinguish image vs video, and to read prompts if content is ambiguous).
3. Propose a folder structure to the user (or confirm an existing structure already matches the project's needs) and get explicit confirmation before moving anything.
4. Execute moves via the hover-then-drag technique once confirmed, taking a fresh screenshot and verifying folder counts after each move.
5. Report the final structure with item counts per folder.

---
*Created by **Khaled Al Refay** · Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and adapt with attribution.*
