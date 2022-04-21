def getHexstring(desiredChars, arr):
    """Comment here"""

    print(desiredChars, arr)
    hexstring = 'ddb30acf4aacfee5'

    return hexstring

if __name__ == '__main__':

    arr = ["e8ce3e0ed2c023f3",
           "2fcca272349c5878"]

    newId = getHexstring(16, arr)
    print(newId)

