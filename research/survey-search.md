# Search strategy and screening flow

**21 November 2026.** This update documents a bounded search of main-conference proceedings and one supplementary record. The repository’s 69 papers include material collected under its earlier, broader policy. The counts below apply to this update only.

## Review question and eligibility

When a user or peer states a belief, supplies a correction, or challenges an answer, how do researchers determine whether the model agrees for evidential reasons, acknowledges feedback, apologizes, or defers without justification? Include empirical studies with a direct measure of one of these outcomes or an intervention evaluated against it. Eligible designs include grounding-act comparisons, warranted and unwarranted challenges, image–prompt conflict, controlled majority opinions, interactive debate, and human-subject experiments on agreement or repair.

For new entries, require a final paper in the main proceedings of a major conference and an identifiable official full text. Exclude workshop papers, Findings papers, preprints, under-review manuscripts, secondary reviews and studies in which the matching term refers to a different behavior. This is a scope decision for the conference collection. Citation counts and whether an intervention succeeds are not eligibility criteria.

## Sources and keywords

Searched the [pinned ACL Anthology metadata](https://github.com/acl-org/acl-anthology/tree/37f8244b23f7647a84173868f26bb0f52fb2cb77/data/xml), covering every available ACL, EMNLP, EACL and NAACL collection from 2022 through 2026. Included volumes labeled `main`, `long` and `short`, omitting paper 0 (front matter). Searched the English title field after joining inline XML and normalizing whitespace. No country, citation or paper-language filters. The period includes an early dialogue-feedback study and runs through the snapshot. Scoping searches informed both synonyms and phrases found in known titles. The strategy was developed during this review and was not preregistered.

| Concept | Search vocabulary and interpretation |
|---|---|
| Social agreement | Sycophancy, sycophantic, conformity, social pressure, groupthink, peer pressure, user disagreement |
| Apology and acknowledgement | Apology, apologies, apologizing/apologising, acknowledgement/acknowledgment, conversational grounding, feedback, repair |
| Evidential updating | Vacillation, misleading cues, rational updating, accepting and resisting persuasion |
| Model setting | Language assistants, vision-language and video models, multi-agent debate. Model setting was coded during screening so a title need not use a specific model acronym. |

**Exact title expression**, case insensitive:

```regex
\b(sycophan\w*|apolog(?:y|ies|iz\w*|is\w*)|acknowledg\w*|conformity|peer pressure|groupthink|social pressure|user disagreement|second.guesser|vacillations?|grounding gaps|taking feedback gracefully|misleading scenarios|debate.aware learning|consistency illusion|rational updating|(?:resisting|accepting) persuasion)\b
```

Run `python research/replay_search.py PATH_TO_ACL_ANTHOLOGY_CHECKOUT` at the pinned revision to emit the matched records. The table gives the expected counts.

| Year | Proceedings records searched / title matches |
|---|---|
| 2022 | ACL 700 / 1, EMNLP 828 / 0, NAACL 442 / 0 |
| 2023 | ACL 1075 / 0, EACL 280 / 0, EMNLP 1047 / 0 |
| 2024 | ACL 940 / 1, EACL 223 / 0, EMNLP 1268 / 0, NAACL 562 / 1 |
| 2025 | ACL 1699 / 2, EMNLP 1809 / 5, NAACL 718 / 1 |
| 2026 | ACL 2296 / 7, EACL 445 / 2, EMNLP 2704 / 9 |

**Supplementary discovery.** The web query `multi agent sycophancy consensus conformity debate majority large language models NeurIPS ICLR ICML EMNLP conformity stubbornness language model debate paper` supplied Weng et al.’s ICLR 2025 BenchForm study. Its five interaction protocols directly cover agent conformity. This was a purposive addition. Exploratory web hits are not counted as a database export.

## Screening flow

| Stage | Count |
|---|---:|
| Proceedings titles tested in 16 venue-year collections | 17,036 |
| Distinct records matching the title expression | 29 |
| Excluded on title and abstract | 3 |
| Retained from the structured search | 26 |
| Already present among the original 52 | 10 |
| New papers from the structured search | 16 |
| Additional unique paper from ICLR | 1 |
| **New conference papers** | **17** |

[Screening ledger, including all three exclusion reasons](screening.csv) · [Original 52-paper inventory and overlap](initial-catalog.csv). Stable Anthology IDs, proceedings URLs and titles were used to identify duplicates and published versions. Counts are papers, with experiments within the same paper treated together. A single assistant screened the records and checked publication status. These are record-level selections, without independent reviewer agreement or a manuscript-wide full-text exclusion count.

## How to weigh the evidence

Extract the initial answer, challenger, challenge type and validity, available evidence, final claim, acknowledgement and apology separately. Record model/version, baseline, prompt, sample, judge and uncertainty. A high-priority study isolates the social cue and has a comparator that can distinguish reasonable updating from capitulation. For factual items, divide correct-to-wrong flips by the initially correct items, and wrong-to-correct recoveries by the initially wrong items. For subjective or unresolved items, report stance shifts separately. For human studies, distinguish the task outcome, reported preference and duration of follow-up.

In visual tasks, check initial recognition of the relevant feature on the same image. In agent debate, distinguish a peer’s identity and majority size from the evidence the peer supplies. For apologies, examine whether the model acknowledges a specific issue, accepts responsibility, changes its claim and completes a repair. [Priority comparisons and limitations](../papers/README.md) · [Evidence-justified correction protocol](evidence-justified-correction-protocol.md).

## Coverage limits for the manuscript

The present run is a high-precision title search. Abstract-only mentions and earlier dialogue work can be missed. Systematic title-and-abstract searches across ML, vision and HCI proceedings (including ICLR, ICML, NeurIPS, CVPR, ICCV, ECCV and CHI), citation chasing and independent full-text screening remain open. Record exports, deduplication, retrieval failures and exclusion reasons before presenting a combined manuscript flow. [PRISMA 2020](https://www.prisma-statement.org/prisma-2020) · [PRISMA-S](https://www.prisma-statement.org/prisma-search).
