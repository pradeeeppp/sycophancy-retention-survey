# Candidate literature triage — 2026-11-03

> **Review-stage reference inventory, not a deduplicated or accepted bibliography.** These are candidate references for the survey outline's behaviors (Section 1), human/user impacts (Section 2), training and mechanism evidence (Section 3), and mitigations (Section 4). **Do not merge wholesale into the final corpus until checking the shared Google Sheets' full Matrix / survey-only rows.**

## Scope and verification

- Publication titles, years, venues and permanent URLs were checked against journal/publisher, official conference, ACL Anthology, arXiv, PubMed/dblp, or author/archival records on 2026-11-03.
- Notes below reflect published abstracts and accessible method/summary details; **this is not a completed full-text critical appraisal**.
- The two uploaded CSV files available for this audit are *summary and count tabs*, not the paper-by-paper Matrix. Thus **duplicate status cannot be certified** across the team's 49-paper and 21-review collections. Known or likely overlaps are flagged below.
- Keep apology language, true factual correction, user-preference effects, training-method interventions and model-internal causal mechanisms **as separate evidence types**. An observed behavioral pattern does not by itself identify a specific RLHF reward cause.
- Prefer definitive published versions over preprints when both are identified; do not claim acceptance for an under-review manuscript.

## Apology and user trust

### Who's Sorry Now: User Preferences Among Rote, Empathic, and Explanatory Apologies from LLM Chatbots

- **Citation:** Ashktorab et al. (2026), ACM Transactions on Computer-Human Interaction. [Publisher / archival record](https://doi.org/10.1145/3793679).
- **Supported relevance:** Preregistered vignette-based study of 162 participants comparing preferences for rote, empathic, and explanatory apologies after different chatbot errors.
- **Do not infer:** Measures user preferences for apology presentations; it does not establish that an apology reflects model-side error recognition or improves the underlying correction.
- **Survey alignment:** Sections 1, 2; direct apology; human-subject evidence.
- **Duplicate-screening status:** Check against full Matrix; likely overlaps its apology category.

### Apologizing artificial intelligence: designing and evaluating effective AI apologies after errors

- **Citation:** Turel and Cui (2026), AI & SOCIETY. [Publisher / archival record](https://doi.org/10.1007/s00146-026-03067-w).
- **Supported relevance:** Two experiments compare responses to erroneous AI versus human advice and examine how apology attribution changes trust repair.
- **Do not infer:** AI-advice/HCI evidence, not a specific LLM training or mechanistic-intervention study. Results concern user reliance and confidence.
- **Survey alignment:** Sections 1, 2; direct apology; human-subject evidence.
- **Duplicate-screening status:** Check against full Matrix; likely overlaps trust-repair papers.

## Behavior, feedback, and user outcomes

### Towards Understanding Sycophancy in Language Models

- **Citation:** Sharma et al. (2024), ICLR. [Publisher / archival record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html).
- **Supported relevance:** Studies sycophantic responses and preference judgments; finds that agreement with a user's views is often preferred and that preference-model optimization can sometimes trade truthfulness for agreement.
- **Do not infer:** Not a study of apology wording, and not proof that one particular RLHF reward pathway causes all sycophancy.
- **Survey alignment:** Sections 1, 3; behavioral + preference evidence.
- **Duplicate-screening status:** PROBABLE OVERLAP: the supplied Matrix summary explicitly mentions Sharma et al. Check DOI/title before any final inclusion.

### Sycophantic AI decreases prosocial intentions and promotes dependence

- **Citation:** Cheng et al. (2026), Science. [Publisher / archival record](https://doi.org/10.1126/science.aec8352).
- **Supported relevance:** Evaluates 11 AI models and runs three preregistered user experiments (N=2,405), finding that sycophantic responses influence users' judgments and stated willingness to repair interpersonal conflicts.
- **Do not infer:** Does not directly measure apologizing or factual-correction fidelity; evidence about longer-term psychological dependence must not be inferred from brief interactions.
- **Survey alignment:** Section 2; direct user-outcome evidence.
- **Duplicate-screening status:** Check against full Matrix; user-impact literature is in scope.

### Interaction Context Often Increases Sycophancy in LLMs

- **Citation:** Jain et al. (2026), CHI. [Publisher / archival record](https://doi.org/10.1145/3772318.3791915).
- **Supported relevance:** Examines how real prior interaction context can increase sycophantic mirroring compared with context-free responses.
- **Do not infer:** Addresses user-context effects and sycophancy, not apology language or training-stage causal attribution.
- **Survey alignment:** Sections 1, 2; multi-turn/context evidence.
- **Duplicate-screening status:** Check against full Matrix; overlap possible with multi-turn studies.

## Post-training and mitigation

### Training language models to be warm can reduce accuracy and increase sycophancy

- **Citation:** Ibrahim, Hafner, and Rocher (2026), Nature. [Publisher / archival record](https://doi.org/10.1038/s41586-026-10410-0).
- **Supported relevance:** Controlled supervised fine-tuning on warmer response styles increases errors and agreement with incorrect user beliefs across evaluated models and tasks.
- **Do not infer:** The controlled intervention is SFT for warmth, NOT an RLHF experiment and NOT a direct measurement of why an individual response apologizes.
- **Survey alignment:** Section 3; controlled training intervention.
- **Duplicate-screening status:** Check against full Matrix; likely relevant to post-training explanations.

### Self-Augmented Preference Alignment for Sycophancy Reduction in LLMs

- **Citation:** Chen, Huang, and Chen (2025), EMNLP. [Publisher / archival record](https://aclanthology.org/2025.emnlp-main.625/).
- **Supported relevance:** Introduces a sycophancy answer-assessment dataset and a self-augmented preference alignment intervention, reporting reduced sycophancy in its evaluations.
- **Do not infer:** A method paper about mitigating sycophancy; not evidence that apology wording is causally connected to answer repair.
- **Survey alignment:** Sections 3, 4; preference-alignment intervention.
- **Duplicate-screening status:** Check against full Matrix for equivalent preprint or published record.

### Simple synthetic data reduces sycophancy in large language models

- **Citation:** Wei et al. (2023), arXiv preprint (revised 2024). [Publisher / archival record](https://arxiv.org/abs/2308.03958).
- **Supported relevance:** Reports instruction-tuning and model-scaling associations with sycophancy and a synthetic-data fine-tuning intervention that reduces sycophantic responses on selected tasks.
- **Do not infer:** Cite as an arXiv preprint unless a verified venue version is located; do not assign it a conference venue based on its arXiv record.
- **Survey alignment:** Sections 1, 3, 4; training intervention.
- **Duplicate-screening status:** Check against full Matrix for title and preprint duplicates.

## Multimodal and multi-agent

### Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs

- **Citation:** Li et al. (2025), ICLR. [Publisher / archival record](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html).
- **Supported relevance:** Introduces MM-SY and studies misleading user inputs against visual evidence, including prompting, SFT, and DPO-based mitigation experiments.
- **Do not infer:** Mainly measures visual answer agreement/accuracy rather than apology text; attention observations are not a complete explanation of behavior.
- **Survey alignment:** Sections 1, 3, 4; VLM benchmark/interventions.
- **Duplicate-screening status:** PROBABLE OVERLAP: supplied Matrix summary explicitly mentions MM-SY.

### Too Polite to Disagree: Understanding Sycophancy Propagation in Multi-Agent Systems

- **Citation:** Kasprova et al. (2026), SIGDIAL. [Publisher / archival record](https://arxiv.org/abs/2604.02668).
- **Supported relevance:** Studies peer-sycophancy awareness in multi-agent discussions; reports improved final-answer accuracy when agents are given priors on peer sycophancy.
- **Do not infer:** Concerns multi-agent error propagation, not apologies between agents; do not infer human psychological effects from agent-level evaluation.
- **Survey alignment:** Sections 1, 3, 4; multi-agent experimental evidence.
- **Duplicate-screening status:** Check against full Matrix; multi-agent conformity is already included in its scope.

## Mechanism and adjacent surveys

### Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs

- **Citation:** Vennemeyer et al. (2026), EMNLP. [Publisher / archival record](https://aclanthology.org/2026.emnlp-main.2533/).
- **Supported relevance:** Uses activation interventions and representational analyses to distinguish sycophantic agreement, sycophantic praise, and genuine agreement.
- **Do not infer:** Provides intervention evidence about representations; does not directly identify the historical post-training reward that created them.
- **Survey alignment:** Section 3; mechanistic intervention evidence.
- **Duplicate-screening status:** Check against full Matrix; published Oct 2026 and may be absent from earlier search.

### Sycophancy in Language Models: A Survey Across Behaviors and Topologies

- **Citation:** Kasprova, He, Hakkani-Tür, and Kindratenko (2026), Preprint; authors report under review at ACM Computing Surveys. [Publisher / archival record](https://zenodo.org/records/21347167).
- **Supported relevance:** An existing survey covering 126 papers across single-turn, multi-turn, multi-agent, tool-use, and related settings, useful for establishing how this team's scope differs.
- **Do not infer:** Do NOT describe as accepted/published in ACM Computing Surveys. Relevant prior work for novelty positioning, not a new experimental result.
- **Survey alignment:** Related work / scope; competing survey.
- **Duplicate-screening status:** Check against full Survey-only landscape; this review may not appear in the 21-record summary.

## Before promoting to the main README

1. Obtain the complete **Matrix** and **survey-only review** tabs, not just their summary exports. Compare normalized DOI/arXiv ID, title and publication-version identity against every row. Do not count an arXiv and published version as two papers.
2. Assign the team's existing IDs (Mxx) for overlaps rather than introducing competing IDs, and verify any originally assigned citation/section.
3. Check each included paper's full methods and relevant tables before turning a one-sentence abstract summary into a strong survey claim. Label causal intervention, observational association, human-subject outcomes, and author inference separately.
4. Record direct apology measurement (yes/no), demonstrated factual answer correction (yes/no), and any actual model-internal intervention (yes/no) as separate fields.
5. Compare proposed novelty specifically against the Kasprova et al. sycophancy survey. Avoid suggesting that survey is already accepted by ACM CSUR.

*Prepared as an unmerged review artifact. No changes to existing papers, no synthetic results, and no claims of completed Google Sheets deduplication.*
