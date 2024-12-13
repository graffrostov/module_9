
def all_variants(text):
    leght = len(text)
    for x in range(1, leght + 1):
        for y in range(leght):
            if y + x <= leght:
                yield text[y:y+x]


a = all_variants("abc")
for i in a:
    print(i)