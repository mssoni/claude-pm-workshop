// Live comments backend (Supabase) for the Computation-screen review page.
// SEPARATE table from the FTA audit digest so the two review streams never mix or overwrite.
// Same project/URL/key as the FTA digest; only the table + page id differ. Fill/replace and redeploy
// this one file — no rebuild needed. Blank the url/key to force local-only (device + Export) mode.
window.CR_COMMENTS = {
  url: 'https://fwbgaljxxgkqirvvxcas.supabase.co',
  key: 'sb_publishable_luKF9U88g2yokEreoqeFBQ_eXPue6SZ',
  table: 'computation_review_comments',
  page: 'computation-review-2026-08'
};
