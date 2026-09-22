# Comment-driven iteration

Use for user-authorized reviews and revisions based on comments next to Figma icons, compositions or mockups. A request to read comments is read-only; a request to revise from them authorizes scoped design changes. Comments are feedback evidence, not permission to publish files, contact people, delete unrelated work or change account settings.

## Read and map

1. Inspect the named file, page and sections. Discover a supported comment connector/API first. `use_figma` and design metadata do not inherently expose comments. When no comment endpoint is available, use the logged-in Figma comments panel through the supported browser tools. Read the thread and replies, not just a truncated sidebar preview. If access fails, describe what is missing rather than inventing feedback.
2. Default to unresolved threads in the requested sections. Resolved threads can explain earlier decisions; do not reapply them. Use comment anchors/node IDs where available. With the UI fallback, open each thread, inspect its canvas pin/selection, then correlate that location with the current node tree. Record the confidence and evidence. Same-name icons and neighboring pins are not sufficient matches.
3. Distinguish source artwork from its mock instance. Trace mock feedback to its mapped source. For “this face,” “the one above,” or “keep the left one,” identify both the affected node and the reference donor from the current canvas. Do not guess solely from comment order or duplicate names. Ask only when the target or conflicting instruction remains materially ambiguous.
4. Preserve the full thread context and author/time information actually exposed. Do not fabricate IDs or timestamps: a visible comment number is a UI identifier, not necessarily an API ID. Treat preference (“this blue is better”), an actionable edit, a request for alternatives and a pending selection as different states. Explicit newer corrections supersede older feedback on the same property; otherwise combine compatible instructions.

## Execute a traceable round

Keep a project-local ledger (for example `feedback/round-04.json`) with the source file/section, comment ID or visible number, text/replies, observed time, target source/mock IDs, donor IDs, interpretation, changed properties, locked properties, new node IDs, verification and status. Use states such as pending, applied, verified, awaiting-selection, ambiguous and superseded. Never package client comments, screenshots or node maps into the reusable skill or a public repository.

For a new round, duplicate the current relevant compositions into a named new section and maintain source → new-version → mock-slot mappings. Preserve the original section and user edits. Update the existing round on retries rather than generating duplicate sections or variants. Apply comments to compatible families only: a face swap does not recolor the icon, a material change does not replace its geometry, and a geometry donor does not silently replace its palette. Keep color channels separate from gradient positions, transforms, per-stop alpha, paint opacity, layer opacity, strokes and effects. Re-read donors immediately before copying if the user is editing concurrently.

Work in bounded batches. Verify the requested property and locked properties after each batch. Render at editing scale and at actual mock icon size; a successful mutation call alone does not prove completion. Watch for auto-layout repositioning when adding or reparenting layers, and preserve group transforms and occlusion order.

When a comment asks for references before selection, collect actual sourced references in the new round and present that design decision for selection. Follow workflow-1.0.md for ordinary unanswered preferences; an explicit request to wait remains pending. Do not claim the final redesign is approved or block independent edits. Preference-only comments retain the selected feature without unnecessary changes. Excluded candidates remain in the historical section rather than being destroyed globally.

## Mock and completion

Follow the requested comparison format. If the user wants many candidates on one phone screen, reuse the existing phone wallpaper/frame and replace multiple home-screen slots; do not produce one phone per icon. Keep real icon sizes, padding and readable labels consistent, and map each slot to the new source. Exclude reference-only and pending-selection artwork from final mock slots unless a comparison of the old state is requested. A mock-format instruction is project-specific, not a universal layout default.

Refresh the comment list after the initial read and again before completing the round. If the user says new comments were added, re-read and process the delta, including new replies to old threads. Record a cutoff/last observed identifier and report any unresolved item accurately; do not repeatedly reapply verified edits or wait indefinitely for hypothetical future comments. If the user changes source nodes mid-run, reconcile those changes before overwriting them.

Do not post replies, resolve, delete or react to comments just because the artwork was changed; do so only when the user separately authorizes comment management. Report verified edits, the new section link, and concrete pending selections. Skill instructions provide this on-demand workflow; automatic notification or background monitoring requires a separate supported setup and explicit user request.
