# Render and review

1. Run `python3 scripts/atelier.py validate <master.svg> --report <proof/structure.json>`.
2. Run `node scripts/render.cjs <master.svg> <new-proof-directory>`. Requires sharp (`npm install` at plugin root, or set NODE_PATH to an available dependency directory). PYTHON may point to a Python 3 runtime. Renderer refuses unsupported SVG profile and refuses an existing output directory. It writes 16/24/32/64/128/1024 px PNGs, light/dark proof sheet, hash manifest and HTML viewer. These are diagnostic sizes, not a complete iOS asset catalog.
3. Open proof.png and native PNGs. Judge actual small files at 100% in a browser/Figma; enlargement is diagnostic only. Inspect clipping, holes closing, ambiguous silhouette, uneven apparent weight and background contrast. The preview does not prove OS appearance. Never approve based only on source code or a beautiful 1024 px mockup.
4. Test monochrome and reverse masters too. A colored master rendered on a dark background is not a reverse-color master. Produce explicit variants in project/variants and run the same checks.
5. Save review.json containing master_sha256, reviewer, date, tested_sizes, actual_viewed_files, findings, changes, structure_status, visual_status, user_approval and pending_checks. A new geometry version invalidates the prior visual review.
6. For material studies compare silhouette with the master. For exact final branding, place the original master with a deterministic renderer; use generated mockups as presentations with declared limitations.

Technical checks automate structural failures. Aesthetic scores and actual visibility need visual examination. This v1 does not certify production readiness automatically, validate trademark registration, or simulate an iPhone.

For concept, color or material exploration, include the focused checks in `taste-integration.md` in this same review record. Keep protected geometry/style decisions visible in the findings; do not add a separate approval gate.
