"""Reference demo for the Txvni pattern: KPI extraction with cited answers.

Illustrative reference demo only. This is not the Txvni product. It reads a
small bundled CSV of clearly fictional sample companies and shows three
ideas from the case study at the smallest possible scale:

1. Extract a few KPIs (revenue growth, gross margin, EBITDA margin).
2. Answer fixed questions with citations to the exact source rows used.
3. Raise simple risk flags and print a short memo style summary.

Standard library only. No network. No real deal data.
EBITDA here is a simple illustrative definition: revenue minus cost of
revenue minus operating expenses, computed on the sample numbers.
"""

import csv
import os

SAMPLE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "sample_financials.csv"
)
GROSS_MARGIN_FLAG = 25.0  # illustrative threshold only, not a benchmark


def load_rows(path):
    rows = []
    with open(path, newline="") as handle:
        reader = csv.DictReader(handle)
        for line_number, raw in enumerate(reader, start=2):
            rows.append(
                {
                    "line": line_number,
                    "company": raw["company"],
                    "period": raw["period"],
                    "revenue": float(raw["revenue"]),
                    "cost_of_revenue": float(raw["cost_of_revenue"]),
                    "operating_expenses": float(raw["operating_expenses"]),
                }
            )
    return rows


def gross_margin_pct(row):
    return (row["revenue"] - row["cost_of_revenue"]) / row["revenue"] * 100


def ebitda(row):
    return row["revenue"] - row["cost_of_revenue"] - row["operating_expenses"]


def ebitda_margin_pct(row):
    return ebitda(row) / row["revenue"] * 100


def cite(row):
    return (
        f"[source: sample_financials.csv line {row['line']}, "
        f"{row['company']}, {row['period']}]"
    )


def main():
    rows = load_rows(SAMPLE_FILE)
    companies = {}
    for row in rows:
        companies.setdefault(row["company"], []).append(row)
    for company_rows in companies.values():
        company_rows.sort(key=lambda r: r["period"])

    print("Txvni reference demo: KPI extraction with cited answers")
    print("Sample data: fictional companies, illustrative numbers only.")
    print()

    print("KPIs by company (latest period vs prior period)")
    latest = {}
    prior = {}
    for company, company_rows in companies.items():
        prev, current = company_rows[-2], company_rows[-1]
        latest[company] = current
        prior[company] = prev
        growth = (current["revenue"] - prev["revenue"]) / prev["revenue"] * 100
        print(f"{company} ({current['period']} vs {prev['period']}):")
        print(f"  Revenue growth: {growth:.1f} percent")
        print(f"  Gross margin: {gross_margin_pct(current):.1f} percent")
        print(
            f"  EBITDA margin: {ebitda_margin_pct(current):.1f} percent "
            f"(EBITDA {ebitda(current):.0f} on revenue {current['revenue']:.0f})"
        )
    print()

    print("Cited answers")
    a_prev, a_cur = prior["Sample Company A"], latest["Sample Company A"]
    b_prev, b_cur = prior["Sample Company B"], latest["Sample Company B"]
    a_growth = (a_cur["revenue"] - a_prev["revenue"]) / a_prev["revenue"] * 100
    print("Q1. How fast did Sample Company A grow revenue in 2024?")
    print(
        f"A1. Revenue grew {a_growth:.1f} percent, from "
        f"{a_prev['revenue']:.0f} to {a_cur['revenue']:.0f}."
    )
    print(f"    Sources: {cite(a_prev)} {cite(a_cur)}")
    print("Q2. Which company has the stronger gross margin in 2024?")
    print(
        f"A2. Sample Company A, at {gross_margin_pct(a_cur):.1f} percent, "
        f"against Sample Company B at {gross_margin_pct(b_cur):.1f} percent."
    )
    print(f"    Sources: {cite(a_cur)} {cite(b_cur)}")
    print("Q3. Which company needs a closer risk review?")
    print(
        "A3. Sample Company B. Its EBITDA margin fell from "
        f"{ebitda_margin_pct(b_prev):.1f} percent to "
        f"{ebitda_margin_pct(b_cur):.1f} percent, and its gross margin "
        "sits below the illustrative flag level."
    )
    print(f"    Sources: {cite(b_prev)} {cite(b_cur)}")
    print()

    print("Risk flags")
    flagged = 0
    for company, current in latest.items():
        prev = prior[company]
        if gross_margin_pct(current) < GROSS_MARGIN_FLAG:
            flagged += 1
            print(
                f"{company}: gross margin {gross_margin_pct(current):.1f} "
                f"percent is below the illustrative flag level of "
                f"{GROSS_MARGIN_FLAG:.1f} percent. {cite(current)}"
            )
        if ebitda_margin_pct(current) < ebitda_margin_pct(prev):
            flagged += 1
            print(
                f"{company}: EBITDA margin fell from "
                f"{ebitda_margin_pct(prev):.1f} percent to "
                f"{ebitda_margin_pct(current):.1f} percent. "
                f"{cite(prev)} {cite(current)}"
            )
    if not flagged:
        print("None.")
    print()

    print("Memo summary (draft, from the cited figures above)")
    print(
        "Sample Company A grew revenue "
        f"{a_growth:.1f} percent with a gross margin of "
        f"{gross_margin_pct(a_cur):.1f} percent and an EBITDA margin of "
        f"{ebitda_margin_pct(a_cur):.1f} percent."
    )
    print(
        "Sample Company B grew more slowly and its margins compressed, "
        "so it is flagged for a closer read before any conclusion."
    )
    print(
        "Every figure in this memo traces to a cited row in "
        "sample_financials.csv, which is the point of the pattern."
    )
    print("Reminder: fictional sample data, illustrative reference demo only.")


if __name__ == "__main__":
    main()
