#!/usr/bin/python3

def test_var_args(f_arg, *argv, **kwargs):
    print('First normal arg: ' + str(f_arg))
    for arg in argv:
        print('Other args: ' + str(arg))
    print(kwargs)

test_var_args('one', 2, 'three', 4, 5, 'six', seven=7)


print('\nKwarg test')
def test_kwargs(*argv, **kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)
    print(argv)

test_kwargs('str', name='david', age=33, school='alx', course='SE')
