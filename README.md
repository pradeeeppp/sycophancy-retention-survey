# Sycophancy & User Retention in Language Models

A curated reading list on sycophancy, user trust, and retention-related behaviors in language models: how they arise, how to measure them, and how to mitigate them.

[![Studies: 83](https://img.shields.io/badge/Studies-83-334155)](#contents)
[![Topics: 10](https://img.shields.io/badge/Topics-10-334155)](#contents)
[![Study notes](https://img.shields.io/badge/Read-Study_notes-2563eb)](literature/selected-papers.md)

> How can an assistant stay helpful and supportive while remaining willing to disagree, correct mistakes, and update when the evidence changes?

**New to the topic?** Follow [Start here](#start-here). **Looking for a paper?** Browse the [contents](#contents). **Need more detail?** Read the [full citations and study notes](literature/selected-papers.md).

## Contents

- [Start here](#start-here)
- [Scope and reading guide](#scope-and-reading-guide)
- [Behavioral definitions and social sycophancy](#behavioral-definitions-and-social-sycophancy) (9)
- [Evaluation and benchmarks](#evaluation-and-benchmarks) (20)
- [Training mechanisms and representations](#training-mechanisms-and-representations) (10)
- [Mitigation and rational updating](#mitigation-and-rational-updating) (11)
- [Multimodal sycophancy](#multimodal-sycophancy) (8)
- [Multi-agent sycophancy](#multi-agent-sycophancy) (9)
- [Human effects, apologies, and trust](#human-effects-apologies-and-trust) (6)
- [Related surveys and background](#related-surveys-and-background) (3)
- [Memory and personalization](#memory-and-personalization) (2)
- [Related visual grounding and hallucination](#related-visual-grounding-and-hallucination) (5)
- [Contributing](#contributing)
- [License](#license)

## Start here

A short path through the collection:

1. **Foundations:** [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) — how agreeable answers can be favored by preference signals.
2. **Social behavior:** [ELEPHANT](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html) — sycophancy beyond factual agreement, including protection of a user's self-image.
3. **Multi-turn evaluation:** [SYCON Bench](https://aclanthology.org/2025.findings-emnlp.121/) — when and how often models change stance under pressure.
4. **Mitigation trade-offs:** [Sycophancy Suppression Can Impair Rational Updating](https://aclanthology.org/2026.findings-emnlp.1208/) — resisting unsupported pressure while accepting valid corrections.
5. **Human consequences:** [Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352) — effects of excessive affirmation on users.

## Scope and reading guide

The collection contains **83 studies across ten topics**. Eight additions selected on 2026-11-17 are documented here; their manuscript inclusion should be reconciled against the screening protocol before claiming a PRISMA count. Each study has one primary category; links in the reading guide are shortcuts to those same papers.

The current coverage centers on sycophancy, factual correction, apologies, trust, and personalization. User retention is a motivating question: studies of trust, reliance, or dependence should not automatically be read as direct measurements of long-term retention.

When comparing papers, keep these distinctions in view:

- **Agreement and correctness:** agreeing with a user can be justified; an answer change alone does not establish sycophancy.
- **Empathy and affirmation:** acknowledging feelings is different from endorsing an unsupported claim.
- **Resistance and updating:** a useful mitigation should preserve responsiveness to valid evidence.
- **Behavior and human outcomes:** model benchmark scores, user trust, and continued use measure different things.

Entries below give a brief description and the year used in the existing catalog. Follow each title to its publication or preprint; the [study notes](literature/selected-papers.md) preserve full citations, findings, and limitations. The two sections labeled **Related** provide adjacent background.

## Behavioral definitions and social sycophancy

Definitions, interpersonal affirmation, epistemic authority, and the pragmatics of challenging users' claims.

- [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/) *(2026)* — Separates claim revision, social validation, and apologies when models respond to user disagreement.
- [Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs](https://aclanthology.org/2026.acl-long.736/) *(2026)* — Tests how framing, source reliability, and pragmatic cues affect whether models challenge harmful beliefs.
- [ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html) *(2026)* — Introduces ELEPHANT, a benchmark for excessive preservation of a user's desired self-image.
- [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/) *(2026)* — Studies how personal disclosures and emotional context affect negative judgments, evasion, and agreement.
- [What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct](https://arxiv.org/abs/2605.21778) *(2026)* — Develops a taxonomy and expert survey to clarify different meanings of AI sycophancy.
- [Is Sycophancy a Form of In-Context Updating?](https://arxiv.org/abs/2610.28325) *(2026)* — Examines factual sycophancy as excessive weighting of user claims during in-context updating.
- [Claim Framing as a Driver of LLM Sycophancy](https://arxiv.org/abs/2610.18159) *(2026)* — Tests how confidence, attribution, and shared framing change responses to incorrect user opinions.
- [Sweet Talkers: How Query Formulation Shapes Sycophancy in Romantic Relationship Advice](https://aclanthology.org/2026.luhme-1.21/) *(2026)* — Studies how phrasing and perspective shape social sycophancy in relationship advice.

- [Decomposing LLM Advice Sycophancy: Content, Style, and Framing Drive Distinct Response Dimensions](https://aclanthology.org/2026.aacl-long.12/) *(2026)* — Separates the effects of advice content, writing style, and whose perspective is presented on warmth, endorsement, and recommendation directness.

[Study notes](literature/selected-papers.md#behavioral-definitions-and-social-sycophancy) · [Back to contents](#contents)

## Evaluation and benchmarks

Benchmarks and measurement protocols for answer reversals, sustained pressure, scientific premises, medical dialogues, and educational use.

- [Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://proceedings.mlr.press/v306/kasneci26a.html) *(2026)* — Introduces EduFrameTrap and argues for evaluating supportive correction in LLM tutors.
- [The Doctor Will Agree With You Now: Sycophancy of Large Language Models in Multi-Turn Medical Conversations](https://aclanthology.org/2026.healing-1.2/) *(2026)* — Measures resistance to repeated medical pushback across ten models and two clinical question-answering datasets.
- [Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy](https://aclanthology.org/2026.findings-emnlp.1558/) *(2026)* — Tests how user roles, evidence, grounding, and dialogue structure affect medical sycophancy.
- [SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants](https://aclanthology.org/2026.findings-acl.1759/) *(2026)* — Evaluates resistance to misleading pressure alongside acceptance of valid corrections.
- [When Helpfulness Becomes Scientific Sycophancy: Triggering and Mitigating LLM Failures on Flawed Scientific Premises](https://aclanthology.org/2026.findings-emnlp.1501/) *(2026)* — Introduces SciSycEval to test whether scientific assistants challenge plausible but flawed premises.
- [Measuring Sycophancy of Language Models in Multi-turn Dialogues](https://aclanthology.org/2025.findings-emnlp.121/) *(2025)* — Introduces SYCON Bench and tracks when and how often models change stance under sustained pressure.
- [SPINE: Measuring LLM Sycophancy under Sustained Multi-Turn Pressure](https://arxiv.org/abs/2609.09090) *(2026)* — Uses an adaptive mistaken-user proxy to test whether assistants abandon correct answers over extended dialogue.
- [FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy](https://arxiv.org/abs/2609.39863) *(2026)* — Scores factual integrity and emotional support separately in multi-turn conversations.
- [Big-Big-SycoBench: A Benchmark to Detect Sycophancy Through Model Responses to Valid vs. Invalid Arguments](https://arxiv.org/abs/2610.15634) *(2026)* — Tests revision under valid and invalid arguments relative to each model's baseline scoring variability.
- [Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark](https://arxiv.org/abs/2609.32867) *(2026)* — Audits benchmark confounds caused by changes in objection wording and output instructions.
- [Disentangling Robustness and Sycophancy in Multilingual LLMs](https://arxiv.org/abs/2610.30696) *(2026)* — Separates multilingual factual competence from yielding to pressure with the SC-matrix.
- [TrussTutor-Bench: Benchmarking large language models on solution accuracy, sycophancy, and error detection in statics](https://arxiv.org/abs/2610.38917) *(2026)* — Tests solution accuracy, error detection, and defense of correct work in statics tutoring.
- [SyPS: Measuring Sycophancy Prompt Sensitivity in Large Language Models](https://aclanthology.org/2026.findings-emnlp.1421/) *(2026)* — Measures sensitivity to confidence, emotional pressure, consensus, and validation-seeking language.
- [BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts](https://arxiv.org/abs/2606.10061) *(2026)* — Introduces a Bengali benchmark that distinguishes empathetic support from excessive validation.
- [Discovering Language Model Behaviors with Model-Written Evaluations](https://aclanthology.org/2023.findings-acl.847/) *(2023)* — Uses model-written evaluations to identify behaviors including repetition of users' preferred answers.

- [Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment](https://arxiv.org/abs/2311.08596) *(2023)* — Early controlled two-turn challenge experiment measuring answer flips and accuracy deterioration without new evidence.
- [Understanding the Effects of Iterative Prompting on Truthfulness](https://proceedings.mlr.press/v235/krishna24a.html) *(2024)* — Tests how repeated prompting can degrade truthfulness and calibration, and evaluates prompting variants that improve reliability.
- [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://aclanthology.org/2025.findings-emnlp.1222/) *(2025)* — Contrasts sequential user rebuttals with simultaneous evaluation of opposing arguments and examines effects of critique wording.
- [SycEval: Evaluating LLM Sycophancy](https://ojs.aaai.org/index.php/AIES/article/view/36598) *(2025)* — Tests factual answer changes under rebuttals in mathematical and medical question-answering and distinguishes progressive from regressive changes.
- [Accounting for Sycophancy in Language Model Uncertainty Estimation](https://aclanthology.org/2025.findings-naacl.438/) *(2025)* — Shows how user correctness and confidence alter answer behavior and uncertainty estimation; proposes SyRoUP.

[Study notes](literature/selected-papers.md#evaluation-and-benchmarks) · [Back to contents](#contents)

## Training mechanisms and representations

Preference signals, conversational warmth, interaction context, and internal representations associated with sycophancy.

- [Sycophancy Hides Linearly in the Attention Heads](https://aclanthology.org/2026.eacl-long.324/) *(2026)* — Probes attention, MLP, and residual-stream activations and tests steering of sycophantic answer changes.
- [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://aclanthology.org/2026.findings-emnlp.2373/) *(2026)* — Compares hidden-state probes and steering across model families and alignment stages.
- [Training language models to be warm can reduce accuracy and increase sycophancy](https://doi.org/10.1038/s41586-026-10410-0) *(2026)* — Studies how warmth-focused fine-tuning affects factual accuracy and endorsement of incorrect user beliefs.
- [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915) *(2026)* — Examines how conversation history and memory profiles affect agreement with users.
- [Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://aclanthology.org/2026.emnlp-main.2533/) *(2026)* — Tests whether praise, sycophantic agreement, and genuine agreement can be influenced separately.
- [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) *(2024)* — Studies sycophancy across assistants and how human and preference-model rankings can favor agreeable answers.
- [How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html) *(2026)* — Formally analyzes how biased human preferences can amplify sycophancy during RLHF.
- [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](https://aclanthology.org/2026.emnlp-main.2636/) *(2026)* — Connects post-training representations of addressivity with sycophancy through sparse autoencoders and steering.
- [Locating Sycophancy Across Training Stages in Open Language Models](https://arxiv.org/abs/2610.37788) *(2026)* — Compares responses to misleading claims across base, supervised-tuned, and preference-tuned checkpoints.

- [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](https://arxiv.org/abs/2601.21183) *(2026)* — Locates causal points in reasoning traces where a model becomes committed to an incorrect user suggestion.

[Study notes](literature/selected-papers.md#training-mechanisms-and-representations) · [Back to contents](#contents)

## Mitigation and rational updating

Methods that reduce unsupported agreement while examining reasoning quality, selective correction, or other capability trade-offs.

- [Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy](https://aclanthology.org/2026.acl-long.1126/) *(2026)* — Examines when reasoning reduces sycophantic answers while still rationalizing deference in explanations.
- [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](https://aclanthology.org/2026.findings-emnlp.1208/) *(2026)* — Shows why mitigation should measure both resistance to unsupported pressure and acceptance of valid corrections.
- [Learning Multilingual Agentic Policy to Control Sycophancy](https://aclanthology.org/2026.eacl-long.169/) *(2026)* — Treats answering, challenging, and requesting clarification as policy choices in multilingual settings.
- [From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning](https://proceedings.mlr.press/v235/chen24u.html) *(2024)* — Introduces targeted tuning of a small subset of model modules and evaluates capability trade-offs.
- [Simple synthetic data reduces sycophancy in large language models](https://arxiv.org/abs/2308.03958) *(2023)* — Tests a lightweight synthetic-data fine-tuning intervention for reducing sycophancy on held-out prompts.
- [Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition](https://arxiv.org/abs/2604.05279) *(2026)* — Separates pressure-driven capitulation from failure to use evidence with distinct reward signals.
- [Mitigating Social Sycophancy via Pluralistic Preference Optimization](https://arxiv.org/abs/2610.02568) *(2026)* — Trains models to consider stakeholders beyond the user when giving interpersonal advice.
- [Gated Activation Steering for Reducing Sycophancy & Hallucination in Medical Question Answering](https://arxiv.org/abs/2608.23666) *(2026)* — Uses gated activation steering for unsupported claims and pressure-driven shifts in medical question answering.
- [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828) *(2026)* — Studies monitor-based interventions for reward hacking, including sycophancy in medical chat.
- [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](https://arxiv.org/abs/2609.35544) *(2026)* — Tests whether reducing sycophancy also improves refusal, finding different effects across settings.

- [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412/) *(2025)* — Introduces persuasion-balanced training to resist misleading influence while preserving uptake of beneficial arguments.

[Study notes](literature/selected-papers.md#mitigation-and-rational-updating) · [Back to contents](#contents)

## Multimodal sycophancy

Image- and video-grounded studies of misleading textual context and visual evidence.

- [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://aclanthology.org/2026.findings-emnlp.479/) *(2026)* — Tests contextual sycophancy with a visual-text diagnostic and a context-blind visual witness.
- [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/) *(2026)* — Introduces ViSE to evaluate leading user input that conflicts with video evidence.
- [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) *(2025)* — Introduces MM-SY and compares prompting, fine-tuning, and preference optimization for visual sycophancy.
- [Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.1020/) *(2025)* — Examines the trade-off between resisting misleading instructions and accepting valid visual corrections.
- [PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models](https://arxiv.org/abs/2512.19350) *(2025)* — Uses human-curated visual questions to test conflicts between user input and image evidence.
- [Uncertainty, Not Concealment: A Mechanistic Reappraisal of Sycophancy in Vision-Language Models](https://arxiv.org/abs/2611.10297) *(2026)* — Tests uncertainty-based explanations for image-report conflicts in medical vision-language retrieval.
- [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](https://aclanthology.org/2026.findings-emnlp.2475/) *(2026)* — Evaluates compact vision-language models on separate capability and behavioral axes, including sycophancy.
- [Talked Out of the Truth: Sycophancy in the Reasoning Chains of Multimodal Models](https://arxiv.org/abs/2608.28623) *(2026)* — Scores both reasoning chains and final answers under misleading multimodal user assertions.

[Study notes](literature/selected-papers.md#multimodal-sycophancy) · [Back to contents](#contents)

## Multi-agent sycophancy

Peer influence, debate convergence, identity effects, and reliability-sensitive group reasoning.

- [When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning](https://aclanthology.org/2026.acl-long.650/) *(2026)* — Studies identity-weighted updating and tests anonymization in multi-agent debate.
- [Too Polite to Disagree: Understanding Sycophancy Propagation in Multi-Agent Systems](https://aclanthology.org/2026.sigdial-1.56/) *(2026)* — Tests whether information about peers' reliability limits sycophancy propagation and improves group reasoning.
- [CONSENSAGENT: Towards Efficient and Effective Consensus in Multi-Agent LLM Interactions Through Sycophancy Mitigation](https://aclanthology.org/2025.findings-acl.1141/) *(2025)* — Uses adaptive debate prompts to address uncritical agreement and evaluates accuracy and efficiency.
- [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy](https://arxiv.org/abs/2605.12991) *(2026)* — Tests incorrect peer consensus in base and instruction-tuned models, alongside a structured-dissent intervention.
- [LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems](https://arxiv.org/abs/2609.33495) *(2026)* — Examines how in-group and out-group identities affect conformity to incorrect peer answers.
- [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289) *(2026)* — Tests majority pressure and authority cues in safety deliberation and proposes evidence-first arbitration.
- [Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate](https://arxiv.org/abs/2608.03648) *(2026)* — Introduces DEAR to regulate peer consultation and reduce blind conformity during debate.
- [DREAM: Dynamic Resolution Assignment For Multimodal Multi-agent Debate](https://arxiv.org/abs/2610.05615) *(2026)* — Allocates image resolution across debating agents and revisits answers overridden by group pressure.
- [The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents](https://arxiv.org/abs/2604.00478) *(2026)* — Proposes context-access controls and a generator-critic loop to check excessive agreement across turns.

[Study notes](literature/selected-papers.md#multi-agent-sycophancy) · [Back to contents](#contents)

## Human effects, apologies, and trust

User experiences, downstream effects of affirmation, and responses to AI apologies or error communication.

- [Who's Sorry Now: User Preferences Among Rote, Empathic, and Explanatory Apologies from LLM Chatbots](https://doi.org/10.1145/3793679) *(2026)* — Compares user preferences for rote, empathic, and explanatory apologies after chatbot errors.
- [Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352) *(2026)* — Studies downstream effects of excessive affirmation on responsibility-taking and interpersonal repair.
- [Evaluation of Failure Communication Strategies for Trust Repair in Human-AI Collaboration](https://aclanthology.org/2026.lrec-1.230/) *(2026)* — Tests how communicating mistakes affects trust during human-AI collaboration.
- [LLM Sycophancy: How Users Flag and Respond](https://proceedings.mlr.press/v318/noshin26a.html) *(2026)* — Analyzes how users notice, test, and respond to sycophancy in Reddit discussions.
- [Apologizing artificial intelligence: designing and evaluating effective AI apologies after errors](https://doi.org/10.1007/s00146-026-03067-w) *(2026)* — Examines when AI apologies restore reliance or confidence, with effects varying by task and attribution.

- [When Do LLMs Admit Their Mistakes? Understanding the Role of Model Belief in Retraction](https://proceedings.colm.cc/paper_files/paper/2026/hash/133239b0506b84c802a12b0e5a764a17-Abstract-Conference.html) *(2026)* — Studies spontaneous, immediate retraction of a model's own false assertions and the relation between momentary internal belief and error admission; distinct from user-triggered apology and correction.

[Study notes](literature/selected-papers.md#human-effects-apologies-and-trust) · [Back to contents](#contents)

## Related surveys and background

Adjacent literature on model correction that informs the survey but is not direct experimental evidence of sycophancy.

- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/) *(2024)* — Reviews when self-correction works, emphasizing reliable feedback and fair comparisons.
- [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) *(2023)* — Introduces methods for monitoring and steering model representations used in later mechanistic studies.

- [AI apology: a critical review of apology in AI systems](https://doi.org/10.1007/s10462-025-11305-8) *(2025)* — Synthesizes AI-apology research, including twelve apology components and a context-sensitive framework; foundational background rather than evidence of model-level sycophancy.

[Study notes](literature/selected-papers.md#related-surveys-and-background) · [Back to contents](#contents)

## Memory and personalization

How long-term user memory and retrieved context can influence agreement, and defenses that balance personalization with current evidence.

- [Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy](https://arxiv.org/abs/2610.07403) *(2026)* — Evaluates memory filtering and rewriting alongside activation steering, including task-information trade-offs.
- [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](https://arxiv.org/abs/2610.05162) *(2026)* — Uses counterfactual and context-aware adaptation to calibrate retrieved memories against current evidence.

[Study notes](literature/selected-papers.md#memory-and-personalization) · [Back to contents](#contents)

## Related visual grounding and hallucination

Adjacent vision and video work on false premises, language-prior bias, and suppressed evidence that informs multimodal sycophancy research.

- [Mechanisms of Prompt-Induced Hallucination in Vision–Language Models](https://aclanthology.org/2026.acl-long.1941/) *(2026)* — Studies how false textual premises override image evidence in object counting and tests attention-head ablation.
- [ACPO: Counteracting Likelihood Displacement in Vision-Language Alignment with Asymmetric Constraints](https://arxiv.org/abs/2603.22165) *(2026)* — Adjusts preference optimization to protect visually grounded responses from language-prior bias.
- [Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs](https://openaccess.thecvf.com/content/WACV2026W/VALED/html/Hong_Tone_Matters_The_Impact_of_Linguistic_Tone_on_Hallucination_in_WACVW_2026_paper.html) *(2026)* — Introduces Ghost-100 to test whether tone and pressure induce invented visual details.
- [SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition](https://doi.org/10.1145/3767308.3835492) *(2026)* — Uses representation-level interventions to recover suppressed temporal evidence in video reasoning.
- [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://aclanthology.org/2026.emnlp-main.251/) *(2026)* — Tests false textual premises that draw attention to plausible but absent objects.

[Study notes](literature/selected-papers.md#related-visual-grounding-and-hallucination) · [Back to contents](#contents)

## Contributing

Suggestions and corrections are welcome through [issues](https://github.com/pradeeeppp/sycophancy-retention-survey/issues) or pull requests.

- Add work relevant to sycophancy, evidence-based correction, or the human outcomes covered here; label adjacent work as background.
- Choose one primary category and use a stable publication, DOI, or arXiv link.
- Use the format: `[Title](url) *(Year)* — One-sentence description.`
- Add the full citation and supporting notes to [the study notes](literature/selected-papers.md), and keep the topic and total counts in sync.
- Distinguish measured findings from interpretation, especially for trust, dependence, and retention.

## License

See [LICENSE](LICENSE) for the repository's license. Linked publications remain subject to their respective licenses.
