T = int(input())
for _ in range(T):
    N, K, W = list(map(int, input().split()))
    Lk = list(map(int, input().split()))
    Al, Bl, Cl, Dl = list(map(int, input().split()))
    Hk = list(map(int, input().split()))
    Ah, Bh, Ch, Dh = list(map(int, input().split()))
    for i in range(K + 1, len(Lk)):
        Lk[i] = (Al * Lk[i - 2] + Bl * Lk[i - 1] + Cl) % Dl + 1
        Hk[i] = (Ah * Hk[i - 2] + Bh * Hk[i - 1] + Ch) % Dh + 1
