# Txvni case study

## What Txvni is

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. It serves private equity, hedge fund, and family office teams. This case study describes the problem it addresses, the ingestion model at its center, and the design choices behind its cited answers, KPI extraction, risk flags, memo drafting, and audit trail. It invents no metrics, users, or outcomes for the product, because none are part of its public record.

## The problem in plain terms

An investment team evaluating a company receives a bundle of material: financial statements, spreadsheets, presentations, and supporting documents. Each file has its own structure. The same figure can appear in several places, in several forms, sometimes with small differences. The team has to answer practical questions under time pressure. What did revenue do over the last two periods. Where are margins heading. What in these documents should worry us. Then those answers have to survive an investment committee, where a number without a source does not last long.

The slow part is not the judgment. The slow part is the reading, the extraction, and the checking, repeated for every deal and every document set. And when the conclusion is challenged a week later, the team needs to show exactly what it rested on.

## The ingestion model

Txvni is built around one multiuse ingestion model. Documents and spreadsheets are ingested in the formats teams already receive, including PDF files, spreadsheets, presentations, and DOCX, XLSX, CSV, and TXT files. Ingestion is not a file store. Its job is to turn mixed documents into one structured base that every later feature draws on: the same figures feed question answering, KPI extraction, risk analysis, and memo drafting, so the workspace never works from two versions of the truth.

Because the model is about document review rather than about one industry, it travels. A bank reviewing loan files and credit documents faces the same pattern: mixed formats, figures to extract, questions to answer with sources, and a record of what was decided. An insurer reviewing claims paperwork and underwriting files faces it too. Txvni is positioned for that reuse deliberately.

## Cited answers

Question answering is only useful in deal work if the answer can be checked. In Txvni, a question about the documents returns an answer with citations to the source material behind it. The citation is not decoration. It is the mechanism that lets a second person verify the answer quickly, catch a wrong period or a wrong file, and trust the answers that hold up.

This changes how the workspace is used. Instead of asking the model to be right and hoping, the team asks, checks the cited source, and moves on. The citation is the trust surface of the whole product.

## KPI extraction

Before analysis comes extraction. Txvni pulls financial KPIs out of the ingested documents and structures them, so figures like revenue, margins, and growth can be compared across periods and across companies without rereading the source files each time. Structured extraction is what makes the rest of the workspace coherent: benchmarks compare structured figures, risk analysis reads structured figures, and memo drafts quote structured figures. When a number in a memo is questioned, it traces back through the extraction to the document it came from.

## Risk flags

Risk analysis in Txvni sits beside the extraction, not after it. As KPIs are structured, signals can be raised early: a margin moving the wrong way, a figure that disagrees across documents, a gap where an expected number should be. Industry benchmarks give those signals context, so a team can see whether a figure is merely weak or weak for its sector. A flag is a prompt for human review, not a verdict. It tells the team where to read closely.

## Investment committee memo drafting

The memo is where deal work becomes a decision, and it is usually written last, from notes and memory. Txvni drafts investment committee memos from the extracted KPIs, the cited answers, and the risk flags already in the workspace. The draft is a starting point for the team to edit, argue with, and own. Because the draft is built from cited material, a claim in the memo can be traced to its source during the meeting, which is exactly when that trace matters most.

## Trust and audit design

Two commitments run through the design. The first is citations everywhere: answers cite sources, extractions trace to documents, and memo claims rest on both. The second is the audit trail. Collaboration in the workspace is recorded, so the team can reconstruct what was asked, what the documents said, what was flagged, and what was concluded, in the order it happened. For regulated and scrutinized work, that record is not a nice extra. It is how the work defends itself later.

Judgment stays human throughout. The workspace ingests, extracts, cites, flags, and drafts. The team decides.

## What the demo shows, and what it does not show

The demo in this repository shows the pattern at miniature scale: a small fictional CSV goes in, KPIs are extracted, three fixed questions are answered with citations to exact source rows, risk flags are raised on simple rules, and a short memo style summary is printed. It does not show real deal documents, real extraction over PDFs or presentations, or the Txvni product itself. It is a reference demo for the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
