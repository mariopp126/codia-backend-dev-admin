# codia-backend-dev-admin
Administration system for codia-mobile-app. User/Report/Inpector managing and Dashboard &amp; Analitics for this app.

 ## Phase 1 (MVP — no DB changes needed):

  • User Management — 7 endpoints: list, detail, update, activate/deactivate, reset password, reset login
  attempts
  
  • Report Management — 5 endpoints: admin-scoped listing (all users), detail with full joins, force status
  update, delete, aggregated stats
  
  • Inspector Management — 6 endpoints: list inspectors, performance stats, manage inspections (assign,
  reassign, remove)
  
  • Dashboard & Analytics — 5 endpoints: system overview, reports over time, by category, by status, top
  inspectors leaderboard

  ## Phase 2 — New  billing  schema with plans, subscriptions, and payment history tables + 9 endpoints

  ## Phase 3 — Audit log, notifications, content moderation, bulk operations, exports
