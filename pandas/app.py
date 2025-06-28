import pandas as pd

# pip install pandas


df = pd.read_csv('/Users/siddharthsharma/Desktop/dataset.csv')

# df.to_excel('/Users/siddharthsharma/Desktop/dataset.xlsx', index=False)
# df -> DataFrame (Varaible)

print(df)

# cols:
'''
Name Age Dept Salary
'''
# average salary
avg_salary = df['Salary'].mean()
print(f"\n Average Salary: ₹{avg_salary}")

# f -> format 

# add a new colms
df['Experience'] = ['Junior', 'Mid', 'Senior', 'Mid']
print("\nAdded Experience Column:")
print(df)

#filter IT Department
it_employees = df[df['Department'] == 'IT']
print("\n IT Employees:")
print(it_employees)

#filter by Name Alice
alice_df = df[df['Name'] == 'Alice']
print(" Rows where Name is Alice:")
print(alice_df)


#Filter by age 25
age_25_df = df[df['Age'] == 25]
print("\n Rows where Age is 25:")

