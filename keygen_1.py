

username = "iluvani" # Replace "your_username" with the actual username

length = len(username)

username = [ord(char) for char in username]
username.append(0)

arr_1 = [0, 170, 137, 196, 254, 70]
arr_2 = [114, 120, 240, 208, 3, 231]
arr_3 = [156, 247, 253, 244, 231, 185]
arr_4 = [55, 181, 27, 201, 80, 115]

def printHexUsername(username, length):
    encrypted_username = []
    for i in range(length + 1):
        encrypted_username.append(hex(username[i]))
    print(encrypted_username)

def toHex(li):
    res = ""
    for i in range(len(li) - 1, -1, -1):
        if (li[i] != "0x0"):
            tmp = ""
            for j in range(len(li[i]) - 2, len(li[i])):    
                tmp += li[i][j]
            res += tmp
    return res


eax = 0x0
esi = 0x0
ecx = 0x0
ebx = 0x0
edi = 0x0
#first encryption
while esi < length:
    ecx =  username[esi + 1]  # Assuming the XOR operation is on ASCII values
    ebx = ecx ^ arr_1[eax + 1]
    eax += 1

    if eax == 5:
        eax = 0
    
    username[esi + 1] = ebx
    arr_1[eax] = ecx

    esi += 1

edi = 0
ecx = 0

printHexUsername(username, length)

#second encryption

while ecx < length:
    ebx = arr_2[edi + 1]
    esi = length
    esi -= ecx
    esi -= 1
    eax = username[esi + 1]
    ebx = ebx ^ eax
    edi += 1
    username[esi + 1] = ebx
    arr_2[edi] = eax
    if (edi != 5):
        ecx += 1
    else:
        edi = 0
        ecx += 1

printHexUsername(username, length)

esi = 0
edi = 0

#third encryption

while edi < length:
    eax = username[edi + 1]
    ecx = arr_3[esi + 1]
    ecx = ecx ^ eax
    esi += 1
    username[edi + 1] = ecx
    arr_3[esi] = eax
    if (esi == 5):
        esi = 0
    edi += 1

printHexUsername(username, length)

edi = 0
ecx = 0

#fourth encryption

while ecx < length:
    ebx = arr_4[edi + 1]
    esi = length
    esi -= ecx
    esi -= 1
    eax = username[esi + 1]
    ebx = ebx ^ eax
    edi += 1
    username[esi + 1] = ebx
    arr_4[edi] = eax
    if (edi == 5):
        edi = 0
    ecx += 1

printHexUsername(username, length)

eax = 0
#div ecx -> eax contains the quotient, edx contains the remainder

edi = [0, 0, 0, 0, 0, 0, 0]
while eax < length:
    ecx = eax
    ecx = ecx & 3
    ebx = edi[ecx]
    esi = ecx
    ecx = username[eax + 1]
    ebx += ecx
    eax += 1
    edi[esi] = ebx

nedi = [hex(num) for num in edi]
print(nedi)

ecx = 10
eax = edi
ebx = 0

eax = int(toHex(nedi), 16)
username.append(0)
username.append(0)
while (eax != 0):
    edx = 0
    
    temp = eax

    eax = int(temp / 10)
    edx = temp % 10 + 48
    username[ebx + 1] = edx
    print(ebx)
    ebx += 1


key = ""
for i in range(len(username) - 1, 0, -1):
    key += str(username[i] - 48)

print(key)