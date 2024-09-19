import pandas as pd
import matplotlib.pyplot as plt
#from ydata_profiling import ProfileReport
df = pd.read_json('FBI_CrimeData_2016.json')
print (df)

print('_' * 40)
# profile = ProfileReport(df, title='FBI Crime Data 2016', explorative=True)
# profile.to_file('FBI_CrimeData_2016.html')

murdrer_fre_by_regions = df.groupby('Region')['Murder'].sum().reset_index()
print('murder frequency according to each region \n' , murdrer_fre_by_regions)

print('_' * 40)

# Assuming your DataFrame 'df' contains columns for Assault, Murder, Robbery, and Rape
violent_crime_by_regions = df.groupby('Region')[['Assault', 'Murder', 'Robbery', 'Rape']].sum().reset_index()
violent_crime_by_regions['Total_Violent_Crime'] = violent_crime_by_regions[['Assault', 'Murder', 'Robbery', 'Rape']].sum(axis=1)

# Display the result
print('total violent crime by regions \n' , violent_crime_by_regions)
print ('_' * 40)

nonviolent_crime_by_regions = df.groupby('Region')[['Burglary', 'Theft' , 'Vehicle_Theft']].sum().reset_index()
nonviolent_crime_by_regions['Total_Nonviolent_Crime'] = nonviolent_crime_by_regions[['Burglary', 'Theft', 'Vehicle_Theft']].sum(axis=1)
print('total nonviolent crime frequency by regions \n ' , nonviolent_crime_by_regions)
print('_' * 40)


plt.figure(figsize = (10,6))
plt.bar(murdrer_fre_by_regions['Region'],murdrer_fre_by_regions['Murder'])
plt.title('Murder Rate by Region')
plt.xlabel('Region')
plt.ylabel('Murder Rate')
plt.show()

plt.figure(figsize = (10 , 6))
plt.bar(violent_crime_by_regions['Region'] , violent_crime_by_regions['Total_Violent_Crime'])
plt.title('Total_Violent_Crime rate by region')
plt.xlabel('Region')
plt.ylabel('Total_Violent_Crime Rate')
plt.show()


