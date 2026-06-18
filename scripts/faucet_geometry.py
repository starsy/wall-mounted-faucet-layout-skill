#!/usr/bin/env python3
import argparse
import math

REQUIRED_INPUTS = {
    "H1": ("K", "WS", "L", "theta", "H2"),
    "L": ("K", "WS", "H1", "H2", "theta"),
    "WS": ("K", "L", "H1", "H2", "theta"),
    "theta": ("K", "WS", "L", "H1", "H2"),
    "K": ("L", "WS", "H1", "H2", "theta"),
    "H2": ("K", "WS", "L", "theta", "H1"),
}

def td(x):
    return math.tan(math.radians(x))

def validate_inputs(parser, a):
    if a.W is not None and a.W <= 0:
        parser.error("--W must be greater than 0")

    if a.WS is None and a.W is not None and a.solve != "WS":
        a.WS = a.W / 2

    for name in REQUIRED_INPUTS[a.solve]:
        if getattr(a, name) is None:
            if name == "WS":
                parser.error(f"--WS is required when --solve {a.solve}, or provide --W to assume a centered drain")
            parser.error(f"--{name} is required when --solve {a.solve}")

    if a.solve != "theta" and not (0 < a.theta < 90):
        parser.error("--theta must be greater than 0 and less than 90 degrees for forward flow")

    if a.W is not None and a.WS is not None and a.solve != "WS" and not (0 < a.WS < a.W):
        parser.error("--WS must be greater than 0 and less than --W")

    if a.solve == "theta" and a.H1 + a.H2 <= 0:
        parser.error("H1 + H2 must be greater than 0 when solving theta")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--solve", required=True, choices=["H1","L","WS","theta","K","H2"])
    for name in ["K","W","WS","H1","H2","L","theta"]:
        p.add_argument(f"--{name}", type=float)
    p.add_argument("--unit", default="cm")
    a = p.parse_args()

    validate_inputs(p, a)

    target = a.solve
    if target == "H1":
        result = (a.K + a.WS - a.L) / td(a.theta) - a.H2
    elif target == "L":
        result = a.K + a.WS - (a.H1 + a.H2) * td(a.theta)
    elif target == "WS":
        result = a.L - a.K + (a.H1 + a.H2) * td(a.theta)
    elif target == "theta":
        result = math.degrees(math.atan2(a.K + a.WS - a.L, a.H1 + a.H2))
    elif target == "K":
        result = a.L - a.WS + (a.H1 + a.H2) * td(a.theta)
    else:
        result = (a.K + a.WS - a.L) / td(a.theta) - a.H1

    setattr(a, target, result)
    suffix = "degrees" if target == "theta" else a.unit
    print(f"{target} = {result:.6f} {suffix}")

    horizontal_offset = None
    vertical_drop = None
    if a.K is not None and a.WS is not None and a.L is not None:
        horizontal_offset = a.K + a.WS - a.L
        print(f"horizontal_offset = {horizontal_offset:.6f} {a.unit}")
    if a.H1 is not None and a.H2 is not None:
        vertical_drop = a.H1 + a.H2
        print(f"vertical_drop = {vertical_drop:.6f} {a.unit}")
    if horizontal_offset is not None and vertical_drop is not None and vertical_drop != 0:
        reverse_theta = math.degrees(math.atan2(horizontal_offset, vertical_drop))
        print(f"reverse_theta = {reverse_theta:.6f} degrees")
    if a.W is not None and a.WS is not None:
        print(f"drain_center_offset = {a.WS - a.W/2:.6f} {a.unit}")

    warnings = []
    if a.H1 is not None and a.H1 < 0:
        warnings.append("H1 is negative; check reference levels or geometry")
    if horizontal_offset is not None and horizontal_offset < 0:
        warnings.append("horizontal offset is negative; the target lies behind the outlet")
    if vertical_drop is not None and vertical_drop <= 0:
        warnings.append("vertical drop is not positive; check H1 and H2")
    if a.W is not None and a.WS is not None and not (0 < a.WS < a.W):
        warnings.append("WS is outside the basin width W")
    for warning in warnings:
        print(f"warning: {warning}")

if __name__ == "__main__":
    main()
