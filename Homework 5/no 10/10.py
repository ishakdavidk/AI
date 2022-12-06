import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

train_df = pd.read_csv('train.tsv', sep='\t')
x_train, y_train = train_df['Phrase'], train_df['Sentiment']
test_df = pd.read_csv('test.tsv', sep='\t')
label = pd.read_csv('sampleSubmission.csv')
x_test, y_test = test_df['Phrase'], label['Sentiment']

vec = CountVectorizer(stop_words='english')
x_train_vec = vec.fit_transform(x_train).toarray()
x_test_vec = vec.transform(x_test).toarray()

from sklearn.naive_bayes import MultinomialNB
gnb = MultinomialNB()
y_pred = gnb.fit(x_train_vec, y_train).predict(x_test_vec)

print("Number of mislabeled points out of a total %d points : %d" % (x_test.shape[0], (y_test != y_pred).sum()))
print('Accuracy: ', gnb.score(x_test_vec, y_test))

