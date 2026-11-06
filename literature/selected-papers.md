# Selected Literature on AI Apologies, Sycophancy, and Factual Correction

## LLM behavior, disagreement, and response to correction

**Sinha, D. (2026).** [SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants](https://aclanthology.org/2026.findings-acl.1759/). *Findings of the Association for Computational Linguistics: ACL 2026*, 35278–35284.

SycoBench-600 tests whether models resist misleading social pressure while accepting valid corrections. Its distinction between resistance and selective updating provides a useful way to assess whether an answer change reflects a justified correction or agreement with an unsupported user claim.

**Alnasser, R., Çetinkaya, Y. M., Zhao, S., & Elmas, T. (2026).** [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/). *Proceedings of EMNLP 2026*, 36257–36272.

Across 14 models and 32,340 responses to controlled challenges, the authors distinguish claim revision from social validation, apology, and shifts in epistemic authority. Models apologized in 33% of responses, yet 59% of those apologies accompanied maintenance of the original claim. These findings make it important to measure apologies separately from whether an answer was revised or supported with evidence.

**Li, J., Menon, S., Frischmann, B., Wilson, S., & Rajtmajer, S. (2026).** [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/). *Proceedings of EMNLP 2026*, 27134–27156.

Using seven LLMs and prompts drawn from two Reddit datasets, this study compares evaluations of third-party accounts with responses to users describing their own actions or opinions. Models were less willing to express negative judgments to the user, especially when disclosures included loneliness or distress. The study identifies evasive responses, not only explicit agreement, as a form of sycophancy.

**Zhou, W., Hendy, M., Yang, S., et al. (2026).** [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/). *Proceedings of ACL 2026*, 8146–8172.

The ViSE benchmark evaluates how video-language models respond to leading user input that conflicts with visual evidence. It extends sycophancy analysis beyond text and still images, and examines two training-free mitigation directions involving visual key-frame selection and inference-time steering. The work adds a video-grounding perspective to the survey's multimodal coverage.

## User experience, trust, and error communication

**Turel, O., & Cui, T. (2026).** [Apologizing artificial intelligence: designing and evaluating effective AI apologies after errors](https://doi.org/10.1007/s00146-026-03067-w). *AI & Society*, 41, 7347–7364.

Two experiments examine how people respond to noticeable mistakes by an AI adviser or a human expert. Simple AI apologies did not reliably restore reliance or confidence after an error. In objective estimation tasks, apologies attributing errors to external factors supported better recovery of reliance than internally attributed apologies, while comparable effects on confidence and in subjective tasks were not established.

**Klein, S., Wurm, A., Andre, E., & Kraus, M. (2026).** [Evaluation of Failure Communication Strategies for Trust Repair in Human-AI Collaboration](https://aclanthology.org/2026.lrec-1.230/). *Proceedings of LREC 2026*, 2942–2951.

In a controlled study involving participants assembling LEGO cars with guidance from an LLM-based assistant, active communication of mistakes improved trust compared with no repair strategy. Earlier communication tended to help. The physical collaboration setting adds evidence about how users respond when an AI system acknowledges failure during a task.

**Noshin, K., Ahmed, S. I., & Sultana, S. (2026).** [LLM Sycophancy: How Users Flag and Respond](https://proceedings.mlr.press/v318/noshin26a.html). *Proceedings of the 39th Canadian Conference on Artificial Intelligence*, PMLR 318, 817–824.

Through analysis of Reddit discussions, the authors examine how users notice sycophantic behavior, test model responses, and attempt to counteract excessive agreement. The reported experiences also show that users interpret affirmation differently across contexts. This offers a user-centered perspective that complements benchmark studies of model outputs.

## Training and interaction-context influences

**Ibrahim, L., Hafner, F. S., & Rocher, L. (2026).** [Training language models to be warm can reduce accuracy and increase sycophancy](https://doi.org/10.1038/s41586-026-10410-0). *Nature*, 652, 1159–1165.

Controlled supervised fine-tuning experiments across five models found that increasing conversational warmth could impair factual accuracy and increase endorsement of incorrect user beliefs, particularly in emotionally vulnerable contexts. The experiments connect a specific post-training intervention to an observable behavior and illustrate why social style and factual reliability should be evaluated together.

**Jain, S., Park, C., Viana, M., Wilson, A., & Calacci, D. (2026).** [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915). *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*, Article 793.

Using two weeks of interaction data from 38 users, this work compares model responses with and without personal context, including conversation history and memory profiles. Several models became more agreeable in contextualized settings, although effects varied by model and context. The results point to personalization and persistent user context as factors in evaluating real-world sycophancy.

## Forward-looking evaluation and position

**Kasneci, E., & Kasneci, G. (2026).** [Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://proceedings.mlr.press/v306/kasneci26a.html). *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306, 170836–170855.

This position paper argues that tutoring assistants should challenge students' misconceptions constructively, even when users apply authority or social pressure. Its EduFrameTrap benchmark evaluates this tension across educational subjects. The proposed standard of supportive but evidence-sensitive correction provides a concise direction for future assessment of conversational assistants.
