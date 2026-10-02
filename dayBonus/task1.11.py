def my_count(stop, start=0, step=1):
    if not all(isinstance(x, int) for x in (stop, start, step)):
        print("Error: stop, start and step must be integers")
        return
    if step == 0:                  # 0칸씩 가면 영원히 제자리 → 막기
        print("Error: step cannot be 0")
        return
    for i in range(start, stop, step):   # 이번엔 stop 미포함 (range와 똑같은 규칙)
        print(i)                         # stop < start인데 step이 양수면 그냥 아무것도 안 찍힘


my_count(100, -100, 42)    # -100 -58 -16 26 68
my_count(-100, 100, -42)   # 100 58 16 -26 -68
my_count(5, 0, 0)          # step = 0
my_count(-5, 5)            # stop < start → 출력 없음
my_count("toto")           # stop = "toto"
