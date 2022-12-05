#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup_sum = [0, 0]
    tup = (tuple_a, tuple_b)
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        for x in tup:
            if len(x) == 1:
                tup_sum[0] = tup_sum[0] + x[0]
            elif not len(x):
                tup_sum[0] = tup_sum[0]
                tup_sum[1] = tup_sum[1]
            else:
                tup_sum[0] = tup_sum[0] + x[0]
                tup_sum[1] = tup_sum[1] + x[1]
    elif len(tup[0]) == 2 or len(tup[1] == 2):
        tup_sum[0] = tup_sum[0] + tuple_a[0] + tuple_b[0]
        tup_sum[1] = tup_sum[1] + tuple_a[1] + tuple_b[1]
    elif len(tup[0]) > 2 or len(tup[1] > 2):
        a1, a2, *a3 = tuple_a
        b1, b2, *b3 = tuple_b
        tup_sum[0] = tup_sum[0] + tuple_a[0] + tuple_b[0]
        tup_sum[1] = tup_sum[1] + tuple_a[1] + tuple_b[1]
    return (tup_sum[0], tup_sum[1])
