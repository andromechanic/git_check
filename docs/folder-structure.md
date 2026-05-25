# Recommended Folder Structure

```txt
.
├─ apps/
│  ├─ web/                        # Next.js frontend
│  │  ├─ app/
│  │  │  ├─ (marketing)/
│  │  │  ├─ dashboard/
│  │  │  ├─ missions/[missionId]/
│  │  │  ├─ pr-workspace/
│  │  │  ├─ profile/
│  │  │  └─ admin/
│  │  ├─ components/
│  │  │  ├─ terminal/
│  │  │  ├─ git-graph/
│  │  │  ├─ pr/
│  │  │  ├─ missions/
│  │  │  └─ ui/
│  │  ├─ stores/
│  │  ├─ lib/
│  │  └─ styles/
│  └─ api/                        # Node backend
│     ├─ src/
│     │  ├─ modules/
│     │  │  ├─ auth/
│     │  │  ├─ missions/
│     │  │  ├─ simulation/
│     │  │  ├─ pull-requests/
│     │  │  ├─ gamification/
│     │  │  └─ achievements/
│     │  ├─ prisma/
│     │  └─ main.ts
├─ packages/
│  ├─ simulation-engine/
│  ├─ ui-kit/
│  └─ shared-types/
├─ prisma/
│  ├─ schema.prisma
│  └─ seed.sql
├─ docs/
└─ docker-compose.yml
```
