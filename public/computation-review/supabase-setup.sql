-- Computation-screen review — comments backend (SEPARATE table from the FTA audit digest).
-- Run ONCE in the Supabase SQL editor of the project you give us. Same shape/RLS as the FTA table,
-- but its OWN table so the two review streams stay independent and answers can never mix.
-- The page writes/reads with the anon (publishable) key; RLS below is the guard. No auth needed.
-- Save is INSERT-only (a re-answer appends a new row; earlier answers are never overwritten).
create table if not exists public.computation_review_comments (
  id         bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  page       text not null,                                   -- 'computation-review-2026-08'
  anchor     text not null,                                   -- 'cell:C16', 'cell:deminimis', 'map:C-1', 'map:U-23' …
  section    text,                                            -- the band or mapping group (context only)
  commenter  text not null check (char_length(commenter) between 1 and 120),
  choice     text,                                            -- the option picked (if any)
  body       text not null default '' check (char_length(body) <= 8000)
);
alter table public.computation_review_comments enable row level security;
drop policy if exists "anon insert computation review" on public.computation_review_comments;
create policy "anon insert computation review" on public.computation_review_comments for insert to anon with check (true);
drop policy if exists "anon read computation review" on public.computation_review_comments;
create policy "anon read computation review" on public.computation_review_comments for select to anon using (true);
-- (optional) drop the read policy above if reviewers should NOT see each other's answers; the page
-- then shows only the reviewer's own device-saved answers.
