

for part1 in range(10000):
    for part2 in range(100000):
        for part3 in range(10000):
            k = 3
            eax = 0
            ecx = 0
            edx = 0
            esi = 0
            i = 0

            key = f"{part1:04d}-{part2:05d}-{part3:04d}"

        #     #ebp-0x10 = eax = i (as in incrementor)
        #     #ebp-0x14 = k
            key = [int(char) for char in key if char.isdigit()]

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

            ecx = key[12]
            edx = k
            eax = edx
            temp = int(eax)
            eax = int(temp / 10)
            edx = temp % 10

            if (edx == ecx):
                print("Here is the key: ") 
                print(key)


