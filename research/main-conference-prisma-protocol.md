# Main-conference systematic-review protocol (working, not a completed PRISMA review)

**Review title:** Agreeing for the Right Reasons: A Survey of Sycophancy, Apology, and Acknowledgement in Language, Vision-Language, and Multi-Agent Models

**As of:** 21 November 2026. This document is a prospective *supplement* to the existing [bounded title-search log](survey-search.md). Do **not** combine its 17,036 / 29 / 26 counts with new records or describe them as a completed cross-database PRISMA flow. Those counts belong only to the previously documented ACL title search.

## Review execution status

**Updated evidence ledger:** [34 publisher-linked candidates](../literature/prisma-core-papers.md), [PRISMA 2020 completeness audit](PRISMA-2020-audit.md), [source-provenance and executed search strings](PRISMA-search-provenance.md). The historical 31-paper CSV is superseded as a reading shortlist and is **not** the final systematic-review selection. No comprehensive search denominator, full-text eligibility decision or independent reviewer consensus has been established. This is a protocol and documented audit, not a completed PRISMA review.

## Retrospective amendment and actual screening

**21 November 2026 correction:** AACL main and COLM main are explicitly eligible because the previously curated literature already contained a high-relevance AACL main advice study and a main COLM 2026 error-retraction study. This is a *post-hoc protocol amendment*, recorded in Git history, **not a preregistered filter**. No preprints, workshops or ACL Findings are quietly relabeled as main-track evidence. When studying important peer-reviewed Findings or specialist-conference papers, retain them as clearly identified contextual evidence instead of representing them as main proceedings.

Actual preliminary screening has now been performed on a **bounded union of the repository's known inventories**: [219 source-occurrences → 89 distinct title records → 34 metadata exclusions / 55 full-text candidates](PRISMA-bounded-executed-screen.md). Each record's sources, decision and reason are archived in [JSONL](repository-screening-snapshot-2026-11-21.jsonl). This was **one assistant screening** on metadata and existing summaries; it does not substitute for a complete per-database title+abstract export or full-text independent screening. The combined manuscript PRISMA flow still has missing denominators; do not fill them with bounded-corpus counts.

## Research questions

* RQ1: Under what conditions do models agree, resist, apologize, acknowledge, ask for clarification, or revise an earlier stance?
* RQ2: What experimental evidence distinguishes justified corrections from unsupported agreement? How are correctness, challenge validity, and uncertainty controlled?
* RQ3: How does the phenomenon differ across text, image/video-grounded tasks, and multi-agent debate?
* RQ4: Which methods improve *both* resistance to misleading pressure and uptake of valid evidence?
* RQ5: How are politeness, empathy, acknowledgement, apology and human trust distinguished from epistemic concession?

## Search coverage and vocabulary

For the **future complete systematic review**, search *titles and abstracts* in ACL Anthology (ACL, EMNLP, NAACL, EACL, AACL; main proceedings), OpenReview/ICLR official accepted conference proceedings, PMLR/ICML, NeurIPS proceedings, CVF Open Access (CVPR, ICCV), ECCV/Springer, COLM official proceedings, and ACM DL (CHI). Record each database, search date, exact query, filter and export file. Citation chasing is a separately labeled route. Run searches over 2022–2026; extend backwards for important foundational dialogue/grounding work. Do not restrict study designs based on positive results.

Use this broad, adapt-to-database Boolean query, then narrower combinations where search interfaces limit syntax:

```text
(sycophan* OR "social conformity" OR "conformity bias" OR "peer influence"
 OR "groupthink" OR "social pressure" OR "user disagreement" OR "answer flip"
 OR "answer revision" OR "rational updating" OR "epistemic vigilance"
 OR apolog* OR acknowledg* OR "conversational repair" OR "dialogue grounding")
AND
("language model" OR LLM OR "language assistant" OR "vision-language"
 OR multimodal OR MLLM OR VLM OR "multi-agent" OR "agent debate"
 OR chatbot OR "conversational agent")
```

For multimodal searches add `("visual evidence" OR "misleading hint" OR "image-text conflict" OR "video grounding")`; for multi-agent add `("majority pressure" OR "agent consensus" OR "peer credibility" OR debate)`; for apology/acknowledgement add `("feedback response" OR "trust repair" OR "common ground" OR "apology appropriateness")`. Keep the *full unmodified executed query* for each source in the search log, not only this prototype.

## Inclusion and exclusion rules

**Core candidate eligible:** final, officially published main-conference research paper in ACL, EMNLP, NAACL, EACL, AACL, ICLR, ICML, NeurIPS, CVPR, ICCV, ECCV, COLM or CHI, plus peer-reviewed archival NeurIPS Datasets and Benchmarks papers explicitly labeled as such; empirical intervention, benchmark, user study or model-behavior study; directly measures agreement, opposition, evidence-sensitive revision, apology, feedback acknowledgement, social conformity, or debate agreement, with an observable outcome. Peer review and main-track status must be confirmed by the publisher.

**Exclude from strict core:** arXiv-only/preprints, under-review or withdrawn manuscripts, Findings tracks, workshops, student research workshops, non-archival satellite tracks, journals, surveys, position/opinion pieces without primary empirical or theoretical contributions, duplicates, and papers mentioning sycophancy only tangentially. Archival NeurIPS Datasets and Benchmarks is separately identified, not a workshop. Retain useful excluded papers in the existing 69-study *background* collection without counting them as core.

**Important:** Conference tier is a *publication filter*, not proof of causal quality. Prioritize designs that vary pressure independently from evidence quality, distinguish initial accuracy, and evaluate both beneficial and harmful answer revisions.

## Screening process

**This is a protocol, not a claim these steps were completed.** The current cross-venue [discovery log](cross-venue-discovery-log.md) records targeted publisher searches, not PRISMA denominators.


1. Export bibliographic records with source and search timestamp; compute search hit counts per venue. No unlogged purposive additions.
2. Deduplicate by DOI, ACL Anthology ID, proceedings URL, normalized title, and accepted-version match. Keep the final published version.
3. Two independent reviewers screen title/abstract, then full text; log both decisions, conflicts, adjudication and named exclusion reasons (or explicitly report a single screener if this is not possible).
4. Full-text eligibility: record retrieval successes and missing papers, and exclude with a single leading reason. Keep rejected and borderline records in the ledger.
5. Use a PRISMA 2020 diagram with *actual observed* counts for identified, deduplicated, screened, full texts sought, not retrieved, excluded (by reason), and included. Report citation-chasing separately.
6. Freeze a dated search snapshot; new papers require a dated update and screening ledger.

## High-priority quality rubric (0–2 on each; maximum 12)

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Direct construct match | incidental | partial | directly operationalized |
| Control of evidence vs pressure | conflated | partly controlled | independently manipulated |
| Outcome validity | vague | one useful measure | correctness + beneficial/harmful changes |
| Experimental comparator | absent | limited | strong controlled baseline |
| Transparency/reproducibility | sparse | partial | sample, prompts, models and eval documented |
| Survey synthesis value | redundant | useful | distinctive comparison, mechanism or consequence |

**Priority E (essential):** high direct relevance and an informative comparator or distinctive human outcome; **Priority S (supporting):** meaningful but narrower context. The E/S labels in [core-conference-manifest.csv](../papers/core-conference-manifest.csv) are provisional topic-fit assessments, NOT scored risk-of-bias or full-text-quality assessments. A full-text rubric and evidence extraction are still required. Do not turn them into numeric claims before coding.

## Extraction schema

For every included paper capture: publisher paper ID, DOI, official PDF, venue+track, year, task, modality, models/versions, sample size, unit of analysis, original answer accuracy, challenger and identity, challenge correctness/evidence, pressure manipulation, final factual accuracy, wrong-to-right transitions, right-to-wrong transitions, acknowledgement act, apology act, stance, effect sizes/CI, evaluation method, limitations, code/data and inter-rater agreement.

**Terminology:** acknowledge = recognize the input/feedback; apologize = express regret/responsibility; agree = adopt the proposition; update = change claim; *justified update* requires evidential support. Do not infer dependence, retention, or trust from an answer flip.

**Quality check before submission:** verify all official links, register executed queries and counts for each source, screen full texts, and obtain professor review of boundary cases. The present manifest is a curated starting set, *not a completed systematic review*.

## Reporting standards

[PRISMA 2020](https://www.prisma-statement.org/prisma-2020) and [PRISMA-S](https://www.prisma-statement.org/prisma-search) provide reporting checklists. PRISMA compliance should not be claimed until search/export/screening records and a reproducible selection flow are complete.
