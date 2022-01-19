import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('cgpa.csv')
# print(data.head(10))
loc = data.columns.get_loc('Result')
data.insert(loc + 1, 'Result_in_point', None)
# print(data.head(5))

ln = len(data)
for i in range(ln):
    if data['Result'].loc[i] == 'A+':
        data['Result_in_point'].loc[i] = 4.00
    elif data['Result'].loc[i] == 'A':
        data['Result_in_point'].loc[i] = 3.75
    elif data['Result'].loc[i] == 'A-':
        data['Result_in_point'].loc[i] = 3.50
    elif data['Result'].loc[i] == 'B+':
        data['Result_in_point'].loc[i] = 3.25
    elif data['Result'].loc[i] == 'B':
        data['Result_in_point'].loc[i] = 3.00
    elif data['Result'].loc[i] == 'B-':
        data['Result_in_point'].loc[i] = 2.75
    elif data['Result'].loc[i] == 'C+':
        data['Result_in_point'].loc[i] = 2.50
    elif data['Result'].loc[i] == 'C':
        data['Result_in_point'].loc[i] = 2.25
    elif data['Result'].loc[i] == 'D':
        data['Result_in_point'].loc[i] = 2.00
    else:
        data['Result_in_point'].loc[i] = 0.0

# print(data[['Result','Result_in_point']])

obtained_credit = 0
total_credit = 0
L1T1, L1T2, L2T1, L2T2, L3T1, L3T2, L4T1, L4T2 = 0, 0, 0, 0, 0, 0, 0, 0
L1T1_TotalCredit, L1T2_TotalCredit, L2T1_TotalCredit, L2T2_TotalCredit, L3T1_TotalCredit, L3T2_TotalCredit, L4T1_TotalCredit, L4T2_TotalCredit = 0, 0, 0, 0, 0, 0, 0, 0

# calculating "obtained_credit" and "total_credit"
for i, j, k in zip(data['Result_in_point'], data['Course Credit'], data['Level-Term']):
    if i != 0:
        obtained_credit = obtained_credit + (i * j)
        total_credit = total_credit + j
    # term wise
    if i != 0 and k == 'Level 1 - Term 1':
        L1T1 = L1T1 + (i * j)
        L1T1_TotalCredit = L1T1_TotalCredit + j
    elif i != 0 and k == 'Level 1 - Term 2':
        L1T2 = L1T2 + (i * j)
        L1T2_TotalCredit = L1T2_TotalCredit + j
    elif i != 0 and k == 'Level 2 - Term 1':
        L2T1 = L2T1 + (i * j)
        L2T1_TotalCredit = L2T1_TotalCredit + j
    elif i != 0 and k == 'Level 2 - Term 2':
        L2T2 = L2T2 + (i * j)
        L2T2_TotalCredit = L2T2_TotalCredit + j
    elif i != 0 and k == 'Level 3 - Term 1':
        L3T1 = L3T1 + (i * j)
        L3T1_TotalCredit = L3T1_TotalCredit + j
    elif i != 0 and k == 'Level 3 - Term 2':
        L3T2 = L3T2 + (i * j)
        L3T2_TotalCredit = L3T2_TotalCredit + j
    elif i != 0 and k == 'Level 4 - Term 1':
        L4T1 = L4T1 + (i * j)
        L4T1_TotalCredit = L4T1_TotalCredit + j
    elif i != 0 and k == 'Level 4 - Term 2':
        L4T2 = L4T2 + (i * j)
        L4T2_TotalCredit = L4T2_TotalCredit + j

# print(obtained_credit, total_credit)
cgpa = obtained_credit / total_credit
print("CGPA:", round(cgpa, 2))

# term wise
L1T1_cgpa = L1T1 / L1T1_TotalCredit
L1T2_cgpa = L1T2 / L1T2_TotalCredit
L2T1_cgpa = L2T1 / L2T1_TotalCredit
L2T2_cgpa = L2T2 / L2T2_TotalCredit
L3T1_cgpa = L3T1 / L3T1_TotalCredit
# L3T2_cgpa = L3T2 / L3T2_TotalCredit
# L4T1_cgpa = L4T1 / L4T1_TotalCredit
# L4T2_cgpa = L4T2 / L4T2_TotalCredit

### --------------------------Visualization----------------------------------
# -->term-wise result<--
term_result = {'L1T1': L1T1_cgpa, 'L1T2': L1T1_cgpa, 'L2T1': L2T1_cgpa, 'L2T2': L2T2_cgpa, 'L3T1': L3T1_cgpa}
# print(term_result)
# line plot
sns.lineplot(term_result.keys(), term_result.values())
plt.title('Term-wise CGPA')
plt.show()
# bar plot
# plt.bar(term_result.keys(),term_result.values())
# plt.show()

# -->comparing among obtained grades<--
grade_counts = data['Result'].value_counts()
# pie chart
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title("Ratio of different grades")
plt.show()
# bar plot
# sns.barplot(grade_counts.index, grade_counts.values)
# plt.show()

# -->result in different courses<--
sns.swarmplot(data=data, x=data['Course Code'], y=data['Result'], )
plt.xticks(rotation=90)
plt.show()
