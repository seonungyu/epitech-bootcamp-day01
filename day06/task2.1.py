def sum_to(n):                 # 1부터 n까지 합을 구하는 함수
    if n == 1:                 # 종료 조건: n이 1이면
        return 1               #   답은 그냥 1 (더 물어볼 필요 없음)
    return n + sum_to(n - 1)   # 아니면: "나(n) + 1부터 n-1까지의 합"
                               #   → 자기 자신을 더 작은 수로 다시 부름
print(sum_to(42))