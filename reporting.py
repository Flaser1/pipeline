

def print_countries_report(report: dict) -> None:
    for country in sorted(report):
        print(country, report[country])

def print_statuses_report(report: dict) -> None:
    for status in sorted(report):
        print(status, report[status])