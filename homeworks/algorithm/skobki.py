# проверяет правильность использования скобок в строке
def test_s(s):
    o = ""
    t = {"(":1,")":2,"[":3,"]":4,"{":5,"}":6}
    s = [i for i in s if i in "{}[]()"]
    for i in s:
        if i in "[{(":
            o += i
        else :
            if len(o) > 0 and t[i] - 1 == t[o[-1]]:
                o = o[:-1]
            else:
                return False
    return len(o) == 0

s = "a(({[]})({[]}))"
s2 = "(){}[]"
s3 = "({["
s4 = "!   )"
print(test_s(s))
print(test_s(s2))
print(test_s(s3))
print(test_s(s4))
