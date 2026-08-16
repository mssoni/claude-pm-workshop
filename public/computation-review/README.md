# Computation-screen review (Manthan workbook)

`index.html` + `img/` (real-stack screenshots) + `comments-config.js` + `supabase-setup.sql`. Static and self-contained (relative paths); publish the folder as-is (GitHub Pages), next to `fta-audit/`.

**What it is.** A top-to-bottom, code-faithful review of our built **Computation of Income** screen (`/staff/filings/:id/computation`), in the same grammar as the FTA-audit digest: fixed left index, one view at a time, a screen per cell / per decision, answer in place, progress bar.

**Layout (left index, mirrors the screen order):**
Start here → **The 30 cells** (Income & accounting base · Add-backs · Deductions & reliefs · Taxable income & tax · on-screen extras) → **Mapping proposal (28)** (14 unmapped lines · 6 collisions · PE/FPE divergence + Free-Zone sign map) → What's already correct → Full replica table → Glossary → Sources.

**Per cell — the three questions:** 1) Correct? 2) Where should it come from? 3) Read-only or editable? Plus a comment + name + Save. Each cell shows today's treatment, the logic in plain words, feeds in/out, any open question, the screenshot crop, and a muted `file:line` footnote (Manthan can ignore it; engineers can't).

**Mapping proposal:** the 28 auto-capture questions from `return-to-computation-mapping-table-2026-08-16.md`, grouped. Each is a keep-or-change decision with options + comment.

**Progress bar** counts answered cells + decisions (30 + 23 = 53 answerable units).

## Comments backend (Supabase) — its OWN table, separate from the FTA digest

The page uses the **same adapter, same column schema, and the same Supabase project/URL/key** as the FTA audit digest, but writes to its **own table `computation_review_comments`** with **page id `computation-review-2026-08`**, so the two review streams are fully independent and can never overwrite or mix.

- **Setup:** if this is a fresh project, run `supabase-setup.sql` once (it creates `computation_review_comments` with the same shape + RLS/insert policy as the FTA table). If the FTA digest is already wired to the same project, you still run this SQL once — it only adds the new table; **no second project or key is needed.**
- **Config:** `comments-config.js` = `{ url, key, table: 'computation_review_comments', page: 'computation-review-2026-08' }`. Same URL + anon/publishable key as the FTA digest; redeploy that one file to change it. Blank `url`/`key` to force local-only (device + "Export my answers") mode.
- **Save = INSERT (append).** Every Save posts a new row (page/anchor/section/commenter/choice/body); a re-answer never upserts or overwrites — the earlier answer is preserved and the thread shows every answer per anchor, newest last.
- **Anchors are stable ids:** cells are `cell:<code>` (e.g. `cell:C16`, `cell:deminimis`); decisions are `map:<id>` (e.g. `map:C-1`, `map:U-23`). Composite cell answers (the three questions) are packed into `body` (`Correct?: … / Should come from: … / Mode: … / Comment: …`) with the "Correct?" pick mirrored into `choice`.
- **Ingestion = one REST query on this page's own table:**
  `GET <url>/rest/v1/computation_review_comments?page=eq.computation-review-2026-08&order=created_at` (with the anon key). This is a **different table** from the FTA digest's — the FTA answers stay in their own table, these stay here.
- **Offline fallback** (identical to the FTA digest): answers are queued in `localStorage` and auto-sync on the next load; "Export my answers" downloads + copies a Markdown file.

## Regenerate

`python3 tools/build_computation_review.py` — cell + decision texts live in `tools/computation_context.py`; the builder references screenshots directly as PNG (sharper on flat UI) and includes only files that exist.
