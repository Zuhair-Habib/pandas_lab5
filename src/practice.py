
import pandas as pd


# ===== Step 1: Series and DataFrames =====

def t1_1_weather_series(df):
    """Return temp_c as a Series indexed by day names."""
    raise NotImplementedError


def t1_2_hottest_day(df):
    """Return the name of the day with the highest temperature."""
    raise NotImplementedError


def t1_3_build_frame():
    """Build and return a DataFrame containing item and price."""
    raise NotImplementedError


def t1_4_series_vs_frame(df):
    """Return the type names of df['temp_c'] and df[['temp_c']]."""
    raise NotImplementedError


# ===== Step 2: Reading and writing files =====

def t2_1_csv_roundtrip(df, path):
    """Save to CSV without index, read back, and return shape."""
    raise NotImplementedError


def t2_2_json_columns(df, path):
    """Save to JSON with one object per row and return column names."""
    raise NotImplementedError


def t2_3_excel_roundtrip(df, path):
    """Save to Excel without index, read back, and return shape."""
    raise NotImplementedError


def t2_4_index_trap(df, path):
    """Save to CSV with index and return the number of columns after reading."""
    raise NotImplementedError


# ===== Step 3: Inspection and cleaning =====

def t3_1_count_missing(df):
    """Return missing-value counts for each column."""
    raise NotImplementedError


def t3_2_math_numeric(df):
    """Convert math marks to numeric values; invalid values become NaN."""
    raise NotImplementedError


def t3_3_remove_duplicates(df):
    """Remove duplicate rows and return the resulting shape."""
    raise NotImplementedError


def t3_4_fill_english_median(df):
    """Remove duplicates and fill missing English marks with the median."""
    raise NotImplementedError


def t3_5_rows_after_dropna(df):
    """Clean math values, remove duplicates, drop missing rows, and count."""
    raise NotImplementedError


def t3_6_section_category(df):
    """Convert section to category dtype and return its name."""
    raise NotImplementedError


def t3_7_clean_students(df):
    """Remove duplicates, convert marks, and fill missing values."""
    raise NotImplementedError


# ===== Step 4: Selecting, filtering, sorting =====

def t4_1_cheap_products(df):
    """Return product names with price below 50."""
    raise NotImplementedError


def t4_2_accessories_in_stock(df):
    """Return Accessories product names with stock above zero."""
    raise NotImplementedError


def t4_3_top_two_by_price(df):
    """Return the two most expensive product names."""
    raise NotImplementedError


def t4_4_loc_price(df):
    """Return the price at index label 3 using loc."""
    raise NotImplementedError


def t4_5_iloc_block(df):
    """Return the first two rows and columns as a list of lists."""
    raise NotImplementedError


def t4_6_low_stock_or_premium(df):
    """Return products with stock below 6 or price above 500."""
    raise NotImplementedError


def t4_7_sort_two_keys(df):
    """Sort by category ascending and price descending."""
    raise NotImplementedError


# ===== Step 5: Grouping, merging, apply =====

def t5_1_stock_by_category(products):
    """Return total stock for each category."""
    raise NotImplementedError


def t5_2_avg_price_by_category(products):
    """Return average price per category rounded to two decimals."""
    raise NotImplementedError


def t5_3_category_summary(products):
    """Return product counts and maximum prices by category."""
    raise NotImplementedError


def t5_4_left_merge_names(orders, products):
    """Left-merge orders with products and return product names."""
    raise NotImplementedError


def t5_5_inner_merge_rows(orders, products):
    """Return the number of rows after an inner merge."""
    raise NotImplementedError


def t5_6_revenue_list(orders, products):
    """Return revenue for each matched order."""
    raise NotImplementedError


def t5_7_revenue_by_customer(orders, products):
    """Return total revenue for each customer."""
    raise NotImplementedError


def t5_8_price_label(products):
    """Label products as cheap, mid, or premium."""
    raise NotImplementedError


def t5_9_upper_names(products):
    """Return product names in uppercase."""
    raise NotImplementedError


# ===== Step 6: Feature preparation =====

def t6_1_price_zscore(df):
    """Return price z-scores rounded to two decimals."""
    raise NotImplementedError


def t6_2_dummy_columns(df):
    """One-hot encode category and return the new column names."""
    raise NotImplementedError


def t6_3_feature_matrix(df):
    """Create price_z and category dummy features."""
    raise NotImplementedError


def t6_4_minmax_stock(df):
    """Scale stock between zero and one."""
    raise NotImplementedError


def t6_5_train_test_sizes(df):
    """Return training and testing row counts using an 80/20 split."""
    raise NotImplementedError


# ===== Step 7: Capstone =====

def t7_1_top_customer(orders, products):
    """Return the customer with the highest total revenue."""
    raise NotImplementedError


def t7_2_best_selling_product(orders, products):
    """Return the product with the highest total quantity sold."""
    raise NotImplementedError


def t7_3_customer_ranking(orders, products):
    """Return customers ranked by total revenue, highest first."""
    raise NotImplementedError


def t7_4_unmatched_orders(orders, products):
    """Return order IDs whose products are not in the catalogue."""
    raise NotImplementedError


def t7_5_save_report(orders, products, path):
    """Save customer revenue totals to CSV without the index."""
    raise NotImplementedError



# ===== Step 1: Series and DataFrames =====

def t1_1_weather_series(df):
    """Return temp_c as a Series indexed by day names."""
    return df.set_index("day")["temp_c"]

# task 
import pandas as pd


# Task 1.1: Set an index and select one column as a Series
def t1_1_weather_series(df):
    return df.set_index("day")["temp_c"]


# Task 1.2: Find the hottest day
def t1_2_hottest_day(df):
    return df.loc[df["temp_c"].idxmax(), "day"]


# Task 1.3: Build a DataFrame from a dictionary
def t1_3_build_frame():
    return pd.DataFrame({
        "item": ["pen", "book", "bag"],
        "price": [10, 120, 800]
    })


# Task 1.4: Compare Series and DataFrame
def t1_4_series_vs_frame(df):
    a = type(df["temp_c"]).__name__
    b = type(df[["temp_c"]]).__name__
    return (a, b)

# task2

# ===== Step 2: Reading and Writing Files =====

def t2_1_csv_roundtrip(df, path):
    """Save df to CSV without index, read it back, return its shape."""
    df.to_csv(path, index=False)

    result = pd.read_csv(path)

    return result.shape


def t2_2_json_columns(df, path):
    """Save df to JSON with one object per row, return column names."""
    df.to_json(path, orient="records")

    result = pd.read_json(path, orient="records")

    return result.columns.tolist()


def t2_3_excel_roundtrip(df, path):
    """Save df to Excel without index, read it back, return its shape."""
    df.to_excel(path, index=False)

    result = pd.read_excel(path)

    return result.shape


def t2_4_index_trap(df, path):
    """Save df to CSV with the default index, return the column count."""
    df.to_csv(path)

    result = pd.read_csv(path)

    return len(result.columns)
    
# task3

# ===== Step 3: Inspection and Cleaning =====

def t3_1_count_missing(df):
    """Return missing-value counts for each column."""
    return df.isna().sum().to_dict()


def t3_2_math_numeric(df):
    """Convert math marks to numbers; invalid values become NaN."""
    return pd.to_numeric(df["math"], errors="coerce").tolist()


def t3_3_remove_duplicates(df):
    """Remove duplicate rows and return the resulting shape."""
    return df.drop_duplicates().shape


def t3_4_fill_english_median(df):
    """Remove duplicates and fill missing English marks with the median."""
    result = df.drop_duplicates().copy()

    median_value = result["english"].median()

    result["english"] = result["english"].fillna(median_value)

    return result["english"].tolist()


def t3_5_rows_after_dropna(df):
    """Convert math to numeric, remove duplicates, drop missing rows."""
    result = df.drop_duplicates().copy()

    result["math"] = pd.to_numeric(
        result["math"],
        errors="coerce"
    )

    result = result.dropna()

    return len(result)


def t3_6_section_category(df):
    """Convert section to category dtype and return its name."""
    result = df["section"].astype("category")

    return result.dtype.name


def t3_7_clean_students(df):
    """Remove duplicates, convert marks, fill missing values."""
    result = df.drop_duplicates().copy()

    result["math"] = pd.to_numeric(
        result["math"],
        errors="coerce"
    )

    math_mean = result["math"].mean()
    english_median = result["english"].median()

    result["math"] = result["math"].fillna(math_mean)
    result["english"] = result["english"].fillna(english_median)

    return result
# task4

# ===== Step 4: Selecting, Filtering and Sorting =====

def t4_1_cheap_products(df):
    """Select products with a price below 50."""
    result = df[df["price"] < 50]
    return result


def t4_2_accessories_in_stock(df):
    """Select accessories that have stock greater than zero."""
    result = df[
        (df["category"] == "Accessories") &
        (df["stock"] > 0)
    ]
    return result


def t4_3_top_two_by_price(df):
    """Return the two most expensive products."""
    result = df.sort_values(
        by="price",
        ascending=False
    ).head(2)
    return result


def t4_4_loc_price(df):
    """Select the price column using loc."""
    return df.loc[:, "price"]


def t4_5_iloc_block(df):
    """Select the first three rows and first two columns by position."""
    return df.iloc[0:3, 0:2]


def t4_6_low_stock_or_premium(df):
    """Select products with low stock or a premium price."""
    result = df[
        (df["stock"] < 10) |
        (df["price"] >= 250)
    ]
    return result


def t4_7_sort_two_keys(df):
    """Sort by category ascending and price descending."""
    result = df.sort_values(
        by=["category", "price"],
        ascending=[True, False]
    )
    return result

#  task5


# ===== Step 5: Grouping, Merging and Applying Functions =====

def t5_1_stock_by_category(products):
    """Calculate total stock for each category."""
    result = products.groupby("category")["stock"].sum()
    return result


def t5_2_avg_price_by_category(products):
    """Calculate average price for each category, rounded to 2 decimals."""
    result = products.groupby("category")["price"].mean().round(2)
    return result


def t5_3_category_summary(products):
    """Summarize product count, average price, and total stock by category."""
    result = products.groupby("category").agg(
        product_count=("product_id", "count"),
        avg_price=("price", "mean"),
        total_stock=("stock", "sum")
    )
    result["avg_price"] = result["avg_price"].round(2)
    return result


def t5_4_left_merge_names(products, orders):
    """Left merge orders with product names."""
    result = orders.merge(
        products[["product_id", "name"]],
        on="product_id",
        how="left"
    )
    return result


def t5_5_inner_merge_rows(products, orders):
    """Inner merge orders with the product catalogue."""
    result = orders.merge(
        products,
        on="product_id",
        how="inner"
    )
    return result


def t5_6_revenue_list(products, orders):
    """Merge orders with prices and calculate revenue per order."""
    result = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="left"
    )
    result["revenue"] = result["quantity"] * result["price"]
    return result


def t5_7_revenue_by_customer(products, orders):
    """Calculate total revenue for each customer."""
    result = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="left"
    )
    result["revenue"] = result["quantity"] * result["price"]

    revenue_by_customer = result.groupby("customer")["revenue"].sum()
    return revenue_by_customer


def t5_8_price_label(products):
    """Label each product as Budget, Mid-range, or Premium."""
    def label_price(price):
        if price < 50:
            return "Budget"
        elif price < 250:
            return "Mid-range"
        else:
            return "Premium"

    result = products.copy()
    result["price_label"] = result["price"].apply(label_price)
    return result


def t5_9_upper_names(products):
    """Convert all product names to uppercase."""
    return products["name"].str.upper()

# task 6

# ===== Step 6: Feature Preparation =====

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
# task 7

# ===== Part B: Capstone Tasks =====

def t7_1_top_customer(products, orders):
    """Find the customer who generated the highest total revenue."""
    merged = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="inner"
    )

    merged["revenue"] = merged["quantity"] * merged["price"]

    revenue_by_customer = merged.groupby("customer")["revenue"].sum()

    return revenue_by_customer.idxmax()


def t7_2_best_selling_product(products, orders):
    """Find the product with the highest total quantity sold."""
    merged = orders.merge(
        products[["product_id", "name"]],
        on="product_id",
        how="inner"
    )

    quantity_by_product = merged.groupby("name")["quantity"].sum()

    return quantity_by_product.idxmax()


def t7_3_customer_ranking(products, orders):
    """Rank customers by total revenue from highest to lowest."""
    merged = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="inner"
    )

    merged["revenue"] = merged["quantity"] * merged["price"]

    ranking = (
        merged.groupby("customer")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return ranking


def t7_4_unmatched_orders(products, orders):
    """Find orders whose product IDs are missing from the catalogue."""
    unmatched = orders[
        ~orders["product_id"].isin(products["product_id"])
    ]

    return unmatched


def t7_5_save_report(
    products,
    orders,
    path="customer_revenue_report.csv"
):
    """Save the customer revenue ranking to a CSV file."""
    ranking = t7_3_customer_ranking(products, orders)

    report = ranking.rename("total_revenue").reset_index()

    report.to_csv(path, index=False)

    return report
