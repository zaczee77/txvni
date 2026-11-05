# Txvni

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. It serves private equity, hedge fund, and family office teams who need to turn deal documents into answers they can defend.

## The problem

Deal work begins with documents that were never written to be read together. A target company sends financial statements, spreadsheets, and presentations, each in a different format and each with its own layout. Before anyone can judge the deal, someone has to read everything, pull out the numbers that matter, and check claims against the pages they came from. Done by hand, that reading and checking is slow, and the trail from a conclusion back to its source is easy to lose. A figure quoted in a meeting may have come from an early draft, a different period, or a page nobody can find again.

## Who it serves

Txvni is built for investment teams: private equity firms, hedge funds, and family offices. These teams share the same working pattern. Documents arrive, questions follow, a risk view forms, and a memo has to be written for an investment committee. The teams differ in strategy, but the document work underneath is the same.

## What it does

1. Ingest. The workspace takes in documents and spreadsheets in the formats deal teams already receive, including PDF files, spreadsheets, presentations, and DOCX, XLSX, CSV, and TXT files.
2. Extract. Financial KPIs are pulled out of the ingested material and structured so they can be compared across periods and across companies.
3. Ask. A user can ask questions about the documents and get cited document question and answer responses, where each answer points back to the source material it rests on.
4. Analyze. Risk analysis and industry benchmarks sit alongside the extracted numbers, so weak points are visible next to the figures that raise them.
5. Draft. Investment committee memos are drafted from the extracted and cited material, rather than from memory of a long reading session.
6. Record. Collaboration happens inside the workspace, and an audit trail records what was asked, what was answered, and what each answer rested on.

## One ingestion model, more than one industry

Txvni is positioned as one multiuse ingestion model. The hard part is shared across document heavy review work: take in mixed formats, structure what matters, answer with citations, and keep an audit trail. That is why the same model is reusable by banks working through loan files and credit documents, and by insurers working through claims paperwork and underwriting files. The documents change. The pattern of review does not.

## Design principles

1. Citations are a trust surface. An answer that cannot point to its source is an opinion. Every answer in Txvni is expected to show where it came from, so a reviewer can check it in seconds.
2. Extraction before opinion. KPIs are structured first, and analysis is built on the structured figures, so a memo and a question answer draw on the same numbers.
3. Risk sits next to the data. A risk flag that lives in a separate report gets ignored. Risk analysis belongs beside the extraction that triggered it.
4. The audit trail is part of the product. Investment decisions get revisited. The workspace should be able to show what was known, what was asked, and what was concluded, in order.
5. People keep the judgment. The workspace prepares, extracts, and drafts. The investment decision stays with the team.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It reads a tiny bundled CSV of clearly fictional sample companies, extracts revenue growth, gross margin, and EBITDA margin, answers three fixed questions with citations to the exact source rows used, flags simple risk signals, and prints a short memo style summary. It shows the shape of the Txvni pattern at the smallest possible scale: extract, cite, flag, and summarize.

## What this is not

This demo is not the Txvni product. It contains no real deal data, no client documents, and no measured results. The sample companies and their numbers are fictional and exist only so the pattern can be run and read. The full case study in the docs folder describes the product and its design without inventing metrics or outcomes for it.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
