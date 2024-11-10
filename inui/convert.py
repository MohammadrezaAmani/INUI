"""
A utility class for handling various unit conversions.

Conversion Ratios:
- px: pixels
- pt: points
- in: inches
- cm: centimeters
- mm: millimeters
- pc: picas
- em: em units
- rem: root em units

Additional Methods:
- px_to_percent: Convert pixels to percentage based on a container width.
- percent_to_px: Convert percentage to pixels based on a container width.
- cm_to_in: Convert centimeters to inches.
- in_to_cm: Convert inches to centimeters.
"""


def convert(value: float, ratio: float) -> float:
    return value * ratio


def px_to_pt(px: float) -> float:
    return convert(px, 0.75)


def pt_to_px(pt: float) -> float:
    return convert(pt, 1 / 0.75)


def px_to_in(px: float) -> float:
    return convert(px, 0.0138889)


def in_to_px(inch: float) -> float:
    return convert(inch, 1 / 0.0138889)


def px_to_cm(px: float) -> float:
    return convert(px, 0.0352778)


def cm_to_px(cm: float) -> float:
    return convert(cm, 1 / 0.0352778)


def px_to_mm(px: float) -> float:
    return convert(px, 0.352778)


def mm_to_px(mm: float) -> float:
    return convert(mm, 1 / 0.352778)


def px_to_pc(px: float) -> float:
    return convert(px, 0.05)


def pc_to_px(pc: float) -> float:
    return convert(pc, 1 / 0.05)


def px_to_em(px: float) -> float:
    return convert(px, 0.0625)


def em_to_px(em: float) -> float:
    return convert(em, 1 / 0.0625)


def px_to_rem(px: float) -> float:
    return convert(px, 0.0625)


def rem_to_px(rem: float) -> float:
    return convert(rem, 1 / 0.0625)


def px_to_percent(px: float, container_width: float) -> float:
    return (px / container_width) * 100


def percent_to_px(percent: float, container_width: float) -> float:
    return (percent / 100) * container_width


def cm_to_in(cm: float) -> float:
    return cm * 0.393701


def in_to_cm(inch: float) -> float:
    return inch / 0.393701
