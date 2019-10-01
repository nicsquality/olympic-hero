# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total' : 'Total_Medals'}, inplace = True)
data.head(10)
#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))
better_event = data['Better_Event'].value_counts().index[0]



# --------------
#Code starts here

top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]

top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(df, col):
    country_list = df.nlargest(10, col)
    return country_list

top_10_summer = list(top_ten(top_countries, 'Total_Summer')['Country_Name'])

top_10_winter = list(top_ten(top_countries, 'Total_Winter')['Country_Name'])

top_10 = list(top_ten(top_countries, 'Total_Medals')['Country_Name'])

test_list = [top_10_summer, top_10_winter, top_10] 

common = list(set.intersection(*map(set, test_list))) 


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(x = 'Country_Name', y = 'Total_Summer', kind = 'bar')
winter_df.plot(x = 'Country_Name', y = 'Total_Winter', kind = 'bar')
top_df.plot(x = 'Country_Name', y = 'Total_Medals', kind = 'bar')
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'].iloc[0]
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'].iloc[0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].iloc[0]


# --------------
#Code starts here
data_1 = data.drop(data.tail(1).index)

data_1['Total_Points'] = data_1['Gold_Total'] * 3 +  data_1['Silver_Total'] * 2 +  data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points'] == most_points]['Country_Name'].iloc[0]



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)

plt.show()


