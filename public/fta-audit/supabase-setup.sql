-- FTA audit digest — comments backend. Run ONCE in the Supabase SQL editor of the project you give us.
-- The page writes/reads with the anon (publishable) key; RLS below is the guard. No auth needed for Manthan.
create table if not exists public.fta_audit_comments (
  id         bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  page       text not null,                                   -- 'fta-audit-2026-08'
  anchor     text not null,                                   -- 'decision-1' … 'decision-13' or 'FTA-011'
  section    text,
  commenter  text not null check (char_length(commenter) between 1 and 120),
  choice     text,                                            -- the option picked (if any)
  body       text not null default '' check (char_length(body) <= 8000)
);
alter table public.fta_audit_comments enable row level security;
drop policy if exists "anon insert fta comments" on public.fta_audit_comments;
create policy "anon insert fta comments" on public.fta_audit_comments for insert to anon with check (true);
drop policy if exists "anon read fta comments" on public.fta_audit_comments;
create policy "anon read fta comments" on public.fta_audit_comments for select to anon using (true);
-- (optional) if you want reviewers NOT to see each other's answers, drop the read policy above; the page then shows only the reviewer's own device-saved answers.
