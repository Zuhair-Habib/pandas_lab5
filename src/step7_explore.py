
from src.dataset import make_orders, make_products


# Create DataFrames
orders = make_orders()
products = make_products()


# Display the shapes
print(orders.shape, products.shape)


# Merge orders with products using a left join
m = orders.merge(
    products,
    on="product_id",
    how="left",
    indicator=True
)


# Count matched and unmatched rows
print(m["_merge"].value_counts())


# Display orders whose products are not in the catalogue
print(
    m[m["_merge"] == "left_only"][
        ["order_id", "customer", "product_id"]
    ]
)

# task6


# ===== Step 6: Feature Preparation =====
import pandas as pd

def t6_1_price_zscore(products):
    """Standardize prices using the z-score formula."""
    price = products["price"]
    result = (price - price.mean()) / price.std(ddof=0)
    return result


def t6_2_dummy_columns(products):
    """Create one-hot encoded columns for product categories."""
    result = pd.get_dummies(products["category"], dtype=int)
    return result


def t6_3_feature_matrix(products):
    """Scale numeric features, encode categories, and drop identifiers."""
    df = products.copy()

    # Standardize price
    df["price"] = t6_1_price_zscore(df)

    # Min-max scale stock
    df["stock"] = t6_4_minmax_stock(df)

    # One-hot encode category
    dummies = t6_2_dummy_columns(df)

    # Combine numeric features and encoded categories
    result = pd.concat(
        [df[["price", "stock"]], dummies],
        axis=1
    )

    # Do not include identifier or product-name columns
    return result


def t6_4_minmax_stock(products):
    """Scale stock values into the 0 to 1 range."""
    stock = products["stock"]
    minimum = stock.min()
    maximum = stock.max()

    if maximum == minimum:
        return stock * 0

    return (stock - minimum) / (maximum - minimum)


def t6_5_train_test_sizes(products):
    """Split rows by position into training and testing sets."""
    split_index = int(len(products) * 0.8)

    train = products.iloc[:split_index]
    test = products.iloc[split_index:]

    return (len(train), len(test))

