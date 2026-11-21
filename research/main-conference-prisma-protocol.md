# Main-conference systematic-review protocol (working, not a completed PRISMA review)

**Review title:** Agreeing for the Right Reasons: A Survey of Sycophancy, Apology, and Acknowledgement in Language, Vision-Language, and Multi-Agent Models

**As of:** 21 November 2026. This document is a prospective *supplement* to the existing [bounded title-search log](survey-search.md). Do **not** combine its 17,036 / 29 / 26 counts with new records or describe them as a completed cross-database PRISMA flow. Those counts belong only to the previously documented ACL title search.

## Research questions

* RQ1: Under what conditions do models agree, resist, apologize, acknowledge, ask for clarification, or revise an earlier stance?
* RQ2: What experimental evidence distinguishes justified corrections from unsupported agreement? How are correctness, challenge validity, and uncertainty controlled?
* RQ3: How does the phenomenon differ across text, image/video-grounded tasks, and multi-agent debate?
* RQ4: Which methods improve *both* resistance to misleading pressure and uptake of valid evidence?
* RQ5: How are politeness, empathy, acknowledgement, apology and human trust distinguished from epistemic concession?

## Search coverage and vocabulary

Search *titles and abstracts* in ACL Anthology (ACL, EMNLP, NAACL, EACL; main proceedings), OpenReview/ICLR official accepted conference proceedings, PMLR/ICML, NeurIPS proceedings, CVF Open Access (CVPR, ICCV), ECCV/Springer, and ACM DL (CHI). Record each database, search date, exact query, filter and export file. Citation chasing is a separately labeled route. Run searches over 2022–2026; extend backwards for important foundational dialogue/grounding work. Do not restrict study designs based on positive results.

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

**Core eligible:** final, officially published **main-conference** paper in ACL, EMNLP, NAACL, EACL, ICLR, ICML, NeurIPS, CVPR, ICCV, ECCV or CHI; empirical intervention, benchmark, user study or model-behavior study; directly measures agreement, opposition, evidence-sensitive revision, apology, feedback acknowledgement, social conformity, or debate agreement, with an observable outcome. Peer review and main-track status must be confirmed by the publisher.

**Exclude from strict core:** arXiv-only/preprints, under-review or withdrawn manuscripts, Findings tracks, workshops, student research workshops, non-main tracks, journals, surveys, opinion-only position pieces without original data, duplicates, and papers mentioning sycophancy only tangentially. Retain useful excluded papers in the existing 69-study *background* collection without counting them as core.

**Important:** Conference tier is a *publication filter*, not proof of causal quality. Prioritize designs that vary pressure independently from evidence quality, distinguish initial accuracy, and evaluate both beneficial and harmful answer revisions.

## Screening process

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

**Tier A:** high direct relevance and informative comparator; **Tier B:** useful published core context. The tiers in [core-conference-manifest.csv](../papers/core-conference-manifest.csv) are *provisional relevance tiers*, not scored methodological-risk assessments. A full-text rubric and evidence extraction are still required. Do not turn them into numeric claims before coding.

## Extraction schema

For every included paper capture: publisher paper ID, DOI, official PDF, venue+track, year, task, modality, models/versions, sample size, unit of analysis, original answer accuracy, challenger and identity, challenge correctness/evidence, pressure manipulation, final factual accuracy, wrong-to-right transitions, right-to-wrong transitions, acknowledgement act, apology act, stance, effect sizes/CI, evaluation method, limitations, code/data and inter-rater agreement.

**Terminology:** acknowledge = recognize the input/feedback; apologize = express regret/responsibility; agree = adopt the proposition; update = change claim; *justified update* requires evidential support. Do not infer dependence, retention, or trust from an answer flip.

**Quality check before submission:** verify all official links, register executed queries and counts for each source, screen full texts, and obtain professor review of boundary cases. The present manifest is a curated starting set, *not a completed systematic review*.

## Reporting standards

[PRISMA 2020](https://www.prisma-statement.org/prisma-2020) and [PRISMA-S](https://www.prisma-statement.org/prisma-search) provide reporting checklists. PRISMA compliance should not be claimed until search/export/screening records and a reproducible selection flow are complete.
