class Convert:
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

    @staticmethod
    def convert(value: float, ratio: float) -> float:
        return value * ratio

    @staticmethod
    def px_to_pt(px: float) -> float:
        return Convert.convert(px, 0.75)

    @staticmethod
    def pt_to_px(pt: float) -> float:
        return Convert.convert(pt, 1 / 0.75)

    @staticmethod
    def px_to_in(px: float) -> float:
        return Convert.convert(px, 0.0138889)

    @staticmethod
    def in_to_px(inch: float) -> float:
        return Convert.convert(inch, 1 / 0.0138889)

    @staticmethod
    def px_to_cm(px: float) -> float:
        return Convert.convert(px, 0.0352778)

    @staticmethod
    def cm_to_px(cm: float) -> float:
        return Convert.convert(cm, 1 / 0.0352778)

    @staticmethod
    def px_to_mm(px: float) -> float:
        return Convert.convert(px, 0.352778)

    @staticmethod
    def mm_to_px(mm: float) -> float:
        return Convert.convert(mm, 1 / 0.352778)

    @staticmethod
    def px_to_pc(px: float) -> float:
        return Convert.convert(px, 0.05)

    @staticmethod
    def pc_to_px(pc: float) -> float:
        return Convert.convert(pc, 1 / 0.05)

    @staticmethod
    def px_to_em(px: float) -> float:
        return Convert.convert(px, 0.0625)

    @staticmethod
    def em_to_px(em: float) -> float:
        return Convert.convert(em, 1 / 0.0625)

    @staticmethod
    def px_to_rem(px: float) -> float:
        return Convert.convert(px, 0.0625)

    @staticmethod
    def rem_to_px(rem: float) -> float:
        return Convert.convert(rem, 1 / 0.0625)

    @staticmethod
    def px_to_percent(px: float, container_width: float) -> float:
        return (px / container_width) * 100

    @staticmethod
    def percent_to_px(percent: float, container_width: float) -> float:
        return (percent / 100) * container_width

    @staticmethod
    def cm_to_in(cm: float) -> float:
        return cm * 0.393701

    @staticmethod
    def in_to_cm(inch: float) -> float:
        return inch / 0.393701
