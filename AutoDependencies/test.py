# import pkgutil

# for m in pkgutil.iter_modules():
#     if "numpy" in m:
#         print(m)

import  sys

for m in sys.builtin_module_names:
    print(m)