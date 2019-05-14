def mirrorBits(a):
    bits = f'{a:b}'
    bits = bits[::-1]
    return int(bits, 2)

print(mirrorBits(97))