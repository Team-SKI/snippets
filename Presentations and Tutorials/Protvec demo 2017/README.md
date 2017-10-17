## Demonstration of biovec (protein sequence embeddings)
* Described by Asgari and Mofrat in [A Continuous Distributed Representation of Biological Sequences](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0141287).  

This folder contains a notebook that shows how to use the [biovec](https://github.com/kyu999/biovec) module to generate vectors from protein sequences and how to use those for clustering and protein family classification (with deep learning).

### Usage:
* Clone the repository with `git clone https://github.com/Team-SKI/snippets.git`
* Change directory to `Presentations and Tutorials/Protvec`
* Dowload biovec submodule with `git submodule init` followed by `git submodule update`
* Run `jupyter notebook`

### Dependencies:
```
pandas
numpy
matplotlib
scikit-learn
gensim
keras (with TensorFlow or Theano)
seaborn
```

##### License and copyright:

Copyright (C) 2017 by Sabrina Jaeger and Samo Turk, BioMed X GmbH

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 License. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, 543 Howard Street, 5th Floor, San Francisco, California, 94105, USA.




