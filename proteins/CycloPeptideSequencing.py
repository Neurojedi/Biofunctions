#!/usr/bin/env python
# coding: utf-8

# In[16]:

# An implementation for branch-and-bound algorithm

from biofunctions.utils.Tables import amino_acid_masses as amino_acid_masses
from biofunctions.proteins.LinearSpectrum import get_LinearSpectrum as LinearSpectrum
from biofunctions.proteins.Cyclospectrum import Cyclospectrum


def expander(peptides,aminoacids):
    peptide_list = []
    for peptide in peptides:
        for amino_acid in aminoacids:
            peptide_list.append(peptide + amino_acid)
    return peptide_list

def get_mass(peptide):
    mass = 0
    for aa in peptide:
        mass += amino_acid_masses[aa]
    return mass

def check(peptide, spectrum):
    ls = LinearSpectrum(peptide)
    for mass in ls:
        if mass not in spectrum:
            return False
    return True


#masses_list = list(set(amino_acid_masses.values()))
aa_list = list(amino_acid_masses.keys())

def CycloPeptideSequencing(spectrum):
    result = []
    candidate_subpeptides = [""]
    parent_mass = max(spectrum)
    while len(candidate_subpeptides):
        candidate_subpeptides = expander(candidate_subpeptides,aa_list)
        for i, peptide in enumerate(candidate_subpeptides):
            if peptide in result:
                continue
            if get_mass(peptide) == parent_mass:
                if Cyclospectrum(peptide) == spectrum:
                    result.append(peptide)
                else:
                    candidate_subpeptides[i] = ""
            elif not check(peptide, spectrum):
                candidate_subpeptides[i] = ""
        candidate_subpeptides = list(filter(lambda x: x != "", candidate_subpeptides))
    return result