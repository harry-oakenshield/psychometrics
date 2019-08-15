import pandas as pd
from scipy.stats import pearsonr
from pandas import ExcelWriter

pd.set_option('display.max_columns',None)
data=pd.read_csv('answers.csv')
print(data.head(5))
print(f'data.shape: {data.shape}')

# Get list of column headers
questions=[]
for i in range(18,107):
    questions.append(list(data)[i])
print(questions)

outputs=[]
for j in range(107,114):
    outputs.append(list(data)[j])
print(outputs)


# Example: finding Pearson's coefficient between an input question and an output
# coef_,_=pearsonr(data.iloc[:,18],data.iloc[:,107])
# print(coef_)

df=pd.DataFrame()

for j in range(107,114):
    q=[]
    for i in range(18,107):
        coef_,_=pearsonr(data.iloc[:,i],data.iloc[:,j])
        q.append(coef_)
    df[f'R{j-106}']=q


max_coef=df.idxmax(axis=1)
# print(max_coef)
df.insert(7,'Max Coef_',max_coef,True)

q=[]
for i in range(18,107):
    q.append(f'Q{i-17}')
df.insert(0,'Question',q,True)

print(df)

df2=pd.DataFrame()
df2['Question #']=df['Question']
df2['Linked Output #']=df['Max Coef_']

question_dict={f'Q{i+1}':questions[i] for i in range(89)}
# print(question_dict)
q_content=[]
for i in df['Question']:
    q_content.append(question_dict[i])

df2['Question Content']=q_content

output_dict={f'R{j+1}':outputs[j] for j in range(7)}
o_content=[]
for j in df['Max Coef_']:
    o_content.append(output_dict[j])

df2['Output']=o_content

print(df2)

writer=ExcelWriter('Input_Output Pairs.xlsx')
df.to_excel(writer,sheet_name='Pearson coefficients')
df2.to_excel(writer,sheet_name='I-O Pairs')
writer.save()
