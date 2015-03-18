## Document Scoring and Evaluation using TF-IDF


TF-IDF: tf–idf, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in information retrieval and text mining. The tf-idf value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general.

Variations of the tf–idf weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query. tf–idf can be successfully used for stop-words filtering in various subject fields including text summarization and classification. (http://en.wikipedia.org/wiki/Tf%E2%80%93idf)



------------------------------------------------------


tfidf.py performs leave-one-out cross validation on the computed tf-idf vectors of each document. The comparison is done by calculating the cosine of the angle of vectors between the two documents. It does not match all good documents with good and bad with bad i.e. the classification is not entirely correct. This is because tfidf does not take into account any sort of context of the words or combinations of words, it just compares values of tfidf per word per document. The accuracy might improve by implementing WEIGHTED tfidf with the cosine method.
Metric for tfidfmetric.py:

		Number of documents with correct classifications / Total number of documents

Stemmer.py: A stemmer basically matches different forms of a word i.e likes, liked and liking become like, otherwise they would be 3 different words with different tfidf values. This should decrease noise by reducing the total number of distinct elements which are not truly distinct. The stemmer tested poorly with all documents, but its accuracy increased with decreasing number of documents.

Stemmer Evaluation: It worked well and showed improvements with a small number of documents, but as the total number of documents increased, the accuracy decreased, to the point where it was lower than that from the cosine method. I think it is so because, since a stemmer reduces words to their  root, any sort of context is lost. Though we were not matching based on context, the form of the word itself is an indicator of context.

Assessment of tfidf vs stemmer: Tfidf uses a basic tfidf input to a cosine function which calculates the ‘distance’ between the 2 documents by measuring the angle between them in a vector space. Stemmer is better because, though it uses the same technique, the tfidf function gets a cleaner more stripped down input, which should ideally improve accuracy.

Appendix A: Output for tfidfmetric.py

filename,  match,  cosine
bad/bad03.txt ,  good/good02.txt ,  0.217397767126
bad/bad01.txt ,  bad/bad08.txt ,  0.0508196797044
good/good08.txt ,  bad/bad07.txt ,  0.103574391881
bad/bad04.txt ,  bad/bad06.txt ,  0.0494963642645
good/good06.txt ,  bad/bad04.txt ,  0.0441460154874
bad/bad02.txt ,  bad/bad06.txt ,  0.0758642113122
bad/bad05.txt ,  bad/bad03.txt ,  0.0551295103495
good/good01.txt ,  bad/bad08.txt ,  0.0463359148237
good/good03.txt ,  good/good02.txt ,  0.036329864994
good/good04.txt ,  bad/bad06.txt ,  0.0370217425463
bad/bad08.txt ,  bad/bad06.txt ,  0.110651442251
bad/bad07.txt ,  good/good08.txt ,  0.103574391881
bad/bad06.txt ,  bad/bad08.txt ,  0.110651442251
good/good07.txt ,  good/good08.txt ,  0.0853077709574
good/good05.txt ,  good/good01.txt ,  0.0374741642762
good/good02.txt ,  bad/bad03.txt ,  0.217397767126
overall:  56.25 %

Appendix B: Output for stemmer.py

bad/bad03.txt ,  good/good02.txt ,  0.168819293235
bad/bad01.txt ,  bad/bad07.txt ,  0.062375168205
good/good08.txt ,  bad/bad07.txt ,  0.0967420300058
bad/bad04.txt ,  good/good07.txt ,  0.05722698765
good/good06.txt ,  good/good03.txt ,  0.0569749220111
bad/bad02.txt ,  bad/bad06.txt ,  0.0798653320783
bad/bad05.txt ,  bad/bad06.txt ,  0.0500224128533
good/good01.txt ,  bad/bad08.txt ,  0.0436201813468
good/good03.txt ,  good/good06.txt ,  0.0569749220111
good/good04.txt ,  bad/bad06.txt ,  0.0466007936509
bad/bad08.txt ,  bad/bad06.txt ,  0.13215257623
bad/bad07.txt ,  good/good08.txt ,  0.0967420300058
bad/bad06.txt ,  bad/bad08.txt ,  0.13215257623
good/good07.txt ,  bad/bad07.txt ,  0.085043193622
good/good05.txt ,  bad/bad01.txt ,  0.0366712751907
good/good02.txt ,  bad/bad03.txt ,  0.168819293235
overall:  43.75 %


