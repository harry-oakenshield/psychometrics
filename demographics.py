import pandas as pd
from matplotlib import pyplot as plt
from pandas import ExcelWriter

# plt.style.use('fivethirtyeight')

pd.set_option('display.max_columns',None)
data=pd.read_csv('answers.csv')
print(data.head(5))
print(f'data.shape: {data.shape}')

# Get list of column headers
print(list(data))
# 'ID', 'Email', 'First Name', 'Last Name', 'Role', 'Industry', 'Country', 'Project_Budget', 'Project_Duration', 'Experience', 'Gender', 'Age'

'''DEMOGRAPHICS'''

'''BY Role'''
# Summarise by Role
Role=data.Role.value_counts().reset_index().rename(columns={'index': 'Role', 'Role': 'Count'})
# Calculate % of each Role
Role['Percentage']=['{:.1%}'.format(Role['Count'][i]/4416) for i in range(len(Role['Count']))]
# plt.barh(Role['Role'][::-1],Role['Count'][::-1])

print(Role)

'''BY Industry'''
Industry=data.Industry.value_counts().reset_index().rename(columns={'index': 'Industry', 'Industry': 'Count'})
Industry['Percentage']=['{:.1%}'.format(Industry['Count'][i]/4416) for i in range(len(Industry['Count']))]
# plt.barh(Industry['Industry'][::-1],Industry['Count'][::-1])
print(Industry)

'''BY Country'''
Country=data.Country.value_counts().reset_index().rename(columns={'index': 'Country', 'Country': 'Count'})
Country['Percentage']=['{:.1%}'.format(Country['Count'][i]/4416) for i in range(len(Country['Count']))]
Country.sort_values(by='Count',ascending=False)
plt.barh(Country['Country'][0:5][::-1],Country['Percentage'][0:5][::-1])
plt.title('By Country')
print(Country)

'''BY Project_Budget'''
Project_Budget=data.Project_Budget.value_counts().reset_index().rename(columns={'index': 'Project_Budget', 'Project_Budget': 'Count'})
Project_Budget['Percentage']=['{:.1%}'.format(Project_Budget['Count'][i]/4416) for i in range(len(Project_Budget['Count']))]
# plt.barh(Project_Budget['Project_Budget'][::-1],Project_Budget['Count'][::-1])
# plt.pie(Project_Budget['Count'],labels=Project_Budget['Project_Budget'],
#         wedgeprops={'edgecolor':'black'},shadow=True,
#         explode=[0.1,0,0,0,0,0,0],autopct='%1.1f%%')
# plt.title('Project Budget (GBP)')
print(Project_Budget)

'''BY Project_Duration'''
Project_Duration=data.Project_Duration.value_counts().reset_index().rename(columns={'index': 'Project_Duration', 'Project_Duration': 'Count'})
Project_Duration['Percentage']=['{:.1%}'.format(Project_Duration['Count'][i]/4416) for i in range(len(Project_Duration['Count']))]
# plt.barh(Project_Duration['Project_Duration'][::-1],Project_Duration['Count'][::-1])
# plt.pie(Project_Duration['Count'],
#         # labels=Project_Duration['Project_Duration'],
#         wedgeprops={'edgecolor':'black'},shadow=True,
#         explode=[0.1,0,0,0,0],autopct='%1.1f%%')
# plt.title('Project Duration (months)')
# plt.legend(Project_Duration['Project_Duration'],loc='bottom center',ncol=5)
print(Project_Duration)

'''BY Experience'''
Experience=data.Experience.value_counts().reset_index().rename(columns={'index': 'Experience', 'Experience': 'Count'})
Experience['Percentage']=['{:.1%}'.format(Experience['Count'][i]/4416) for i in range(len(Experience['Count']))]
# plt.barh(Experience['Experience'][::-1],Experience['Count'][::-1])
# plt.pie(Experience['Count'],labels=Experience['Experience'],
#         wedgeprops={'edgecolor':'black'},shadow=True,
#         explode=[0.1,0,0,0,0,0],autopct='%1.1f%%')
# plt.title('Experience (years)')
print(Experience)

'''BY Gender'''
Gender=data.Gender.value_counts().reset_index().rename(columns={'index': 'Gender', 'Gender': 'Count'})
Gender['Percentage']=['{:.1%}'.format(Gender['Count'][i]/4416) for i in range(len(Gender['Count']))]
# plt.barh(Gender['Gender'][::-1],Gender['Count'][::-1])
# plt.pie(Gender['Count'],labels=Gender['Gender'],
#         wedgeprops={'edgecolor':'black'},shadow=True,
#         explode=[0.1,0],autopct='%1.1f%%')
# plt.title('Gender')
print(Gender)

'''BY Age'''
Age=data.Age.value_counts().reset_index().rename(columns={'index': 'Age', 'Age': 'Count'})
Age['Percentage']=['{:.1%}'.format(Age['Count'][i]/4416) for i in range(len(Age['Count']))]
# plt.barh(Age['Age'][::-1],Age['Count'][::-1])
# plt.pie(Age['Count'],labels=Age['Age'],
#         wedgeprops={'edgecolor':'black'},shadow=True,
#         explode=[0.1,0,0,0],autopct='%1.1f%%')
# plt.title('Age (years)')
print(Age)

# plotting the charts
plt.tight_layout()
plt.show()
plt.savefig('Role.png')

'''Export to Excel'''
writer=ExcelWriter('PythonExport.xlsx')
Country.to_excel(writer,sheet_name='Country')
Industry.to_excel(writer,sheet_name='Industry')
Project_Budget.to_excel(writer,sheet_name='Project_Budget')
Project_Duration.to_excel(writer,sheet_name='Project_Duration')
Experience.to_excel(writer,sheet_name='Experience')
Gender.to_excel(writer,sheet_name='Gender')
Age.to_excel(writer,sheet_name='Age')
writer.save()
