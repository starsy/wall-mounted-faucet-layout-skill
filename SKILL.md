---
name: wall-mounted-faucet-layout
description: Calculate and validate wall-mounted faucet installation geometry. Use when an agent needs to solve or check faucet reach, outlet height, basin depth, stream angle, wall setback, or drain position from K, W/WS, L, H1, H2, and theta.
---

# Wall-Mounted Faucet Layout

## Purpose

Use this skill to calculate or validate the installation geometry of a wall-mounted faucet and basin.

It can solve for:

- `H1`: vertical distance from the basin rim to the faucet outlet
- `L`: horizontal reach of the faucet outlet from the finished wall
- `WS`: horizontal distance from the rear inner basin wall to the drain center
- `theta`: water-flow angle measured from the vertical
- `K`: horizontal distance from the finished wall to the rear inner basin wall
- `H2`: vertical depth from the basin rim reference line to the target point at the drain

It can also use `W`, the front-to-back inner basin width, to assume a centered drain when `WS` is not supplied.

## Coordinate convention

All linear measurements must use the same unit.

- Horizontal distance increases from the wall toward the front of the basin.
- Vertical distance increases downward from the faucet outlet toward the drain.
- `theta` is measured from the vertical direction.
- A positive `theta` means the water points forward, away from the wall.

| Symbol | Meaning |
|---|---|
| `K` | Finished wall to rear inner basin wall |
| `W` | Front-to-back inner width of the basin |
| `WS` | Rear inner basin wall to drain center |
| `L` | Finished wall to faucet outlet |
| `H1` | Basin rim to faucet outlet, vertically upward |
| `H2` | Basin rim to drain target point, vertically downward |
| `theta` | Water angle from vertical, in degrees |

If the drain is centered:

\[
WS = \frac{W}{2}
\]

## Core geometry

Horizontal offset:

\[
\Delta x = K + WS - L
\]

Vertical drop:

\[
\Delta y = H1 + H2
\]

Core relationship:

\[
\tan(\theta)=\frac{K+WS-L}{H1+H2}
\]

This models the water path as a straight centerline. Real water flow curves under gravity and varies with pressure, aerator design, and flow rate.

## Solving formulas

### Solve for `H1`

\[
H1=\frac{K+WS-L}{\tan(\theta)}-H2
\]

### Solve for `L`

\[
L=K+WS-(H1+H2)\tan(\theta)
\]

### Solve for `WS`

\[
WS=L-K+(H1+H2)\tan(\theta)
\]

### Solve for `theta`

\[
\theta=\arctan\left(\frac{K+WS-L}{H1+H2}\right)
\]

Convert the result to degrees.

### Solve for `K`

\[
K=L-WS+(H1+H2)\tan(\theta)
\]

### Solve for `H2`

\[
H2=\frac{K+WS-L}{\tan(\theta)}-H1
\]

## Required calculation procedure

1. Identify the target variable.
2. Normalize all lengths to one unit.
3. Confirm that `theta` is measured from the vertical.
4. Resolve the drain location:
   - Use supplied `WS`; or
   - If `WS` is absent and `W` is supplied, set `WS = W / 2`.
5. Select the target formula.
6. Convert degrees to radians before calling a trigonometric function.
7. Calculate with a calculator or script.
8. Report the formula, substitution, exact result, and practical rounded result.
9. Run the validation checks.
10. Recommend an on-site water test before concealed installation.

## Validation checks

- Require all inputs needed by the selected formula.
- Require one consistent length unit.
- Normally require `0° < theta < 90°` for forward flow.
- If `W` is known, require `0 < WS < W`.
- If `H1 < 0`, the geometry or reference lines are incompatible.
- If `K + WS - L < 0`, the target point lies behind the outlet under this coordinate convention.

Reverse-check the result by substituting it into:

\[
\tan(\theta)=\frac{K+WS-L}{H1+H2}
\]

If `W` is known, report the drain offset from basin center:

\[
\text{center offset}=WS-\frac{W}{2}
\]

- Positive: forward of center
- Negative: rearward of center
- Zero: centered

## Sensitivity

For fixed `K`, `WS`, `H2`, and `theta`:

\[
\frac{\partial H1}{\partial L}=-\frac{1}{\tan(\theta)}
\]

At `theta = 10°`:

\[
\frac{1}{\tan(10^\circ)}\approx5.67
\]

So increasing `L` by 1 cm lowers theoretical `H1` by about 5.67 cm.

## Response template

```text
Known:
K = ...
WS = ...  (or W = ... and WS = W/2)
H1 = ...
H2 = ...
L = ...
theta = ... degrees

Formula:
[target formula]

Substitution:
[...]

Result:
[target] = ... [unit]

Validation:
- Horizontal offset Δx = ...
- Vertical drop Δy = ...
- Reverse check = ...
- Drain offset from basin center = ... (when W is known)

Practical note:
This is a straight-line geometric estimate. Confirm with a full-scale mock-up or water-flow test.
```

## Worked examples

### Example 1: centered drain, solve for `H1`

Given `K=5 cm`, `W=40 cm`, `H2=14 cm`, `L=20.5 cm`, `theta=10°`:

\[
WS=20
\]

\[
H1=\frac{5+20-20.5}{\tan(10^\circ)}-14\approx11.52\text{ cm}
\]

### Example 2: short reach, solve for `H1`

Given `K=5 cm`, `WS=20 cm`, `H2=14 cm`, `L=16 cm`, `theta=10°`:

\[
H1=\frac{5+20-16}{\tan(10^\circ)}-14\approx37.04\text{ cm}
\]

The large result is expected because a 10-degree stream is close to vertical.

### Example 3: solve for `WS`

Given `K=5 cm`, `H1=15 cm`, `H2=14 cm`, `L=20.5 cm`, `theta=10°`:

\[
WS=20.5-5+(15+14)\tan(10^\circ)\approx20.61\text{ cm}
\]

For `W=40 cm`, the drain is approximately `0.61 cm` forward of center.

## Agent implementation note

Prefer deterministic calculation with the included script. Do not estimate trigonometric values mentally when exact dimensions matter.

Reference calculator:

```text
scripts/faucet_geometry.py
```
