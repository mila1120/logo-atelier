# Model interface v1

`config/models.json` defines roles independently of workflow:

| Role | Default route | Responsibility |
|---|---|---|
| svg | host / current-agent | reasoning and editable SVG geometry |
| explore | Gemini / gemini-3.1-flash-image | raster concepts and material experiments |
| presentation | Gemini / gemini-3-pro-image | raster presentation studies |

Model IDs are configurable defaults, not a ranking or availability guarantee. Verify them against the provider's current model documentation when live requests fail. `host` records a handoff to the current agent; changing its model string does not change the Codex session model. The Gemini image adapter cannot produce genuine SVG. It can supply raster reference for subsequent deliberate vector reconstruction.

The built-in Gemini adapter uses generateContent, inline PNG/JPEG/WebP references (maximum four; 10 MB each by default), aspect ratio and text/image response modalities. No external Python packages. Set GEMINI_API_KEY in the process environment or use the `api_key_env` configuration field. Never paste keys into prompts, manifests, Figma or versioned files. The Codex process must inherit the environment; exporting in a different terminal may not affect it.

Generate is dry-run by default. `--execute` sends the supplied prompt and selected references to Google and can incur charges. Only send assets within the user's authorized task. `--count` caps requests at the configured budget, not output images guaranteed by provider. Requests are not automatically retried: timeout outcomes may be unknown and retrying can duplicate charges. Partial outputs and run metadata are preserved.

Run directories store prompt, model, role, reference hashes, output hashes, settings and status. No keys or base64 inputs are persisted. An output is generated_unreviewed until examined. Missing credentials fail before sending a request. Doctor only checks configuration, not live availability. Adapter tests use mock responses; they do not establish real service connectivity.

To add a provider, implement request/response conversion behind the same interface; validate supported output type; add missing-key, dry-run, malformed response, partial failure and no-secret regression tests. Do not hide provider-specific failures behind silent fallback.

Official source: https://ai.google.dev/gemini-api/docs/generate-content/image-generation (checked 2026-09-20). Model choices should be rechecked at execution time.

REST contract follows the current documented v1 generateContent endpoint and generationConfig.responseFormat.image. Provider labels this API legacy; live compatibility is still pending until credentials are configured.
