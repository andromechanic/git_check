# GitSim Academy

GitSim Academy is an interactive GitHub Learning Simulator that teaches Git workflows through project-based missions and team collaboration simulations.

## MVP Included in This Repo
- Interactive terminal with command parsing (`git init`, `git add`, `git commit`, `git push`, `git checkout`, `git merge`, `git rebase`, `git cherry-pick`)
- Mission engine with 5 scenarios (beginner, intermediate, advanced)
- AI teammate simulation feed (PM, frontend, backend personas)
- Pull request simulation (`open-pr`, `merge-pr`, review state)
- Live commit graph visualization
- Gamification (XP, levels, streak placeholder, badges)
- Hint and solution assistance mode

## Architecture (Target Production)
- Frontend: Next.js + React + TypeScript + Tailwind + Framer Motion + xterm.js + Monaco + Zustand
- Backend: Node.js (Fastify/Nest) + Prisma + PostgreSQL
- Auth: Clerk or NextAuth
- Deploy: Vercel (frontend), Railway/Render/AWS (backend)

See:
- `docs/architecture.md`
- `docs/folder-structure.md`
- `docs/api-spec.md`
- `prisma/schema.prisma`
- `prisma/seed.sql`

## Run Local Prototype
1. Open `index.html` in browser.
2. Start mission 1 by typing `git init` in terminal.

## Suggested Next Build Step
Convert this prototype into full Next.js app using the provided architecture docs and schema.
