#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python lists
 * @p: is the python list element
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i = 0, j = Py_SIZE(p);
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", j);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < j; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
