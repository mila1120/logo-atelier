# Taste for Logo Atelier

This is a logo-specific adaptation, not a replacement workflow or a dependency on the full frontend skill. Read for concept exploration, visual refinement and material/color studies. Keep research, editable masters, background extraction, the ten-palette board and rendered review in their existing stages.

## Read the brief through the existing work

Before drawing, reuse the confirmed keywords and inspect the latest selected references and Figma nodes. In the project's existing design notes, summarize the intended impression, recognizable motif, protected features and requested degree of change in one sentence. Ask only when an unresolved choice would materially change the result. Do not reopen a style choice already made.

Extract the 3–5 reference rules described in `design-rules.md`. Make “premium”, “fluid” or “cute” concrete: silhouette occupancy, curve transitions, gaps, optical weight, expression strokes, palette span and depth. Record the source for each rule; never claim Taste supplies a proprietary brand's exact material recipe.

## Three adapted controls

Choose qualitative levels from the request; record them in existing project notes, without making the user configure numbers. These controls are local adaptations, not aliases for the upstream frontend variables.

| Control | Low | Medium | High |
| --- | --- | --- | --- |
| Geometry variation | Preserve silhouette; adjust proportion or gaps | Change connection, segmentation or negative space within the motif | Explore different structural families while retaining the confirmed concept |
| Material depth | Flat fills, crisp layers, no simulated volume | Restrained highlight, short shadow or shallow bevel | Deliberate sculptural treatment supported by the selected reference |
| Detail density | Few forms, broad readable gaps | Additional meaningful internal structure | Expressive form with an explicit simplified small-size version |

Recoloring locks geometry. Removing a mouth-corner stroke locks the rest of the expression. A flat keyboard request sets material depth low. Many geometric variants may justify high variation but do not imply high depth or detail. Static “liquid flow” means geometry, not animation. Only introduce actual motion when it is part of the requested deliverable.

## Make variation structural and controlled

Use `modular-design.md` for the visible Figma workbench and default exploration funnel: 6–12 distinct rough directions, shortlist 2–3, then about 25 geometry variants per selected intention and about 25 color/material variants per selected shape under workflow-1.0.md. Hold one comparison axis at a time and honor requested counts or existing selections. Independent role Sections, Palette and Composition / Final make options selectable and reusable; groups inside one final icon alone are insufficient for full exploration.

- For broad explorations, organize the requested count into distinct structural families. For example, 30 shapes can use six families with five developments each; choose families from the brief, not a permanent template. Vary topology, positive/negative space, direction, proportion or connection strategy. Recolors alone do not count as geometric variants.
- Within a comparison, hold background, scale and material consistent so shape differences remain legible. Color comparisons instead hold geometry and composition fixed. Preserve the same reference perspective when perspective is a protected feature.
- For fluid shapes, use smooth tangent transitions and a consistent curve vocabulary. Inspect narrow bridges and concave turns for pinches; keep intended gaps open at actual small sizes. A soft blur cannot repair an awkward contour.
- Use optical centering and apparent weight. Allow purposeful asymmetry inside a balanced mark; the frontend preference for asymmetric page layouts does not require off-center app icons.
- Keep each family's corner, terminal and expression grammar coherent. Do not force one radius onto every shape; use a small proportional system appropriate to the geometry.

## Color and material discipline

Use the existing ten-palette workflow and role-based swatches below the Background Section. Match each candidate's exact approved colors, gradient stops, direction and neutral temperature. Multiple palettes are intentional alternatives; the frontend one-accent rule does not reduce ten requested combinations to one.

For a segmented mark intended to read as one surface, map gradients across the whole mark rather than restarting the gradient in each segment. Keep lighting direction, edge highlights and shallow depth consistent across the family. Material supports the silhouette; it must not hide weak geometry, soften exported edges or change the intended apparent size.

Blue, violet, gradients, sparks and symmetry are valid when the brief or selected reference supports them. Avoid habitual defaults, not the user's requested aesthetic. A white-only or flat request takes precedence over any suggestion to add shadows, texture or depth. Preserve intended white keycap surfaces when removing an unwanted outer white rectangle.

## Add to the existing visual review

Use `review.md` and its actual rendered evidence, rather than a second scoring system. Check:

1. The intended motif reads in silhouette and native small-size exports; bridges, gaps and expression strokes survive.
2. Variants differ in the requested dimension and protected features remain intact.
3. Curves, corners, spacing, weight and centering follow the chosen family rules.
4. Palette and material remain coherent across connected and separated parts; edges and crops are clean.
5. Each distinction supports the brief rather than adding decoration to fill the requested count.

Record findings, unresolved weaknesses and changes in the existing review record. Aesthetic review does not establish trademark uniqueness or replace user selection. Keep concept boards visual-only with native frame/section/layer names.

## Source and maintenance

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), core `skills/taste-skill/SKILL.md`, revision `5217fb45be2c0b302f29c9cd31cbd3237501c684` (installed 2026-09-21; upstream calls this v2 experimental). Relevant source areas: brief inference, three dials, color/shape consistency, material restraint, redesign preservation and final visual checks. License: MIT; see `taste-license.txt`.

The full upstream skill is installed independently as `design-taste-frontend` for its frontend use cases. This adaptation is self-contained so Logo Atelier remains usable when shared without that installation. Future upstream updates should be reviewed before changing this adaptation; do not automatically import framework mandates, stock-icon restrictions, fixed palette bans, mandatory motion or page-copy rules into logo work.
