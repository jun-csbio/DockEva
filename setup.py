# setup.py  
from setuptools import setup, Extension  
from Cython.Build import cythonize  
  
extensions = [  
    Extension(  
        name="DockEva",  
        sources=["DockEva.pyx", "./code/DockEva.cpp"],  
        language="c++",  
    ),  
]  
  
setup(  
    name="DockEva_package",  
    version="0.1",  
    description="DockEva package with Cython-wrapped C++ code",  
    ext_modules=cythonize(extensions),  
)
