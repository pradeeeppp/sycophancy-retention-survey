# Publisher-linked evidence map: core candidates, not final PRISMA inclusions

**Survey:** *Agreeing for the Right Reasons: A Survey of Sycophancy, Apology, and Acknowledgement in Language, Vision-Language, and Multi-Agent Models.*

**Research snapshot:** 2026-11-21. **Status:** publisher-linked **candidate** set; title/abstract relevance assessments and historical catalog metadata. **NOT** an exhaustive database-derived inclusion sample, second-reviewer consensus, full-text critical appraisal, or complete PRISMA flow. This resource is designed for substantive reading and discussion, not to inflate a final paper count.

## Decision and methodology

- **34 unique candidate records**: 29 retained from an earlier 31-record shortlist plus 5 additional, official-proceedings-verified conference studies. Two older candidates were moved to *background* because their connection to pressure-responsive conversational behavior is indirect.
- Publication counts: ACL 6; CHI 2; EMNLP 7; ICLR 5; ICML 7; NAACL 2; NeurIPS 5. **Venue totals are descriptive, not quotas.**
- **E = essential topical relevance**, not a numerical methodological score. **S = supporting evidence**. Actual study-design appraisal, result extraction, uncertainty, and risk of bias remain unassessed unless explicitly documented. Links to official publisher records are supplied to facilitate that work.
- Main-conference-only is a *scoping decision*; one NeurIPS paper belongs to the separate peer-reviewed **archival Datasets and Benchmarks track** and is flagged separately. No workshop or preprint-only publication is counted.
- An `acknowledgement` recognizes feedback; an `apology` expresses regret/responsibility; `agreement` adopts a proposition; `update` changes belief or answer. None alone implies justified factual correction.

## Study catalog by survey question

### Sycophancy, user pressure, and correction selectivity (13 candidates)

| Publication | Role | Why the result matters / what to extract |
|---|---|---|
| [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) (ICLR 2024) | E | Tests preference-induced agreement against truthfulness across response tasks. **Extract:** Human and preference-model ranking of sycophantic versus truthful responses. [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf). |
| [ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html) (ICLR 2026) | E | Directly measures face-preserving social agreement separately from factual compliance. **Extract:** Agreement with users' self-image in controlled social scenarios. [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d3362f84979d16cee000f09eef61244c-Paper-Conference.pdf). |
| [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/) (EMNLP 2026) | S | Shows how emotional framing changes criticism and agreement. **Extract:** Rates of negative judgment, endorsement and evasion. [Publisher PDF](https://aclanthology.org/2026.emnlp-main.1184.pdf). |
| [From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning](https://proceedings.mlr.press/v235/chen24u.html) (ICML 2024) | S | Targeted anti-sycophancy tuning from official ICML proceedings. **Extract:** Sycophancy mitigation and capability tradeoffs. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/chen24u/chen24u.pdf). |
| [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412/) (NAACL 2025) | E | Tests resistance to misleading persuasion while preserving valid corrections. **Extract:** Right-to-wrong and wrong-to-right persuasion effects. [Publisher PDF](https://aclanthology.org/2025.naacl-long.412.pdf). |
| [Ask Again, Then Fail: Large Language Models’ Vacillations in Judgment](https://aclanthology.org/2024.acl-long.577/) (ACL 2024) | E | Measures unreliable reversal under repeated user challenges. **Extract:** Initially correct answer flips after follow-up. [Publisher PDF](https://aclanthology.org/2024.acl-long.577.pdf). |
| [How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html) (ICML 2026) | E | Formal explanation for preference-data amplification of sycophancy. **Extract:** Analytical amplification mechanism. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/shapira26a/shapira26a.pdf). |
| [Causally Motivated Sycophancy Mitigation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a52b0d191b619477cc798d544f4f0e4b-Abstract-Conference.html) (ICLR 2025) | E | Causal approach to preference-signal spurious correlations and head reweighting. **Extract:** Sycophancy under controlled user preference features. [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/a52b0d191b619477cc798d544f4f0e4b-Paper-Conference.pdf). |
| [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](https://proceedings.mlr.press/v306/petrov26a.html) (ICML 2026) | E | False-premise theorem proving with expert-refined incorrect statements. **Extract:** Invalid proof acceptance and failure to challenge premises. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/petrov26a/petrov26a.pdf). |
| [Real-Time Monitoring and Calibration of Chain-of-Thought Sycophancy in Large Reasoning Models](https://proceedings.mlr.press/v306/hu26bb.html) (ICML 2026) | E | Direct monitor of sycophancy in reasoning steps, not only final answers. **Extract:** Step-level pressure drift and calibration. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/hu26bb/hu26bb.pdf). |
| [PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?](https://proceedings.mlr.press/v306/pulipaka26a.html) (ICML 2026) | S | Directly evaluates memory-induced user-bias reinforcement. **Extract:** Memory-induced sycophancy versus cross-domain leakage. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/pulipaka26a/pulipaka26a.pdf). |
| [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915) (CHI 2026) | E | Evaluates personalization/memory context as causal contributor to agreement. **Extract:** Agreement sycophancy with versus without interaction context. Publisher landing only; do not invent a PDF URL. |
| [DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios](https://proceedings.neurips.cc/paper_files/paper/2025/hash/55494d8756b72c2219027edc9de1ee5a-Abstract-Datasets_and_Benchmarks_Track.html) (NeurIPS 2025; archival D&B) | S | Explicit user-appeasement dimension amid deception and coerced multi-turn settings. **Extract:** Sycophantic responses among multiple deception behaviors. [Publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/55494d8756b72c2219027edc9de1ee5a-Paper-Datasets_and_Benchmarks_Track.pdf). |

### Vision-language and video-grounded conflict (4 candidates)

| Publication | Role | Why the result matters / what to extract |
|---|---|---|
| [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) (ICLR 2025) | E | Direct image-based sycophancy benchmark and interventions. **Extract:** MM-SY visual sycophancy and mitigation. [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf). |
| [Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.1020/) (EMNLP 2025) | E | Tests misleading visual instructions against valid visual corrections. **Extract:** Evidence-sensitive visual updating. [Publisher PDF](https://aclanthology.org/2025.emnlp-main.1020.pdf). |
| [Exploring Response Uncertainty in MLLMs: An Empirical Evaluation under Misleading Scenarios](https://aclanthology.org/2025.emnlp-main.916/) (EMNLP 2025) | S | Measures initially correct image answers after misleading hints. **Extract:** Visual answer flip and uncertainty. [Publisher PDF](https://aclanthology.org/2025.emnlp-main.916.pdf). |
| [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/) (ACL 2026) | E | Benchmarks user leading cues against video evidence. **Extract:** ViSE pressure-induced video-answer changes. [Publisher PDF](https://aclanthology.org/2026.acl-long.369.pdf). |

### Multi-agent peer pressure and debate (11 candidates)

| Publication | Role | Why the result matters / what to extract |
|---|---|---|
| [Multi-LLM Debate: Framework, Principals, and Interventions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) (NeurIPS 2024) | E | Formally demonstrates majority-convergence under shared misconceptions; tests three debate interventions across four benchmark tasks. **Extract:** majority convergence versus correctness and effect of interventions. [Publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf). |
| [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) (NeurIPS 2025) | E | Disentangles majority-vote benefits from interaction; tests belief-update interventions on seven NLP benchmarks. **Extract:** vote-only versus debate accuracy, expected correctness and correction-oriented intervention. [Publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/934252acd87f254d5d4672fbde283bd2-Paper-Conference.pdf). |
| [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html) (NeurIPS 2024) | E | Compares two-sided debate, persuasive single-consultant, and direct judgment with correct/incorrect claims and information asymmetry. **Extract:** judge accuracy and susceptibility to an agent arguing for an incorrect answer. [Publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf). |
| [Multi-Agent Debate for LLM Judges with Adaptive Stability Detection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html) (NeurIPS 2025) | S | Benchmarks correctness of deliberating LLM judges versus static majority vote; adaptive stability and early consensus are relevant but interpersonal sycophancy is not isolated. **Extract:** judge accuracy, majority-vote baseline and stopping/stability metrics. [Publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/42475c537936b2394b5015e871765056-Paper-Conference.pdf). |
| [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://proceedings.mlr.press/v235/du24e.html) (ICML 2024) | S | Foundational multi-agent debate comparator; shows task-level factuality gains but does not isolate social conformity or evidence validity. **Extract:** factuality and reasoning changes relative to non-debate baselines. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf). |
| [Conformity in Large Language Models](https://aclanthology.org/2025.acl-long.195/) (ACL 2025) | E | Controlled majority-pressure manipulation on language-model conformity. **Extract:** Initial uncertainty and conformity to majority. [Publisher PDF](https://aclanthology.org/2025.acl-long.195.pdf). |
| [Do as We Do, Not as You Think: the Conformity of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html) (ICLR 2025) | E | BenchForm studies group conformity under five interaction protocols. **Extract:** Conformity rate and independence rate. [Publisher PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/1da9ca7e9cef4b1af63913f05d1630a4-Paper-Conference.pdf). |
| [When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning](https://aclanthology.org/2026.acl-long.650/) (ACL 2026) | E | Separates speaker identity influence from argument content in debates. **Extract:** Identity-driven update under anonymization. [Publisher PDF](https://aclanthology.org/2026.acl-long.650.pdf). |
| [The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment](https://aclanthology.org/2026.emnlp-main.1780/) (EMNLP 2026) | E | Tests misleading consensus when rationales remain divergent. **Extract:** Rationale alignment against answer agreement. [Publisher PDF](https://aclanthology.org/2026.emnlp-main.1780.pdf). |
| [Debate-aware Learning Makes LLMs Genuine Debaters](https://aclanthology.org/2026.emnlp-main.1907/) (EMNLP 2026) | S | Tests rebuttal engagement and updates in trained debaters. **Extract:** Debate response quality and revision. [Publisher PDF](https://aclanthology.org/2026.emnlp-main.1907.pdf). |
| [A Diagnostic Study of Multi-Agent LLMs for Real-World Debates](https://proceedings.mlr.press/v306/pitre26a.html) (ICML 2026) | E | Measures deliberation process rather than consensus alone. **Extract:** Engagement, influence asymmetry, stability, responsiveness. [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/pitre26a/pitre26a.pdf). |

### Apology, acknowledgment and dialogue repair (4 candidates)

| Publication | Role | Why the result matters / what to extract |
|---|---|---|
| [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/) (EMNLP 2026) | E | Measures apologizing, validating, and changing claims as distinct dialogue acts. **Extract:** Epistemic stance change versus apology/recognition. [Publisher PDF](https://aclanthology.org/2026.emnlp-main.1595.pdf). |
| [SaFeRDialogues: Taking Feedback Gracefully after Conversational Safety Failures](https://aclanthology.org/2022.acl-long.447/) (ACL 2022) | E | Human evaluations of acknowledging feedback after a conversational safety failure. **Extract:** Feedback response adequacy and apology. [Publisher PDF](https://aclanthology.org/2022.acl-long.447.pdf). |
| [Grounding Gaps in Language Model Generations](https://aclanthology.org/2024.naacl-long.348/) (NAACL 2024) | E | Separates dialogue grounding and mere acknowledgement. **Extract:** Clarification/acknowledgement acts. [Publisher PDF](https://aclanthology.org/2024.naacl-long.348.pdf). |
| [Talking to a Know-It-All GPT or a Second-Guesser Claude? How Repair reveals distinct Multi-Turn Behavior in LLMs](https://aclanthology.org/2026.acl-long.651/) (ACL 2026) | E | Compares justified and misleading attempts at dialogue repair. **Extract:** Who initiates repair and resulting correctness. [Publisher PDF](https://aclanthology.org/2026.acl-long.651.pdf). |

### Human interaction and consequences (1 candidates)

| Publication | Role | Why the result matters / what to extract |
|---|---|---|
| [Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks](https://doi.org/10.1145/3772318.3791365) (CHI 2026) | E | Human experiment on learner misconceptions and sycophantic feedback. **Extract:** Novice task performance, misconceptions and over-reliance. Publisher landing only; do not invent a PDF URL. |

### Other methods / cross-cutting studies

- [Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://aclanthology.org/2026.emnlp-main.2533/) (EMNLP 2026; E) — Causally distinguishes praise, genuine agreement and sycophantic agreement. Extract: Representation separation and intervention.

**Full-text method checks:** Four NeurIPS main-conference papers have a separate [publisher-PDF-grounded extraction](../research/NeurIPS-full-text-evidence.md); the rest of this candidate map remains abstract-level until similarly extracted.

## Five new, source-verified studies and critical boundaries

### Estornell & Liu (NeurIPS 2024): majority is not evidence

[Official proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) · [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf). The paper provides formal results for static debate dynamics under agents with similar responses and tests three interventions on four benchmarks. **Use it to compare a collective misconception with independently grounded evidence**. Do **not** claim that all majority agreement is sycophancy; the paper is about the failure of debate under shared mistakes.

### Choi, Zhu & Li (NeurIPS 2025): vote vs genuine debate

[Official proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) · [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/934252acd87f254d5d4672fbde283bd2-Paper-Conference.pdf). Separates gains from multi-sample voting and interactive belief updates on seven NLP benchmarks; proposes interventions aimed at correcting errors. The paper directly limits the claim that convergence is evidence of productive disagreement. **Do not conflate majority-vote accuracy with individual agents' susceptibility to pressure.**

### Kenton et al. (NeurIPS 2024): an agent can persuade a weak judge

[Official proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html) · [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf). Compares debate, consultancy, and direct answers under correctness and knowledge asymmetries, including multimodal tasks. This directly informs *evidence vs persuasive source*, but it is an oversight/judge experiment, not a direct measurement of user-directed apologies.

### Hu et al. (NeurIPS 2025): consensus and judge accuracy

[Official proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html) · [Official PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/42475c537936b2394b5015e871765056-Paper-Conference.pdf). Evaluates a debate-based LLM judging approach with adaptive stability detection against static majority voting. **Supporting** rather than essential for sycophancy; the study does not explicitly isolate unwarranted interpersonal agreement.

### Du et al. (ICML 2024): what debate was expected to achieve

[Official proceedings](https://proceedings.mlr.press/v235/du24e.html) · [Publisher PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/du24e/du24e.pdf). A foundational baseline showing that multi-instance debate can improve reasoning and factuality. **Supporting** comparator, not evidence that a debate gain was caused by agents selecting stronger evidence over social pressure.

## Boundary/exclusion decisions

| Paper | Disposition | Defensible reason |
|---|---|---|
| [Rectifying Shortcut Behaviors in Preference-based Reward Learning (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5d97b7e62022c859347397f6c1e8d0f9-Abstract-Conference.html) | **Background** | Published main track, but sycophancy is one example of a broader preference-shortcut problem; direct answer revision / apology not isolated in publisher abstract |
| [Spurious Correlation Learning in Preference Optimization (ICML 2026)](https://proceedings.mlr.press/v306/moya26a.html) | **Background**, moved from previous core | Training mechanism only; no clearly isolated evidence-vs-pressure conversational outcome in the prior shortlist |
| [One Bias After Another (ICML 2026)](https://proceedings.mlr.press/v306/fein26a.html) | **Background**, moved from previous core | Broad reward-model bias with less direct behavioral alignment to the survey's operational outcomes |
| [Metacognitive Monitoring of Internal Activations (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56a225639da77e8f7c0409f6d5ba996b-Abstract-Conference.html) | **Exclude** | Uses synthetic sycophancy examples, but main outcome is control of internal activations, not evidence-justified conversational revision |
| [CVPRW 2026: To Agree or To Be Right?](https://openaccess.thecvf.com/content/CVPR2026W/Med-Reasoner/html/Aranya_To_Agree_or_To_Be_Right_The_Grounding-Sycophancy_Tradeoff_in_CVPRW_2026_paper.html) | **Exclude from conference main-track core** | Relevant multimodal study, but published at a workshop; may be cited as clearly identified contextual evidence |
| [SYCON Bench (Findings of EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.121/) | **Contextual citation, not strict core** | The introduction discusses it; Findings is peer-reviewed but **not the EMNLP main proceedings** |
| [AI apology: a critical review (2025)](https://doi.org/10.1007/s10462-025-11305-8) | **Background** | Secondary journal review, rather than primary main-conference evidence |
| [Who's Sorry Now (2026)](https://doi.org/10.1145/3793679) | **Contextual human-apology evidence** | TOCHI journal rather than CHI conference paper |

## How to use this evidence in the manuscript

1. **Define correctness before discussing answer flips:** assess original correctness, external evidence/feedback validity, and final correctness independently. For subjective disputes where ground truth is unavailable, label *stance shift* instead of correctness.
2. **Distinguish verbal acts from epistemic results:** code apology, validation, acknowledgment, refusal, confidence, and factual revision as separate variables.
3. **In VLMs** require image/video-grounding baseline before adding a misleading language cue; quantify false-hint-induced flips and acceptance of valid visual feedback separately.
4. **In multi-agent experiments** record individual private answer, argument content, peer identities, voting protocol, round count, and final truthfulness; consensus alone is insufficient.
5. **Synthesis without meta-analysis is likely appropriate** unless studies share compatible tasks, denominators, outcomes, and intervention definitions. Do not pool heterogeneous flip rates or trust scales.
6. **Human effects are not user retention:** immediate trust, dependence, judgment accuracy, and long-term return are distinct constructs.

## Critical transparency

This Markdown file is a candidate reading guide, not a claim that 34 reports were retrieved, fully read, methodologically scored, or included by a two-reviewer systematic screening process. Consult [PRISMA audit](../research/PRISMA-2020-audit.md), [search provenance](../research/PRISMA-search-provenance.md), and [evidence comparison](../research/evidence-synthesis.md) before writing the methods/results sections. No publisher PDF binaries were mirrored to GitHub; use official download links and verify redistribution licenses individually.
