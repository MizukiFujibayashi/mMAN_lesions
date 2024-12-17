# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:08:35 2024

@author: fmizt
"""
import re

sequences = [['song1'],['song2']..]

""" paremeters to be defined in class """

#cleanup_paremters
#cleanup_paremters

""""""

def replace_rep(sequences,uniq_labels):
    """
    re.sub('({})'.format('a')+'{2,}','b','aaggbdurs')
    Out[8]: 'bggbdurs'
    
    re.sub('({})'.format('a1')+'{2,}','b','a1a1ggbdurs') no need
    Out[9]: 'bggbdurs'
    
    s='s1'
    s.upper()
    Out[11]: 'S1'
    
    s='s+'
    s.upper()
    Out[12]: 'S+'
    """
    sequences_ = [''.join(seq) for seq in sequences]
    sequences_replaced = []
    for seq in sequences_:
        for syl in uniq_labels:
            seq = re.replace('{}'.format(syl)+'{2,}',syl.upper(),seq)
        sequences_replaced.append(list(seq))
    return sequences_replaced

def calc_bigram(sequences):
    # prob of all syls to all possible following syl
    """ transition probability from row to col - shold be just frequency
    Row (in forcus)
               a     b     c     d     f    col
           ------------------------------
    a     |  ==.... ==....==....==....==.
    b     | .==.... ==....==....==....==
    c     |..==.... ==....==....==....==
    d     | .==.... ==....==....==....==
    f     | .==.... ==....==....==....==
    """
    return matrix


def calc_trigram(sequences):
     # prob of all syls to all possible following syl and depending on before syl
         """ transition probability from row syl to col-depth sequence - shold be just frequency
              
         Depth
                c/==.... ==....==....==....==.
             b/==.... ==....==....==....==.   
         a / ==.... ==....==....==....==.
               a     b     c     d     f    Col (in forcus)
    Row     ------------------------------
    a     |  ==.... ==....==....==....==.
    b     | .==.... ==....==....==....==
    c     |..==.... ==....==....==....==
    d     | .==.... ==....==....==....==
    f     | .==.... ==....==....==....==
    """
    return matrix

def clean_up_bigram(bigram):
    # cleanup rare transitions 1% ?
    return matrix


def calc_trigram(trigram):
     # cleanup rare transitions 10% ? ref line 66 to 84
     # much more 
    return matrix


def chunk_extraction(sequences):
    
    uniq_labels=list(set([s[0] for s in sequences]))
    
    sequences_preprocessed = replace_rep(sequences, uniq_labels)
    
    bigram = calc_bigram(sequences_preprocessed) 
    bigram_clean = calc_bigram(bigram) #countst
    
    trigram = calc_bigram(sequences_preprocessed)
    trigram_clean = calc_trigram(trigram) # countstg
    
    
     """#chi sq test
     observe if the state of syllable in focus is differenciated by the one preceeding syllable 
     → know if a syllable is in a kind of special contextual state or not
     
     syllable in focus : T
     preceeding syllable of t : P
     
     chi-sq test
                     a     c     d     k     j    syllabels matters (>0.01)
        Row     ------------------------------
        T     |  ==.... ==....==....==....==. Frequency (distrib following T)
                            
                            Depth
                     a     c     d     k     j    syllabels matters (>0.01)
        RowCol   ------------------------------
        PT     |  ==.... ==....==....==....==. Frequency (distrib following PT)
     
     """
    
    
    #keep only the ones with h=1
    
    #relabel
    """
    based on chi-sq test,
    syllables in special context is replaced by T1, T2...
    """
    #some stuff
    
    
    """# see if the replaced syls actually are different WITHIN themselves
    I don't understand 141 to 202?
    zi(focus) is in b
    
    But in my expectation
    chi-sq test
                        a     c     d     k     j    syllabels matters? how were they selected
        RowCol       ------------------------------
        T1 (= P1T)  |  ==.... ==....==....==....==. Frequency (distrib following T1 specified by its preceeding syllable P1)
                                
                                Depth
                        a     c     d     k     j    syllabels matters? how were they selected
        RowCol       ------------------------------
        T2 (= P2T)  |  ==.... ==....==....==....==. Frequency (distrib following T2 specified by its preceeding syllable P2)
    
    no comparison between T and T1,2,3.... I guess
    
    """
    
