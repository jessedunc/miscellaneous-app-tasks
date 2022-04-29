import uuid


def getHexstring(desiredChars, arr):
    """Comment here"""

    while True:
        hexstring = uuid.uuid4()
        hexstring = str(hexstring)

        if hexstring not in arr:
            break
    hexstring = hexstring.replace('-', '')
    return str(hexstring)[:desiredChars]


if __name__ == '__main__':
    arr = ["e8ce3e0ed2c023f3",
           "2fcca272349c5878"]

    newId = getHexstring(16, arr)
    print(newId)
