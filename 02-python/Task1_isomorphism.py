def is_isomorphic(s,t):
    """
    Проверяет, являются ли строки s и t изоморфными.

    Временная сложность: O(N)
    Пространственная сложность: O(K), где K - количество уникальных символов
    """
    ds = {}
    dt = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in ds:
            if t[i] not in dt:
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
            else:
                return False
        else:
            if ds[s[i]] != t[i]:
                return False
    return True