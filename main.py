

from config import load_config_customers, load_config_orders
from pipeline import run_pipeline_customers, run_pipeline_orders
from transformations import normalize_customers, normalize_orders
from metrics import build_summary_country, build_summary_status
from reporting import print_countries_report, print_statuses_report

def main():
    config_customers = load_config_customers()
    config_orders = load_config_orders()

    customers_raw_csv = run_pipeline_customers(config_customers.input_path, config_customers.output_dir)
    orders_raw_csv = run_pipeline_orders(config_orders.input_path, config_orders.output_dir)

    clean_customers, invalid_customers = normalize_customers(customers_raw_csv)
    clean_orders, invalid_orders = normalize_orders(orders_raw_csv)

    countries_summary = build_summary_country(clean_customers, clean_orders)
    statuses_summary = build_summary_status(clean_customers, clean_orders)

    print_countries_report(countries_summary)
    print_statuses_report(statuses_summary)
    print(invalid_orders)
    print(invalid_customers)

if __name__ == "__main__":
    main()