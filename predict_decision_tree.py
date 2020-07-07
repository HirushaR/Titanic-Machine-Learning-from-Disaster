import pandas as pd
import utils
from sklearn import tree

train = pd.read_csv('data/train.csv')
utils.clean_data(train)

target = train["Survived"].values
features_names = ["Pclass","Age","Sex","Fare", "Embarked","SibSp","Parch"]
features = train[features_names].values

decision_tree = tree.DecisionTreeClassifier(random_state=1)
decision_tree = decision_tree.fit(features,target)

print(decision_tree.score(features, target))