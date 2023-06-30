#include "Python.h"

/**
 * print_python_string - function to be used
 * @p: pointer to be used
 *
 * Return: nothing
 */

void print_python_string(PyObject *p)
{

	long int le;

	fflush(stdout);

	printf("[.] string object info\n");

	if (strcmp(p->ob_typr->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");

		return;
	}

	le = ((PyASCIIObject *)(p))->le;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	printf("  length: %ld\n", le);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &le));
}
