
def hexa(x):
    x=hex(x)
    if len(x)%2==1:
        x='0'+x
    return x



print(bytes().fromhex(hexa(hex(3))))
print(bytes().fromhex(hexa(hex(30))))
print(bytes().fromhex(hexa(hex(0))))
# print(bytes().fromhex(hexa(hex('a'))))
print(bytes().fromhex(hexa('ae')))
print(bytes().fromhex(hexa('ae')))


