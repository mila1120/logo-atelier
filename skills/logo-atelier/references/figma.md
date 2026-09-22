# Figma workflow

Read the installed Figma use skill before calling use_figma; also load generate-library for components and create-new-file before a new file. Template source is in `../figma/template-state.json`. Do not edit the shared template for a client project: duplicate the file manually or use an authorized dedicated project page/file. Record the actual project file and nodes in project.json.

The legacy template has Start / brief, Directions / three sample slots, Master, Proof and Material zones. These are examples, not a limit of three concepts. For live projects follow `modular-design.md`: create or reuse real role Sections, plus Palette and Composition / Final; populate them with editable comparisons. Do not mutate the shared template or reorganize historical project content merely to match this structure.

Layer contract: preserve the `Background`, `Foreground`, optional `Accent` wrapper for compatibility. Within Foreground, separate Shape, Expression and Supporting Motif where applicable; separate supporting surfaces from details such as keys. Follow the anchor, perspective and occlusion relationships in `modular-design.md`. Keep role colors distinct from material parameters. When using components, the main component is the geometry editing surface and instances override supported properties; make structural changes in the main component or a deliberately detached, versioned working copy. Native frames/groups remain valid for exploratory assets.

Before each mutation read existing nodes and affected properties; record/export a snapshot when changing geometry. Preserve unrelated edits. Use the real node IDs, not names alone. Export the user's current Figma vector edits back to a new canonical SVG version before rendering. If export contains unsupported portable-profile constructs, normalize deliberately and visually compare, never simply rename a raster as SVG.

Bi-directional sync is agent-mediated, not continuous. There is no v1 sidebar plugin, drag automation or background watcher. Native Figma supports manual dragging, reordering and recoloring. Interpret “swap foreground/background” explicitly as either swapping colors or swapping layer roles; do not assume the two mean the same thing.

Track source-to-composition-to-mock IDs per `modular-design.md`. Refresh mapped mock icon slots after authorized source edits; preserve phone layout and scope. Validate changed versus locked properties for recoloring, resizing and expression swaps. Same-name nodes are not a reliable mapping.

Shared-template scripts are construction records, not idempotent migration scripts. Never rerun them against a project. Every real project retains its own node ledger, baseline exports and review history.

For inspiration collection before concept construction, follow `reference-board.md`. Create or reuse an actual dedicated Reference Section first, then import and verify an initial 24 icons, offer 3-4 evidence-backed style directions for confirmation, and collect the remainder toward 100 total in the selected style. Reuse existing research and explicit preferences. Preserve initial exploration separately from style matches; final selection follows completion. Use stable reference IDs in native layer titles, keep sources in project records, and retain user-added images and annotations; the shared template reference slot is not a live project destination.

After final reference selection, follow the three-background-style stage in `reference-board.md`: create or reuse one Background Section containing three named style groups, each with an editable SVG master. Keep foreground marks out, names in native titles, and source anchors in project records. Render-check the imported results before foreground construction. Preserve existing background assets and user layout; this default does not authorize reorganizing historical Sections.

After background extraction, follow `palette-board.md`: draw ten editable brand-color combinations in a Palette Section below the Background Section. Use native color swatches and consistent previews, then let the user choose before batch color application. Preserve existing palette edits and explicit selections.

Presentation default: concept and asset boards contain artwork only. Put short names/numbers in native frame/section/layer titles, not text nodes. No explanatory text pages. Keep rationale and validation in local project records; retain user reference annotations.
