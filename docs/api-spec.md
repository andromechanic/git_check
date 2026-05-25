# API Spec (MVP)

## Auth
- `POST /api/auth/sign-in`
- `POST /api/auth/sign-out`
- `GET /api/auth/session`

## Missions
- `GET /api/missions`
- `GET /api/missions/:id`
- `POST /api/admin/missions`
- `PATCH /api/admin/missions/:id`

## Simulation Sessions
- `POST /api/sessions` -> create session
- `GET /api/sessions/:id/state` -> current repo and mission state
- `POST /api/sessions/:id/command` -> run command

Command payload:
```json
{
  "command": "git checkout -b feature/navbar"
}
```

Response payload:
```json
{
  "ok": true,
  "output": "Switched to a new branch 'feature/navbar'",
  "repoState": {
    "head": "feature/navbar",
    "branches": ["main", "feature/navbar"],
    "commits": []
  },
  "xpDelta": 12,
  "missionProgress": 0.33
}
```

## Pull Requests
- `POST /api/sessions/:id/prs`
- `POST /api/sessions/:id/prs/:prId/review`
- `POST /api/sessions/:id/prs/:prId/merge`

## Profile & Gamification
- `GET /api/me/profile`
- `GET /api/me/achievements`
- `GET /api/me/progress`

## Admin
- `GET /api/admin/content`
- `POST /api/admin/scenarios`
- `POST /api/admin/badges`
