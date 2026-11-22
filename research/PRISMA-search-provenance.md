# PRISMA-S search provenance and reproducibility (2026-11-21)

> **Scope warning:** This file documents executed *targeted discovery* searches and one earlier *bounded title-metadata search*. It does **not** transform web search results into a database-wide PRISMA corpus. Search engine results are not a deterministic export, and exact results counts were not retained for the new queries. Hence no combined identification count is reported.

## Information sources

| Source/platform | Actual use | Reporting limits |
|---|---|---|
| ACL Anthology pinned metadata | Historical structured title screening, 16 conference/year collections, 2022–2026 | 17,036 proceeding records examined; exact title regex and replay script in [survey-search.md](survey-search.md) / [replay_search.py](replay_search.py). Title-only discovery; not a complete title+abstract search |
| NeurIPS official proceedings | Direct publisher search and verification of main-track records, 2024–2025; separate 2025 D&B | Targeted search only; no full proceedings export or all-year 2022–2026 hit count |
| PMLR / ICML proceedings | Direct publisher search and verification, including ICML 2024 Du et al. and ICML 2026 papers | Targeted search only |
| ICLR proceedings | Publisher-check for Causally Motivated Sycophancy Mitigation (2025) and prior ICLR papers | Targeted search only |
| ACM CHI DOI listings | Publisher DOI link to human-effects and interaction-context papers | No complete ACM DL query export |
| CVF (CVPR/ICCV/WACV) | Discovery of related visual evidence; main-vs-workshop boundary check | No main-track comprehensive export |
| PRISMA and PRISMA-S guideline websites | Reporting standards | Not part of primary research screening |

**No claim of comprehensive search across ECCV, ICCV, CVPR, COLM, NeurIPS 2026, OpenAlex, Scopus, Web of Science or ACM DL** can be made from these records. Accessibility of a venue website or isolated page is not equivalent to executing a reproducible database search.

## Executed targeted search strings

The following are *literal search expressions executed during the 2026-11-21 research audit* (search-engine routing varied). **No date, language or citation cutoff was applied to these searches beyond any year shown inside each query.** These are not Boolean database queries and no exhaustive result counts are available.

```text
site:proceedings.neurips.cc/paper_files/paper/2025 sycophancy conformity large language models
site:proceedings.neurips.cc/paper_files/paper/2024 multi agent debate llms conform evidence
site:proceedings.neurips.cc/paper_files/paper/2023 sycophancy assistant models preference agreement
site:proceedings.neurips.cc/paper_files/paper/2025 "debate" "vote" agents
site:proceedings.neurips.cc/paper_files/paper/2025/ "sycophancy" "large language"
site:proceedings.neurips.cc/paper_files/paper/2024/ "sycophancy" "large language"
site:proceedings.neurips.cc/paper_files/paper/2023/ "sycophancy" "language"
site:proceedings.neurips.cc/paper_files/paper/2025/ "multi-agent" "conformity"
site:proceedings.neurips.cc/paper_files/paper/2025/ "debate" "belief" "correctness"
site:proceedings.neurips.cc/paper_files/paper/2024/ "social" "sycophancy"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "sycophancy" "benchmark"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "conformity" "language"
site:proceedings.neurips.cc/paper_files/paper/2024/hash "debate" "LLM" "judge"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "feedback" "truthfulness" "language models"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "visual" "misleading" "language models"
NeurIPS 2025 2024 main conference multi-agent debate sycophancy conformity peer pressure papers proceedings
NeurIPS 2025 sycophancy "real time" mechanistic agreeableness model user
NeurIPS 2025 social sycophancy benchmark peer correction conference
site:proceedings.neurips.cc/paper_files/paper/2025/hash "sycophancy" "Main Conference"
site:proceedings.neurips.cc/paper_files/paper/2024/hash "debate" "Main Conference"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "social conformity" "language models"
site:proceedings.neurips.cc/paper_files/paper/2025/hash "multi agent" "misconception"
Improving Factuality and Reasoning in Language Models through Multiagent Debate publication ICML 2024
site:proceedings.neurips.cc/paper_files/paper/2024 "multiagent debate" "truth"
site:proceedings.neurips.cc/paper_files/paper/2025 "debate" "majority"
site:proceedings.neurips.cc/paper_files/paper/2024 "sycophancy" "humans"
```

The older log [cross-venue-discovery-log.md](cross-venue-discovery-log.md) contains directional searches from the previous iteration. They should not be described as prospectively registered or treated as independent database strata.

## Actual publisher verification with direct official landing pages

- [NeurIPS 2024, Estornell & Liu](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html): Main Conference, DOI 10.52202/079017-0911
- [NeurIPS 2025, Choi, Zhu & Li](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html): Main Conference, DOI 10.52202/085713-3405
- [NeurIPS 2024, Kenton et al.](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html): Main Conference, DOI 10.52202/079017-2395
- [NeurIPS 2025, Hu et al.](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html): Main Conference, DOI 10.52202/085713-1548
- [NeurIPS 2025, DeceptionBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/55494d8756b72c2219027edc9de1ee5a-Abstract-Datasets_and_Benchmarks_Track.html): archival **Datasets and Benchmarks** track, DOI 10.52202/085713-1979; not a workshop, nor a main-track research paper
- [NeurIPS 2025, Rectifying Shortcut Behaviors](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5d97b7e62022c859347397f6c1e8d0f9-Abstract-Conference.html): Main Conference, DOI 10.52202/085713-2168; background mechanism
- [ICML 2024, Du et al.](https://proceedings.mlr.press/v235/du24e.html): PMLR 235, 11733–11763
- [ICML 2026, Pitre et al.](https://proceedings.mlr.press/v306/pitre26a.html): PMLR 306, 99003–99017
- [ICML 2026, Petrov et al.](https://proceedings.mlr.press/v306/petrov26a.html): PMLR 306, 98430–98458
- [ICLR 2025, Li et al.](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a52b0d191b619477cc798d544f4f0e4b-Abstract-Conference.html): official ICLR conference publication
- [EMNLP 2026, Alnasser et al.](https://aclanthology.org/2026.emnlp-main.1595/): main conference, DOI 10.18653/2026.emnlp-main.1595
- [NAACL 2024, Shaikh et al.](https://aclanthology.org/2024.naacl-long.348/): main conference, DOI 10.18653/v1/2024.naacl-long.348
- [ACL 2022, Ung et al.](https://aclanthology.org/2022.acl-long.447/): main conference, DOI 10.18653/v1/2022.acl-long.447

## Historical bounded ACL metadata screen (the ONLY existing source with recorded search counts)

As recorded in [survey-search.md](survey-search.md) and [screening.csv](screening.csv): 16 proceedings venue-year collections; **17,036 titles tested**; 29 title-regex matches; three title/abstract exclusions; 26 retained as *title-screened candidates*; 10 overlapping prior inventory, 16 not previously present; an additional purposive ICLR record was subsequently added. These numbers are **not** full-text studies included in a cross-database systematic review and do **not** reconcile with the updated 34-candidate reading set. No cross-platform identification, deduplication or final inclusion denominator can be computed from the present materials.

## Search design for a reproducible future database run (NOT EXECUTED as a full export)

For each source, record complete API query, exact timestamp, conference/year/track filters, retrieved record count, raw export checksum, duplicate IDs and manually screened decisions. Run three concept families and deduplicate the union:

```text
A: (sycophan* OR "user agreement" OR "conformity" OR "social pressure" OR "peer influence" OR "groupthink")
B: (apolog* OR acknowledg* OR "dialogue grounding" OR "trust repair" OR "error attribution" OR "repair")
C: ("answer revision" OR "factual correction" OR "belief updating" OR "valid feedback" OR "misleading feedback" OR "debate" OR "majority voting" OR "visual grounding")
Model context: ("large language model" OR LLM OR VLM OR MLLM OR "vision-language" OR "multi-agent" OR chatbot)
```

When using database APIs, adapt syntax per API. Do **not** require the term `sycophancy` to be in the title: NeurIPS debate studies demonstrate why broader concepts matter. Freeze a dated list of source IDs and store a retrieved-record ledger before claiming exhaustive coverage. 

## Record-level publication validation

A [34-record title/venue verification ledger](publisher-verification-ledger.md) distinguishes directly accessible publisher landing pages, separately corroborated CHI bibliographic records, and four targeted NeurIPS PDF method checks. This only validates the current candidate set and is **not a complete proceedings-level export**.

## Additional source-verification pass (21 November 2026)

After building the 34-record evidence map, the reviewer opened each recorded publisher/DOI landing URL to validate its existence, publication title and track, not to count unidentified records. **32 publisher landing pages returned directly accessible metadata.** Two CHI DOI pages were inaccessible; CHI publication details were corroborated via targeted bibliographic searches and indexed CHI/dblp publication pages. See [record-level verification ledger](publisher-verification-ledger.md).

Search queries actually used in this verification, in addition to visiting all 34 recorded URLs:

```text
"Interaction Context Often Increases Sycophancy in LLMs" CHI 2026 DOI 3772318 3791915
"Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks" CHI 2026 DOI
"Kasprova" "sycophancy" "2026" survey multi agent topologies
"Harland" "AI apology" 2025 2026 review
"Pitre" "A Diagnostic Study of Multi-Agent LLMs for Real-World Debates" 2026 2025
```

**Search type:** targeted title/venue/source corroboration, **not** a comprehensive database search. Search ranking and result totals were not captured as reproducible publication exports, so none are entered in the manuscript PRISMA identification stage. The two CHI records have independently corroborated bibliographic provenance; this is not a claim that their publisher PDFs were retrieved.

## Completed six-inventory reconciliation (distinct from systematic database retrieval)

The latest [executed screening and flow](PRISMA-bounded-executed-screen.md) contains **219 catalog sightings and 89 unique titles after 130 repeated sightings were removed**, with **34 explicitly excluded at preliminary screening and 55 sent for full-text assessment**. It combines the 52-study original inventory, 30 historical screening records (29 ACL regex title matches plus one purposive ICLR entry), 31 prior strict-core records, 69 general README records, 34 annotated core records, and three **new** publisher discoveries.

The three targeted publisher records were located using the following executed searches, then checked against official proceedings (all three had **zero previous matching occurrences** in the local five inventory files):

```text
site:openaccess.thecvf.com/content/CVPR2025 "sycophancy" "vision" "text"
site:openaccess.thecvf.com/content/CVPR2025 "vision" "language" "conflicting" "text" "visual"
site:openaccess.thecvf.com/content/CVPR2025 "misleading" "visual" language
"Words or Vision: Do Vision-Language Models Have Blind Faith in Text?" CVPR2025 abstract
"Unveiling the Ignorance of MLLMs: Seeing Clearly, Answering Incorrectly" CVPR2025
site:proceedings.mlr.press/v306/ "sycophancy" "researchers" "misalignment"
"Sycophancy Towards Researchers Drives Performative Misalignment" PMLR 306
```

**Source URLs:** [Deng et al. CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Words_or_Vision_Do_Vision-Language_Models_Have_Blind_Faith_in_CVPR_2025_paper.html), [Liu et al. CVPR 2025 publisher PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Unveiling_the_Ignorance_of_MLLMs_Seeing_Clearly_Answering_Incorrectly_CVPR_2025_paper.pdf), [Baek et al. ICML 2026](https://proceedings.mlr.press/v306/baek26d.html).

Neither these search-engine queries nor the inventory counts are an exhaustive conference proceedings export. **Web search engine results are not a stable database denominator**; no such numerator/denominator is claimed.

## Explicit later negative search hit (not counted in frozen 89)

The targeted query involving *contextual pressure* also surfaced [**ConPress: Learning Efficient Reasoning from Multi-Question Contextual Pressure** (ICML 2026)](https://proceedings.mlr.press/v306/deng26m.html). The official PMLR abstract confirms that "pressure" means fitting **multiple independent questions into one prompt** to shorten reasoning traces. There is **no interlocutor challenge, apology, acknowledgement, or evidence-vs-social-influence outcome**. It is therefore **excluded for construct mismatch**. This negative discovery was checked **after** the six-inventory repository snapshot and does **not** change the frozen 219/89/34/55 counts; it illustrates why keyword matches alone cannot determine inclusion. Search-engine results were not exported as a complete query result set.

## Reporting standards

PRISMA 2020: https://www.prisma-statement.org/prisma-2020  
PRISMA-S: https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/  

Report all searches, restrictions, updates, dates, deduplication, automation, and missing data. Search-engine hit pages are **not** substitutes for reproducible database exports.
