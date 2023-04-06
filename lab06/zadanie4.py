def group_by_type(lst):
    res = {}
    for el in lst:
        t = type(el).__name__
        if t not in res:
            res[t] = []
        res[t].append(el)
    return res
mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
res = group_by_type(mieszana)
print(res)