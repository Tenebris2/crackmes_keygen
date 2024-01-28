#     #ebp-0x10 = eax = i (as in incrementor)
#     #ebp-0x14 = k

key = "1234-12345-1234"
key_2 = "0000-00167-3775"
key = [2, 5, 0, 0, 0, 0, 2, 0, 6, 0, 1, 2, 8]
# 0, 0, 0, 0, 0, 0, 1, 6, 7, 3, 7, 7, 5
k = 3
eax = 0
ecx = 0
edx = 0
esi = 0
i = 0

for i in range(12):
    eax = k
    eax = eax << 1
    ecx = key[i]
    edx = eax
    edx = edx ^ int("0xffffffff", 16)
    esi = ecx
    esi = esi & edx
    ecx = ecx ^ int("0xffffffff", 16)
    eax = eax & ecx
    esi = esi | eax
    eax = k
    eax += esi
    k = eax

l = 0

print(eax)

ecx = key[12]
edx = k
eax = edx
temp = int(eax)
eax = int(temp / 10)
edx = temp % 10

print(eax)
print(edx)
print(ecx)

for i in range(13):
    if (i == 4): print("-", end="")
    if (i == 9): print("-", end="")
    print(key[i], end="")


