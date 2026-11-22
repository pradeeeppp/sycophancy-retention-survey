# Cross-venue correction: discovery evidence and decisions

**Date:** 2026-11-21. **Goal:** correct the previous ACL-heavy 31-paper shortlist, not to construct fictional PRISMA totals.

## What went wrong previously

25 of the previous 31 priority records came from the ACL family (ACL 11, EMNLP 10, NAACL 2, EACL 2), versus ICLR 4 and ICML 2. This reflects narrow discovery coverage, not a scientifically justified venue distribution. The repository's prior 69-study catalog was not a main-conference-only, full-text-screened PRISMA inclusion set. The previous main-conference manifest lacked important published ICLR, ICML and CHI work.

## Actual discovery route used in this correction

This update used targeted web searches against publisher landing pages, in addition to the repo's existing list. Example executed queries (these are *directional discovery queries*, **not** a complete database search or export):

```text
site:proceedings.neurips.cc/paper_files/paper sycophancy large language models preference 2024 2025 2026
site:proceedings.mlr.press sycophancy ICLR ICML 2025 2026 reasoning
site:proceedings.iclr.cc/paper_files/paper/2025 sycophancy conformity agreement
site:openaccess.thecvf.com sycophancy multimodal vision language model CVPR 2024 2025 2026
site:openaccess.thecvf.com/content/ICCV2025 sycophancy multimodal misleading visual
site:dl.acm.org/doi/10.1145 LLM sycophancy user trust 2025 CHI 2026
"Interaction Context Often Increases Sycophancy in LLMs" CHI 2026
"Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks" CHI 2026 proceedings
site:proceedings.neurips.cc/paper_files/paper/2025/hash sycophancy "we introduce" benchmark
```

Sources are distinct: [ICLR proceedings](https://proceedings.iclr.cc/), [PMLR ICML proceedings](https://proceedings.mlr.press/v306/), [NeurIPS proceedings](https://proceedings.neurips.cc/), [CHI ACM publication DOI](https://doi.org/10.1145/3772318.3791915), [ACL Anthology](https://aclanthology.org/), and [CVF proceedings](https://openaccess.thecvf.com/).

**Important honesty:** This list of queries is not comprehensive; interface-dependent search ranking does not yield an auditable denominator. No number of search results retrieved, deduplicated, excluded at full-text or finally included can be inferred from it.

## Candidate-level decisions of particular importance

| Candidate | Publication check | Decision and reason |
|---|---|---|
| [ICLR 2025, Causally Motivated Sycophancy Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a52b0d191b619477cc798d544f4f0e4b-Abstract-Conference.html) | ICLR official proceedings | **Essential:** direct causal intervention against user-preference confounding |
| [ICML 2026, BrokenMath](https://proceedings.mlr.press/v306/petrov26a.html) | PMLR vol. 306 | **Essential:** expert-refined false mathematical premises |
| [ICML 2026, Real-Time CoT Sycophancy](https://proceedings.mlr.press/v306/hu26bb.html) | PMLR vol. 306 | **Essential:** intermediate-step sycophancy measurement |
| [ICML 2026, Real-World Multi-Agent Debates](https://proceedings.mlr.press/v306/pitre26a.html) | PMLR vol. 306 | **Essential:** debate process rather than consensus alone |
| [ICML 2026, Spurious Correlation Learning](https://proceedings.mlr.press/v306/moya26a.html) | PMLR vol. 306 | **Essential:** explain preference-driven spurious learning |
| [ICML 2026, PersistBench](https://proceedings.mlr.press/v306/pulipaka26a.html) | PMLR vol. 306 | **Supporting:** memory-induced sycophancy directly measured; narrower personalization setting |
| [CHI 2026, Invisible Saboteurs](https://doi.org/10.1145/3772318.3791365) | ACM CHI 2026 article, DOI corroborated by dblp | **Essential:** experimental human consequences of excessive agreement |
| [CHI 2026, Interaction Context](https://doi.org/10.1145/3772318.3791915) | ACM CHI 2026 proceedings, article 793 | **Essential:** real interaction history and user memory effects |
| [NeurIPS 2025, DeceptionBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/55494d8756b72c2219027edc9de1ee5a-Abstract-Datasets_and_Benchmarks_Track.html) | Archival Datasets and Benchmarks track; **not a workshop** | **Supporting:** user appeasement/sycophancy is one measured component of a broader deception benchmark |
| [NeurIPS 2025, Rectifying Shortcut Behaviors](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5d97b7e62022c859347397f6c1e8d0f9-Abstract-Conference.html) | Main track | **Defer:** valid publication but abstract only mentions sycophancy as one shortcut; does not clearly isolate a sycophancy-specific outcome |
| [CVPR 2026, To Agree or To Be Right?](https://openaccess.thecvf.com/content/CVPR2026W/Med-Reasoner/html/Aranya_To_Agree_or_To_Be_Right_The_Grounding-Sycophancy_Tradeoff_in_CVPRW_2026_paper.html) | **CVPR Workshops** explicitly | **Exclude from strict core:** excellent topical fit, wrong track; use as background if desired |
| [CHI/TOCHI 2026, Who's Sorry Now](https://doi.org/10.1145/3793679) | ACM Transactions on Computer-Human Interaction journal | **Exclude from conference-only core:** useful apology paper, not a CHI conference proceedings paper |
| [ICML 2026, Position: Sycophancy Is an Educational Safety Risk](https://proceedings.mlr.press/v306/kasneci26a.html) | PMLR position paper | **Exclude from empirical core:** position piece rather than directly comparable primary result |
| [NeurIPS 2025 Workshop, Sycophancy Claims about Language Models: The Missing Human-in-the-Loop](https://arxiv.org/abs/2512.00656) | Workshop / preprint only | **Exclude:** not a main conference proceedings study |

## Next steps before manuscript PRISMA

1. Export **all title/abstract records** per source, with search strings, date, source identifiers, track filter and retrieval counts.
2. Deduplicate and screen **the whole retrieved universe** (not just this shortlist); retain every exclusion reason.
3. Two human reviewers independently verify full text and extraction if the research team can support it.
4. Create PRISMA 2020 flow only from reconciled export and screening ledger; report database and citation-chasing routes separately.

Nothing here asserts a finished systematic literature review or suggests that an abstract assessment equals full-text verification.
