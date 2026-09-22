# Simple Icons / 现有品牌矢量参考

Use for known-brand SVG lookup, supplemental shape studies and authorized brand collections. Simple Icons is a community-maintained brand-icon library, not a generator of original logos or proof that a brand officially endorses an asset. The separately installed skill is MengTo's `company-logos`, not an official skill named `simple-icons`.

## Source and retrieve

1. Confirm the exact brand/product from the brief. Search [Simple Icons](https://simpleicons.org/) or the [Iconify Simple Icons collection](https://icon-sets.iconify.design/simple-icons/). Read the actual slug; do not guess it from a display name. Iconify IDs use `simple-icons:<slug>`.
2. Check the entry's source and available brand guidelines against the brand's current identity. For complete app-icon shape, background or material, obtain the actual product icon separately. If a brand is absent or the result is stale, prefer the brand's own asset page and record the gap; do not substitute another company's mark.
3. Retrieve SVG from the verified entry. The official Simple Icons README documents the color CDN `https://cdn.simpleicons.org/<slug>` and versioned package assets `https://cdn.jsdelivr.net/npm/simple-icons@<exact-version>/icons/<slug>.svg`. Resolve a real available version before constructing a pinned URL. The color CDN is convenient but unversioned; retain the fetched file and its date/hash. Do not install a frontend framework or MCP server merely to retrieve SVG.
4. When a project already uses the `simple-icons` package, obtain the selected icon's `title`, `slug`, `hex`, `source`, `svg`/`path` and available `guidelines`/`license` fields. Missing fields stay unknown. Refer to the package's actual exports rather than fabricating an import name. Pin the package version when adding it is necessary for the requested implementation.
5. Confirm the response is SVG, not an HTML error or empty file. Inspect its paths/viewBox and reject scripts or external executable content before native import. Save the untouched original separately from any presentation copy.

## Integrate with Logo Atelier

- Put these assets in the existing Reference Section's supplemental `Logo / 形体参考` group. Use native frame/layer names and project provenance records. Count relevant ones as brand-mark/shape references within their intention, never as verified app-icon screenshots.
- Import actual SVG paths through the Figma workflow; keep aspect ratio and path geometry. Use a consistent comparison box, normally 64×64 when making a small standalone logo row, or match the existing board's dimensions. Optically balance occupancy without stretching.
- Preserve each research reference's original retrieved appearance. A separate monochrome study can expose silhouette and negative space when requested or useful, but identify it as a recolored study. Brand-color references must not be silently neutralized by the standalone skill's monochrome presentation default.
- Keep filled marks, outlines and wordmarks in coherent comparison groups without discarding a relevant reference just because it belongs to another group. Do not add shadows or gradients that misrepresent the source.
- For actual website logo rows, use the standalone `company-logos` guidance and accessible brand labels. A recognizable logo does not establish a customer relationship or endorsement; use the factual relationships supplied by the project.
- Extract curve, spacing, weight and negative-space principles. New client marks remain custom editable SVG geometry; do not recolor a library brand and present it as an original candidate. The upstream preference against custom embedded SVG applies to website brand sourcing, not Logo Atelier's original design work.

## Evidence and review

Store in the existing project `references.json` entry: asset kind (`brand_svg`), brand, slug/Iconify ID, retrieval URL, package version or retrieval date, brand source URL, available guideline/license links, original SVG path/hash, presentation changes, Figma node ID and actual visual-review status. Preserve the original and render/import proof. Count downloaded, imported and visually checked assets separately.

Check silhouette at the intended size, unclipped bounds, aspect ratio, fill visibility and accurate brand identification. Follow the normal reference-selection and master-review stages; this integration adds no new approval gate. Keep any known brand-specific usage limits with the asset record; the library license does not establish trademark clearance.

## Sources and maintenance

- [MengTo company-logos skill](https://github.com/MengTo/Skills/tree/5f47e389dac337a1bca5cddf376419248b3010f6/agent-skills/web-design/company-logos), MIT, installed 2026-09-21. Attribution retained in `company-logos-license.txt`.
- [Simple Icons usage and metadata](https://github.com/simple-icons/simple-icons#usage).
- [Simple Icons disclaimer](https://github.com/simple-icons/simple-icons/blob/develop/DISCLAIMER.md).

This reference is self-contained for shared Logo Atelier installations. Recheck upstream availability when fetching assets; no fixed catalog count or hardcoded brand slug list is assumed.
