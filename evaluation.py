"""
Functions for evaluating correlations between scores and human ratings.
"""

from scipy.stats import spearmanr, kendalltau

def spearman_corr(x, y):
    """
    Returns Spearman's rank correlation coefficient and p-value.
    """
    return spearmanr(x, y)

def kendall_corr(x, y):
    """
    Returns Kendall's tau correlation coefficient and p-value.
    """
    return kendalltau(x, y)