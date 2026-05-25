# Production Architecture

## High-Level
- Web App (Next.js): UI, simulation workspace, mission player, profile/achievements, admin mission builder
- API Service (Node.js): auth session validation, mission engine, PR simulation, AI teammate events, scoring
- Postgres: users, missions, scenarios, commands, progress, PR events, achievements
- Redis (optional): low-latency session state for live simulations

## Core Services
- `SimulationEngine`: repository state machine and command execution
- `ValidationEngine`: checks exercise outcomes against expected repo graph state
- `NarrativeEngine`: teammate comments, deadlines, sprint events
- `GamificationEngine`: XP, levels, badges, streak logic
- `PRWorkflowEngine`: open/review/change request/merge states

## Frontend Modules
- Mission Timeline
- Interactive Terminal (`xterm.js`)
- Git Graph Panel (DAG rendering + animations)
- PR Workspace (diff, reviewer comments, status checks)
- Teammate Feed
- Hint/Recovery Assistant

## Backend Modules
- Auth
- Mission CRUD (admin)
- Simulation Sessions
- Command Runner
- Progress & Analytics
- Badge Rules

## Deployment
- Frontend on Vercel
- Backend on Railway/Render/AWS ECS
- Managed Postgres
- Object storage for mission assets

## Scaling Notes
- Session data event-sourced (`simulation_events`)
- Deterministic command replay for auditing and certification mode
- Multiplayer ready by introducing team session channels + WebSocket gateway
