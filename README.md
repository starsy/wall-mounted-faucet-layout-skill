# Wall-Mounted Faucet Geometry Skill

Language: [English](README.md) | [中文](README.zh-CN.md)

Calculate the straight-line geometric relationship among a wall-mounted faucet outlet, basin rim, drain target point, and water stream angle.

![Wall-mounted faucet and basin geometry](assets/wall_mounted_faucet_geometry_v2.svg)

## Installation

This repository is a filesystem skill package. The install folder should be named `wall-mounted-faucet-layout`, because that is the skill name in `SKILL.md`.

### Codex / OpenAI-style skills

Install as a user skill:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.codex/skills/wall-mounted-faucet-layout
```

### Claude / Claude Code

For Claude surfaces that support local skill folders:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.claude/skills/wall-mounted-faucet-layout
```

For Claude surfaces that import skills as archives, clone the repo, zip the `wall-mounted-faucet-layout` folder, and import that ZIP in the Skills UI.

### OpenClaw

Install globally for OpenClaw agents:

```bash
mkdir -p ~/.openclaw/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git ~/.openclaw/skills/wall-mounted-faucet-layout
```

For workspace-scoped OpenClaw installs, clone the same folder into that workspace's skills directory if your OpenClaw setup uses one.

### Cursor and other rule/context-based agents

If the agent does not auto-discover `SKILL.md` packages, clone this repo into a stable project path and point the agent's rule/context system at `SKILL.md`.

```bash
mkdir -p vendor/skills
git clone https://github.com/starsy/wall-mounted-faucet-layout-skill.git vendor/skills/wall-mounted-faucet-layout
```

For Cursor, add a project rule such as `.cursor/rules/wall-mounted-faucet-layout.mdc`:

```md
---
description: Use wall-mounted faucet geometry calculations
alwaysApply: false
---

When asked about wall-mounted faucet installation geometry, read and follow
`vendor/skills/wall-mounted-faucet-layout/SKILL.md`. Prefer the deterministic
calculator at `vendor/skills/wall-mounted-faucet-layout/scripts/faucet_geometry.py`.
```

Use it from an agent prompt:

```text
Use $wall-mounted-faucet-layout to calculate the faucet layout with K=5 cm, W=40 cm, H2=14 cm, L=20.5 cm, and theta=10 degrees.
```

Files:

- `SKILL.md` — formulas, workflow, validation, and examples
- `agents/openai.yaml` — optional UI metadata for agents that support it
- `scripts/faucet_geometry.py` — deterministic calculator
- `assets/wall_mounted_faucet_geometry_v2.svg` — scalable diagram for GitHub
- `assets/wall_mounted_faucet_geometry_v2.png` — raster fallback of the same diagram

Core relationship:

```text
tan(theta) = (K + WS - L) / (H1 + H2)
```

Use the SVG in rendered documentation because it stays crisp when zoomed and keeps the parameter labels readable.

Example:

```bash
python scripts/faucet_geometry.py \
  --solve WS \
  --K 5 \
  --H1 15 \
  --H2 14 \
  --L 20.5 \
  --theta 10 \
  --W 40 \
  --unit cm
```

Expected result:

```text
WS = 20.613482 cm
horizontal_offset = 5.113482 cm
vertical_drop = 29.000000 cm
reverse_theta = 10.000000 degrees
drain_center_offset = 0.613482 cm
```

This calculator is a geometric estimate. Confirm the final installation with an on-site mock-up or water-flow test before closing the wall.
