def my_count(stop, start=0):       # start=0 → 안 주면 자동으로 0 (기본값)
    for i in range(start, stop + 1):   # PDF: start부터 stop까지 (stop 포함이라 +1)
        print(i)


my_count(3)        # 0 1 2 3
my_count(7, 5)     # 5 6 7
