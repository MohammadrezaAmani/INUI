class Convert:
    @staticmethod
    def px_to_pt(px):
        return px * 0.75

    @staticmethod
    def pt_to_px(pt):
        return pt / 0.75

    @staticmethod
    def px_to_in(px):
        return px * 0.0138889

    @staticmethod
    def in_to_px(inch):
        return inch / 0.0138889

    @staticmethod
    def px_to_cm(px):
        return px * 0.0352778

    @staticmethod
    def cm_to_px(cm):
        return cm / 0.0352778

    @staticmethod
    def px_to_mm(px):
        return px * 0.352778

    @staticmethod
    def mm_to_px(mm):
        return mm / 0.352778

    @staticmethod
    def px_to_pc(px):
        return px * 0.05

    @staticmethod
    def pc_to_px(pc):
        return pc / 0.05

    @staticmethod
    def px_to_em(px):
        return px * 0.0625

    @staticmethod
    def em_to_px(em):

        return em / 0.0625

    @staticmethod
    def px_to_rem(px):
        return px * 0.0625

    @staticmethod
    def rem_to_px(rem):
        return rem / 0.0625
