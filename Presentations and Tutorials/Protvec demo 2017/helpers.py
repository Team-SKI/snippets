import matplotlib.pyplot as plt
import numpy as np

"""
Copyright (C) 2017 by Samo Turk and Sabrina Jaeger, BioMed X GmbH
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 License. 
To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/ or send a letter 
to Creative Commons, 543 Howard Street, 5th Floor, San Francisco, California, 94105, USA.
"""

class nGram:
    """Class for storing n-grams with useful default depiction in jupyter.
    >>>nGram(split_ngrams('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ',3))"""
    
    def __init__(self, n_gram):
        self.n_gram = n_gram
    def __len___(self):
        return len(self.n_gram)
    def __str__(self): # Stringe representation
        return 'n-gram with %i sentences' %len(self.n_gram)
    __repr__ = __str__ # Default representation
    def __contains__(self, word): # Contains method enable usage of "'Word' in nGram"
        if word in [item for sublist in self.n_gram for item in sublist]:
            return True
        else:
            return False
    contains = __contains__ # nGram.contains('word')
    def __iter__(self): # Iterate over sentences (for sentence in nGram:...)
        for x in self.n_gram:
            yield x
    def _repr_html_(self): # default jupyter representation
        colors = ['Red','Maroon','Yellow','Olive','Lime','Green','Aqua','Teal','Blue','Navy','Fuchsia','Purple']
        html = "<samp><b>"
        for i,ng in enumerate(self.n_gram):
            ng_2 = ''
            for n,c in zip(ng, colors[:len(ng)]): # depicts only as many as we have colors
                ng_2 += '<span style="color: %s">' %c
                ng_2 += n
                ng_2 += '</span>'
            html += " "*i + ng_2
            if len(ng) > len(colors): # append ... if we run out of colors
                html += "..."
            html += "\n"
        html += "</b></samp>"
        return html

class DfVec:
    """
    Helper class to store vectors in a pandas DataFrame
    
    Parameters  
    ---------- 
    vec: np.array
    """
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        return "%d dimensional vector" % len(self.vec)
    def __repr__(self):
        return "%d dimensional vector" % len(self.vec)
    def __len__(self):
        return len(self.vec)

def confusion_matrix_plot(cm, names, title='Confusion matrix', cmap=plt.cm.Blues):
    """Creates confusion matrix plot from confusion_matrix(observations, predictions).
    You can calculate confusion matrix with help of ``sklearn.metrics.confusion_matrix``
    
    Parameters
    ----------
    cm : np.array
        Confusion matrix
    names : list
        Names of classes
    title : str
        Title of the plot
    cmap : plt.cm
        Matplotlib colormap

    Returns
    -------    
    plt.figure
        matplotlib figure
    """
    fig = plt.figure()
    axes = fig.add_axes([0, 0, 1, 1])
    im = axes.imshow(cm, interpolation='nearest', cmap=cmap)
    fig.colorbar(im)
    tick_marks = np.arange(len(names))
    plt.xticks(tick_marks, names, rotation=45)
    plt.yticks(tick_marks, names,)
    axes.set_ylabel('True value')
    axes.set_xlabel('Predicted value')
    axes.set_title(title)
    return fig
