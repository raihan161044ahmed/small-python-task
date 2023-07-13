import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DataSet/titanic.csv')

has_cabin = df[df['Cabin'].notnull()]
no_cabin = df[df['Cabin'].isnull()]

# print("Passengers with a cabin:")
# print(has_cabin['Name'])

# print("Passengers without a cabin:")
# print(no_cabin['Name'])

# Count of passengers with and without a cabin
# count_has_cabin = len(has_cabin)
# count_no_cabin = len(no_cabin)
#print(has_cabin ['Fare'].sort_values(ascending=False))
# print("Count of passengers with a cabin:", count_has_cabin)
# print("Count of passengers without a cabin:", count_no_cabin)

# fil= df[df['Age'] < 30]
# print(fil[['Name', 'Age','Cabin','Fare']])
male=has_cabin[has_cabin['Sex']=='male']
female=has_cabin[has_cabin['Sex']=='female']
male_count=len(male)
female_count=len(female)


# Plot a graph of Fare price for male passengers

plt.plot(male['Fare'], male['PassengerId'])
plt.xlabel('Fare')
plt.ylabel('Male')
plt.title('Fare Price vs Sex for Male Passengers with Cabins')
plt.show()
# Plot a graph of Fare price for female passengers

plt.plot(female['Fare'], female['PassengerId'])
plt.xlabel('Fare')
plt.ylabel('Female')
plt.title('Fare Price vs Sex for FeMale Passengers with Cabins')
plt.show()
