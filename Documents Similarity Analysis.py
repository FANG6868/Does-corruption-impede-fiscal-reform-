#coding:utf-8
import jieba
from gensim import corpora,models,similarities

doc0 = ''
doc1 = ''
doc2 = ''

doc_test = ''
all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
all_doc.append(doc2)



all_doc_list = []
for doc in all_doc:
  doc_list = [word for word in jieba.cut(doc)]
  all_doc_list.append(doc_list)

doc_test_list = [word for word in jieba.cut(doc_test)]
doc_test_list

dictionary = corpora.Dictionary(all_doc_list)
dictionary.keys()

dictionary.token2id
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]

doc_test_vec = dictionary.doc2bow(doc_test_list)
doc_test_vec

tfidf = models.TfidfModel(corpus)
tfidf[doc_test_vec]

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
sim = index[tfidf[doc_test_vec]]
print(sorted(enumerate(sim), key=lambda item: -item[1]))
