# DockEva
DockEva: a fast open-source tool for atom mapping and docking evaluation of highly symmetric molecules

Identifying the ATP-binding sites of proteins is fundamentally important to uncover the mechanisms of protein functions and explore drug discovery. Many computational methods are proposed to predict ATP-binding sites. However, due to the limitation of the quality of feature representation, the prediction performance still has a big room for improvements. In this study, we propose an end-to-end deep learning model, E2EATP, to dig out more discriminative information from protein sequence for improving the ATP-binding site prediction performance. Concretely, we employ a pre-trained deep learning-based protein language model (ESM2) to automatically extract high-latent discriminative representations of protein sequences relevant for protein functions. Based on ESM2, we design a residual convolutional neural network to learn protein-ATP binding site prediction model. Furthermore, a weighted focal loss function is used to reduce the negative impact of imbalanced data on the model training stage. Experimental results on the independent testing data set demonstrate that E2EATP could achieve a Matthew’s correlation coefficient value of 0.668 and the AUC score of 0.914, which are higher than that of most existing state-of-the-art prediction methods. <b>The speed (about 0.05 second per protein) of E2EATP is much faster than the other existing prediction method. We have predicted all 207,892 human proteins in UniProt (up to 2023-07-10)</b>. 

## Pre-requisite:
    - g++

## Installation:

* Download this repository at https://github.com/jun-csbio/dockeva.git. Then, uncompress it and run the following command lines on Linux System.

~~~
  $ cd dockeva-main
  $ chmod 755 ./install.sh
  $ ./install.sh
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
