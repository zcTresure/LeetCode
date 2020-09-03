def addBinary(self, a: str, b: str) -> str:
    return '{0:b}'.format(int(a, 2) + int(b, 2))


# 位运算
def addBinary(self, a, b) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]
