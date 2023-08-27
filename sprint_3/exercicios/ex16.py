def string_parse(string):
    SUM = 0
    s = string.split(",")
    for i in range(len(s)):
        SUM = SUM + int(s[i])
    return SUM
    



string = "1,3,4,6,10,76"
res = string_parse(string)

print (res)