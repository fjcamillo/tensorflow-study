from sklearn.linear_model import SGDClassifier

x = [[145, 25], [190, 10], [130, 26]]
#Apple, Orange, Apple
#Apple == 1
# Orange == 0
y = [1, 0, 1]

testing_set = [[180,50], [200, 0.5]]
clf = SGDClassifier(loss='hinge')
clf.fit(x, y)
print(clf.predict(testing_set))
