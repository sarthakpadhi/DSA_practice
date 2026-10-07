import sys
MOD = 10**9 + 7


def solve(n, k, v):
    """
    n, k: as in the statement
    v: list of n values; the first k are special
    Return (Alice's expected score, Bob's expected score) modulo MOD
    """
    alice = 0
    bob = 0
    m = n - k
    S = sum(v[:k]) % MOD
    T = sum(v[k:]) % MOD
    total = (S + T) % MOD
    if m == 0:
        return total, 0

    alice = S * (m // 2 + 1) % MOD * pow(m + 1, MOD - 2, MOD) % MOD
    alice += T * ((m + 1) // 2) % MOD * pow(m, MOD - 2, MOD) % MOD
    alice %= MOD
    bob = (total - alice) % MOD

    return alice, bob


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(data[pos]); k = int(data[pos + 1]); pos += 2
        v = list(map(int, data[pos:pos + n])); pos += n
        a, b = solve(n, k, v)
        out.append(f"{a} {b}")
    print("\n".join(out))


if __name__ == "__main__":
    main()