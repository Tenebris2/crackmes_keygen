import threading

key = "4567-45678-4567"
key_2 = "5678-56789-5678"
key = [int(char) for char in key if char.isdigit()]

def check(key):
    j = 0 #ebp-0x15
    k = 0 #ebp-0x14
    i = 0 #ebp-0x10
    esi = 0
    al = 0
    eax = 0

    while 1:
        eax = 0
        ecx = 0
        edx = int("0xffffffff", 16)
        eax *= edx
        eax = eax & 1
        bl = 1 if eax == 0 else 0
        bh = 1 if ecx < int("0xa", 16) else 0
        bl |= bh

        al = 1 if i < int("0xc", 16) else 0
        ecx = 0
        edx = 0
        ecx = ecx * (ecx - 1)
        ecx &= 1
        ah = 1 if ecx == 0 else 0 
        bl = 1 if edx < int("0xa", 16) else 0
        ah |= bl
        if (al != 1): break
        eax = key[i]
        ecx = key[i + 1]
        eax *= ecx
        eax += k
        k = eax

        eax = 0
        ecx = 0
        edx = eax
        edx -= 1
        eax *= edx
        eax &= 1
        bl = 1 if eax == 0 else 0
        bh = 1 if ecx < int("0xa", 16) else 0
        bl |= bh
        i += 2
        eax = 0
        ecx = 0
        edx = eax
        edx -= 1
        eax *= edx
        eax &= 1
        bl = 1 if eax == 0 else 0
        bh = 1 if ecx < int("0xa", 16) else 0
        bl |= bh

    eax = int("0xa", 16)
    ecx = key[i]
    edx = k

    j = eax
    eax = edx
    temp = eax
    eax = int(temp / j)
    edx = temp % j
    bl = 1 if ecx == edx else 0
    bl &= 1
    ecx = bl
    eax = ecx

    return eax
def key_checker(key):
    eax = check(key)
    cl = 1 if eax != 0 else 0
    al = cl
    return al == 1



from concurrent.futures import ThreadPoolExecutor

def check_keys(start1, end1, start2, end2, start3, end3):
    for part1 in range(start1, end1):
        for part2 in range(start2, end2):
            for part3 in range(start3, end3):
                key = f"{part1:04d}-{part2:05d}-{part3:04d}"
                key = [int(char) for char in key if char.isdigit()]

            
                if key_checker(key):
                    print(key)

def main():
    # Create a thread pool with 10 worker threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Submit 4 tasks to the pool
        for i in range(4):
            start1 = i * 2500
            end1 = (i + 1) * 2500

            future = executor.submit(check_keys, start1, end1, 0, 100000, 0, 10000)
            # Optionally, you can get the result of each task
            # result = future.result()

if __name__ == "__main__":
    main()
