INSERT INTO "Achievement" (id, code, name, description)
VALUES
  ('ach_1', 'MERGE_CONFLICT_SURVIVOR', 'Merge Conflict Survivor', 'Resolved your first simulated merge conflict.'),
  ('ach_2', 'REBASE_MASTER', 'Rebase Master', 'Successfully rebased branches under pressure.'),
  ('ach_3', 'FIRST_OS_CONTRIBUTOR', 'First Open Source Contributor', 'Opened and merged first contribution PR.'),
  ('ach_4', 'GIT_WIZARD', 'Git Wizard', 'Completed all core Git path missions.');

INSERT INTO "Mission" (id, title, slug, "storyIntro", objective, difficulty, "orderIndex")
VALUES
  ('mis_1', 'Portfolio Launch', 'portfolio-launch', 'You joined startup WeGuide and must bootstrap your first repo.', 'Initialize and push first commit.', 'BEGINNER', 1),
  ('mis_2', 'Feature Branch Sprint', 'feature-branch-sprint', 'Team is building navigation revamp for demo day.', 'Create branch, commit feature, open PR.', 'INTERMEDIATE', 2),
  ('mis_3', 'Conflict Survivor', 'conflict-survivor', 'Two teammates touched same file before release.', 'Resolve merge conflict safely.', 'INTERMEDIATE', 3),
  ('mis_4', 'Production Hotfix', 'production-hotfix', 'Login crash reported by customers.', 'Ship hotfix branch via PR and merge.', 'ADVANCED', 4),
  ('mis_5', 'Recovery Drill', 'recovery-drill', 'Detached HEAD caused lost work panic.', 'Recover with checkout and cherry-pick.', 'ADVANCED', 5);
