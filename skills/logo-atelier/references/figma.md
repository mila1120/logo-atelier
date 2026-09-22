# Figma workflow

Read the installed Figma use skill before calling use_figma; also load generate-library for components and create-new-file before a new file. Template source is in `../figma/template-state.json`. Do not edit the shared template for a client project: duplicate the file manually or use an authorized dedicated project page/file. Record the actual project file and nodes in project.json.

The legacy template has Start / brief, Directions / three sample slots, Master, Proof and Material zones. These are examples, not a limit of three concepts. For live projects follow `modular-design.md`: create or reuse real role Sections, plus Palette and Composition / Final; populate them with editable comparisons. Do not mutate the shared template or reorganize historical project content merely to match this structure.

Layer contract: preserve the `Background`, `Foreground`, optional `Accent` wrapper for compatibility. Within Foreground, separate Shape, Expression and Supporting Motif where applicable; separate supporting surfaces from details such as keys. Follow the anchor, perspective and occlusion relationships in `modular-design.md`. Keep role colors distinct from material parameters. When using components, the main component is the geometry editing surface and instances override supported properties; make structural changes in the main component or a deliberately detached, versioned working copy. Native frames/groups remain valid for exploratory assets.

Before each mutation read existing nodes and affected properties; record/export a snapshot when changing geometry. Preserve unrelated edits. Use the real node IDs, not names alone. Export the user's current Figma vector edits back to a new canonical SVG version before rendering. If export contains unsupported portable-profile constructs, normalize deliberately and visually compare, never simply rename a raster as SVG.

Bi-directional sync is agent-mediated, not continuous. There is no v1 sidebar plugin, drag automation or background watcher. Native Figma supports manual dragging, reordering and recoloring. Interpret “swap foreground/background” explicitly as either swapping colors or swapping layer roles; do not assume the two mean the same thing.

Track source-to-composition-to-mock IDs per `modular-design.md`. Refresh mapped mock icon slots after authorized source edits; preserve phone layout and scope. Validate changed versus locked properties for recoloring, resizing and expression swaps. Same-name nodes are not a reliable mapping.

Shared-template scripts are construction records, not idempotent migration scripts. Never rerun them against a project. Every real project retains its own node ledger, baseline exports and review history.

For the stage order and counts, read `workflow-1.0.md`. Create or reuse a Reference Section, collect about 30 verified references per intention across suitable styles and sources, and let the user pick 2–3 per category. Reference kinds remain distinct. Reuse existing research and selections; keep sources in project records.

Build rough geometry, background and applicable supporting motif independently, then combine representative previews. Color/material exploration follows geometry selection; use `palette-board.md` for about 25 variants per selected shape and separate background comparisons. There is no mandatory three-background or ten-palette pre-stage.

Presentation default: concept and asset boards contain artwork only. Put short names/numbers in native frame/section/layer titles, not text nodes. No explanatory text pages. Keep rationale and validation in local project records; retain user reference annotations.

For comment-based revisions, follow `comment-driven-iteration.md`: read actual threads through a supported connector or the Figma UI, map pins to source/mock nodes, preserve versions and verify each feedback item. Do not infer comment contents from design metadata.
