# DockEva (https://zhanglab.comp.nus.edu.sg/DockEva/)
DockEva: a fast open-source tool for atom mapping and docking evaluation of symmetric small molecules

Correctly comparing two poses of small molecule ligands with symmetry in fast is of significance important for the development of the related fields of receptor-ligand docking. Most of existing tools that correct for molecular symmetry do not consider the bonding structure of molecules, therefore resulting in non-physical atomic mapping. Using exhaustive algorithm to directly solve high sym-metry atom mapping problem is time-consuming. We present DockEva, a fast method for docking pose evaluation that converts the symmetry atom mapping problem to multiple maximum clique problems using the shortest road algorithm, in which the optimal atomic mapping and docking pose evaluation are performed in fast by solving the multiple maximum clique problems. Benchmarked results on decoys generated by AutoDock Vina demonstrate that DockEva can efficiently achieve the symmetry-corrected atom mapping with the minimum root mean square deviation (RMSD). Compared DockRMSD, one of the best existing methods for calculating RMSD of symmetric molecules, the average computational efficiency of DockEva (4.78×10<sup>-3</sup> seconds) is improved by about 6.36×10<sup>2</sup> times on the highly symmetric small molecules (their reasonable atom mapping numbers are all larger than 100) with more robust.

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

- First release          2024-10-14

## Tips

* <b>This package is free for all users</b>. If you have any question, please email Jun Hu: junh_cs@126.com

## References
[1] Jun Hu, Jiawen Li, Yang Zhang. DockEva: a fast open-source tool for atom mapping and docking evaluation of highly symmetric molecules. sumitted.
