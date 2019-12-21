import math
def Right(data):
    data = str(data)
    data = data[-1:]
    return int(data)

def jxM1(red, blue):
    result = round(sum(red) / 17)
    return Right(result)


def jxM2(red, blue):
    result = round(sum(red) / 18)
    return Right(result)


def jxM3(red, blue):
    result = round(sum(red) / 22)
    return Right(result)


def jxM4(red, blue):
    result = round(sum(red) / 23)
    return Right(result)


def jxM5(red, blue):
    result = int((sum(red) / 100) % 10) + int((sum(red) / 10) % 10) + int((sum(red) % 10))
    return Right(result)


def jxM6(red, blue):
    return Right(abs(red[3] - 12))


def jxM7(red, blue):
    if int((sum(red) - red[0]) / red[0]) > 105:
        result = int((sum(red) - red[0]) / red[0]) - 105
    elif int((sum(red) - red[0]) / red[0]) > 70:
        result = int((sum(red) - red[0]) / red[0]) - 70
    elif int((sum(red) - red[0]) / red[0]) > 35:
        result = int((sum(red) - red[0]) / red[0]) - 35
    else:
        result = int((sum(red) - red[0]) / red[0])
    return Right(result)


def jxM8(red, blue):
    if int((sum(red) - red[1]) / red[1]) > 35:
        result = int((sum(red) - red[1]) / red[1]) - 35
    else:
        result = int((sum(red) - red[1]) / red[1])
    return Right(result)


def jxM9(red, blue):
    return Right(int((sum(red) - red[2]) / red[2]))


def jxM10(red, blue):
    return Right(int((sum(red) - red[3]) / red[3]))


def jxM11(red, blue):
    return Right(int((sum(red) - red[4]) / red[4]))


def jxM12(red, blue):
    return Right(int((sum(red) - (sum(blue)) /sum(blue))))


def jxM13(red, blue):
    return Right((sum(red) - red[0]) % red[0])


def jxM14(red, blue):
    return Right((sum(red) - red[1]) % red[1])


def jxM15(red, blue):
    return Right((sum(red) - red[2]) % red[2])


def jxM16(red, blue):
    return Right((sum(red) - red[3]) % red[3])


def jxM17(red, blue):
    return Right((sum(red) - red[4]) % red[4])


def jxM18(red, blue):
    return Right((sum(red) - blue[0]) % blue[0])


def jxM19(red, blue):
    return Right(int(math.pow(red[0] * red[1], 1 / 2)))


def jxM20(red, blue):
    return Right(int(math.pow(red[1] * red[2], 1 / 2)))


def jxM21(red, blue):
    return Right(int(math.pow(red[2] * red[3], 1 / 2)))


def jxM22(red, blue):
    return Right(int(math.pow(red[3] * red[4], 1 / 2)))


def jxM23(red, blue):
    return Right(int(math.pow(red[4] * blue[0], 1 / 2)))


def jxM24(red, blue):
    return Right(int(math.pow(red[0] * blue[0], 1 / 2)))


def jxM25(red, blue):
    return Right(int(math.pow(red[0] * red[2], 1 / 2)))


def jxM26(red, blue):
    return Right(int(math.pow(red[0] * red[3], 1 / 2)))


def jxM27(red, blue):
    return Right(int(math.pow(red[0] * red[4], 1 / 2)))


def jxM28(red, blue):
    return Right(int(math.pow(red[1] * red[3], 1 / 2)))


def jxM29(red, blue):
    return Right(int(math.pow(red[1] * red[4], 1 / 2)))


def jxM30(red, blue):
    return Right(int(math.pow(red[1] * blue[0], 1 / 2)))


def jxM31(red, blue):
    return Right(int(math.pow(red[2] * red[4], 1 / 2)))


def jxM32(red, blue):
    return Right(int(math.pow(red[2] * blue[0], 1 / 2)))


def jxM33(red, blue):
    return Right(int(math.pow(red[3] * blue[0], 1 / 2)))


def jxM34(red, blue):
    if blue[0] + sum(blue) <= 35:
        result = blue[0] + sum(blue)
    else:
        result = blue[0] + sum(blue) - 35
    return Right(result)


def jxM35(red, blue):
    return Right(round((red[1] + red[2] + red[3] + red[4] + (sum(blue)) / 6)))


def jxM36(red, blue):
    return Right(red[1] + sum(blue))


def jxM37(red, blue):
    return Right(blue[0] - red[1] + 1)


def jxM38(red, blue):
    if red[1] + blue[0] + 1 <= 35:
        return Right(red[1] + blue[0] + 1)
    else:
        return Right(red[1] + blue[0] + 1 - 35)


def jxM39(red, blue):
    if blue[0] - red[1] + 10 <= 35:
        return Right(blue[0] - red[1] + 10)
    else:
        return Right(blue[0] - red[1] + 10 - 35)


def jxM40(red, blue):
    return Right(red[0] + red[1])


def jxM41(red, blue):
    if red[3] + red[0] > 35:
        return Right(red[3] + red[0] - 35)
    else:
        return Right(red[3] + red[0])


def jxM42(red, blue):
    return Right(red[3] - red[0] + 7)


def jxM43(red, blue):
    return Right(int(sum(red[2:6]) / 4))


def jxM44(red, blue):
    return Right(int(sum(red[:3]) / 3))


def jxM45(red, blue):
    if red[1] + red[2] <= 35:
        return Right(red[1] + red[2])
    else:
        return Right(red[1] + red[2] - 35)


def jxM46(red, blue):
    return Right(abs(red[4] - red[3] + 10))


def jxM47(red, blue):
    return Right(red[0] + 12)


def jxM48(red, blue):
    return Right(red[1] - red[0])


def jxM49(red, blue):
    return Right(red[2] - red[0])


def jxM50(red, blue):
    return Right(red[3] - red[0])


def jxM51(red, blue):
    return Right(red[4] - red[0])


def jxM52(red, blue):
    return Right(blue[0] - red[0])


def jxM53(red, blue):
    return Right(red[2] - red[1])


def jxM54(red, blue):
    return Right(red[3] - red[1])


def jxM55(red, blue):
    return Right(red[4] - red[1])


def jxM56(red, blue):
    return Right(blue[0] - red[1])


def jxM57(red, blue):
    return Right(red[3] - red[2])


def jxM58(red, blue):
    return Right(red[4] - red[2])


def jxM59(red, blue):
    return Right(blue[0] - red[2])


def jxM60(red, blue):
    return Right((blue[1] - blue[0]))


def jxM61(red, blue):
    if int(math.pow((red[2] * red[3] * red[4]), 1 / 2)) <= 35:
        return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 2)))
    else:
        return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 4)))


def jxM62(red, blue):
    return Right(red[4] - red[3])


def jxM63(red, blue):
    return Right(blue[0] - red[3])


def jxM64(red, blue):
    return Right(blue[0] - red[4])


def jxM65(red, blue):
    return Right(abs(red[0] - 5))


def jxM66(red, blue):
    return Right(abs(red[1] - 5))


def jxM67(red, blue):
    return Right(abs(red[2] - 5))


def jxM68(red, blue):
    return Right(abs(red[3] - 5))


def jxM69(red, blue):
    return Right(abs(red[4] - 5))


def jxM70(red, blue):
    return Right(abs(blue[0] - 5))


def jxM71(red, blue):
    return Right(red[0] + 5)


def jxM72(red, blue):
    return Right(red[1] + 5)


def jxM73(red, blue):
    return Right(red[2] + 5)


def jxM74(red, blue):
    return Right(red[3] + 5)


def jxM75(red, blue):
    if red[4] + 5 > 35:
        return Right(red[4] + 5 - 35)
    else:
        return Right(red[4] + 5)


def jxM76(red, blue):
    if blue[0] + 5 > 35:
        return Right(blue[0] + 5 - 35)
    else:
        return Right(blue[0] + 5)


def jxM77(red, blue):
    return Right(int(math.pow((red[0] * blue[1]), 1 / 2)))


def jxM78(red, blue):
    return Right(int(math.pow((red[1] * blue[1]), 1 / 2)))


def jxM79(red, blue):
    return Right(int(math.pow((red[2] * blue[1]), 1 / 2)))


def jxM80(red, blue):
    return Right(int(math.pow((red[3] * blue[1]), 1 / 2)))


def jxM81(red, blue):
    return Right(int(math.pow((red[4] * blue[1]), 1 / 2)))


def jxM82(red, blue):
    return Right(int(math.pow((blue[0] * blue[1]), 1 / 2)))


def jxM83(red, blue):
    if int(math.pow((red[3] * red[1] * red[2]), 1 / 2)) <= 35:
        return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 2)))
    else:
        return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 4)))


def jxM84(red, blue):
    if int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)))


def jxM85(red, blue):
    if int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)))


def jxM86(red, blue):
    if int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)))


def jxM87(red, blue):
    if int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) > 70:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) > 35:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)))


def jxM88(red, blue):
    if int(math.pow((red[4] * red[1] * red[2]), 1 / 2)) <= 35:
        return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 2)))
    else:
        return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 4)))


def jxM89(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2]), 1 / 2)) <= 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 2)))
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 4)))


def jxM90(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 3)))


def jxM91(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)))


def jxM92(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)))


def jxM93(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)))


def jxM94(red, blue):
    if int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) > 70:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) - 70)
    elif int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) > 35:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)))


def jxM95(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) > 70:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) - 70)
    elif int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) > 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)))


def jxM96(red, blue):
    if int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) > 70:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) - 70)
    elif int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) > 35:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)))


def jxM97(red, blue):
    if int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) > 70:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) - 70)
    elif int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) > 35:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)))


def jxM98(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 3)))


def jxM99(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 3)))


def jxM100(red, blue):
    return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 3)))


def jxM101(red, blue):
    return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 3)))


def jxM102(red, blue):
    return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 3)))


def jxM103(red, blue):
    return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 3)))


def jxM104(red, blue):
    return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 3)))


def jxM105(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 4)))


def jxM106(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 4)))


def jxM107(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 4)))


def jxM108(red, blue):
    return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 4)))


def jxM109(red, blue):
    return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 4)))


def jxM110(red, blue):
    return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 4)))


def jxM111(red, blue):
    return Right(int(math.pow((red[3] * red[4] * blue[0] * red[1]), 1 / 4)))


def jxM112(red, blue):
    return Right(36 - red[0])


def jxM113(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)))


def jxM114(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)))


def jxM115(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) > 70:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) - 70)
    elif int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) > 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)))


def jxM116(red, blue):
    if int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)) > 35:
        return Right(int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)))


def jxM117(red, blue):
    if int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)) > 35:
        return Right(int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)))


def jxM118(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)))


def jxM119(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) > 105:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) - 105)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)))


def jxM120(red, blue):
    return Right((sum(red[1:4]) + blue[1]) / 4)


def jxM121(red, blue):
    return Right(abs(blue[0] - (sum(red[1:4]) + blue[1]) / 4))


def jxM122(red, blue):
    return Right(abs((sum(red[2:5]) + (sum(blue)) / 4 - blue[1])))


def jxM123(red, blue):
    return Right(19 - (sum(blue)))


def jxM124(red, blue):
    return Right(21 - (sum(blue)))


def jxM125(red, blue):
    return Right((sum(blue) + 2))


def jxM126(red, blue):
    return Right((sum(blue) + 4))


def jxM127(red, blue):
    return Right((sum(blue) * 2))


def jxM128(red, blue):
    if ((sum(blue) * 4)) <= 35:
        return Right((sum(blue) * 4))
    else:
        return Right(((sum(blue) * 4) - 35))


def jxM129(red, blue):
    return Right((sum(blue) + 6))


def jxM130(red, blue):
    return Right(blue[0] - red[0])


def jxM131(red, blue):
    return Right(abs(blue[0] - 2 * red[0]))


def jxM132(red, blue):
    return Right(abs(blue[0] - red[0] - red[1]))


def jxM133(red, blue):
    return Right(int(math.pow((red[2] * red[3] * blue[0]), 1 / 3)))


def jxM134(red, blue):
    return Right(int(math.pow((red[3] * red[4] * blue[0]), 1 / 3)))


def jxM135(red, blue):
    return Right(int(math.pow((red[0] * red[4] * blue[0]), 1 / 3)))


def jxM136(red, blue):
    return Right(abs(blue[0] - red[0] - red[2]))


def jxM137(red, blue):
    return Right(abs(blue[0] - red[0] - red[3]))


def jxM138(red, blue):
    return Right(abs(blue[0] - red[0] - red[4]))


def jxM139(red, blue):
    return Right(abs(blue[0] - red[0] - blue[0]))


def jxM140(red, blue):
    if int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) > 70:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) - 70)
    elif int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) > 35:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) - 35)
    else:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)))


def jxM141(red, blue):
    return Right(abs(red[0] - 11))


def jxM142(red, blue):
    return Right(abs(red[1] - 11))


def jxM143(red, blue):
    return Right(abs(red[2] - 11))


def jxM144(red, blue):
    return Right(abs(red[3] - 11))


def jxM145(red, blue):
    return Right(abs(red[4] - 11))


def jxM146(red, blue):
    return Right(abs(blue[0] - 11))


def jxM147(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[4] * blue[0]), 1 / 4)))


def jxM148(red, blue):
    return Right(red[0] + 11)


def jxM149(red, blue):
    return Right(red[1] + 11)


def jxM150(red, blue):
    if red[2] + 11 > 35:
        return Right(red[2] + 11 - 35)
    else:
        return Right(red[2] + 11)


def jxM151(red, blue):
    if red[3] + 11 > 35:
        return Right(red[3] + 11 - 35)
    else:
        return Right(red[3] + 11)


def jxM152(red, blue):
    if red[4] + 11 > 35:
        return Right(red[4] + 11 - 35)
    else:
        return Right(red[4] + 11)


def jxM153(red, blue):
    if blue[0] + 11 > 35:
        return Right(blue[0] + 11 - 35)
    else:
        return Right(blue[0] + 11)


def jxM154(red, blue):
    return Right(round(sum(red) / 39))


def jxM155(red, blue):
    return Right(abs(red[0] - 9))


def jxM156(red, blue):
    return Right(abs(red[1] - 9))


def jxM157(red, blue):
    return Right(abs(red[2] - 9))


def jxM158(red, blue):
    return Right(abs(red[3] - 9))


def jxM159(red, blue):
    return Right(abs(red[4] - 9))


def jxM160(red, blue):
    return Right(abs(blue[0] - 9))


def jxM161(red, blue):
    return Right(round(sum(red) / 38))


def jxM162(red, blue):
    return Right(red[0] + 9)


def jxM163(red, blue):
    return Right(red[1] + 9)


def jxM164(red, blue):
    if red[2] + 9 > 35:
        return Right(red[2] + 9 - 35)
    else:
        return Right(red[2] + 9)


def jxM165(red, blue):
    if red[3] + 9 > 35:
        return Right(red[3] + 9 - 35)
    else:
        return Right(red[3] + 9)


def jxM166(red, blue):
    if red[4] + 9 > 35:
        return Right(red[4] + 9 - 35)
    else:
        return Right(red[4] + 9)


def jxM167(red, blue):
    if blue[0] + 9 > 35:
        return Right(blue[0] + 9 - 35)
    else:
        return Right(blue[0] + 9)


def jxM168(red, blue):
    return Right((sum(red[:4]) + min(red)) / 6 - 3)


def jxM169(red, blue):
    return Right(red[0] + 7)


def jxM170(red, blue):
    return Right(red[1] + 7)


def jxM171(red, blue):
    return Right(red[2] + 7)


def jxM172(red, blue):
    if red[3] + 7 > 35:
        return Right(red[3] + 7 - 35)
    else:
        return Right(red[3] + 7)


def jxM173(red, blue):
    if red[4] + 7 > 35:
        return Right(red[4] + 7 - 35)
    else:
        return Right(red[4] + 7)


def jxM174(red, blue):
    if blue[0] + 7 > 35:
        return Right(blue[0] + 7 - 35)
    else:
        return Right(blue[0] + 7)


def jxM175(red, blue):
    if int(sum(red) / 4) > 35:
        return Right(int(sum(red) / 4) - 35)
    else:
        return Right(int(sum(red) / 4))


def jxM176(red, blue):
    if round(sum(red) / 3) > 35:
        return Right(round(sum(red) / 3) - 35)
    else:
        return Right(round(sum(red) / 3))


def jxM177(red, blue):
    if round(sum(red) / 2) > 70:
        return Right(round(sum(red) / 2) - 70)
    elif round(sum(red) / 2, 0) > 35:
        return Right(round(sum(red) / 2) - 35)
    else:
        return Right(round(sum(red) / 2))


def jxM178(red, blue):
    return Right(round(sum(red) / 7))


def jxM179(red, blue):
    return Right(round(sum(red) / 8))


def jxM180(red, blue):
    return Right(round(sum(red) / 9))


def jxM181(red, blue):
    return Right(round(sum(red) / 10))


def jxM182(red, blue):
    return Right(round(sum(red) / 11))


def jxM183(red, blue):
    return Right(round(sum(red) / 12))


def jxM184(red, blue):
    return Right(round(sum(red) / 13))


def jxM185(red, blue):
    return Right(round(sum(red) / 14))


def jxM186(red, blue):
    return Right(round(sum(red) / 15))


def jxM187(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[2]), 1 / 2)))


def jxM188(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[3]), 1 / 2)))


def jxM189(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[4]), 1 / 2)))


def jxM190(red, blue):
    return Right(round(math.pow((red[1] * red[0] + blue[0]), 1 / 2)))


def jxM191(red, blue):
    return Right(round(math.pow((blue[0] * red[0] + red[1]), 1 / 2)))


def jxM192(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[2]), 1 / 2)))


def jxM193(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[3]), 1 / 2)))


def jxM194(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[4]), 1 / 2)))


def jxM195(red, blue):
    return Right(round(sum(red) / 16))


def jxM196(red, blue):
    return Right(round(sum(red) / 35))


def jxM197(red, blue):
    return Right(round(math.pow((red[2] * red[3] + red[0]), 1 / 2)))


def jxM198(red, blue):
    return Right(round(math.pow((red[2] * red[3] + red[4]), 1 / 2)))


def jxM199(red, blue):
    return Right(round(math.pow((blue[0] * red[4] + red[0]), 1 / 2)))


def jxM200(red, blue):
    return Right(round(math.pow((red[3] * red[4] + red[1]), 1 / 2)))


def jxM201(red, blue):
    return Right(round(math.pow((red[3] * red[4] + red[0]), 1 / 2)))


def jxM202(red, blue):
    return Right(round(math.pow((red[3] * red[4] + blue[0]), 1 / 2)))


def jxM203(red, blue):
    return Right(round(sum(red) / 19))


def jxM204(red, blue):
    return Right(round(sum(red) / 20))


def jxM205(red, blue):
    return Right(round(sum(red) / 21))


def jxM206(red, blue):
    return Right(round(sum(red) / 24))


def jxM207(red, blue):
    return Right(round(sum(red) / 25))


def jxM208(red, blue):
    return Right(round(sum(red) / 26))


def jxM209(red, blue):
    return Right(round(sum(red) / 27))


def jxM210(red, blue):
    return Right(round(sum(red) / 28))


def jxM211(red, blue):
    return Right(round(sum(red) / 29))


def jxM212(red, blue):
    return Right(round(sum(red) / 30))


def jxM213(red, blue):
    return Right(round(sum(red) / 31))


def jxM214(red, blue):
    return Right(round(sum(red) / 32))


def jxM215(red, blue):
    return Right(round(sum(red) / 35))


def jxM216(red, blue):
    return Right(round(sum(red) / 34))


def jxM217(red, blue):
    return Right(round(sum(red) / 40))


def jxM218(red, blue):
    return Right(max(min((red[1] - red[0]), (red[2] - red[0]), (red[3] - red[0]), (red[4] - red[0]), (blue[0] - red[0])),
                     min((red[1] - red[0]), (red[2] - red[1]), (red[3] - red[1]), (red[4] - red[1]), (blue[0] - red[1])),
                     min((red[2] - red[0]), (red[2] - red[1]), (red[3] - red[2]), (red[4] - red[2]), (blue[0] - red[2])),
                     min((red[3] - red[0]), (red[3] - red[1]), (red[3] - red[2]), (red[4] - red[3]), (blue[0] - red[3])),
                     min((red[4] - red[0]), (red[4] - red[1]), (red[4] - red[2]), (red[4] - red[3]), (blue[0] - red[4])),
                     min((blue[0] - red[0]), (blue[0] - red[1]), (blue[0] - red[2]), (blue[0] - red[3]),
                         (blue[0] - red[4]))))


def jxM219(red, blue):
    result = round(sum(red) / 17 + 1)
    return Right(result)


def jxM220(red, blue):
    result = round(sum(red) / 18 + 4)
    return Right(result)


def jxM221(red, blue):
    result = round(sum(red) / 22 + 1)
    return Right(result)


def jxM222(red, blue):
    result = round(sum(red) / 23 + 5)
    return Right(result)


def jxM223(red, blue):
    result = int((sum(red) / 100) % 10) + int((sum(red) / 10) % 10) + int((sum(red) % 10)) + 9
    return Right(result)


def jxM224(red, blue):
    return Right(abs(red[3] - 12) + 2)


def jxM225(red, blue):
    if int((sum(red) - red[0]) / red[0]) + 6 > 105:
        result = int((sum(red) - red[0]) / red[0]) + 6 - 105
    elif int((sum(red) - red[0]) / red[0]) + 6 > 70:
        result = int((sum(red) - red[0]) / red[0]) + 6 - 70
    elif int((sum(red) - red[0]) / red[0]) + 6 > 35:
        result = int((sum(red) - red[0]) / red[0]) + 6 - 35
    else:
        result = int((sum(red) - red[0]) / red[0]) + 6
    return Right(result + 6)


def jxM226(red, blue):
    if int((sum(red) - red[1]) / red[1]) + 5 > 35:
        result = int((sum(red) - red[1]) / red[1]) - 35 + 5
    else:
        result = int((sum(red) - red[1]) / red[1]) + 5
    return Right(result)


def jxM227(red, blue):
    return Right(int((sum(red) - red[2]) / red[2]) + 3)


def jxM228(red, blue):
    return Right(int((sum(red) - red[3]) / red[3]) + 5)


def jxM229(red, blue):
    return Right(int((sum(red) - red[4]) / red[4]) + 8)


def jxM230(red, blue):
    return Right(int((sum(red) - blue[0]) / blue[0]) + 9)


def jxM231(red, blue):
    return Right((sum(red) - red[0]) % red[0] + 7)


def jxM232(red, blue):
    return Right((sum(red) - red[1]) % red[1] + 9)


def jxM233(red, blue):
    return Right((sum(red) - red[2]) % red[2] + 3)


def jxM234(red, blue):
    return Right((sum(red) - red[3]) % red[3] + 2)


def jxM235(red, blue):
    return Right((sum(red) - red[4]) % red[4] + 3)


def jxM236(red, blue):
    return Right((sum(red) - blue[0]) % blue[0] + 8)


def jxM237(red, blue):
    return Right(int(math.pow(red[0] * red[1], 1 / 2)) + 4)


def jxM238(red, blue):
    return Right(int(math.pow(red[1] * red[2], 1 / 2)) + 6)


def jxM239(red, blue):
    return Right(int(math.pow(red[2] * red[3], 1 / 2)) + 2)


def jxM240(red, blue):
    return Right(int(math.pow(red[3] * red[4], 1 / 2)) + 6)


def jxM241(red, blue):
    return Right(int(math.pow(red[4] * blue[0], 1 / 2)) + 4)


def jxM242(red, blue):
    return Right(int(math.pow(red[0] * blue[0], 1 / 2)) + 3)


def jxM243(red, blue):
    return Right(int(math.pow(red[0] * red[2], 1 / 2)) + 3)


def jxM244(red, blue):
    return Right(int(math.pow(red[0] * red[3], 1 / 2)) + 8)


def jxM245(red, blue):
    return Right(int(math.pow(red[0] * red[4], 1 / 2)) + 3)


def jxM246(red, blue):
    return Right(int(math.pow(red[1] * red[3], 1 / 2)) + 2)


def jxM247(red, blue):
    return Right(int(math.pow(red[1] * red[4], 1 / 2)) + 7)


def jxM248(red, blue):
    return Right(int(math.pow(red[1] * blue[0], 1 / 2)) + 9)


def jxM249(red, blue):
    return Right(int(math.pow(red[2] * red[4], 1 / 2)) + 5)


def jxM250(red, blue):
    return Right(int(math.pow(red[2] * blue[0], 1 / 2)) + 0)


def jxM251(red, blue):
    return Right(int(math.pow(red[3] * blue[0], 1 / 2)) + 2)


def jxM252(red, blue):
    if blue[0] + sum(blue) + 8 <= 35:
        result = blue[0]+sum(blue) + 8
    else:
        result = blue[0] + sum(blue) + 8 - 35
    return Right(result)


def jxM253(red, blue):
    return Right(round((red[1] + red[2] + red[3] + red[4] + sum(blue) / 6) + 8))


def jxM254(red, blue):
    return Right(red[1] + (sum(blue) + 4))


def jxM255(red, blue):
    return Right(blue[0] - red[1] + 1 + 1)


def jxM256(red, blue):
    if red[1] + blue[0] + 1 + 9 <= 35:
        return Right(red[1] + blue[0] + 1 + 9)
    else:
        return Right(red[1] + blue[0] + 1 + 9 - 35)


def jxM257(red, blue):
    if blue[0] - red[1] + 10 + 7 <= 35:
        return Right(blue[0] - red[1] + 10 + 7)
    else:
        return Right(blue[0] - red[1] + 10 + 7 - 35)


def jxM258(red, blue):
    return Right(red[0] + red[1] + 1)


def jxM259(red, blue):
    if red[3] + red[0] + 6 > 35:
        return Right(red[3] + red[0] + 6 - 35)
    else:
        return Right(red[3] + red[0] + 6)


def jxM260(red, blue):
    return Right(red[3] - red[0] + 7 + 9)


def jxM261(red, blue):
    return Right(int(sum(red[2:6]) / 4) + 3)


def jxM262(red, blue):
    return Right(int(sum(red[:3]) / 3) + 9)


def jxM263(red, blue):
    if red[1] + red[2] + 9 <= 35:
        return Right(red[1] + red[2] + 9)
    else:
        return Right(red[1] + red[2] + 9 - 35)


def jxM264(red, blue):
    return Right(abs(red[4] - red[3] + 10) + 3)


def jxM265(red, blue):
    return Right(red[0] + 12 + 7)


def jxM266(red, blue):
    return Right(red[1] - red[0] + 5)


def jxM267(red, blue):
    return Right(red[2] - red[0] + 1)


def jxM268(red, blue):
    return Right(red[3] - red[0] + 0)


def jxM269(red, blue):
    return Right(red[4] - red[0] + 5)


def jxM270(red, blue):
    return Right(blue[0] - red[0] + 8)


def jxM271(red, blue):
    return Right(red[2] - red[1] + 2)


def jxM272(red, blue):
    return Right(red[3] - red[1] + 0)


def jxM273(red, blue):
    return Right(red[4] - red[1] + 9)


def jxM274(red, blue):
    return Right(blue[0] - red[1] + 7)


def jxM275(red, blue):
    return Right(red[3] - red[2] + 4)


def jxM276(red, blue):
    return Right(red[4] - red[2] + 9)


def jxM277(red, blue):
    return Right(blue[0] - red[2] + 4)


def jxM278(red, blue):
    return Right(blue[1] - blue[0] + 4)


def jxM279(red, blue):
    if int(math.pow((red[2] * red[3] * red[4]), 1 / 2) + 5) <= 35:
        return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 2)) + 5)
    else:
        return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 4)) + 5)


def jxM280(red, blue):
    return Right(red[4] - red[3] + 9)


def jxM281(red, blue):
    return Right(blue[0] - red[3] + 2)


def jxM282(red, blue):
    return Right(blue[0] - red[4] + 3)


def jxM283(red, blue):
    return Right(abs(red[0] - 5) + 0)


def jxM284(red, blue):
    return Right(abs(red[1] - 5) + 7)


def jxM285(red, blue):
    return Right(abs(red[2] - 5) + 8)


def jxM286(red, blue):
    return Right(abs(red[3] - 5) + 1)


def jxM287(red, blue):
    return Right(abs(red[4] - 5) + 6)


def jxM288(red, blue):
    return Right(abs(blue[0] - 5) + 4)


def jxM289(red, blue):
    return Right(red[0] + 5 + 0)


def jxM290(red, blue):
    return Right(red[1] + 5 + 6)


def jxM291(red, blue):
    return Right(red[2] + 5 + 2)


def jxM292(red, blue):
    return Right(red[3] + 5 + 8)


def jxM293(red, blue):
    if red[4] + 5 + 6 > 35:
        return Right(red[4] + 5 + 6 - 35)
    else:
        return Right(red[4] + 5 + 6)


def jxM294(red, blue):
    if blue[0] + 5 + 2 > 35:
        return Right(blue[0] + 5 + 2 - 35)
    else:
        return Right(blue[0] + 5 + 2)


def jxM295(red, blue):
    return Right(int(math.pow((red[0] * blue[1]), 1 / 2)) + 0)


def jxM296(red, blue):
    return Right(int(math.pow((red[1] * blue[1]), 1 / 2)) + 8)


def jxM297(red, blue):
    return Right(int(math.pow((red[2] * blue[1]), 1 / 2)) + 9)


def jxM298(red, blue):
    return Right(int(math.pow((red[3] * blue[1]), 1 / 2)) + 9)


def jxM299(red, blue):
    return Right(int(math.pow((red[4] * blue[1]), 1 / 2)) + 8)


def jxM300(red, blue):
    return Right(int(math.pow((blue[0] * blue[1]), 1 / 2)) + 6)


def jxM301(red, blue):
    if int(math.pow((red[3] * red[1] * red[2]), 1 / 2)) + 2 <= 35:
        return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 2)) + 2)
    else:
        return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 4)) + 2)


def jxM302(red, blue):
    if int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 8 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 8 - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 8 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 8 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 8)


def jxM303(red, blue):
    if int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) + 0 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) + 0 - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 0 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) + 0 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 2)) + 0)


def jxM304(red, blue):
    if int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) + 3 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) + 3 - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 3 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) + 3 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 2)) + 3)


def jxM305(red, blue):
    if int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) + 4 > 70:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) + 4 - 70)
    elif int(math.pow((red[0] * red[1] * red[2]), 1 / 2)) + 4 > 35:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) + 4 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 2)) + 4)


def jxM306(red, blue):
    if int(math.pow((red[4] * red[1] * red[2]), 1 / 2)) + 8 <= 35:
        return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 2)) + 8)
    else:
        return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 4)) + 8)


def jxM307(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2]), 1 / 2)) + 2 <= 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 2)) + 2)
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 4)) + 2)


def jxM308(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2]), 1 / 3)) + 5)


def jxM309(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) + 3 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) + 3 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) + 3 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 3)) + 3)


def jxM310(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) + 4 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) + 4 - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) + 4 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) + 4 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 3)) + 4)


def jxM311(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) + 2 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) + 2 - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) + 2 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) + 2 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 3)) + 2)


def jxM312(red, blue):
    if int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) + 1 > 70:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) + 1 - 70)
    elif int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) + 1 > 35:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) + 1 - 35)
    else:
        return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 3)) + 1)


def jxM313(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) + 1 > 70:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) + 1 - 70)
    elif int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) + 1 > 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) + 1 - 35)
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 3)) + 1)


def jxM314(red, blue):
    if int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) + 7 > 70:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) + 7 - 70)
    elif int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) + 7 > 35:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) + 7 - 35)
    else:
        return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 3)) + 7)


def jxM315(red, blue):
    if int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) + 0 > 70:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) + 0 - 70)
    elif int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) + 0 > 35:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) + 0 - 35)
    else:
        return Right(int(math.pow((red[3] * red[4] * blue[0] * red[0]), 1 / 3)) + 0)


def jxM316(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[3]), 1 / 3)) + 6)


def jxM317(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[4]), 1 / 3)) + 7)


def jxM318(red, blue):
    return Right(int(math.pow((red[0] * red[1] * blue[0]), 1 / 3)) + 9)


def jxM319(red, blue):
    return Right(int(math.pow((red[3] * red[1] * red[2]), 1 / 3)) + 8)


def jxM320(red, blue):
    return Right(int(math.pow((red[4] * red[1] * red[2]), 1 / 3)) + 2)


def jxM321(red, blue):
    return Right(int(math.pow((blue[0] * red[1] * red[2]), 1 / 3)) + 1)


def jxM322(red, blue):
    return Right(int(math.pow((red[2] * red[3] * red[4]), 1 / 3)) + 4)


def jxM323(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * red[3]), 1 / 4)) + 8)


def jxM324(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * red[4]), 1 / 4)) + 0)


def jxM325(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0]), 1 / 4)) + 8)


def jxM326(red, blue):
    return Right(int(math.pow((red[4] * red[1] * red[2] * red[3]), 1 / 4)) + 6)


def jxM327(red, blue):
    return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3]), 1 / 4)) + 5)


def jxM328(red, blue):
    return Right(int(math.pow((red[4] * blue[0] * red[2] * red[3]), 1 / 4)) + 1)


def jxM329(red, blue):
    return Right(int(math.pow((red[3] * red[4] * blue[0] * red[1]), 1 / 4)) + 3)


def jxM330(red, blue):
    return Right(36 - red[0] + 2)


def jxM331(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 8 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 8 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 8)


def jxM332(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)) + 2 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)) + 2 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * blue[0]), 1 / 4)) + 2)


def jxM333(red, blue):
    if int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 3 > 70:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 3 - 70)
    elif int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 3 > 35:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 3 - 35)
    else:
        return Right(int(math.pow((blue[0] * red[1] * red[2] * red[3] * red[4]), 1 / 4)) + 3)


def jxM334(red, blue):
    if int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)) + 0 > 35:
        return Right(int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)) + 0 - 35)
    else:
        return Right(int(math.pow((blue[0] * red[0] * red[2] * red[3] * red[4]), 1 / 4)) + 0)


def jxM335(red, blue):
    if int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)) + 6 > 35:
        return Right(int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)) + 6 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * blue[0] * red[3] * red[4]), 1 / 4)) + 6)


def jxM336(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)) + 6 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)) + 6 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * blue[0] * red[4]), 1 / 4)) + 6)


def jxM337(red, blue):
    if int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 > 105:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 - 105)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 > 70:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 - 70)
    elif int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 > 35:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4 - 35)
    else:
        return Right(int(math.pow((red[0] * red[1] * red[2] * red[3] * red[4] * blue[0]), 1 / 4)) + 4)


def jxM338(red, blue):
    return Right((sum(red[1:4]) + (sum(blue)) / 4 + 7))


def jxM339(red, blue):
    return Right(abs((blue[0]) - (sum(red[1:4]) + blue[1]) / 4) + 0)


def jxM340(red, blue):
    return Right(abs((sum(red[2:5]) + (sum(blue)) / 4 - (sum(blue)) + 9)))


def jxM341(red, blue):
    return Right(19 - (sum(blue) + 3))


def jxM342(red, blue):
    return Right(21 - (sum(blue) + 8))


def jxM343(red, blue):
    return Right((sum(blue) + 2 + 4))


def jxM344(red, blue):
    return Right((sum(blue) + 4 + 4))


def jxM345(red, blue):
    return Right((sum(blue) * 2 + 6))


def jxM346(red, blue):
    if ((sum(blue) * 4 + 0)) <= 35:
        return Right((sum(blue) * 4 + 0))
    else:
        return Right(((sum(blue) * 4) + 0 - 35))


def jxM347(red, blue):
    return Right((sum(blue) + 6 + 9))


def jxM348(red, blue):
    return Right(blue[0] - red[0] + 5)


def jxM349(red, blue):
    return Right(abs(blue[0] - 2 * red[0]) + 5)


def jxM350(red, blue):
    return Right(abs(blue[0] - red[0] - red[1]) + 0)


def jxM351(red, blue):
    return Right(int(math.pow((red[2] * red[3] * blue[0]), 1 / 3)) + 5)


def jxM352(red, blue):
    return Right(int(math.pow((red[3] * red[4] * blue[0]), 1 / 3)) + 8)


def jxM353(red, blue):
    return Right(int(math.pow((red[0] * red[4] * blue[0]), 1 / 3)) + 2)


def jxM354(red, blue):
    return Right(abs(blue[0] - red[0] - red[2]) + 2)


def jxM355(red, blue):
    return Right(abs(blue[0] - red[0] - red[3]) + 3)


def jxM356(red, blue):
    return Right(abs(blue[0] - red[0] - red[4]) + 1)


def jxM357(red, blue):
    return Right(abs(blue[0] - red[0] - blue[0]) + 7)


def jxM358(red, blue):
    if int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) + 2 > 70:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) + 2 - 70)
    elif int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) + 2 > 35:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) + 2 - 35)
    else:
        return Right(int(math.pow((red[4] * blue[0] * red[0] * red[1]), 1 / 3)) + 2)


def jxM359(red, blue):
    return Right(abs(red[0] - 11) + 5)


def jxM360(red, blue):
    return Right(abs(red[1] - 11) + 3)


def jxM361(red, blue):
    return Right(abs(red[2] - 11) + 5)


def jxM362(red, blue):
    return Right(abs(red[3] - 11) + 9)


def jxM363(red, blue):
    return Right(abs(red[4] - 11) + 4)


def jxM364(red, blue):
    return Right(abs(blue[0] - 11) + 9)


def jxM365(red, blue):
    return Right(int(math.pow((red[0] * red[1] * red[4] * blue[0]), 1 / 4)) + 8)


def jxM366(red, blue):
    return Right(red[0] + 11 + 1)


def jxM367(red, blue):
    return Right(red[1] + 11 + 2)


def jxM368(red, blue):
    if red[2] + 11 + 8 > 35:
        return Right(red[2] + 11 + 8 - 35)
    else:
        return Right(red[2] + 11 + 8)


def jxM369(red, blue):
    if red[3] + 11 + 4 > 35:
        return Right(red[3] + 11 + 4 - 35)
    else:
        return Right(red[3] + 11 + 4)


def jxM370(red, blue):
    if red[4] + 11 + 8 > 35:
        return Right(red[4] + 11 + 8 - 35)
    else:
        return Right(red[4] + 11 + 8)


def jxM371(red, blue):
    if blue[0] + 11 + 1 > 35:
        return Right(blue[0] + 11 + 1 - 35)
    else:
        return Right(blue[0] + 11 + 1)


def jxM372(red, blue):
    return Right(round(sum(red) / 39) + 1)


def jxM373(red, blue):
    return Right(abs(red[0] - 9) + 1)


def jxM374(red, blue):
    return Right(abs(red[1] - 9) + 7)


def jxM375(red, blue):
    return Right(abs(red[2] - 9) + 4)


def jxM376(red, blue):
    return Right(abs(red[3] - 9) + 5)


def jxM377(red, blue):
    return Right(abs(red[4] - 9) + 0)


def jxM378(red, blue):
    return Right(abs(blue[0] - 9) + 2)


def jxM379(red, blue):
    return Right(round(sum(red) / 38) + 8)


def jxM380(red, blue):
    return Right(red[0] + 9 + 4)


def jxM381(red, blue):
    return Right(red[1] + 9 + 1)


def jxM382(red, blue):
    if red[2] + 9 + 0 > 35:
        return Right(red[2] + 9 + 0 - 35)
    else:
        return Right(red[2] + 9 + 0)


def jxM383(red, blue):
    if red[3] + 9 + 2 > 35:
        return Right(red[3] + 9 + 2 - 35)
    else:
        return Right(red[3] + 9 + 2)


def jxM384(red, blue):
    if red[4] + 9 + 7 > 35:
        return Right(red[4] + 9 + 7 - 35)
    else:
        return Right(red[4] + 9 + 7)


def jxM385(red, blue):
    if blue[0] + 9 + 6 > 35:
        return Right(blue[0] + 9 + 6 - 35)
    else:
        return Right(blue[0] + 9 + 6)


def jxM386(red, blue):
    return Right((sum(red[:4]) + min(red)) / 6 - 3 + 1)


def jxM387(red, blue):
    return Right(red[0] + 7 + 9)


def jxM388(red, blue):
    return Right(red[1] + 7 + 3)


def jxM389(red, blue):
    return Right(red[2] + 7 + 8)


def jxM390(red, blue):
    if red[3] + 7 + 5 > 35:
        return Right(red[3] + 7 + 5 - 35)
    else:
        return Right(red[3] + 7 + 5)


def jxM391(red, blue):
    if red[4] + 7 + 2 > 35:
        return Right(red[4] + 7 + 2 - 35)
    else:
        return Right(red[4] + 7 + 2)


def jxM392(red, blue):
    if blue[0] + 7 + 1 > 35:
        return Right(blue[0] + 7 + 1 - 35)
    else:
        return Right(blue[0] + 7 + 1)


def jxM393(red, blue):
    if int(sum(red) / 4) + 1 > 35:
        return Right(int(sum(red) / 4) + 1 - 35)
    else:
        return Right(int(sum(red) / 4) + 1)


def jxM394(red, blue):
    if round(sum(red) / 3) + 0 > 35:
        return Right(round(sum(red) / 3) + 0 - 35)
    else:
        return Right(round(sum(red) / 3) + 0)


def jxM395(red, blue):
    if round(sum(red) / 2) + 5 > 70:
        return Right(round(sum(red) / 2) + 5 - 70)
    elif round(sum(red) / 2, 0) + 5 > 35:
        return Right(round(sum(red) / 2) + 5 - 35)
    else:
        return Right(round(sum(red) / 2) + 5)


def jxM396(red, blue):
    return Right(round(sum(red) / 7) + 5)


def jxM397(red, blue):
    return Right(round(sum(red) / 8) + 5)


def jxM398(red, blue):
    return Right(round(sum(red) / 9) + 9)


def jxM399(red, blue):
    return Right(round(sum(red) / 10) + 6)


def jxM400(red, blue):
    return Right(round(sum(red) / 11) + 4)


def jxM401(red, blue):
    return Right(round(sum(red) / 12) + 4)


def jxM402(red, blue):
    return Right(round(sum(red) / 13) + 6)


def jxM403(red, blue):
    return Right(round(sum(red) / 14) + 2)


def jxM404(red, blue):
    return Right(round(sum(red) / 15) + 2)


def jxM405(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[2]), 1 / 2)) + 9)


def jxM406(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[3]), 1 / 2)) + 4)


def jxM407(red, blue):
    return Right(round(math.pow((red[0] * red[1] + red[4]), 1 / 2)) + 8)


def jxM408(red, blue):
    return Right(round(math.pow((red[1] * red[0] + blue[0]), 1 / 2)) + 9)


def jxM409(red, blue):
    return Right(round(math.pow((blue[0] * red[0] + red[1]), 1 / 2)) + 5)


def jxM410(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[2]), 1 / 2)) + 4)


def jxM411(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[3]), 1 / 2)) + 9)


def jxM412(red, blue):
    return Right(round(math.pow((red[0] * blue[0] + red[4]), 1 / 2)) + 3)


def jxM413(red, blue):
    return Right(round(sum(red) / 16) + 0)


def jxM414(red, blue):
    return Right(round(sum(red) / 35) + 3)


def jxM415(red, blue):
    return Right(round(math.pow((red[2] * red[3] + red[0]), 1 / 2)) + 8)


def jxM416(red, blue):
    return Right(round(math.pow((red[2] * red[3] + red[4]), 1 / 2)) + 1)


def jxM417(red, blue):
    return Right(round(math.pow((blue[0] * red[4] + red[0]), 1 / 2)) + 9)


def jxM418(red, blue):
    return Right(round(math.pow((red[3] * red[4] + red[1]), 1 / 2)) + 6)


def jxM419(red, blue):
    return Right(round(math.pow((red[3] * red[4] + red[0]), 1 / 2)) + 4)


def jxM420(red, blue):
    return Right(round(math.pow((red[3] * red[4] + blue[0]), 1 / 2)) + 4)


def jxM421(red, blue):
    return Right(round(sum(red) / 19) + 2)


def jxM422(red, blue):
    return Right(round(sum(red) / 20) + 8)


def jxM423(red, blue):
    return Right(round(sum(red) / 21) + 8)


def jxM424(red, blue):
    return Right(round(sum(red) / 24) + 1)


def jxM425(red, blue):
    return Right(round(sum(red) / 25) + 0)


def jxM426(red, blue):
    return Right(round(sum(red) / 26) + 9)


def jxM427(red, blue):
    return Right(round(sum(red) / 27) + 7)


def jxM428(red, blue):
    return Right(round(sum(red) / 28) + 5)


def jxM429(red, blue):
    return Right(round(sum(red) / 29) + 6)


def jxM430(red, blue):
    return Right(round(sum(red) / 30) + 6)


def jxM431(red, blue):
    return Right(round(sum(red) / 31) + 5)


def jxM432(red, blue):
    return Right(round(sum(red) / 32) + 9)


def jxM433(red, blue):
    return Right(round(sum(red) / 35) + 3)


def jxM434(red, blue):
    return Right(round(sum(red) / 34) + 3)


def jxM435(red, blue):
    return Right(round(sum(red) / 40) + 4)

