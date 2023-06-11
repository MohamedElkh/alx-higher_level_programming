#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - function prints some basic info Python lists.
 * @p: the pointer to be connected
 *
 * Return: nothing.
 */

void print_python_list_info(PyObject *p)
{
	PyObject *elem;
	int x, curr;
	int length_of_list;
	length_of_list = Py_SIZE(p);
	curr = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", length_of_list);
	printf("[*] Allocated = %d\n", curr);

	for (x = 0; x < length_of_list; x++)
	{
		printf("Element %d: ", x);
		elem = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(elem)->tp_name);
	}
}
