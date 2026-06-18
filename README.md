# Wall-Mounted Faucet Geometry Skill

Language: [English](README.md) | [中文](README.zh-CN.md)

Calculate the straight-line geometric relationship among a wall-mounted faucet outlet, basin rim, drain target point, and water stream angle.

![Wall-mounted faucet and basin geometry](assets/wall_mounted_faucet_geometry_v2.svg)

Files:

- `SKILL.md` — formulas, workflow, validation, and examples
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
