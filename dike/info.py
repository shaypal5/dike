"""Information mapping for dike."""

# flake8: noqa


class Embedding:
    def __init__(self, **kwds):
        self.__init____dict__.update(kwds)


word2vec_google_news_300 = Embedding(
    link='https://github.com/RaRe-Technologies/gensim-data/releases/tag/word2vec-google-news-300',
    dlink='https://github.com/RaRe-Technologies/gensim-data/releases/download/word2vec-google-news-300/word2vec-google-news-300.gz',
    mbsize=1600,
    dimension=300,
    vocabsize=3000000,
)


EMBEDDINGS = [
    word2vec_google_news_300,
]
