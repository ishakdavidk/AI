from sklearn.feature_extraction.text import CountVectorizer
import glob
from sklearn.model_selection import train_test_split

paths = glob.glob('./bt.1.0/bt.1.0/docs/*')

files = []
for path in paths:
    f = open(path, "r")
    files.append(f.read())

labels = []
for path in paths:
    if path[-3:-1] == 'is':
        labels.append('Israeli')
    elif path[-3:-1] == 'al':
        labels.append('Palestinian')
    else:
        print('unknown label')

x_train, x_test, y_train, y_test \
    = train_test_split(files, labels, test_size = 0.2, random_state=42)

vec = CountVectorizer(stop_words='english')
x_train_vec = vec.fit_transform(x_train).toarray()
x_test_vec = vec.transform(x_test).toarray()

from sklearn.naive_bayes import MultinomialNB
gnb = MultinomialNB()
y_pred = gnb.fit(x_train_vec, y_train).predict(x_test_vec)

print('Accuracy: ', gnb.score(x_test_vec, y_test))