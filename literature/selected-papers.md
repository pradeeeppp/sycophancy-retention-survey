# Study Notes on AI Apologies, Sycophancy, and Factual Correction

[← Back to the reading list](../README.md)

The repository's main reading list is now in [README.md](../README.md). This companion keeps the full citations and detailed study summaries.

This index classifies 81 selected studies by their primary research focus. Some papers span several topics; each appears once for straightforward navigation. Related background is identified separately.

## Contents

- [Behavioral definitions and social sycophancy](#behavioral-definitions-and-social-sycophancy) (9)
- [Evaluation and benchmarks](#evaluation-and-benchmarks) (20)
- [Training mechanisms and representations](#training-mechanisms-and-representations) (10)
- [Mitigation and rational updating](#mitigation-and-rational-updating) (11)
- [Multimodal sycophancy](#multimodal-sycophancy) (8)
- [Multi-agent sycophancy](#multi-agent-sycophancy) (9)
- [Human effects, apologies, and trust](#human-effects-apologies-and-trust) (5)
- [Related surveys and background](#related-surveys-and-background) (2)
- [Memory and personalization](#memory-and-personalization) (2)
- [Related visual grounding and hallucination](#related-visual-grounding-and-hallucination) (5)

## Behavioral definitions and social sycophancy

Definitions, interpersonal affirmation, epistemic authority, and the pragmatics of challenging users' claims.

**Alnasser, R., Çetinkaya, Y. M., Zhao, S., & Elmas, T. (2026).** [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/). *Proceedings of EMNLP 2026*, 36257–36272.

Across 14 models and 32,340 responses to controlled challenges, the authors distinguish claim revision from social validation, apology, and shifts in epistemic authority. Models apologized in 33% of responses, yet 59% of those apologies accompanied maintenance of the original claim. These findings make it important to measure apologies separately from whether an answer was revised or supported with evidence.

**Cheng, M., Hawkins, R. D., & Jurafsky, D. (2026).** [Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs](https://aclanthology.org/2026.acl-long.736/). *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)*, 16181–16203.

The authors study how pragmatic cues, including whether a claim is at issue, linguistic framing and source reliability, affect a model's willingness to challenge harmful beliefs. Experiments span misinformation and social-sycophancy benchmarks and test simple prompting interventions. The work motivates analyzing context and false-positive challenges alongside correction success.

**Cheng, M., Yu, S., Lee, C., Khadpe, P., Ibrahim, L., & Jurafsky, D. (2026).** [ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html). *International Conference on Learning Representations (ICLR 2026)*.

ELEPHANT measures social sycophancy as excessive preservation of a user's desired self-image, beyond explicit factual agreement. Across 11 evaluated models, face-preserving responses were more common than in human comparisons, including cases where models endorsed opposing sides of the same conflict. The benchmark captures a form of agreement that cannot be reduced to answer-flip accuracy.

**Li, J., Menon, S., Frischmann, B., Wilson, S., & Rajtmajer, S. (2026).** [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/). *Proceedings of EMNLP 2026*, 27134–27156.

Using seven LLMs and prompts drawn from two Reddit datasets, this study compares evaluations of third-party accounts with responses to users describing their own actions or opinions. Models were less willing to express negative judgments to the user, especially when disclosures included loneliness or distress. The study identifies evasive responses, not only explicit agreement, as a form of sycophancy.

**Ye, M., Ibrahim, L., Bo, J. Y., et al. (2026).** [What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct](https://arxiv.org/abs/2605.21778). *arXiv:2605.21778*.

The authors develop a taxonomy and survey experts on the fragmented meaning of AI sycophancy. The paper helps distinguish factual agreement, excessive praise, and withheld correction when comparing evaluations.

**Shapira, I., Cheng, M., & Orgad, H. (2026).** [Is Sycophancy a Form of In-Context Updating?](https://arxiv.org/abs/2610.28325). *arXiv:2610.28325*.

The paper treats factual sycophancy as excessive weighting of a user's claim during in-context updating. Its behavioral and mechanistic tests suggest that mitigation must preserve useful evidence-based updating.

**Seo, J., Atanasova, P., & Augenstein, I. (2026).** [Claim Framing as a Driver of LLM Sycophancy](https://arxiv.org/abs/2610.18159). *arXiv:2610.18159*.

This study varies how a user's claim is framed while keeping factual questions verifiable. It finds that confidence, attribution, and shared framing can change how strongly models follow incorrect opinions.

**Choi, H., Hao, E. C. C., Bautista, K., et al. (2026).** [Sweet Talkers: How Query Formulation Shapes Sycophancy in Romantic Relationship Advice](https://aclanthology.org/2026.luhme-1.21/). *Proceedings of the LUHME Workshop at EMNLP 2026*.

Using relationship-advice prompts, the authors compare how different phrasings and perspectives affect social sycophancy. The results highlight the importance of implied framing and follow-up turns in interpersonal advice.


**Singh, J., & Kaynig-Fittkau, V. (2026).** [Decomposing LLM Advice Sycophancy: Content, Style, and Framing Drive Distinct Response Dimensions](https://aclanthology.org/2026.aacl-long.12/). *Proceedings of AACL-IJCNLP 2026 (Long Papers), 255–274.*

Across 787 advice-seeking scenarios, the study independently varies semantic content, linguistic style, and narrative framing. Emotional warmth tracks content, stance endorsement tracks framing, and recommendation directness tracks style. The paper is directly relevant to distinguishing social validation from factual agreement and to avoiding interventions that mistakenly suppress empathy.


## Evaluation and benchmarks

Benchmarks and measurement protocols for answer reversals, sustained pressure, scientific premises, medical dialogues, and educational use.

**Kasneci, E., & Kasneci, G. (2026).** [Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://proceedings.mlr.press/v306/kasneci26a.html). *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306, 170836–170855.

This position paper argues that tutoring assistants should challenge students' misconceptions constructively, even when users apply authority or social pressure. Its EduFrameTrap benchmark evaluates this tension across educational subjects. The proposed standard of supportive but evidence-sensitive correction provides a concise direction for future assessment of conversational assistants.

**Kim, T. M., Luo, L., Kim, S. E., et al. (2026).** [The Doctor Will Agree With You Now: Sycophancy of Large Language Models in Multi-Turn Medical Conversations](https://aclanthology.org/2026.healing-1.2/). *Proceedings of the 1st Workshop on Linguistic Analysis for Health (HeaLing 2026)*, 19–34.

The authors test ten models under repeated medical pushback using MedCaseReasoning and PubMedQA, introducing a turn-level Resistance measure. They find that resistance varies strongly with the clinical task and form of the answer. This workshop paper adds medical dialogue context; resistance should not be equated with factual correctness.

**Ping, K., Çarık, B., Wohn, C., et al. (2026).** [Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy](https://aclanthology.org/2026.findings-emnlp.1558/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

Using five open-weight models, 500 MEDQUAD questions and 1.2 million controlled trials, the authors vary user role, evidence, interaction structure and grounding. Incorrect pushback after an initial answer produces substantially more sycophancy than a false claim placed in the opening question. The findings show that medical sycophancy depends on conversational design, not only model identity.

**Sinha, D. (2026).** [SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants](https://aclanthology.org/2026.findings-acl.1759/). *Findings of the Association for Computational Linguistics: ACL 2026*, 35278–35284.

SycoBench-600 tests whether models resist misleading social pressure while accepting valid corrections. Its distinction between resistance and selective updating provides a useful way to assess whether an answer change reflects a justified correction or agreement with an unsupported user claim.

**Zhang, Y., Hua, C., Salapaka, M., & Kang, D. (2026).** [When Helpfulness Becomes Scientific Sycophancy: Triggering and Mitigating LLM Failures on Flawed Scientific Premises](https://aclanthology.org/2026.findings-emnlp.1501/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

SciSycEval tests whether scientific assistants reject, qualify or proceed with plausible but flawed premises across several scientific settings. The paper examines factors that encourage unsupported premise acceptance and evaluates critical-evaluation prompting as a mitigation. Premise acceptance should be distinguished from answer-flip measures used in ordinary question-answering benchmarks.

**Hong, J., Byun, G., Kim, S., & Shu, K. (2025).** [Measuring Sycophancy of Language Models in Multi-turn Dialogues](https://aclanthology.org/2025.findings-emnlp.121/). *Findings of the Association for Computational Linguistics: EMNLP 2025*, 2239–2259.

SYCON Bench evaluates 17 language models under sustained user pressure and reports Turn of Flip and Number of Flip to describe when and how often a model changes its stance. Third-person prompting reduces sycophancy in a tested debate setting. These trajectory measures are informative, but a stance change alone does not establish whether the final answer is factually wrong.

**Tang, L., Wei, K., Jiang, T., et al. (2026).** [SPINE: Measuring LLM Sycophancy under Sustained Multi-Turn Pressure](https://arxiv.org/abs/2609.09090). *arXiv:2609.09090*.

SPINE uses an adaptive, mistaken-user proxy to challenge an assistant over an extended dialogue. It measures whether models abandon correct answers under sustained pressure that shorter scripts can miss.

**Pulipaka, S., Binkyte, R., Sheth, I., et al. (2026).** [FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy](https://arxiv.org/abs/2609.39863). *arXiv:2609.39863*.

FIGS evaluates extended conversations on separate axes for factual integrity and calibrated emotional support. This avoids counting an empathetic response as sycophancy merely because it acknowledges a user's feelings.

**Ballon, M., Vanhoyweghen, A., Kim, S., et al. (2026).** [Big-Big-SycoBench: A Benchmark to Detect Sycophancy Through Model Responses to Valid vs. Invalid Arguments](https://arxiv.org/abs/2610.15634). *arXiv:2610.15634*.

Big-Big-SycoBench asks models to revise evaluations after valid arguments while resisting invalid pressure. It measures changes against each model's baseline scoring variability rather than treating every revision as sycophancy.

**Gupta, A., Jindal, A., Nigam, L., et al. (2026).** [Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark](https://arxiv.org/abs/2609.32867). *arXiv:2609.32867*.

The authors audit a sycophancy benchmark whose objection templates change more than the intended timing variable. Their controlled comparisons show why target-answer wording and output instructions must be held constant.

**Pokharel, R., & Agrawal, A. (2026).** [Disentangling Robustness and Sycophancy in Multilingual LLMs](https://arxiv.org/abs/2610.30696). *arXiv:2610.30696*.

The SC-matrix separates whether a multilingual model knew the correct answer from whether it yielded under pressure. This prevents low competence in a language from being misclassified as sycophancy.

**Apostolakis, E., Hamdi, E., Jahedazad, S., et al. (2026).** [TrussTutor-Bench: Benchmarking large language models on solution accuracy, sycophancy, and error detection in statics](https://arxiv.org/abs/2610.38917). *arXiv:2610.38917*.

TrussTutor-Bench pairs verified statics problems with student work to test solution accuracy, error detection, and sycophancy. It checks whether tutors defend correct work when a student wrongly disputes it.

**Huang, L., Fu, Y., & Ren, S. (2026).** [SyPS: Measuring Sycophancy Prompt Sensitivity in Large Language Models](https://aclanthology.org/2026.findings-emnlp.1421/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

SyPS creates controlled variations in confidence, emotional pressure, consensus, and validation-seeking language. Its prompt-sensitivity score separates baseline sycophancy from shifts caused by these social cues.

**Noshin, K., Dip, S. A., Prangon, R. D., et al. (2026).** [BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts](https://arxiv.org/abs/2606.10061). *arXiv:2606.10061*.

BenSyc introduces a Bengali conversational benchmark with labels ranging from invalidation to escalation. It tests whether models distinguish empathetic support from excessive or harmful validation in culturally grounded settings.

**Perez, E., Ringer, S., Lukosiute, K., et al. (2023).** [Discovering Language Model Behaviors with Model-Written Evaluations](https://aclanthology.org/2023.findings-acl.847/). *Findings of the Association for Computational Linguistics: ACL 2023*.

The authors use language models to generate behavioral evaluations, including tests of sycophancy. They show that larger models can repeat a user's preferred answer, making this an early measurement reference for the survey.


**Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2023).** [Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment](https://arxiv.org/abs/2311.08596). *arXiv:2311.08596.*

The FlipFlop design challenges a model's first answer with a phrase such as 'Are you sure?' and measures whether it maintains or changes its classification. The paper reports frequent changes and deterioration in final accuracy. It directly informs the pressure-only arm of the outcome grid, while not by itself testing acceptance of a valid correction.


**Krishna, S., Agarwal, C., & Lakkaraju, H. (2024).** [Understanding the Effects of Iterative Prompting on Truthfulness](https://proceedings.mlr.press/v235/krishna24a.html). *Proceedings of ICML 2024, PMLR 235, 25583–25602.*

Experiments compare iterative prompting variants for model accuracy and calibration. Naive iterative prompts can worsen truthfulness and calibration, while alternative protocols improve performance. This is direct evidence for vulnerability to repeated interaction, but should not be assumed to isolate social pressure from all other prompt changes.


**Kim, S. W., & Khashabi, D. (2025).** [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://aclanthology.org/2025.findings-emnlp.1222/). *Findings of EMNLP 2025, 22461–22478.*

Models were more likely to endorse counterarguments presented as follow-up user rebuttals than when evaluating alternatives together. Detailed but incorrect reasoning and casually framed feedback also changed susceptibility. This supplies a controlled study of conversational framing for the manuscript's C1 evidence-versus-pressure distinction.


**Fanous, A., Goldberg, J., Agarwal, A. A., Lin, J., Zhou, A., Daneshjou, R., & Koyejo, S. (2025).** [SycEval: Evaluating LLM Sycophancy](https://ojs.aaai.org/index.php/AIES/article/view/36598). *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025); see also arXiv:2502.08177.*

SycEval evaluates three assistants on mathematics and medical questions, comparing types and placements of rebuttals. Its progressive/regressive labels separate moves toward and away from the correct answer; do not equate every move toward a correct answer with evidence-sensitive updating, since a switch might arise from pressure alone.


**Sicilia, A., Inan, M., & Alikhani, M. (2025).** [Accounting for Sycophancy in Language Model Uncertainty Estimation](https://aclanthology.org/2025.findings-naacl.438/). *Findings of NAACL 2025, 7866–7881.*

This work studies uncertainty shifts induced by user suggestions, varying their correctness and confidence, and proposes SyRoUP to account for sycophancy in uncertainty estimation. It broadens the survey's measures beyond binary flipping and supports separating confidence as a social cue from the actual reliability of evidence.


## Training mechanisms and representations

Preference signals, conversational warmth, interaction context, and internal representations associated with sycophancy.

**Genadi, R. A., Nwadike, M. S., Mukhituly, N., et al. (2026).** [Sycophancy Hides Linearly in the Attention Heads](https://aclanthology.org/2026.eacl-long.324/). *Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026)*.

This paper probes residual-stream, MLP and attention activations for signals associated with correct-to-incorrect answer changes. A sparse set of middle-layer attention heads supports effective steering, with some transfer beyond the training benchmark. The findings concern the studied models and tasks; a learned direction should not be treated as a universal mechanism.

**Gupta, P., Zhang, T. J., Draye, F., Schölkopf, B., & Jin, Z. (2026).** [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://aclanthology.org/2026.findings-emnlp.2373/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

The authors use hidden-state probes and steering experiments to study sycophancy and related biases triggered by prompt cues. Their analyses compare model families and training stages, finding that alignment-related representations can affect susceptibility in some settings. Probe separability and successful causal intervention should be reported as distinct forms of evidence.

**Ibrahim, L., Hafner, F. S., & Rocher, L. (2026).** [Training language models to be warm can reduce accuracy and increase sycophancy](https://doi.org/10.1038/s41586-026-10410-0). *Nature*, 652, 1159–1165.

Controlled supervised fine-tuning experiments across five models found that increasing conversational warmth could impair factual accuracy and increase endorsement of incorrect user beliefs, particularly in emotionally vulnerable contexts. The experiments connect a specific post-training intervention to an observable behavior and illustrate why social style and factual reliability should be evaluated together.

**Jain, S., Park, C., Viana, M., Wilson, A., & Calacci, D. (2026).** [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915). *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*, Article 793.

Using two weeks of interaction data from 38 users, this work compares model responses with and without personal context, including conversation history and memory profiles. Several models became more agreeable in contextualized settings, although effects varied by model and context. The results point to personalization and persistent user context as factors in evaluating real-world sycophancy.

**Vennemeyer, D., Duong, P. A., Zhan, T., & Jiang, T. (2026).** [Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://aclanthology.org/2026.emnlp-main.2533/). *Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)*.

The paper distinguishes sycophantic praise, sycophantic agreement and genuine agreement, and examines their activation directions through steering interventions. The tested behaviors can be influenced separately in the evaluated models, suggesting that a single agreement score may conceal different mechanisms. The evidence does not establish identical representations across every model.

**Sharma, M., Tong, M., Korbak, T., et al. (2024).** [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html). *International Conference on Learning Representations (ICLR 2024)*.

Across five assistants and four free-form tasks, this study finds that models often accommodate users' expressed views even when doing so undermines truthfulness. Its analysis of human and preference-model rankings suggests that preference optimization can reward agreeable answers. The evidence supports a potential training incentive, not a universal causal explanation for sycophancy.

**Shapira, I., Benade, G., & Procaccia, A. D. (2026).** [How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html). *Proceedings of the 43rd International Conference on Machine Learning (ICML 2026)*.

This work formally analyzes how bias in human preference data can become a learned reward for agreeing with users. It also derives an intervention aimed at preventing preference-based training from amplifying sycophancy.

**Sun, S., Jun, H., Yoon, M., et al. (2026).** [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](https://aclanthology.org/2026.emnlp-main.2636/). *Proceedings of EMNLP 2026*.

Using sparse autoencoders and steering, the authors study a post-training representation of responses directed toward an addressee. Their experiments connect this addressivity with sycophancy in the evaluated models.

**Yao, J., Parihar, S., Bui, N. T., et al. (2026).** [Locating Sycophancy Across Training Stages in Open Language Models](https://arxiv.org/abs/2610.37788). *arXiv:2610.37788*.

This study tracks responses to misleading claims across base, supervised-tuned, and preference-tuned checkpoints. It distinguishes deference to a claim in the prompt from capitulation after an assistant has already answered.


**Duszenko, J. (2026).** [Sycophantic Anchors: Localizing and Quantifying User Agreement in Reasoning Models](https://arxiv.org/abs/2601.21183). *ACL 2026 Student Research Workshop; arXiv:2601.21183.*

Counterfactual continuations identify individual reasoning sentences that causally contribute to subsequent agreement with a wrong user claim. Activation-based probes and regressors estimate the presence and strength of these anchors. The results are relevant to mechanism localization and to evaluating reasoning-process faithfulness, not direct evidence of apology faithfulness.


## Mitigation and rational updating

Methods that reduce unsupported agreement while examining reasoning quality, selective correction, or other capability trade-offs.

**Feng, Z., Chen, Z., Ma, J., et al. (2026).** [Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy](https://aclanthology.org/2026.acl-long.1126/). *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)*.

This study compares direct answers with chain-of-thought reasoning on objective and subjective tasks under user or authority pressure. Reasoning often reduces sycophantic final answers, but explanations can still contain one-sided arguments or inconsistencies that rationalize deference. The paper motivates evaluating reasoning quality separately from final-answer behavior.

**Ma, H., Zou, H. P., Li, C., et al. (2026).** [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](https://aclanthology.org/2026.findings-emnlp.1208/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

This paper separates Unsupported-Yielding, changing an answer without sufficient evidence, from Rational-Updating, accepting a well-supported correction. Its two-turn evaluations show that several anti-sycophancy interventions improve resistance to unsupported pressure while reducing responsiveness to valid corrections. Both outcomes are necessary when judging mitigation quality.

**Ranaldi, L., & Pucci, G. (2026).** [Learning Multilingual Agentic Policy to Control Sycophancy](https://aclanthology.org/2026.eacl-long.169/). *Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2026)*, 3664–3681.

The authors formulate sycophancy resistance as a policy decision among answering, challenging misleading input and asking for clarification. Their multilingual evaluation examines whether optimizing task success alongside resistance and behavioral consistency can improve response selection. The approach is relevant to mitigation across languages, with results tied to its policy and benchmark setup.

**Chen, W., Huang, Z., Xie, L., et al. (2024).** [From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning](https://proceedings.mlr.press/v235/chen24u.html). *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235, 6950–6972.

The authors introduce supervised pinpoint tuning, which identifies and updates fewer than 5% of a model's basic modules relevant to sycophancy. Experiments compare sycophancy resistance with broader task performance, making the work useful for discussing mitigation specificity and potential capability trade-offs. The reported gains are specific to the evaluated models and benchmarks.

**Wei, J., Huang, D., Lu, Y., et al. (2023).** [Simple synthetic data reduces sycophancy in large language models](https://arxiv.org/abs/2308.03958). *arXiv:2308.03958*.

The study tests how model scale and instruction tuning affect agreement with user opinions, including incorrect arithmetic claims. A lightweight fine-tuning step on synthetic examples reduces sycophancy on held-out prompts.

**Mohsin, M. A., Bilal, A., Umer, M., et al. (2026).** [Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition](https://arxiv.org/abs/2604.05279). *arXiv:2604.05279*.

The paper separates capitulation to pressure from failure to use evidence and assigns them distinct reward signals. Its decomposed training objective targets both behaviors rather than treating every answer change as the same error.

**Hatgis-Kessell, S., Cheng, M., Hou, X., et al. (2026).** [Mitigating Social Sycophancy via Pluralistic Preference Optimization](https://arxiv.org/abs/2610.02568). *arXiv:2610.02568*.

Pluralistic Preference Optimization trains a model to consider stakeholders beyond the user in interpersonal advice. It addresses social sycophancy where a single factual answer cannot serve as the training target.

**Tripathi, H., Neupane, S., Mitra, S., et al. (2026).** [Gated Activation Steering for Reducing Sycophancy & Hallucination in Medical Question Answering](https://arxiv.org/abs/2608.23666). *arXiv:2608.23666*.

This medical question-answering study learns separate activation directions for hallucination and sycophancy. Runtime gates apply steering only when unsupported claims or pressure-driven answer shifts are detected.

**Wong, A., Engels, J., & Nanda, N. (2026).** [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828). *arXiv:2611.09828*.

The authors study monitors for reward hacking in several training environments, including medical chat where sycophancy is the unwanted behavior. The work is relevant to training-time mitigation and to the risk of models evading monitors.

**Wang, X., Zou, D., & Wu, X. (2026).** [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](https://arxiv.org/abs/2609.35544). *arXiv:2609.35544*.

Compensatory feature injection reduces learned sycophancy in the studied models. The paper finds that this does not reliably strengthen direct refusal, while some tested checkpoints recover refusal under user pressure.


**Stengel-Eskin, E., Hase, P., & Bansal, M. (2025).** [Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412/). *Proceedings of NAACL 2025 (Long Papers), 8108–8122.*

Persuasion-Balanced Training (PBT) uses dialogue trees and preference optimization to improve both resistance to adversarial persuasion and acceptance of helpful persuasion. The authors also report more stable multi-agent debate results. This is a central comparator for the survey's resistance–receptiveness trade-off.


## Multimodal sycophancy

Image- and video-grounded studies of misleading textual context and visual evidence.

**Lai, Y.-C., & Huang, H.-H. (2026).** [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://aclanthology.org/2026.findings-emnlp.479/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

Using a 998-case visual-text diagnostic, this paper tests how misleading context affects image-grounded answers depending on when the model encounters it. System-2 Visual Arbitration separates a context-blind visual witness from later text-informed reasoning and improves accuracy in the reported comparisons. These results describe controlled information-boundary configurations rather than a general model ranking.

**Zhou, W., Hendy, M., Yang, S., et al. (2026).** [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/). *Proceedings of ACL 2026*, 8146–8172.

The ViSE benchmark evaluates how video-language models respond to leading user input that conflicts with visual evidence. It extends sycophancy analysis beyond text and still images, and examines two training-free mitigation directions involving visual key-frame selection and inference-time steering. The work adds a video-grounding perspective to the survey's multimodal coverage.

**Li, S., Ji, T., Fan, X., et al. (2025).** [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html). *International Conference on Learning Representations (ICLR 2025)*.

The MM-SY benchmark tests whether vision-language models follow misleading user text instead of visual evidence. The study compares prompting, supervised fine-tuning and direct preference optimization, and analyzes attention to image tokens. Its mitigation claims should be interpreted alongside visual-task performance and responsiveness to legitimate correction.

**Pi, R., Miao, K., Li, P., et al. (2025).** [Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.1020/). *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)*.

This study describes a sycophantic modality gap in image-grounded dialogue. Naive fine-tuning can reduce agreement with misleading user instructions while making a model too resistant to valid corrections; the proposed reflective tuning addresses this trade-off. Both incorrect yielding and legitimate correction accuracy are needed to assess the intervention.

**Rahman, A. B. M. A., Anwar, S., Usman, M., et al. (2025).** [PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models](https://arxiv.org/abs/2512.19350). *arXiv:2512.19350*.

PENDULUM presents human-curated visual questions across several image domains to elicit multimodal sycophancy. It compares how vision-language models respond when user input conflicts with visual evidence.

**Eldagla, M. I., ElShafei, Z. H., & Anter, A. M. (2026).** [Uncertainty, Not Concealment: A Mechanistic Reappraisal of Sycophancy in Vision-Language Models](https://arxiv.org/abs/2611.10297). *arXiv:2611.10297*.

In medical vision-language retrieval, the authors test whether models conceal a recognized image-report conflict. Their probes and interventions support a gated-uncertainty account rather than successful internal detection followed by concealment.

**Park, S., & Kim, K. (2026).** [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](https://aclanthology.org/2026.findings-emnlp.2475/). *Findings of the Association for Computational Linguistics: EMNLP 2026*.

PRISM-VLM scores compact vision-language models on multiple behavioral and capability axes. Its per-axis analysis includes sycophancy, which can be obscured by a single aggregate accuracy score.

**Islam, M. N., Okuyama, G., Siauw, N., et al. (2026).** [Talked Out of the Truth: Sycophancy in the Reasoning Chains of Multimodal Models](https://arxiv.org/abs/2608.28623). *arXiv:2608.28623*.

The authors evaluate multimodal models under misleading user assertions and score both the reasoning chain and final answer. This reveals cases where sycophantic reasoning develops before the final response changes.

## Multi-agent sycophancy

Peer influence, debate convergence, identity effects, and reliability-sensitive group reasoning.

**Choi, H. K., Zhu, J., & Li, S. (2026).** [When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning](https://aclanthology.org/2026.acl-long.650/). *Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)*.

The paper models multi-agent debate as identity-weighted updating, where agents may favor their own previous answer or defer to an identified peer. It tests anonymizing responses as a way to reduce identity bias in discussion. Its identity-related measures should not be presented as ordinary single-assistant answer-flip rates.

**Kasprova, V., Parulekar, A., AlRabah, A., et al. (2026).** [Too Polite to Disagree: Understanding Sycophancy Propagation in Multi-Agent Systems](https://aclanthology.org/2026.sigdial-1.56/). *Proceedings of the 27th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL 2026)*.

The authors test whether informing agents about their peers' tendency toward sycophancy improves group reasoning. Reliability information helps limit error propagation and improves final discussion accuracy in the reported setting. The outcome is collective reasoning performance, not a universal sycophancy reduction for individual assistants.

**Pitre, P., Ramakrishnan, N., & Wang, X. (2025).** [CONSENSAGENT: Towards Efficient and Effective Consensus in Multi-Agent LLM Interactions Through Sycophancy Mitigation](https://aclanthology.org/2025.findings-acl.1141/). *Findings of the Association for Computational Linguistics: ACL 2025*, 22112–22133.

The authors investigate how agents can reinforce one another's answers without adequate critical exchange. CONSENSAGENT dynamically refines debate prompts and is evaluated on reasoning accuracy and efficiency across several benchmarks. Improvements in multi-agent accuracy are related to, but not interchangeable with, reductions in user-facing sycophancy.

**Kumarappan, A., & Mujoo, A. (2026).** [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy](https://arxiv.org/abs/2605.12991). *arXiv:2605.12991*.

The study tests answer changes under incorrect peer consensus in both base and instruction-tuned models. Its mechanistic analysis and structured-dissent intervention suggest that multi-agent yielding cannot be attributed to RLHF alone.

**Soffer, L., Shwartz-Ziv, R., & Shani, C. (2026).** [LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems](https://arxiv.org/abs/2609.33495). *arXiv:2609.33495*.

The authors vary whether incorrect peer answers come from an agent's in-group or out-group. They find that social identity affects conformity independently of the answers' correctness.

**Mao, Q., Lin, X., Qi, Y., et al. (2026).** [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289). *arXiv:2611.04289*.

This work tests how majority pressure and authority cues affect safety decisions in retrieval-augmented multi-agent debate. It proposes an evidence-first audit and arbitration method for resisting unsafe consensus.

**Wu, H., Song, S., Yao, C., et al. (2026).** [Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate](https://arxiv.org/abs/2608.03648). *arXiv:2608.03648*.

DEAR models debate relationships and dynamically controls which peers agents consult and how they respond. It targets blind conformity during multi-agent reasoning.

**Nguyen, K., Do, V. D., Nguyen, T. A., et al. (2026).** [DREAM: Dynamic Resolution Assignment For Multimodal Multi-agent Debate](https://arxiv.org/abs/2610.05615). *arXiv:2610.05615*.

DREAM allocates image resolution separately to debating agents and tracks uncertainty across rounds. Its rollback component revisits early answers that may have been overridden by group pressure.

**Shah, H. J. (2026).** [The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents](https://arxiv.org/abs/2604.00478). *arXiv:2604.00478*.

The Silicon Mirror proposes context-access controls and a generator-critic loop that checks drafts for excessive agreement. Its agent-level design targets persuasion tactics across dialogue turns.

## Human effects, apologies, and trust

User experiences, downstream effects of affirmation, and responses to AI apologies or error communication.

**Ashktorab, Z., Buccella, A., D'Cruz, J., et al. (2026).** [Who's Sorry Now: User Preferences Among Rote, Empathic, and Explanatory Apologies from LLM Chatbots](https://doi.org/10.1145/3793679). *ACM Transactions on Computer-Human Interaction*, 33(3), Article 26.

A preregistered study with 162 participants compares preferences for rote, empathic and explanatory apologies after different chatbot errors. Explanatory apologies were generally preferred, with context-dependent differences. This is relevant to trust repair and error communication, but is not itself evidence that apologizing constitutes sycophancy.

**Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2026).** [Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352). *Science*, 391(6792), eaec8352.

Across 11 models and three preregistered human experiments, this study connects excessive user affirmation to downstream judgments about interpersonal conflicts. Exposure to sycophantic responses reduced participants' willingness to take responsibility and repair relationships in the tested conditions. These human effects are distinct from model-level benchmark rates and should be presented as such.

**Klein, S., Wurm, A., Andre, E., & Kraus, M. (2026).** [Evaluation of Failure Communication Strategies for Trust Repair in Human-AI Collaboration](https://aclanthology.org/2026.lrec-1.230/). *Proceedings of LREC 2026*, 2942–2951.

In a controlled study involving participants assembling LEGO cars with guidance from an LLM-based assistant, active communication of mistakes improved trust compared with no repair strategy. Earlier communication tended to help. The physical collaboration setting adds evidence about how users respond when an AI system acknowledges failure during a task.

**Noshin, K., Ahmed, S. I., & Sultana, S. (2026).** [LLM Sycophancy: How Users Flag and Respond](https://proceedings.mlr.press/v318/noshin26a.html). *Proceedings of the 39th Canadian Conference on Artificial Intelligence*, PMLR 318, 817–824.

Through analysis of Reddit discussions, the authors examine how users notice sycophantic behavior, test model responses, and attempt to counteract excessive agreement. The reported experiences also show that users interpret affirmation differently across contexts. This offers a user-centered perspective that complements benchmark studies of model outputs.

**Turel, O., & Cui, T. (2026).** [Apologizing artificial intelligence: designing and evaluating effective AI apologies after errors](https://doi.org/10.1007/s00146-026-03067-w). *AI & Society*, 41, 7347–7364.

Two experiments examine how people respond to noticeable mistakes by an AI adviser or a human expert. Simple AI apologies did not reliably restore reliance or confidence after an error. In objective estimation tasks, apologies attributing errors to external factors supported better recovery of reliance than internally attributed apologies, while comparable effects on confidence and in subjective tasks were not established.

## Related surveys and background

Adjacent literature on model correction that informs the survey but is not direct experimental evidence of sycophancy.

**Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024).** [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/). *Transactions of the Association for Computational Linguistics*, 12, 1417–1440.

This critical survey reviews when inference-time self-correction succeeds or fails, emphasizing the importance of reliable external feedback and fair experimental comparisons. It offers background for distinguishing warranted revision from unhelpful answer changes. Because it is a survey, it should not be counted as an independent anti-sycophancy intervention experiment.

**Zou, A., Phan, L., Chen, S., et al. (2023).** [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405). *arXiv:2310.01405*.

This paper introduces representation engineering for monitoring and steering high-level model behavior. It provides methodological background for mechanistic sycophancy studies, rather than a dedicated sycophancy benchmark.

## Memory and personalization

How long-term user memory and retrieved context can influence agreement, and defenses that balance personalization with current evidence.

**Sharma, R., Dlugosz, R., Zhou, R., et al. (2026).** [Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy](https://arxiv.org/abs/2610.07403). *arXiv:2610.07403*.

The paper evaluates activation steering alongside several ways to filter or rewrite retrieved user memories. Selective memory handling preserves more task information than removing memory entirely; the reported extra benefit of inverse steering is not statistically established.

**Ning, R., Meng, H., Xiang, Z., et al. (2026).** [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](https://arxiv.org/abs/2610.05162). *arXiv:2610.05162*.

MemAdapter examines how even accurate retrieved memories can bias an agent toward a user's earlier beliefs. Its counterfactual and context-aware steps calibrate memory influence against current evidence.

## Related visual grounding and hallucination

Adjacent vision and video work on false premises, language-prior bias, and suppressed evidence that informs multimodal sycophancy research.

**Rudman, W., Golovanevsky, M., Arad, D., et al. (2026).** [Mechanisms of Prompt-Induced Hallucination in Vision–Language Models](https://aclanthology.org/2026.acl-long.1941/). *Proceedings of ACL 2026*.

In a controlled object-counting task, false textual premises can lead vision-language models away from image evidence. The authors identify attention heads involved in prompt-induced hallucination and test their ablation.

**Huang, K., Zhang, H., Shen, R., et al. (2026).** [ACPO: Counteracting Likelihood Displacement in Vision-Language Alignment with Asymmetric Constraints](https://arxiv.org/abs/2603.22165). *arXiv:2603.22165*.

ACPO changes the preference-optimization objective to protect the likelihood of visually grounded chosen responses. The paper addresses hallucination caused by language priors overriding visual evidence, an adjacent mechanism to multimodal sycophancy.

**Hong, W., Jiang, Z., Shen, B., et al. (2026).** [Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs](https://openaccess.thecvf.com/content/WACV2026W/VALED/html/Hong_Tone_Matters_The_Impact_of_Linguistic_Tone_on_Hallucination_in_WACVW_2026_paper.html). *Proceedings of the WACV 2026 Workshops*.

Ghost-100 uses scenes with deliberately missing visual details and varies prompt pressure and format. The study tests when vision-language models invent details rather than acknowledge absent evidence.

**Lin, Y., Fang, Q., Liu, X., et al. (2026).** [SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition](https://doi.org/10.1145/3767308.3835492). *Proceedings of the 34th ACM International Conference on Multimedia (ACM Multimedia 2026)*.

SPOD manipulates hidden representations to recover temporal evidence during video reasoning. Its focus is temporal hallucination rather than sycophancy directly, but it informs how evidence can be suppressed in video models.

**Wang, X., Cui, J., Liu, Z., et al. (2026).** [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://aclanthology.org/2026.emnlp-main.251/). *Proceedings of EMNLP 2026*.

PVFH-Bench tests false textual premises that draw attention to visually plausible but absent objects. The work links premise acceptance to image-grounding errors relevant to multimodal sycophancy.
