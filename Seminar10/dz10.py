# Задача из презентации семинара
'''Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()'''

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# d1 = data.head()

# one hot
human_view = data['whoAmI'].to_list()

print(f"human_view " f"one_hot_human " f"one_hot_robot")

for i in range(len(human_view)):
    lst = []
    lst.append(human_view[i])
    if human_view[i] == 'human':
        lst.append(1)
        lst.append(0)
    else:
        lst.append(0)
        lst.append(1)
    print(f"{lst[0]:>8} {lst[1]:>8} {lst[2]:>12}")