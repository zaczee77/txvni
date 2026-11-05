# Demo: KPI extraction with cited answers

This demo is a small reference implementation of the Txvni pattern in plain Python with no external packages. It calls no model and uses no network. It is an illustrative reference demo, not the Txvni product.

## How to run it

1. Open a terminal in this folder.
2. Make sure sample_financials.csv sits in the same folder as the script. It is bundled with the demo.
3. Run the command: python3 kpi_demo.py

## What it does

1. It loads the bundled sample dataset, which holds two clearly fictional sample companies with two periods of simple financials each.
2. It extracts three KPIs for the latest period of each company: revenue growth against the prior period, gross margin, and EBITDA margin. EBITDA in this demo is a simple illustrative definition: revenue minus cost of revenue minus operating expenses.
3. It answers three fixed questions and cites the exact source rows used for each answer, by file name, line number, company, and period.
4. It raises simple risk flags: a gross margin below an illustrative flag level, or an EBITDA margin that fell against the prior period.
5. It prints a short memo style summary built only from the cited figures.

## Expected output

1. Sample Company A: revenue growth 25.0 percent, gross margin 44.0 percent, EBITDA margin 20.0 percent.
2. Sample Company B: revenue growth 5.0 percent, gross margin 19.0 percent, EBITDA margin 2.4 percent.
3. Cited answers: Sample Company A grew revenue 25.0 percent in 2024; Sample Company A has the stronger 2024 gross margin; Sample Company B needs the closer risk review.
4. Risk flags: 2, both for Sample Company B (gross margin below the flag level, and EBITDA margin down from 10.0 percent to 2.4 percent).

## Limits

The sample companies and every number in sample_financials.csv are fictional, written only so the pattern can be run and read. The flag level is illustrative only and is not an industry benchmark. The demo reads one small structured CSV. The product described in the case study ingests mixed document formats, which this demo does not attempt. Nothing here is a measured result from the real product.
