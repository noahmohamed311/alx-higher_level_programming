#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
f = 3.14
lib.print_python_float(f);
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l);
lib.print_python_float(l);
lib.print_python_list(f);
julien@ubuntu:~/CPython$ ./103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: ??
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello

