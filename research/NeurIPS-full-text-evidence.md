# Source-checked NeurIPS full-text evidence: four main-conference papers

**Review date:** 21 November 2026. **Review method:** targeted inspection of the publisher's official, accepted NeurIPS PDF versions and named method/results sections. A single assistant extracted the observations below. This is **not** independent dual-reviewer screening or a full-text appraisal of all 34 candidate studies.

**Scope:** In the strict conference core, distinguish an actual manipulated *incorrect claim or weak evidence* from an improvement in aggregated problem-solving. None of these four experiments directly measures whether an assistant apologizes to a user; each informs the **multi-agent influence and evidence-dependent correction** part of the manuscript.

## Source 1 — Estornell and Liu (NeurIPS 2024)

**Multi-LLM Debate: Framework, Principals, and Interventions**  
[Official main-track entry](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) · [Accepted PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf) · DOI **10.52202/079017-0911**.

**Study design and evidence:** formalize multi-model debate as exchange of responses across rounds, and examine convergence to a majority, including majorities carrying a common misconception. Evaluate three interventions—**diversity pruning**, **quality pruning**, and **misconception refutation**—against vanilla debate. The experiments use **BoolQ, an MMLU high-school subset, TruthfulQA and MathQ** (PDF pp. 7–8; source PDF pp. 1–2 introduction and p. 7 experimental design). Reported model families include GPT-3.5, Llama-2, Llama-3 and Mistral. BoolQ/MMLU/MathQ correctness is matched to answers, while TruthfulQA uses a **GPT-4 judge**; therefore the metrics differ in ground-truth certainty. Their ablations show the **combined** intervention performs more consistently than isolated interventions (PDF appendix, pp. 18–19).

**Eligibility decision: directly relevant; retain as an essential multi-agent mechanism study.** Main-conference official PDF verified. It bears on *consensus without reliable evidence*. **Critical caution:** convergence to an erroneous majority from shared misconceptions is not, by itself, proof that each agent socially defers to peers; correlated prior knowledge and independent errors are possible. A GPT-4-generated truthfulness judgment has different error properties from exact-match labeling.

**Cross-paper use:** compare with Choi et al. on when repeated peer exchange improves accuracy beyond aggregation, and with identity-weighted debate studies on whether social/role influence is independently manipulated.

## Source 2 — Choi, Zhu and Li (NeurIPS 2025)

**Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?**  
[Official main-track entry](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) · [Accepted PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/934252acd87f254d5d4672fbde283bd2-Paper-Conference.pdf) · DOI **10.52202/085713-3405**.

**Study design and evidence:** compare single agents, **majority vote without debate (T=0)**, and decentralized/sparse/centralized multi-agent debate; the principal experiment uses **five agents** and **seven benchmark datasets** spanning arithmetic, mathematical reasoning, factual QA, natural-language inference, commonsense, and preference-labeling (PDF pp. 3–4). They find **most apparent gains are attributable to majority voting**, not interactive discussion, and analyze belief trajectories under specified stochastic assumptions. They test correction-oriented interventions. Their published argument is conditional on the mathematical/model assumptions described in the article and appendices, not a universal impossibility theorem about all debate architectures.

**Eligibility decision: directly relevant; retain as an essential comparator.** Crucial for testing the manuscript's claim that consensus/answer changes do not necessarily reflect evidence-based revision. **Critical caution:** ordinary vote aggregation is not a conversational influence exposure; compare it to debate only with matched samples, benchmarks and costs. Not an apology or acknowledgment experiment.

**Cross-paper use:** the introduction should state that convergence alone is insufficient evidence of improved reasoning, and draw a clear boundary between multiple independent samples (vote) and peer-influenced belief updates.

## Source 3 — Kenton et al. (NeurIPS 2024)

**On scalable oversight with weak LLMs judging strong LLMs**  
[Official main-track entry](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html) · [Accepted PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf) · DOI **10.52202/079017-2395**.

**Study design and evidence:** compare **two-sided debate**, **one-sided consultancy**, and **direct question answering** with weaker LLM-based judge models. Evaluate **assigned-argument roles** where the consultant/debater must argue for a randomly assigned correct **or incorrect** proposition, and **open-role** settings where agents choose an answer. Includes extractive QA with information asymmetry, mathematics, coding, logic and multimodal reasoning tasks (PDF pp. 1–2, 5–6). The selected assigned-role protocol uses **three interaction rounds** and best-of-four response selection; main figures display **judge-accuracy confidence intervals**.

**Eligibility decision: directly relevant to evidence versus persuasion; essential for the survey's peer influence discussion.** The intentional correct-versus-incorrect advocate condition is especially valuable, although this is an **oversight/judging** setting rather than a user's conversational correction.

**Critical caution:** the *judges are LLM stand-ins for humans*, so findings cannot be transferred directly to human belief revision. Oversight accuracy is a distinct unit of analysis from the initial/final response of a single assistant.

**Cross-paper use:** contrast agent-persuasive influence under correct/incorrect advocacy with agreement pressure in conversational assistants; explain why multimodal oversight is not the same as VLM sycophancy under misleading visual-text hints.

## Source 4 — Hu et al. (NeurIPS 2025)

**Multi-Agent Debate for LLM Judges with Adaptive Stability Detection**  
[Official main-track entry](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html) · [Accepted PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/42475c537936b2394b5015e871765056-Paper-Conference.pdf) · DOI **10.52202/085713-1548**.

**Study design and evidence:** propose a debate process for LLM judges and dynamic stopping via a **time-varying Beta-Binomial mixture** and Kolmogorov–Smirnov criterion; compare judging accuracy with majority voting (PDF first page, §4–§6). The reported experiment setup includes **seven-agent ensembles, up to ten rounds**, sampling temperature 1.0 (PDF appendix). One theoretical assumption explicitly treats agent responses as **conditionally independent**, while noting that copying, shared biases or referencing peers may violate it (PDF p. 5).

**Eligibility decision: supporting contextual comparator, not direct sycophancy measurement.** Main-conference track verified; judge accuracy and consensus process are relevant, but no isolated variable establishes whether agreement is driven by interpersonal compliance versus the substantive strength of peer evidence.

**Critical caution:** a higher voting/debate score may be caused by improved aggregation. Independence-based results may not generalize to agents copying one another, which is specifically relevant to the surveyed failure mode.

## Structured comparison of the four source-checked studies

| Study | Incorrect influence independently represented? | Initial/final truth test? | Primary recorded behavior | Construct fit |
|---|---|---|---|---|
| Estornell & Liu 2024 | Common misconception and majority-target interventions | Task answer accuracy with mixed exact-match/LLM judgments | Debate convergence, corrected answer accuracy, intervention ablations | Directly informs wrong-consensus mechanism; not direct user sycophancy |
| Choi, Zhu & Li 2025 | Comparison vote vs debate rather than assigned false claim | Benchmark answer accuracy and belief trajectories | Improvement attributable to voting vs debate | Essential methodological comparator |
| Kenton et al. 2024 | **Yes: assigned correct vs incorrect argument** | Judge chooses correct versus incorrect proposition | Judge accuracy under competitive persuasion or consultancy | Strong evidence-vs-persuasion comparator |
| Hu et al. 2025 | Not isolated | Judge accuracy and stability | Group judging and adaptive stopping | Supporting only; no sycophancy-specific measure |

### Audit trail and limits

The four PDFs were checked through the official publisher pages and inspected by source page. This extraction is **not** a pooled result and does not claim that independent reviewers assessed the articles. No risk-of-bias number, certainty score, or invented effect-size estimate has been assigned. One paper's accuracy improvement is not commensurable with another's debate-consensus probability without harmonized denominators and interventions. The fifth NeurIPS archive candidate, **DeceptionBench (2025, archival Datasets & Benchmarks)**, has **not** been full-text extracted in this note. It remains supporting and outside the four main-conference studies documented here.

See [the full candidate map](../literature/prisma-core-papers.md), [PRISMA report](PRISMA-2020-audit.md), and [evidence synthesis](evidence-synthesis.md). 
