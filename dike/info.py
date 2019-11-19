"""Information mapping for dike."""

# flake8: noqa

import os

from munch import Munch

from .cfg import CFG


class Embedding(Munch):

    @property
    def fname(self):
        return self.name + '.gz'

    @property
    def fpath(self):
        return os.path.join(CFG['datadir'], self.fname)

    @property
    def vocab_fpath(self):
        return os.path.join(CFG['datadir'], self.name + '_vocab.txt')


THOUSAND = 1000
MILLION = 1000 * THOUSAND
BILLION = 1000 * MILLION

word2vec_google_news_300 = Embedding(
    name='word2vec_google_news_300',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/word2vec-google-news-300',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/word2vec-google-news-300/word2vec-google-news-300.gz',
    mbsize=1600,
    dimension=300,
    vocabsize=3000000,
    tokens=100 * BILLION,
    ftype='gensim',
)


glove_twitter_200 = Embedding(
    name='glove_twitter_200',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-200',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-200/glove-twitter-200.gz',
    mbsize=759,
    dimension=200,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_100 = Embedding(
    name='glove_twitter_100',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-100',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-100/glove-twitter-100.gz',
    mbsize=387,
    dimension=100,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_50 = Embedding(
    name='glove_twitter_50',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-50',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-50/glove-twitter-50.gz',
    mbsize=200,
    dimension=50,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_twitter_25 = Embedding(
    name='glove_twitter_25',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-twitter-25',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-twitter-25/glove-twitter-25.gz',
    mbsize=105,
    dimension=25,
    vocabsize=1193514,
    tokens=27 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_300 = Embedding(
    name='glove_wiki_gigaword_300',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-300',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-300/glove-wiki-gigaword-300.gz',
    mbsize=376,
    dimension=300,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_200 = Embedding(
    name='glove_wiki_gigaword_200',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-200',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-200/glove-wiki-gigaword-200.gz',
    mbsize=252,
    dimension=200,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


glove_wiki_gigaword_100 = Embedding(
    name='glove_wiki_gigaword_100',
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/glove-wiki-gigaword-100',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/glove-wiki-gigaword-100/glove-wiki-gigaword-100.gz',
    mbsize=128,
    dimension=100,
    vocabsize=400 * THOUSAND,
    tokens=5.6 * BILLION,
    ftype='gensim',
)


EMBEDDINGS = [
    word2vec_google_news_300,
    glove_twitter_200,
    glove_twitter_100,
    glove_twitter_50,
    glove_twitter_25,
    glove_wiki_gigaword_300,
    glove_wiki_gigaword_200,
    glove_wiki_gigaword_100,
]


for e in EMBEDDINGS:
    setattr(Embedding, e.name, e)
