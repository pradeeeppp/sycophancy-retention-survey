# Selected Literature on AI Apologies, Sycophancy, and Factual Correction

## LLM behaviors and response to correction

**Sinha, D. (2026).** [SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants](https://aclanthology.org/2026.findings-acl.1759/). *Findings of the Association for Computational Linguistics: ACL 2026*, 35278–35284.

SycoBench-600 evaluates whether assistants resist misleading user pressure while accepting valid corrections. Its treatment of correction selectivity helps distinguish evidence-based answer revision from agreement with a user's assertion. This distinction is particularly relevant when an apology accompanies a changed answer.

## User experience and apology quality

**Ashktorab, Z., Buccella, A., D'Cruz, J., et al. (2026).** [Who's Sorry Now: User Preferences Among Rote, Empathic, and Explanatory Apologies from LLM Chatbots](https://doi.org/10.1145/3793679). *ACM Transactions on Computer-Human Interaction*, 33(3), Article 26.

A preregistered study with 162 participants compares rote, empathic, and explanatory apologies following bias, fabricated information, and factual errors. Explanatory apologies were generally preferred, although the pattern varied with the type of mistake. The study examines users' preferences for repair messages; it does not establish that apologizing makes a model more capable of detecting or correcting an error.

## Training-related explanations

**Ibrahim, L., Hafner, F. S., & Rocher, L. (2026).** [Training language models to be warm can reduce accuracy and increase sycophancy](https://doi.org/10.1038/s41586-026-10410-0). *Nature*, 652, 1159–1165.

Across five models, supervised fine-tuning for warmer responses increased factual errors and endorsement of incorrect user beliefs on the tasks evaluated. The results offer controlled evidence that a conversational quality commonly regarded as desirable can conflict with factual accuracy. The intervention was supervised fine-tuning, not an experiment that isolated the effects of RLHF.

## Forward-looking position and evaluation

**Kasneci, E., & Kasneci, G. (2026).** [Position: Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://proceedings.mlr.press/v306/kasneci26a.html). *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306, 170836–170855.

This position paper argues that tutoring systems should identify misconceptions and correct them supportively, even when students invoke authority or social pressure. It introduces the EduFrameTrap benchmark and proposes evaluating a tutor's ability to remain constructive without conceding incorrect claims. The proposed principle extends to other assistants that must balance social responsiveness with factual correction.
