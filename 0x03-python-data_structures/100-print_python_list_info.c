#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - A function that prints information about a
 * Python list
 * @p: The pointer
 */
void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int x = 0;
PyListObject *obj = (PyListObject *)p;
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj->allocated);   
while (x < size)
{
printf("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
x++;
}
}
