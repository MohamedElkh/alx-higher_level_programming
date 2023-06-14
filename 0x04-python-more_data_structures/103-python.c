#include <listobject.h>
#include <bytesobject.h>
#include <Python.h>
#include <object.h>

void print_python_bytes(PyObject *p)
{
	int x;
	char *str_try = NULL;
	long int value;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str_try, &value);
	printf("  size: %li\n", value);
	printf("  trying string: %s\n", str_try);

	if (value < 10)
	{
		printf("  first %li bytes:", value + 1);
	}
	else
	{
		printf("  first 10 bytes:");
	}
	for (x = 0; x <= value && x < 10; x++)
	{
		printf(" %02hhx", str_try[x]);
	}
	printf("\n");
}

void print_python_list(PyObject *p)
{
	int x;
	long int value = PyList_Size(p);
	const char *form;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", value);
	printf("[*] Allocated = %li\n", list->allocated);

	for (x = 0; x < value; x++)
	{
		form = (list->ob_item[x])->ob_type->tp_name;

		printf("Element %i: %s\n", x, form);

		if (!strcmp(form, "bytes"))
		{
			print_python_bytes(list->ob_item[x]);
		}
	}
}
