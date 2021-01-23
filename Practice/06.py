def to_camel_case(s):
    return s[0] + s.title().translate(str.maketrans('', '', '_- '))[1:] if s else s
    
    # text = text.split("_")
    # i = 0
    # cnt = 0
    # x = ""
    # for elem in text:
    #     s = elem
    #     if "-" in s:
    #         s = s.split("-")
    #         for el in s:
    #             if cnt == 0:
    #                 x += el
    #             else:
    #                 x += el.capitalize()
    #             cnt += 1
    #     else:
    #         if cnt == 0:
    #             x += s
    #         else:
    #             x += s.capitalize()
    #         cnt += 1
    #     i += 1
    #     print(x)
    #

to_camel_case("a_dog-cat_was_savage")


