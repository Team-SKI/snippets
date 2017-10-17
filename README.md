#### Code snippets from Team-SKI 
This repository contains code snippets that shall demonstrate the use of RDKit, pandas, and other python libaries for common computer-aided drug design tasks. 

```
├── Cheminformatics
│   └── scaffold-analysis
│
├── Kinase inhibitors
│   └── approved-or-in-clinical-trials
│
├── Presentations and Tutorials
│   ├── Molecular Modelling Workshop 2014
│   └── Protvec demo 2017
│   └── RDKit UGM 2014
│       └── hackaton
│
└── Virtual-Screening
```
These projects were supported by [BioMed X](http://bio.mx/) Innovation Center, Heidelberg 

---
#### Presentations and tutorials
  * **Molecular Modelling Workshop 2014**  
*Scaffold analysis in Python with RDKit and pandas*  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Presentations%20and%20tutorials/Molecular%20Modelling%20Workshop%202014/Scaffold%20analysis%20in%20Python%20with%20RDKit%20and%20pandas%20-%20MMWS%20Erlangen%202014.ipynb)

  * **Protvec demo 2017**  
*Demo of encoding protein sequences via vectors*

  * **RDKit UGM 2014** - [RDKit UGM](https://github.com/rdkit/UGM_2014)  
*Scaffold analysis of ChEMBL data with pandas and RDKit*  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Presentations%20and%20tutorials/RDKit%20UGM%202014/Scaffold%20analysis%20of%20ChEMBL%20data%20with%20pandas%20and%20RDKit%20-%20RDKit%20UGM2014.ipynb)  

    *hackaton contribution*  
Demo of SaveXlsxFromFrame function that can export PandasDataFrame to Excel including images of molecules.  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Presentations%20and%20tutorials/RDKit%20UGM%202014/rdkit_hackaton/XLSX%20export.ipynb) -- Resulting demo xlsx: [download](https://github.com/Team-SKI/snippets/blob/master/IPython/rdkit_hackaton/demo.xlsx)

---
#### Cheminformatics
  * **Scaffold analysis in Python with RDKit and pandas**  
Internal presentation given at BioMed X team meeting, March 2014.  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Cheminformatics/Basics/Scaffold%20analysis%20%26%20Schnellkurs%20in%20chemoinformatics.ipynb)

  * **Markdown usage**  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Cheminformatics/Basics/Markdown%20demo.ipynb)
 
  * **RDKit pandas integration**  
Demo of new functions that were integrated in [RDKit] (https://github.com/rdkit/rdkit/commit/8269bc9002cf3c6b106c847d86bcbabc016b697e), 2013.   
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Cheminformatics/Basics/RDKit%26pandas%20demo%20of%20new%20functions.ipynb)

  * **Rendering of images in IPython**  
Example of how to use object representations.  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Cheminformatics/Basics/Custom%20objects%20and%20their%20rendering%20in%20IPython.ipynb)

---
#### Kinase-Inhibitors
  * **approved or in clinical trials**  
Notebook that extracts all kinase inhibitors that are in clinical trials or are on the market.  
Jupyter notebook: [view](https://github.com/Team-SKI/snippets/blob/master/Kinase%20inhibitors/Kinase%20inhibitors%20-%20approved%20or%20in%20clinical%20trials.ipynb)

---
#### Virtual-Screening
  * **ligand-3D-conformations**  
[prepare_for_docking.py](https://github.com/Team-SKI/snippets/blob/master/Structural%20bioinformatics/prepare_for_docking.py): Script that uses Open Babel to generate 3D structures of compounds.    
For usage info run `prepare_for_docking.py -h`

  * **filtering**  
[filter_pains.py](https://github.com/Team-SKI/snippets/blob/master/Cheminformatics/Screening/filter_pains.py): Script that uses RDKit to remove PAINS compounds from sdf or smile files.  
For usage info run `filter_pains.py -h`
