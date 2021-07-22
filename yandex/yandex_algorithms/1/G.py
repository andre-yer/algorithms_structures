def get_details(n, k, m):
    if n >= k >= m:
        k_n = n // k  # количество заготовок
        k_rest = n % k  # количество оставшегося от заготовок металла
        m_n = k // m * k_n  # количество деталей
        m_rest = k % m * k_n  # количесвто оставшегося металла от деталей
        return m_n + get_details(m_rest + k_rest, k, m)
    else:
        return 0


def main():
    n, k, m = map(int, input().split())
    print(get_details(n, k, m))


if __name__ == '__main__':
    main()
