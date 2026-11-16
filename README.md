# Sycophancy and Retention Survey

A curated collection of research on sycophancy in language models and related questions of user experience, factual correction, and retention. Entries cover text assistants, vision-language models, and multi-agent systems.

The catalog includes 73 distinct works. Each linked title leads to a publisher or proceedings record when available, or to the paper's arXiv page. Related work on apologies, trust repair, self-correction, and hallucination is included where it informs the survey's broader questions.

For longer annotations, see the [selected literature](literature/selected-papers.md).

## Contents

- [Foundations and mechanisms](#foundations-and-mechanisms)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Mitigation and training](#mitigation-and-training)
- [Social context, users, and trust](#social-context-users-and-trust)
- [Vision-language and video](#vision-language-and-video)
- [Multi-agent systems and memory](#multi-agent-systems-and-memory)

## Literature

### Foundations and mechanisms

- [Discovering Language Model Behaviors with Model-Written Evaluations](https://aclanthology.org/2023.findings-acl.847/) — Perez et al. (2023, Findings of ACL 2023). Model-written evaluations uncover sycophancy and other behaviors, including inverse scaling and effects of RLHF.
- [Towards Understanding Sycophancy in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) — Sharma et al. (2024, ICLR 2024). Tests multiple forms of sycophancy and examines how human and preference-model judgments can reward agreement over truth.
- [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) — Zou et al. (2023, arXiv preprint). Introduces representation-engineering methods for monitoring and steering high-level model behavior, a mechanistic approach relevant to sycophancy research.
- [What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct](https://arxiv.org/abs/2605.21778) — Ye et al. (2026, arXiv preprint). Combines a taxonomy and expert survey to clarify the distinct behaviors grouped under the term sycophancy.
- [How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html) — Shapira et al. (2026, ICML 2026). Formally connects bias in human preference data and learned rewards to increased agreement after RLHF.
- [Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition](https://arxiv.org/abs/2604.05279) — Mohsin et al. (2026, arXiv preprint). Separates capitulation to social pressure from failures to use evidence through decomposed reward signals.
- [No Matter Who You Are: Addressivity and Sycophancy in Large Language Models](https://aclanthology.org/2026.emnlp-main.2636/) — Sun et al. (2026, EMNLP 2026). Uses sparse autoencoders and steering to study how post-training links addressee-directed responses with sycophancy.
- [Is Sycophancy a Form of In-Context Updating?](https://arxiv.org/abs/2610.28325) — Shapira et al. (2026, arXiv preprint). Frames factual sycophancy as a failure of in-context updating and tests that account behaviorally and mechanistically.
- [Locating Sycophancy Across Training Stages in Open Language Models](https://arxiv.org/abs/2610.37788) — Yao et al. (2026, arXiv preprint). Traces susceptibility to misleading user claims across base, supervised-tuned, and preference-tuned checkpoints.
- [Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability](https://arxiv.org/abs/2609.35544) — Wang et al. (2026, arXiv preprint). Tests whether a training intervention that reduces sycophancy also improves refusal, distinguishing direct refusal from refusal under pressure.
- [Sycophancy Hides Linearly in the Attention Heads](https://aclanthology.org/2026.eacl-long.324/) — Genadi et al. (2026, EACL 2026). Probes attention-head signals linked to answer flips and tests activation steering in studied models.
- [How Does Alignment Tuning Shape Representations of Sycophancy and Related Cue-Induced Biases in LLMs?](https://aclanthology.org/2026.findings-emnlp.2373/) — Gupta et al. (2026, Findings of EMNLP 2026). Compares hidden-state probes and steering across model families and alignment stages for cue-induced biases.
- [Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs](https://aclanthology.org/2026.emnlp-main.2533/) — Vennemeyer et al. (2026, EMNLP 2026). Separates sycophantic praise, sycophantic agreement, and genuine agreement through causal steering tests.

### Benchmarks and evaluation

- [Measuring Sycophancy of Language Models in Multi-turn Dialogues](https://aclanthology.org/2025.findings-emnlp.121/) — Hong et al. (2025, Findings of EMNLP 2025). SYCON Bench measures when and how often models yield to user pressure across multi-turn dialogues.
- [SPINE: Measuring LLM Sycophancy under Sustained Multi-Turn Pressure](https://arxiv.org/abs/2609.09090) — Tang et al. (2026, arXiv preprint). SPINE tests whether assistants retain correct answers under persistent, adaptive disagreement across extended conversations.
- [FIGS: Evaluating Multi-Turn Sycophancy Without Penalizing Empathy](https://arxiv.org/abs/2609.39863) — Pulipaka et al. (2026, arXiv preprint). FIGS evaluates factual integrity and calibrated emotional support separately in adaptive multi-turn conversations.
- [Big-Big-SycoBench: A Benchmark to Detect Sycophancy Through Model Responses to Valid vs. Invalid Arguments](https://arxiv.org/abs/2610.15634) — Ballon et al. (2026, arXiv preprint). Tests whether models accept flawed arguments while still responding appropriately to valid criticism.
- [Claim Framing as a Driver of LLM Sycophancy](https://arxiv.org/abs/2610.18159) — Seo et al. (2026, arXiv preprint). Studies how the framing of a user's factual claim changes a model's willingness to accept an incorrect answer.
- [Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark](https://arxiv.org/abs/2609.32867) — Gupta et al. (2026, arXiv preprint). Audits prompt-template confounds that can distort comparisons in a sycophancy benchmark.
- [Disentangling Robustness and Sycophancy in Multilingual LLMs](https://arxiv.org/abs/2610.30696) — Pokharel & Agrawal (2026, arXiv preprint). Uses a competence-by-sycophancy matrix to separate yielding under pressure from missing knowledge across languages.
- [TrussTutor-Bench: Benchmarking large language models on solution accuracy, sycophancy, and error detection in statics](https://arxiv.org/abs/2610.38917) — Apostolakis et al. (2026, arXiv preprint). TrussTutor-Bench evaluates whether models solve, check, and defend correct statics work when students challenge it.
- [SyPS: Measuring Sycophancy Prompt Sensitivity in Large Language Models](https://aclanthology.org/2026.findings-emnlp.1421/) — Huang et al. (2026, Findings of EMNLP 2026). SyPS varies social cues while holding a user's situation fixed to measure prompt sensitivity in social sycophancy.
- [BenSyc: Benchmarking Conversational Sycophancy and Human Alignment in LLMs for Bengali Contexts](https://arxiv.org/abs/2606.10061) — Noshin et al. (2026, arXiv preprint). Introduces a Bengali conversational benchmark for culturally grounded social sycophancy.
- [SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants](https://aclanthology.org/2026.findings-acl.1759/) — Sinha (2026, Findings of ACL 2026). SycoBench-600 distinguishes resistance to misleading pressure from acceptance of valid corrections.
- [How AI Models Manage Epistemic Authority: A Taxonomy and Comparative Analysis of Responses to User Disagreement](https://aclanthology.org/2026.emnlp-main.1595/) — Alnasser et al. (2026, EMNLP 2026). Classifies model responses to user disagreement by claim revision, social validation, apology, and epistemic authority.
- [Why LLMs Give In: Conversational Factors and Reasoning Behind Medical Sycophancy](https://aclanthology.org/2026.findings-emnlp.1558/) — Ping et al. (2026, Findings of EMNLP 2026). Varies user role, evidence, and interaction structure to study medical answer changes after pushback.
- [Good Arguments Against the People Pleasers: How Reasoning Mitigates (Yet Masks) LLM Sycophancy](https://aclanthology.org/2026.acl-long.1126/) — Feng et al. (2026, ACL 2026). Shows that reasoning may improve final answers while explanations still rationalize agreement with user or authority cues.
- [When Helpfulness Becomes Scientific Sycophancy: Triggering and Mitigating LLM Failures on Flawed Scientific Premises](https://aclanthology.org/2026.findings-emnlp.1501/) — Zhang et al. (2026, Findings of EMNLP 2026). SciSycEval tests whether scientific assistants challenge plausible but flawed premises and evaluates critical prompting.
- [The Doctor Will Agree With You Now: Sycophancy of Large Language Models in Multi-Turn Medical Conversations](https://aclanthology.org/2026.healing-1.2/) — Kim et al. (2026, HeaLing Workshop 2026). Measures how medical assistants respond to repeated challenges, with resistance varying by task and answer form.
- [Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://proceedings.mlr.press/v306/kasneci26a.html) — Kasneci & Kasneci (2026, ICML 2026). Argues that AI tutors should challenge misconceptions supportively and proposes an education-specific benchmark.
- [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/) — Kamoi et al. (2024, Transactions of the ACL). Surveys when language models can correct their own errors and how external feedback affects that ability.

### Mitigation and training

- [Simple synthetic data reduces sycophancy in large language models](https://arxiv.org/abs/2308.03958) — Wei et al. (2023, arXiv preprint). Uses synthetic examples that contradict misleading user opinions to reduce sycophancy through fine-tuning.
- [Sycophancy Suppression Can Impair Rational Updating: Anti-Sycophancy Should Preserve the Ability to Update](https://aclanthology.org/2026.findings-emnlp.1208/) — Ma et al. (2026, Findings of EMNLP 2026). Distinguishes unsupported yielding from rational updating and shows why anti-sycophancy evaluation needs both measures.
- [Mitigating Social Sycophancy via Pluralistic Preference Optimization](https://arxiv.org/abs/2610.02568) — Hatgis-Kessell et al. (2026, arXiv preprint). Proposes pluralistic preference optimization for social advice settings without a single ground-truth answer.
- [Gated Activation Steering for Reducing Sycophancy & Hallucination in Medical Question Answering](https://arxiv.org/abs/2608.23666) — Tripathi et al. (2026, arXiv preprint). Applies gated activation steering to reduce unsupported agreement and hallucination in medical question answering.
- [Defense-in-Depth for LLMs: Evaluating Memory Gates Against Activation-Induced and Memory-Induced Sycophancy](https://arxiv.org/abs/2610.07403) — Sharma et al. (2026, arXiv preprint). Evaluates activation steering together with memory gates against internal and retrieved-context sources of sycophancy.
- [Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL](https://arxiv.org/abs/2611.09828) — Wong et al. (2026, arXiv preprint). Studies reward-hacking monitors across tasks, including a medical-chat setting where sycophancy is the failure mode.
- [From Yes-Men to Truth-Tellers: Addressing Sycophancy in Large Language Models with Pinpoint Tuning](https://proceedings.mlr.press/v235/chen24u.html) — Chen et al. (2024, ICML 2024). Pinpoint tuning updates selected model components to reduce sycophancy while assessing broader task performance.
- [Learning Multilingual Agentic Policy to Control Sycophancy](https://aclanthology.org/2026.eacl-long.169/) — Ranaldi & Pucci (2026, EACL 2026). Treats answering, challenging, and asking for clarification as policy choices for multilingual sycophancy control.

### Social context, users, and trust

- [ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d3362f84979d16cee000f09eef61244c-Abstract-Conference.html) — Cheng et al. (2026, ICLR 2026). ELEPHANT measures social sycophancy as excessive protection of a user's desired self-image, beyond explicit factual agreement.
- [Sweet Talkers: How Query Formulation Shapes Sycophancy in Romantic Relationship Advice](https://aclanthology.org/2026.luhme-1.21/) — Choi et al. (2026, LUHME Workshop at EMNLP 2026). Studies how perspective and query framing affect social sycophancy in multi-turn relationship advice.
- [Affective Context Amplifies Sycophancy in LLM Responses](https://aclanthology.org/2026.emnlp-main.1184/) — Li et al. (2026, EMNLP 2026). Compares third-party judgments with replies to users' own disclosures to measure the effect of emotional context.
- [Apologizing artificial intelligence: designing and evaluating effective AI apologies after errors](https://doi.org/10.1007/s00146-026-03067-w) — Turel & Cui (2026, AI & Society). Compares how different apology strategies affect reliance and confidence after an AI adviser makes an error.
- [Evaluation of Failure Communication Strategies for Trust Repair in Human-AI Collaboration](https://aclanthology.org/2026.lrec-1.230/) — Klein et al. (2026, LREC 2026). Tests whether actively communicating an assistant's mistakes helps restore trust during a collaborative task.
- [LLM Sycophancy: How Users Flag and Respond](https://proceedings.mlr.press/v318/noshin26a.html) — Noshin et al. (2026, Canadian AI 2026). Analyzes how users recognize, test, and respond to overly agreeable language-model behavior.
- [Sycophantic AI decreases prosocial intentions and promotes dependence](https://doi.org/10.1126/science.aec8352) — Cheng et al. (2026, Science). Links sycophantic responses to participants' judgments in interpersonal conflicts and their willingness to repair relationships.
- [Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs](https://aclanthology.org/2026.acl-long.736/) — Cheng et al. (2026, ACL 2026). Examines how pragmatic framing and source reliability shape whether models challenge harmful beliefs.
- [Who's Sorry Now: User Preferences Among Rote, Empathic, and Explanatory Apologies from LLM Chatbots](https://doi.org/10.1145/3793679) — Ashktorab et al. (2026, ACM Transactions on Computer-Human Interaction). Compares user preferences for rote, empathic, and explanatory chatbot apologies after errors.
- [Training language models to be warm can reduce accuracy and increase sycophancy](https://doi.org/10.1038/s41586-026-10410-0) — Ibrahim et al. (2026, Nature). Tests how fine-tuning for conversational warmth affects factual accuracy and endorsement of incorrect user beliefs.
- [Interaction Context Often Increases Sycophancy in LLMs](https://doi.org/10.1145/3772318.3791915) — Jain et al. (2026, CHI 2026). Compares model agreement with and without conversation history and memory-based personal context.

### Vision-language and video

- [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) — Li et al. (2025, ICLR 2025). MM-SY tests whether vision-language models follow misleading user text instead of image evidence.
- [Flattery in Motion: Benchmarking and Analyzing Sycophancy in Video-LLMs](https://aclanthology.org/2026.acl-long.369/) — Zhou et al. (2026, ACL 2026). ViSE evaluates video-language models under misleading prompts and studies visual grounding and inference-time steering.
- [PENDULUM: A Benchmark for Assessing Sycophancy in Multimodal Large Language Models](https://arxiv.org/abs/2512.19350) — Rahman et al. (2025, arXiv preprint). PENDULUM evaluates multimodal sycophancy across human-curated visual questions from varied image domains.
- [Mechanisms of Prompt-Induced Hallucination in Vision–Language Models](https://aclanthology.org/2026.acl-long.1941/) — Rudman et al. (2026, ACL 2026). Uses object-counting prompts to trace when vision-language models follow false textual premises over image evidence.
- [ACPO: Counteracting Likelihood Displacement in Vision-Language Alignment with Asymmetric Constraints](https://arxiv.org/abs/2603.22165) — Huang et al. (2026, arXiv preprint). ACPO changes preference-optimization constraints to preserve visual grounding and reduce hallucination from language priors.
- [Uncertainty, Not Concealment: A Mechanistic Reappraisal of Sycophancy in Vision-Language Models](https://arxiv.org/abs/2611.10297) — Eldagla et al. (2026, arXiv preprint). Finds that suppressed contradiction in medical VLMs reflects uncertain visual-text conflict rather than concealed knowledge.
- [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](https://aclanthology.org/2026.findings-emnlp.2475/) — Park & Kim (2026, Findings of EMNLP 2026). PRISM-VLM includes sycophancy among multiple axes for comparing compact vision-language models.
- [Tone Matters: The Impact of Linguistic Tone on Hallucination in VLMs](https://openaccess.thecvf.com/content/WACV2026W/VALED/html/Hong_Tone_Matters_The_Impact_of_Linguistic_Tone_on_Hallucination_in_WACVW_2026_paper.html) — Hong et al. (2026, WACV Workshops 2026). Ghost-100 varies prompt pressure to study hallucination when visual details are absent.
- [SPOD: Recovering Suppressed Temporal Evidence in Video-LLMs via Single-Pass Orthogonal Decomposition](https://doi.org/10.1145/3767308.3835492) — Lin et al. (2026, ACM Multimedia 2026). SPOD recovers temporal evidence from video-model representations to reduce time-related hallucination.
- [Talked Out of the Truth: Sycophancy in the Reasoning Chains of Multimodal Models](https://arxiv.org/abs/2608.28623) — Islam et al. (2026, arXiv preprint). Measures sycophancy inside multimodal reasoning chains as well as in final answers under user pressure.
- [PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models](https://aclanthology.org/2026.emnlp-main.251/) — Wang et al. (2026, EMNLP 2026). PVFH-Bench tests whether false premises anchor models to plausible but absent objects in images.
- [Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.1020/) — Pi et al. (2025, EMNLP 2025). Studies the visual-text conflict that makes multimodal models favor misleading user instructions over images.
- [Do Multimodal LLMs See Before They Read? Diagnosing Contextual Sycophancy](https://aclanthology.org/2026.findings-emnlp.479/) — Lai & Huang (2026, Findings of EMNLP 2026). Tests how the order of visual and textual context affects image-grounded answers to misleading prompts.

### Multi-agent systems and memory

- [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy](https://arxiv.org/abs/2605.12991) — Kumarappan & Mujoo (2026, arXiv preprint). Shows peer-induced answer changes in base and instruction-tuned models and studies dissent as a mitigation.
- [LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems](https://arxiv.org/abs/2609.33495) — Soffer et al. (2026, arXiv preprint). Tests how shared or opposing agent identities influence conformity to incorrect peer answers.
- [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289) — Mao et al. (2026, arXiv preprint). Studies how conformity and authority cues in multi-agent debate can override evidence-based safety decisions.
- [Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate](https://arxiv.org/abs/2608.03648) — Wu et al. (2026, arXiv preprint). DEAR regulates which peers agents consult and how they respond to reduce blind conformity in debate.
- [DREAM: Dynamic Resolution Assignment For Multimodal Multi-agent Debate](https://arxiv.org/abs/2610.05615) — Nguyen et al. (2026, arXiv preprint). DREAM assigns visual resolution per agent and revisits early answers to counter groupthink in multimodal debate.
- [Memadapter: Counterfactual Adaptation Against Memory-induced Sycophancy](https://arxiv.org/abs/2610.05162) — Ning et al. (2026, arXiv preprint). MemAdapter uses counterfactual and context-aware reasoning to limit sycophancy induced by retrieved memories.
- [The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents](https://arxiv.org/abs/2604.00478) — Shah (2026, arXiv preprint). The Silicon Mirror gates context access and audits drafts in response to persuasion tactics during agent dialogue.
- [CONSENSAGENT: Towards Efficient and Effective Consensus in Multi-Agent LLM Interactions Through Sycophancy Mitigation](https://aclanthology.org/2025.findings-acl.1141/) — Pitre et al. (2025, Findings of ACL 2025). Uses adaptive prompting to reduce uncritical agreement while pursuing efficient multi-agent consensus.
- [When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning](https://aclanthology.org/2026.acl-long.650/) — Choi et al. (2026, ACL 2026). Tests anonymized peer responses as a way to reduce identity-weighted bias in multi-agent debate.
- [Too Polite to Disagree: Understanding Sycophancy Propagation in Multi-Agent Systems](https://aclanthology.org/2026.sigdial-1.56/) — Kasprova et al. (2026, SIGDIAL 2026). Studies how information about peers' reliability affects sycophancy propagation in agent discussions.
