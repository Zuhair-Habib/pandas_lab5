
from src.dataset import make_df


df = make_df()


# Select specific columns and display the first 2 rows
print(df[["name", "salary"]].head(2))


# Select the city at row index 1
print(df.loc[1, "city"])


# Select the first 2 rows and first 2 columns
print(df.iloc[0:2, 0:2])


# Filter rows where salary > 50 and city is Karachi
print(df[(df.salary > 50) & (df.city == "Karachi")])


# Sort by salary in descending order
top = df.sort_values("salary", ascending=False)
print(top[["name", "salary"]].head(3))


# Sort by city and then by age
by = df.sort_values(["city", "age"])
print(by[["city", "age"]])
