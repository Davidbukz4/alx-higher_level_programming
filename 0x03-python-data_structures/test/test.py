import ctypes

lib = ctypes.CDLL("./mylib.so")
lib.print_list.argtypes = [ctypes.py_object]

l = ['element1', 'element2', 'element3']
lib.print_list(l)

del l[1]
lib.print_list(l)
