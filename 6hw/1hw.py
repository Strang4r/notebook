from time import sleep
from itertools import cycle


class TLight:
    __colors = {"Red": 7, 'Orange': 3, 'Green': 5}

    def Running(self, r_cnt):
        c_iter = cycle(self.__colors)
        while r_cnt:
            c_l_val = next(c_iter)
            print(f"currnet light is {c_l_val} "
                  f'{TLight.__colors[c_l_val]} sec. ')
            sleep(self.__colors[c_l_val])
            r_cnt -= 1

    def get_color(self, password):
        if password == "Secret password":
            return self.__colors
        else:
            ValueError("Authorization error")


TLight = TLight()
TLight.Running(7)
print(TLight.get_color("Secret password"))
