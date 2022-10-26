#!/usr/bin/env python
# coding: utf-8

# In[16]:


from biofunctions.proteins.LinearPeptideScoring import LinearPeptideScoring
from biofunctions.proteins.CyclopeptideScoring import CyclopeptideScoring
from biofunctions.utils.Tables import amino_acid_masses as amino_acid_masses
from collections import defaultdict


def expander(leaderboard, masses):
    leaderboards = []
    for peptide in leaderboard:
        for mass in masses:
            new_peptide = peptide + [mass]
            leaderboards.append(new_peptide)
    return leaderboards

def get_trim(lb, spectrum, n):
    result_board = []
    peptide_scores = defaultdict(list)
    leaderboard = list(filter(lambda x: x != '', lb))
    if n >= len(leaderboard):
        return leaderboard
    for mass in leaderboard:
        peptide_scores[LinearPeptideScoring(spectrum, mass)].append(mass)
    sorted_keys = sorted(peptide_scores.keys())
    i = 0
    len_keys=len(sorted_keys)
    placer = len_keys - 1
    while i < n:
        key = sorted_keys[placer]
        result_board += peptide_scores[key]
        i+= len(peptide_scores[key])
        placer-=1
    return result_board

def LeaderboardCyclopeptideSequencing(spectrum, masses, n):
    leaderboard = [[]]
    lp = ''
    lp_score = 0
    parent_mass = max(spectrum)
    while len(leaderboard):
        leaderboard = expander(leaderboard, masses)
        for i, j in enumerate(leaderboard):
            peptide_mass = sum(j)
            if peptide_mass == parent_mass:
                peptide_score = CyclopeptideScoring(spectrum, j)
                if peptide_score > lp_score:
                    lp = j
                    lp_score = peptide_score
            elif peptide_mass > parent_mass:
                leaderboard[i] = ""
        leaderboard = get_trim(leaderboard, spectrum, n)
    print('Leader peptide score:', lp_score)
    return lp

def LeaderboardCyclopeptideSequencing_Long(spectrum, masses, n):
    leaderboard = [[]]
    lp = defaultdict(list)
    lp_score = 0
    parent_mass = max(spectrum)
    while len(leaderboard):
        leaderboard = expander(leaderboard, masses)
        for i, j in enumerate(leaderboard):
            peptide_mass = sum(j)
            if peptide_mass == parent_mass:
                peptide_score = CyclopeptideScoring(spectrum, j)
                if peptide_score >= lp_score:
                    lp[peptide_score].append(j)
                    lp_score = peptide_score
            elif peptide_mass > parent_mass:
                leaderboard[i] = ""
        leaderboard = get_trim(leaderboard, spectrum, n)
    print('Leader peptide score:', lp_score)
    return lp