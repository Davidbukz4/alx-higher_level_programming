#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python lists
 * @p: is the python list element
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	unsigned int i;
	PyObject *item;
	PyListObject *list;

	list = (PyListObject *)p

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", Py_SIZE(p));
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < Py_SIZE(p); i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
