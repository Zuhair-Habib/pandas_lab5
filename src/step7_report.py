
from src.dataset import make_orders, make_products
from src.practice import t7_5_save_report

t7_5_save_report(
    make_products(),
    make_orders(),
    "results/report.csv"
)

print("saved results/report.csv")
