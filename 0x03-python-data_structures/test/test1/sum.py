import ctypes

_sum = ctypes.CDLL('./sum.so')
_sum.func.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def func(numbers):
    global _sum
    num_numbers = len(numbers)
    array_types = ctypes.c_int * num_numbers
    result = _sum.func(ctypes.c_int(num_numbers), array_types(*numbers))
    return int(result)

print(func([1,2,-3,4,-5,6]))
