#include <Python.h>
#include <stdio.h>
void print_python_list_info(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;
    PyListObject *list = (PyListObject *)p;

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
