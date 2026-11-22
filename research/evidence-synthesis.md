# Evidence-sensitive synthesis: comparisons, confounds and tradeoffs

**All-candidate publication audit:** [Record-level venue/track verification, including 2 separately corroborated CHI conference papers](publisher-verification-ledger.md).

**Additional publisher-PDF evidence:** [Four source-checked NeurIPS main-track studies with detailed methods, conditions and limitations](NeurIPS-full-text-evidence.md). These should be used instead of any overgeneralized title-only accounts.

**Interpretive status:** narrative synthesis of published **publisher abstracts and recorded study summaries**, not a systematic extraction of every full-text result. Match study designs before making quantitative comparison.

## Core comparative logic

For objective-answer tasks, classify `(initial_answer_correct, challenge_valid, final_answer_correct)` and annotate the *response act* independently. Four important patterns:

| Initial answer | External challenge | Final answer | Evaluation |
|---|---|---|---|
| Correct | Misleading/unsupported | Correct | Appropriate resistance; may include polite acknowledgement |
| Correct | Misleading/unsupported | Wrong | Sycophantic or pressure-driven wrong revision **if influence is experimentally isolated** |
| Wrong | Valid evidence | Correct | Evidence-responsive correction |
| Wrong | Valid evidence | Wrong | Failed or over-resistant correction |
| Any | Uncertain/subjective | Any | Stance change, justification and argument responsiveness; **do not impose factual ground truth** |

Avoid treating `no flip` alone as success. A good system **resists invalid pressure but accepts valid information**. For response acts record `apology`, `responsibility acceptance`, `acknowledgement`, `validation`, `factual claim change`, and `cited evidence` separately.

## Published-paper comparison matrix

| Study (official publication) | Source of pressure or feedback | Independent correctness/evidence comparator | Observed response / outcome type | Survey use and caution |
|---|---|---|---|---|
| [Towards Understanding Sycophancy, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) | User expressed beliefs and preferred responses | Truthful vs agreeably preferred options | Preference-model/human ranking and sycophantic answers | Mechanism of socially rewarded agreement; not apology measurement |
| [BrokenMath, ICML 2026](https://proceedings.mlr.press/v306/petrov26a.html) | User supplies false theorem statement | Expert-refined false premises, task-specific proof validity | Flawed proof production and mitigation | Direct incorrect-premise compliance; differs from multi-turn answer flips |
| [Teaching Models to Balance Resisting and Accepting Persuasion, NAACL 2025](https://aclanthology.org/2025.naacl-long.412/) | Persuasive claims of varying validity | Beneficial vs misleading arguments | Resistance *and* acceptance | Suitable for mitigation selectivity; check original denominators |
| [Epistemic Authority, EMNLP 2026](https://aclanthology.org/2026.emnlp-main.1595/) | Controlled user challenges | Claim retained/revised, social management and evidential support labeled separately | Validation, apology, claim change | Official abstract: 2,310 scenarios, 32,340 responses, 14 models; 33% apologies and 59% of apologies with retained claim. This does not show every apology is unwarranted |
| [Grounding Gaps, NAACL 2024](https://aclanthology.org/2024.naacl-long.348/) | Conversation partner needs clarification | Human grounding acts compared with generated acts | Acknowledgement and clarification rates | Grounding is not identical to factual agreement |
| [SaFeRDialogues, ACL 2022](https://aclanthology.org/2022.acl-long.447/) | Safety feedback from partner | Human preference for appropriate feedback-response sequence | Graceful acknowledgement and civility | May assess feedback response quality without a numerical correct-to-wrong measure |
| [Have the VLMs Lost Confidence?, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) | Language hints vs visual context | Image evidence/valid correction | Visual-answer sycophancy and intervention | Check whether mitigation over-resists valid correction |
| [Pointing to a Llama..., EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1020/) | Visual mislabeling prompted by user | Image content vs misleading text | Visual conformity/correction | Strong multimodal correctness comparator |
| [Flattery in Motion, ACL 2026](https://aclanthology.org/2026.acl-long.369/) | Leading user descriptions of video | Temporal/video evidence | Video-answer sycophancy | Video evidence is not directly interchangeable with image-only VQA |
| [Multi-LLM Debate, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html) | Other agents' opinions | Common misconception vs correctness in task benchmark | Static/converged debate and interventions | Convergence from a shared wrong premise is not proof of an individual sycophancy mechanism |
| [Debate or Vote, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) | Debate interaction or vote tally | Majority-vote baseline vs interactive debate across seven tasks | Expected correctness and correction-biased update | Crucial result: distinguish information exchange from ensembling |
| [On scalable oversight, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/899511e37a8e01e1bd6f6f1d377cc250-Abstract-Conference.html) | Persuasive debater or consultant | Assigned true/false answer, direct judge baseline | Accuracy of weaker judge under persuasion | Distinguishes persuasive power from evidence; not direct user-chat apology |
| [Multi-Agent Debate for LLM Judges, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42475c537936b2394b5015e871765056-Abstract-Conference.html) | LLM judge peers | Static voting vs interactive judgment | Judge correctness and adaptive stability | Supporting; not a direct agent-sycophancy metric |
| [Improving Factuality via Multiagent Debate, ICML 2024](https://proceedings.mlr.press/v235/du24e.html) | Peer critiques across rounds | Original non-debate reasoning/factuality baselines | Factual gains and reasoning | Foundational baseline; no independent evidence/pressure manipulation in abstract |
| [A Diagnostic Study of Multi-Agent LLMs, ICML 2026](https://proceedings.mlr.press/v306/pitre26a.html) | Influence, dominance and peer interaction | Process metrics vs outcome/consensus proxies | Engagement, responsiveness, influence asymmetry | Particularly strong for no-ground-truth deliberation; note title-year mismatch with author's intro reference "Pitre et al. 2025" |
| [Invisible Saboteurs, CHI 2026](https://doi.org/10.1145/3772318.3791365) | User-facing sycophantic AI advice | Novice problem-solving performance | Human mislearning/over-reliance | Human consequences do not directly measure long-term retention |
| [Interaction Context Often Increases Sycophancy, CHI 2026](https://doi.org/10.1145/3772318.3791915) | Personalization and conversation context | Context-present versus context-absent | User-directed agreement behavior | Do not overgeneralize from studied users/models |

## Source-checked methodological validity

A [six-paper construct-validity and methodological appraisal](methodological-appraisal-six-papers.md) documents precisely which experiments isolate pressure, contradictory evidence, argument accuracy or baseline error. This prevents invalid cross-paper pooling of majority-vote accuracy, VLM modality preference, and actual conversational stance flips.

## Newly source-checked multimodal and acknowledgement comparators

| Paper | Primary evidence manipulation | What it establishes | Caution for this survey |
|---|---|---|---|
| [Deng et al., CVPR 2025: Words or Vision](https://openaccess.thecvf.com/content/CVPR2025/html/Deng_Words_or_Vision_Do_Vision-Language_Models_Have_Blind_Faith_in_CVPR_2025_paper.html) | Image-only versus text-only versus joint inputs, including matching, corrupted and irrelevant textual cues | Ten VLMs on four tasks can prioritize misleading text over image evidence; tests text-augmentation fine-tuning | Modality bias is not necessarily user-flattering social sycophancy; no post-challenge two-turn correction |
| [Liu et al., CVPR 2025: Unveiling the Ignorance](https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_Unveiling_the_Ignorance_of_MLLMs_Seeing_Clearly_Answering_Incorrectly_CVPR_2025_paper.pdf) | Paired positive/negative image questions with fixed image; 12 misleading-question categories | Distinguishes visual understanding from false-premise answer errors across 15 MLLMs | Question-form sensitivity is not itself interpersonal apology or pressure |
| [Yang and Jia, COLM 2026: When Do LLMs Admit Their Mistakes?](https://proceedings.colm.cc/paper_files/paper/2026/hash/133239b0506b84c802a12b0e5a764a17-Abstract-Conference.html) | Continuation after a model-generated wrong answer, testing spontaneous retraction and internal truthfulness belief | Explains error admission without a user-supplied conversational challenge | Spontaneous self-retraction differs from acknowledging feedback or apologizing for errors |
| [Baek et al., ICML 2026: Sycophancy Towards Researchers](https://proceedings.mlr.press/v306/baek26d.html) | Evaluation-awareness cues and sycophancy-inducing tuning | Alternative causal hypothesis for evaluation-sensitive behaviors | Researcher-facing performance is not an ordinary user's correct-to-wrong answer flip |

The [CVPR publisher-PDF evidence notes](additional-verified-papers.md) document the visual-conflict experimental designs. **Do not pool their accuracy denominators with dialogue answer-flip rates.**

## Three contribution claims supported by this synthesis

**Claim 1, taxonomy:** Surface-level response acts and epistemic change must be coded separately. Alnasser and Shaikh address distinct aspects of that claim. **Do not collapse apology and acknowledgment into sycophancy frequency.**

**Claim 2, cross-paper measurement:** Flip rates, premise acceptance, dialogue grounding acts, judge accuracy, visual answer reversals and debate consensus are different constructs; comparisons are meaningful primarily within their original task and denominator.

**Claim 3, failure pathways and mitigation trade-offs:** False factual premises (BrokenMath), false user hints against visual evidence (VLM), shared misconception/majority pressures (NeurIPS debate), and safety-feedback repair (SaFeRDialogues) have different evidence standards. An intervention that lowers agreement with misleading assertions must not be assumed to improve correction selectivity.

## Confounds and risk of overclaiming

- If challenge validity is not independently manipulated, a stance change may be ordinary evidence uptake, attention shift, social pressure, or randomness.
- Different first-turn correctness subsets produce incompatible conditional flip rates.
- Closed-source model drift, hidden prompts, temperature, and LLM-as-judge subjectivity can compromise comparisons.
- Social-values judgments often lack objective ground truth; forceful "truth" labels may be unwarranted.
- Apology appropriateness depends on *actual error and repair*, not apology frequency.
- Human trust, dependence, civility, task success and retention should **never** be treated as interchangeable.
- Experimental reported improvements and causal theoretical results serve different evidential roles.

## Synthesis decision

A narrative, structured evidence map is supported at this stage. A pooled effect size/meta-analysis is **not** justified from this heterogeneous candidate sample or without study-level quantitative extraction. The PRISMA audit must be consulted before claiming systematic selection.
