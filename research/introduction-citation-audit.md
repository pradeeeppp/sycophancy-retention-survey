# Introduction citation and publication-type audit

**Checked 21 November 2026.** Scope: the introduction excerpt supplied for *Agreeing for the Right Reasons*. This is a bibliographic integrity check; the repository does not contain the author's full LaTeX manuscript or .bib file, so no manuscript citation key has been edited. **Do not treat a preprint as an accepted conference paper.**

| Introduction citation or claim | Verifiable publication | Required correction or clarification |
|---|---|---|
| Foundational sycophancy vs truthfulness | [Sharma et al., *Towards Understanding Sycophancy in Language Models*, **ICLR 2024**](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) | Published ICLR; directly anchors preference-induced agreement |
| **Hong et al. [2025]** on sustained multi-turn pressure | [Hong et al., *Measuring Sycophancy of Language Models in Multi-turn Dialogues*, **Findings of EMNLP 2025**](https://aclanthology.org/2025.findings-emnlp.121/) | This is peer-reviewed *published Findings*, **not** EMNLP main; retain as explicitly labeled contextual citation if strict-main conference policy is adopted. It is not a preprint |
| **Li et al. [2025]** on VLM sycophancy | [Li et al., *Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs*, **ICLR 2025**](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html) | Publication and authors match Li; cite directly for VLM sycophancy |
| **Pi et al. [2025]** on visual correction trade-offs | [Pi et al., *Pointing to a Llama and Call it a Camel*, **EMNLP 2025 main**](https://aclanthology.org/2025.emnlp-main.1020/) | Publication confirmed; distinguish visual misleading hints from correct visual feedback |
| **Kasprova et al. [2026b]** on multi-agent propagation | [Kasprova et al., *Too Polite to Disagree*, **SIGDIAL 2026 conference proceedings**](https://aclanthology.org/2026.sigdial-1.56/) | Published specialist-conference work, **not a preprint-only item**. Outside the stated ICLR/ICML/NeurIPS/ACL-family main-track filter; either label as supporting specialist-conference evidence or define the policy to include SIGDIAL |
| **Pitre et al. [2025]** on multi-agent diagnostic debate | [Pitre et al., *A Diagnostic Study of Multi-Agent LLMs for Real-World Debates*, **ICML 2026**](https://proceedings.mlr.press/v306/pitre26a.html) | **Change publisher-version year to 2026.** Do not cite the preliminary 2025 version as if it were the final ICML publication |
| **Harland [2025]** on AI-apology literature | [Harland et al., *AI apology: a critical review of apology in AI systems*, **Artificial Intelligence Review (2025)**](https://doi.org/10.1007/s10462-025-11305-8) | Peer-reviewed journal review; supports background and theoretical framing, **not** the primary empirical conference-only inclusion set |
| **Alnasser et al. [2026a]** on validation, apology and claim retention | [Alnasser et al., *How AI Models Manage Epistemic Authority*, **EMNLP 2026 main**](https://aclanthology.org/2026.emnlp-main.1595/) | Published main conference; directly relevant. Check whether suffix "a" is correct for the complete final bibliography |
| **Kasprova et al. [2026a]** referenced as an existing sycophancy survey | [*Sycophancy in Language Models: A Survey Across Behaviors and Topologies*](https://virakasprova.github.io/publication/2026-07-14-sycophancy-survey) | Author page currently describes **an ACM Computing Surveys preprint under review**. **Do not label it peer reviewed or include in strict published evidence.** Replace as evidence with published primary studies, or cite it only if a separate clearly labeled non-peer-reviewed related-work section is permitted |

## Citation selection implications

1. **Publication quality is not binary preprint/non-preprint:** ACL *Findings* and SIGDIAL proceedings are published peer-reviewed records, though they do not meet the user's strict *major-main-track-only* rule. Harland 2025 is a peer-reviewed **journal review**. The Kasprova survey is described as **under review**, which is the disallowed status. These must not be conflated.
2. **Do not modify the manuscript's citation keys automatically** without seeing its bibliography: changing the citation year, suffix "a"/"b", or listed paper may break references if multiple same-author entries are present.
3. **Fix Pitre year** to the accepted final 2026 conference version. This is a concrete citation discrepancy already visible in the provided excerpt.
4. **Use the introduction as an outcome taxonomy, not a search restriction.** Search terms like "debate" and "repair" are needed because papers can test the right behavior without the word "sycophancy."

## One-sentence, source-grounded replacement for the questionable Kasprova survey assertion

> Prior work has characterized social sycophancy in controlled conversational scenarios and the tendency of groups of language-model agents to converge to majority positions despite shared misconceptions (Cheng et al., ICLR 2026; Estornell and Liu, NeurIPS 2024).

The replacement uses **published main-conference empirical or theoretical papers**. It does not assert there is an already peer-reviewed comprehensive sycophancy survey when the named work is under review.

**Not an automatic manuscript edit:** The full manuscript and bibliographic database are not present among this repository's files. This audit supplies precise reference corrections without fabricating unseen LaTeX text or creating mismatched citation keys.
