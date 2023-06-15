#include <Python.h>
/**
 * print_python_bytes - func to Prints basic info about Python byte objects.
 * @p: pointer PyObject byte object.
 *
 * Return: nothing.
 */

void print_python_bytes(PyObject *p)
{
	unsigned int x;
	unsigned int value;
	PyBytesObject *byte = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", byte->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		value = 10;
	}
	else
	{
		value = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %d bytes: ", value);

	for (x = 0; x < value; x++)
	{
		printf("%02hhx", bytes->ob_sval[x]);

		if (x == (value - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}

/**
 * print_python_list - func to prints basic info about Python lists.
 * @p: pointer PyObject list object.
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	const char *kind;
	int value, x, loc;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;

	value = var->ob_size;
	loc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", value);
	printf("[*] Allocated = %d\n", loc);

	for (x = 0; x < value; x++)
	{
		kind = list->ob_item[x]->ob_type->tp_name;
		printf("Element %d: %s\n", x, kind);

		if (strcmp(kind, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[x]);
		}
	}


}
