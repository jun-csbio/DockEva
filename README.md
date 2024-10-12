# DockEva
DockEva: a fast open-source tool for atom mapping and docking evaluation of symmetric small molecules

Correctly comparing two poses of symmetric small molecule ligands in fast is of significance important for the development of the fields of receptor-ligand docking and complex structure prediction. DockEva can xxx. In average, its speed is xxxx.

## Pre-requisite:
    - g++

## Installation:
### On Linux system:
* Download this repository at https://github.com/jun-csbio/DockEva.git. Then, uncompress it and run the following command lines on Linux System.

~~~
  $ cd DockEva-main
  $ chmod 755 ./install.sh
  $ ./install.sh
~~~
### On Python environment:
* Download this repository at https://github.com/jun-csbio/DockEva.git. Then, uncompress it and run the following command lines on Linux System.

~~~
  $ cd DockEva-main
  $ python setup.py build_ext --inplace  
  $ pip install .
~~~
## Run example
~~~
  $ ./dockeva example/crystal.mol2 decoy.mol2
~~~

## Release History:

- First release          2023-07-12

## Tips

* <b>This package is free for all users</b>. If you have any question, please email Jun Hu: junh_cs@126.com

## References
[1] Jun Hu, Jiawen Li, Yang Zhang. DockEva: a fast open-source tool for atom mapping and docking evaluation of highly symmetric molecules. sumitted.
