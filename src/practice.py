
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
