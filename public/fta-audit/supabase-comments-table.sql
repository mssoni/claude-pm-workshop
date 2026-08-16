-- ============================================================================
-- prototype_comments — Nexdigm review comments on the CT prototype
-- Run ONCE in the Supabase SQL editor (project fwbgaljxxgkqirvvxcas).
-- Separate table from brd_comments / safe-neighbors — this is prototype-only.
-- The prototype writes with the PUBLISHABLE (anon) key; RLS below is the guard.
-- ============================================================================

create table if not exists public.prototype_comments (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  route      text not null,                       -- hash route, e.g. '#/dashboard'
  screen     text,                                -- friendly screen name
  section    text,                                -- optional section/element label
  commenter  text not null,                       -- reviewer name (self-entered)
  body       text not null check (char_length(body) between 1 and 4000),
  status     text not null default 'open',        -- 'open' | 'resolved'
  resolved   boolean not null default false
);

alter table public.prototype_comments enable row level security;

-- anon (publishable key) may INSERT a comment...
drop policy if exists "anon insert prototype comments" on public.prototype_comments;
create policy "anon insert prototype comments"
  on public.prototype_comments for insert to anon with check (
    char_length(commenter) between 1 and 120 and char_length(body) between 1 and 4000
  );

-- ...and SELECT comments (so reviewers see the thread on-screen).
-- If you'd rather reviewers NOT see each other's comments, delete this policy
-- (they'll still be able to post; we read them via harvest with the same key).
drop policy if exists "anon read prototype comments" on public.prototype_comments;
create policy "anon read prototype comments"
  on public.prototype_comments for select to anon using (true);

-- NOTE: anon cannot UPDATE/DELETE (no policy) — resolving a comment is done by us
-- (service side / dashboard), so reviewers can't tamper with the thread.

-- ⚠ FOLLOW-UP MIGRATION (2026-07-03): element-anchored comments add 5 columns —
-- run comments/prototype_comments_migration_element-anchors.sql after this file.
