
for i in range(1,101):
    so_chia_het = 0
    for j in range(1,i+1):
        if i%j==0:
            so_chia_het +=1

    if so_chia_het==2:
        print(f"{i} la so nguyen to")
        print()
        



 