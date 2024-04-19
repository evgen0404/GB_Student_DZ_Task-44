import random
import pandas as pd
import seaborn as sps

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


def robot(x):
    if x == 'robot':
        return 1
    else:
        return 0
    
def human(x):
    if x == 'human':
        return 1
    else:
        return 0
    
data['is_robot'] = data['whoAmI'].apply(robot)
data['is_human'] = data['whoAmI'].apply(human)

data = data.drop('whoAmI', axis=1)

print(data.head())