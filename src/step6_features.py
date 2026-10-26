
import pandas as pd
from src.dataset import make_df


# Remove duplicate rows and create a copy
f = make_df().drop_duplicates().copy()


# Fill missing ages with the median
f["age"] = f["age"].fillna(f["age"].median())


# Calculate the salary z-score
f["salary_z"] = (
    (f["salary"] - f["salary"].mean())
    / f["salary"].std()
)


# Convert city values into dummy columns
f = pd.get_dummies(
    f,
    columns=["city"],
    prefix="c",
    dtype=int
)


# Create the feature DataFrame
X = f.drop(columns=["name", "salary"]).round(2)


# Display the results
print(X.shape)
print(X.head(3))


# Save features to CSV
X.to_csv("results/features.csv", index=False)
