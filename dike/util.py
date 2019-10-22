"""Utility functions for dike."""

from collections import Counter


def string_iter_to_vocab_counter(slist, sep=None):
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
    if sep is None:
        sep = ' '
    c = Counter()
    for doc in slist:
        c.update(doc.split(sep))
    return c


def corpus_file_to_vocab_counter(fpath, sep=None):
    """Converts a text file corpus to a vocabulary counter.

    Paramters
    ---------
    fpath : str
        The full path to the corpus file.
    sep : str, optional
        The separator used to separate words in the document. Whitespace by
        default.

    Returns
    -------
    collections.Counter
        Word counts in the input corpus.
    """
    with open(fpath, 'rt') as f:
        return string_iter_to_vocab_counter(
            slist=f,
            sep=sep,
        )
