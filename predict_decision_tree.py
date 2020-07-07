import pandas as pd
import utils
from sklearn import tree, model_selection

train = pd.read_csv('data/train.csv')
utils.clean_data(train)

target = train["Survived"].values
features_names = ["Pclass","Age","Sex","Fare", "Embarked","SibSp","Parch"]
features = train[features_names].values

decision_tree = tree.DecisionTreeClassifier(random_state=1)
decision_tree = decision_tree.fit(features,target)

print(decision_tree.score(features, target))

score = model_selection.cross_val_score(decision_tree, features, target, scoring='accuracy', cv=50)
print(score)
print(score.mean())
print("=====================")
generalize_tree = tree.DecisionTreeClassifier(
    random_state=1,
    max_depth=7,
    min_samples_split=2,
)
generalize_tree = generalize_tree.fit(features,target)

print(generalize_tree.score(features, target))

score = model_selection.cross_val_score(generalize_tree, features, target, scoring='accuracy', cv=50)
print(score)
print(score.mean())