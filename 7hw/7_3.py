class Cells:
    def __init__(self,C_num):
        self.C_num=C_num
    def __add__(self, other):
        return self.C_num+ other.C_num

    def __sub__(self, other):
        if (self.C_num - other.C_num) >0:
            return self.C_num - other.C_num
        else: ValueError("Разность не может быть меньше нуля")
    def __mul__(self, other):
        return self.C_num * other.C_num
