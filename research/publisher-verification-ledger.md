# Record-level publisher and conference-track verification

**Audit date:** 2026-11-21 (America/Los_Angeles). **Reviewer:** single assistant using publicly accessible official proceeding records and cross-checks; no separate human verification. **Corpus:** the **34 *already-curated* candidate records** in [the paper map](../literature/prisma-core-papers.md), not an exhaustive output from a multi-database search.

## Findings

- **34 of 34 catalog records have publisher or official DOI URL identifiers; no arXiv link is used as the recorded publication.** 
- **32 of 34 official publisher/proceedings landing pages were directly accessible for title and track checking in this pass.** The two CHI DOI redirect pages returned access restrictions; their status was corroborated through CHI proceedings indexing in ACM search results and DBLP (see notes below). Direct access and indirect corroboration are **not equivalent**.
- **5 NeurIPS** entries include **four Main Conference and one archival Datasets and Benchmarks**, which must not be described as five main-track studies.
- **2 CHI** entries are ACM CHI 2026 proceedings papers, *not* TOCHI journal or workshop papers.
- No exact venue counts in this file are being represented as systematic-review identification counts; this only verifies the known candidate selection.

## Verification ledger

| # | Published paper (publisher landing) | Venue and year | Audit outcome | Depth |
|---:|---|---|---|---|
| 1 | [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) | ICLR 2024 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 2 | [ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html) | ICLR 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 3 | [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/) | EMNLP 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 4 | [From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning](https://proceedings.mlr.press/v235/chen24u.html) | ICML 2024 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 5 | [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412/) | NAACL 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 6 | [Ask Again, Then Fail: Large Language Models’ Vacillations in Judgment](https://aclanthology.org/2024.acl-long.577/) | ACL 2024 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 7 | [How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html) | ICML 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 8 | [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a52b0d191b619477cc798d544f4f0e4b-Abstract-Conference.html) | ICLR 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 9 | [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](https://proceedings.mlr.press/v306/petrov26a.html) | ICML 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 10 | [Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models](https://proceedings.mlr.press/v306/hu26bb.html) | ICML 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 11 | [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?](https://proceedings.mlr.press/v306/pulipaka26a.html) | ICML 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 12 | [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915) | CHI 2026 | **Indexed / DOI corroborated**; DOI fetch was blocked | Publisher DOI / bibliographic indexing; no direct PDF |
| 13 | [DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios](https://proceedings.neurips.cc/paper_files/paper/2025/hash/55494d8756b72c2219027edc9de1ee5a-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2025; archival D&B | **Official archival D&B** (not main) | Title + abstract/proceedings metadata checked |
| 14 | [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) | ICLR 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 15 | [Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.1020/) | EMNLP 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 16 | [Exploring Response Uncertainty in MLLMs: An Empirical Evaluation under Misleading Scenarios](https://aclanthology.org/2025.emnlp-main.916/) | EMNLP 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 17 | [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/) | ACL 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 18 | [Multi-LLM Debate: Framework, Principals, and Interventions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) | NeurIPS 2024 | **Official proceeding record located** | Publisher PDF methods examined |
| 19 | [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) | NeurIPS 2025 | **Official proceeding record located** | Publisher PDF methods examined |
| 20 | [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html) | NeurIPS 2024 | **Official proceeding record located** | Publisher PDF methods examined |
| 21 | [Multi-Agent Debate for LLM Judges with Adaptive Stability Detection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html) | NeurIPS 2025 | **Official proceeding record located** | Publisher PDF methods examined |
| 22 | [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://proceedings.mlr.press/v235/du24e.html) | ICML 2024 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 23 | [Conformity in Large Language Models](https://aclanthology.org/2025.acl-long.195/) | ACL 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 24 | [Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html) | ICLR 2025 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 25 | [When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning](https://aclanthology.org/2026.acl-long.650/) | ACL 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 26 | [The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment](https://aclanthology.org/2026.emnlp-main.1780/) | EMNLP 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 27 | [Debate-aware Learning Makes LLMs Genuine Debaters](https://aclanthology.org/2026.emnlp-main.1907/) | EMNLP 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 28 | [A Diagnostic Study of Multi-Agent LLMs for Real-World Debates](https://proceedings.mlr.press/v306/pitre26a.html) | ICML 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 29 | [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/) | EMNLP 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 30 | [SaFeRDialogues: Taking Feedback Gracefully after Conversational Safety Failures](https://aclanthology.org/2022.acl-long.447/) | ACL 2022 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 31 | [Grounding Gaps in Language Model Generations](https://aclanthology.org/2024.naacl-long.348/) | NAACL 2024 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 32 | [Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals distinct Multi-Turn Behavior in LLMs](https://aclanthology.org/2026.acl-long.651/) | ACL 2026 | **Official proceeding record located** | Title + abstract/proceedings metadata checked |
| 33 | [Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks](https://doi.org/10.1145/3772318.3791365) | CHI 2026 | **Indexed / DOI corroborated**; DOI fetch was blocked | Publisher DOI / bibliographic indexing; no direct PDF |
| 34 | [Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://aclanthology.org/2026.emnlp-main.2533/) | EMNLP 2026; E | **Official proceeding record located** | Title + abstract/proceedings metadata checked |

## Additional publication evidence for the two CHI records

- [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915), **CHI 2026 article 793**, verified through [ACM search-index publication listing](https://dl.acm.org/doi/10.1145/3772318.3791915) and [DBLP bibliographic record](https://dblp.org/rec/conf/chi/JainPVWC26.html); the DOI resolver was inaccessible to the web fetcher. This is a **conference proceeding**. No direct publisher PDF URL was inferred.
- [Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks](https://doi.org/10.1145/3772318.3791365), **CHI 2026 article 1258**, corroborated through [DBLP](https://dblp.org/rec/conf/chi/BoKDIA26.html). DOI resolver was inaccessible. The available author-hosted manuscript is **not** treated as the publisher copy or a preprint-only inclusion.
- All the other core rows were checked against their corresponding published title/proceedings landing pages, not only a search-engine snippet. **Four NeurIPS main-conference PDFs** were additionally inspected for experimental conditions; see [source-grounded full-text notes](NeurIPS-full-text-evidence.md).

## Verification boundaries and independence

The prior selection used topical relevance, not a predefined exhaustive corpus. Checking 34/34 selected records **does not establish** that all eligible publications were identified; that requires full venue/export searches, duplicate record reconciliation and a study-level PRISMA flow. The two CHI DOI pages remain not directly retrievable in this browsing environment; their publication records were corroborated elsewhere.

Neither this ledger nor its counts prove that the 34 have been full-text screened, appraised for risk-of-bias, independently reviewed, or included in the final systematic synthesis. This wording is deliberate: source verification and PRISMA completeness are different milestones.
