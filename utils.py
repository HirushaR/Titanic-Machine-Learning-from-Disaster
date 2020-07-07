def clean_data(data):
    data['Fare'] = data['Fare'].fillna(data['Fare'].dropna().median())
    data['Age'] = data['Age'].fillna(data['Age'].dropna().median())

    data.loc[['Sex'] == "male", "Sex"] = 0
    data.loc[['Sex'] == "female", "Sex"] = 1

    data["Embarked"] = data['Embarked'].fillna("S")
    data.loc[['Embarked'] == "S", 'Embarked'] = 0
    data.loc[['Embarked'] == "C", 'Embarked'] = 1
    data.loc[['Embarked'] == "Q", 'Embarked'] = 2
