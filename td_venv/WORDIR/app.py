#app.py

from sklearn.externals import joblib

clf = joblib.load('model.pkl')

def predict(a):
        predicted = clf.predict(a)    # predicted is 1x1 numpy array
        return int(predicted[0])
