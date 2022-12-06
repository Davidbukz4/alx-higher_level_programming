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
    unsigned int i, j = Py_SIZE(p);
	PyObject *item;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < j; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
