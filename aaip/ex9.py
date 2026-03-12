import pandas as pd

url = "https://raw.githubusercontent.com/ADSLab-Salzburg/DataAnalysiswithPython/main/data/titanic.csv"
df = pd.read_csv(url)

# 1. How many passengers have embarked in Southampton?
num_southampton = df['Embarked'].value_counts().get('S', 0)
print(f"1. Number of passengers who embarked in Southampton: {num_southampton}\n")

# 2. Names of passengers who bought the most expensive ticket
max_fare = df['Fare'].max()
max_fare_passenger = df.loc[df['Fare'] == max_fare, 'Name']
print(f"2. People who bought the most expensive ticket for {max_fare}:")
print(max_fare_passenger.to_string(index=False) + "\n")

# 3. Youngest passengers
min_age = df['Age'].min()
min_age_passenger = df.loc[df['Age'] == min_age, 'Name']
print(f"3. Youngest passenger(s) (age {min_age}):")
print(min_age_passenger.to_string(index=False) + "\n")

# 4. Oldest passengers who died
oldest_dead = df.loc[df['Survived'] == 0, 'Age'].max()
oldest_dead_passenger = df.loc[(df['Age'] == oldest_dead) & (df['Survived'] == 0), 'Name']
print(f"4. Oldest passenger(s) who died (age {oldest_dead}):")
print(oldest_dead_passenger.to_string(index=False))