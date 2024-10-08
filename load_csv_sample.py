
import pandas as pd
from pprint import pprint 

rest_dict = {
    'breakfast_rest': pd.read_csv('taichungeatba/breakfast_rest.csv').dropna(axis=1).groupby('區域'),
    'lunch_rest': pd.read_csv('taichungeatba/lunch_rest.csv').dropna(axis=1).groupby('區域'),
    'dinner_rest': pd.read_csv('taichungeatba/dinner_rest.csv').dropna(axis=1).groupby('區域')
}


def get_group_sample(group):
    group_size = len(group)
    return group.sample(min(group_size, 3))

a = rest_dict['breakfast_rest'].get_group('北區').apply(get_group_sample)
b = rest_dict['lunch_rest'].get_group('北區').apply(get_group_sample)
c = rest_dict['dinner_rest'].get_group('北區').apply(get_group_sample)

for sample in c.values:
    name, opentime, phone, section, address, comment = sample
    # print(name, opentime, phone, section, address, comment)

# 根據group數量去取前幾名的區
group_size = rest_dict['breakfast_rest'].size()
# print(group_size)
print(group_size.sort_values(ascending=False).head(3).index.to_list())