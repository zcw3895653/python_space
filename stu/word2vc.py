#coding=utf-8
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = gensim.models.word2vec.Text8Corpus(u"D:\\zcw\\answer\\C36-Medical")
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)

try:
    y1 = model.similarity(u"国家", u"国务院")
except KeyError:
    y1 = 0
print u"【国家】和【国务院】的相似度为：", y1
print"-----\n"