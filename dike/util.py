"""Utility functions for dike."""

from collections import Counter


def string_iter_to_vocab_counter(slist, sep=' '):
    """Converts an iterable-of-strings corpus to a vocabulary counter.

    Paramters
    ---------
    slist : iterable of str
        The corpus represented as an iterable of strings.
    sep : str, optional
        The separator used to separate words in the document. Whitespace by
        default.

    Returns
    -------
    collections.Counter
        Word counts in the input corpus.
    """
    c = Counter()
    for doc in slist:
        c.update(doc.split(sep))
    return c
