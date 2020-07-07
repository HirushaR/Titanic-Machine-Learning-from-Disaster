import pandas as pd
import utils
from sklearn import linear_model

train = pd.read_csv('data/train.csv')
utils.clean_data(train)

target = train["Survived"].values
features = train[["Pclass","Age","Sex","Fare", "Embarked","SibSp","Parch"]].values

classifier = linear_model.LogisticRegression()
classifier_ = classifier.fit(features, target)

print(classifier_.score(features,target))