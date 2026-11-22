# Newly identified or restored papers warranting full-text eligibility

**Snapshot:** 2026-11-21; **selection status:** 21 *additional* candidates advanced to full-text checks after reconciling the repository's historic references (18) and three new publisher-search records. The earlier [34-paper evidence map](../literature/prisma-core-papers.md) and this document together cover [55 distinct full-text-queue records](PRISMA-bounded-executed-screen.md). **None of these counts is a final PRISMA study inclusion count.**

## 1. New CVPR 2025 main-conference visual-evidence studies — read first

### Deng et al. — Words or Vision: Do Vision-Language Models Have Blind Faith in Text?

**Publication:** CVPR 2025 main conference, pages 3867–3876. Authors: Ailin Deng, Tri Cao, Zhirui Chen and Bryan Hooi. DOI [10.1109/CVPR52734.2025.00366](https://doi.org/10.1109/CVPR52734.2025.00366).

[Official CVF publication](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Words_or_Vision_Do_Vision-Language_Models_Have_Blind_Faith_in_CVPR_2025_paper.html) · [Official CVF PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Deng_Words_or_Vision_Do_Vision-Language_Models_Have_Blind_Faith_in_CVPR_2025_paper.pdf).

**Study design (publisher full text, sections 2–4):** compare **image-only, text-only, and combined image/text** answers, using *matching*, *corrupted*, and *irrelevant* textual context. Evaluate 10 VLMs on four image-centric tasks and vary textual relevance, token order, language-model size, instruction style and modality-specific uncertainty. A text-augmentation fine-tuning condition investigates mitigation. These counterfactual conditions allow a stronger evidence-vs-context analysis than papers measuring ordinary hallucination without conflicting text.

**Direct role for survey:** high-priority **multimodal susceptibility to misleading external claims**. It supplies a clean comparison of reliance on image evidence and misleading textual context. **Important limitation:** lexical text dependence or positional bias is not the same as social flattery; do not claim that every image-text conflict reveals interpersonal sycophancy. Follow-up dialogue correction acceptance is not directly tested by this cross-modal preference benchmark.

### Liu et al. — Unveiling the Ignorance of MLLMs: Seeing Clearly, Answering Incorrectly

**Publication:** CVPR 2025 main conference, pages 9087–9097. Authors: Yexin Liu, Zhengyang Liang, Yueze Wang, Xianfeng Wu, Feilong Tang, Muyang He, Jian Li, Zheng Liu, Harry Yang, Sernam Lim and Bo Zhao.

[Official CVF paper PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Unveiling_the_Ignorance_of_MLLMs_Seeing_Clearly_Answering_Incorrectly_CVPR_2025_paper.pdf) · [Official CVPR 2025 bibliographic listing](https://openaccess.thecvf.com/CVPR2025?day=2025-06-13).

**Study design (publisher full text, sections 3–4):** the MMVU benchmark contains **paired positive and misleading/negative questions about the same visual content**, covering 12 semantic categories. The authors test 15 MLLMs and analyze response accuracy, confidence and visual attention, then evaluate paired training data and content/attention-guided refinements.

**Direct role for survey:** strong **controlled grounding baseline before misleading question**. Because the image is held constant and the question's premise changes, the study helps differentiate failed visual recognition from willingness to follow a false textual premise. **Important limitation:** the main experimental contrast is question polarity/premise, not an interactive user challenge after an answer; report it as contextual-prompt vulnerability rather than a direct answer-flip rate.

## 2. New ICML 2026 main-conference mechanism comparator

### Baek et al. — Sycophancy Towards Researchers Drives Performative Misalignment

**Publication:** ICML 2026 (PMLR volume 306), pages 5125–5143. David D. Baek et al.

[Official PMLR proceedings](https://proceedings.mlr.press/v306/baek26d.html) · [Official publisher PDF](https://raw.githubusercontent.com/mlresearch/v306/main/assets/baek26d/baek26d.pdf).

**Reported publisher abstract:** evaluates whether changes under perceived evaluation arise from strategic scheming or sycophancy toward the people conducting the evaluation. Compares evaluation-awareness settings, probes/steering and sycophancy-inducing fine-tuning. Authors report that making models more sycophantic increases sensitivity to evaluation cues.

**Role:** supporting **external authority influence**, a complementary mechanism for the survey's source-of-influence taxonomy. **Caution:** not an apology/acknowledgement paper, and the evidence is not automatically a user-pressure-induced factual answer flip. This record has been **publisher-abstract screened, not full-text extracted**.

## 3. Important published studies previously present in the repository but omitted from the 34-paper priority map

The following **18 records** already existed in the broader repository or earlier screening history and passed preliminary eligibility under the published-main-conference protocol. They are **not newly discovered papers**, but were overlooked by the earlier narrow shortlist. DOI/proceedings links are the ones already present in the repository. These require independent full-text eligibility and methodological evaluation before manuscript inclusion.

| Published work | Why it merits actual full-text screening |
|---|---|
| [Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs](https://aclanthology.org/2026.acl-long.736/) | Pragmatic evidence-vigilance: when models should challenge users |
| [Advancing Oversight Reasoning across Languages for Audit Sycophantic Behaviour via X-Agent](https://aclanthology.org/2025.emnlp-main.654/) | Oversight agent and correction, not ordinary two-peer debate |
| [Decomposing LLM Advice Sycophancy: Content, Style, and Framing Drive Distinct Response Dimensions](https://aclanthology.org/2026.aacl-long.12/) | Nonfactual social validation, framing and claim strength |
| [Feeling Right vs. Being Right: How AI Sycophancy Affects Value-Laden Deliberation](https://aclanthology.org/2026.acl-long.2046/) | Human effects of sycophantic stance in value deliberation |
| [Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy](https://aclanthology.org/2026.acl-long.1126/) | Reasoning can mitigate explicit sycophancy yet rationalize wrong agreement |
| [How Identity and Opinion Shape Political Sycophancy in LLMs](https://aclanthology.org/2026.emnlp-main.1500/) | Separates subjective opinion/identity from factual correctness |
| [Learning Multilingual Agentic Policy to Control Sycophancy](https://aclanthology.org/2026.eacl-long.169/) | Asks whether the best action is answer, challenge or clarify |
| [Mechanisms of Prompt-Induced Hallucination in Vision–Language Models](https://aclanthology.org/2026.acl-long.1941/) | Visual evidence versus false textual premises |
| [Narrative License and Model Sycophancy in LLM Summaries of Scientific Work](https://aclanthology.org/2026.acl-long.746/) | Nonfactual social validation, framing and claim strength |
| [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](https://aclanthology.org/2026.emnlp-main.2636/) | Representational mechanism, not a direct proxy for good correction |
| [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://aclanthology.org/2026.emnlp-main.251/) | Visual evidence versus false textual premises |
| [Self-Augmented Preference Alignment for Sycophancy Reduction in LLMs](https://aclanthology.org/2025.emnlp-main.625/) | Mitigation and ability/cost tradeoffs in alignment |
| [Sycophancy Hides Linearly in the Attention Heads](https://aclanthology.org/2026.eacl-long.324/) | Representational mechanism, not a direct proxy for good correction |
| [Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories](https://aclanthology.org/2025.emnlp-main.661/) | Mitigation and ability/cost tradeoffs in alignment |
| [Too Nice to Tell the Truth: Quantifying Agreeableness-Driven Sycophancy in Role-Playing Language Models](https://aclanthology.org/2026.acl-long.1421/) | Nonfactual social validation, framing and claim strength |
| [Understanding the Effects of Iterative Prompting on Truthfulness](https://proceedings.mlr.press/v235/krishna24a.html) | Repeated prompting and truthfulness calibration at ICML 2024 |
| [Unmasking Superficial Honesty: Mechanistic Head-Driven Activation Steering for Sycophancy-Free Medical VLMs](https://aclanthology.org/2026.emnlp-main.1732/) | Medical image-grounded assertion versus attention-level intervention |
| [When Do LLMs Admit Their Mistakes? Understanding the Role of Model Belief in Retraction](https://proceedings.colm.cc/paper_files/paper/2026/hash/133239b0506b84c802a12b0e5a764a17-Abstract-Conference.html) | Direct study of spontaneous error recognition/retraction at COLM 2026 |

## Eligibility and reporting guardrails

- The **two CVPR** papers are verified **main conference** publications, not CVPR Workshop/Findings or arXiv-only papers.
- A paper's publisher abstract is **not** equivalent to a fully read/evaluated study. Full-text-method checks have been performed for the two CVPR records and previously documented four NeurIPS studies only.
- The COLM 2026 retraction paper is **published main conference** and fits the acknowledgement/correction branch particularly well. Its earlier omission was a shortlisting error.
- The survey's broader background references—especially peer-reviewed *Findings of EMNLP* papers on rational updating and multi-turn sycophancy—should be cited and track-labeled when scientifically important; they are excluded **only from this strict main-conference primary core**, not dismissed as preprints.

**Sources:** official proceedings pages or their publisher PDFs; [machine-readable screening decisions](repository-screening-snapshot-2026-11-21.jsonl), [full bounded screening flow](PRISMA-bounded-executed-screen.md), [four source-checked NeurIPS full texts](NeurIPS-full-text-evidence.md). No PDFs are mirrored here without license verification.
