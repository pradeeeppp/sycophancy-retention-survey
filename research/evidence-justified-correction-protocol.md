# Evidence-Justified Correction: Survey Analysis Protocol (Draft)

This is a proposed methodological extension, **not** a completed systematic review or a new experimental result. It is designed to help the survey answer a more specific question than a broad taxonomy:

> What observations justify concluding that an AI model changed an answer for valid evidential reasons and communicated that change accurately?

## Three layers for coding each paper

1. **Manipulation:** Was factual evidence held constant while pressure changed? Was valid corrective evidence supplied? Were initial-answer correctness and source reliability independently labeled?
2. **Observation:** Did researchers measure answer correctness, answer revision, apology/acknowledgement, confidence, group consensus, or human reliance?
3. **Identification:** Which claim is **identified**, **partially identified**, or **not identified** by those observations and contrasts?

**Important:** A paper can be excellent for one research question while being unable to support another. Missing measurements are not zero effects.

## Four distinct proposed outcomes

Conditional on a validated prior answer and correction label:
- **U — Incorrect capitulation under an unsupported challenge:** how often a previously correct answer becomes incorrect after pressure.
- **R — Successful updating after valid correction:** how often a previously incorrect answer changes to the correct one after independently verified corrective evidence.
- **F — False error admission:** how often the model explicitly says its earlier correct answer was wrong.
- **T — Truthful error admission:** how often a model explicitly acknowledges a genuinely earlier error.

These are **distinct rates**, not one sycophancy score. U and R alone cannot establish causal reasons; causal attribution requires paired neutral/pressure and evidence-absent/present controls. F and T require precise coding of explicit epistemic statements, not warm tone or generic empathy. A revised answer can be correct for the wrong reason.

## Proposed minimal matched evaluation

1. Obtain an initial answer before presenting the challenge; independently assess whether it was correct.
2. Vary validated corrective evidence separately from conversational pressure, using matched wording and prompt lengths where possible.
3. Repeat baselines to account for model stochasticity.
4. Score final answer correctness, answer revision, explicit error admission, truthful change acknowledgement, and non-epistemic empathy separately.
5. Analyze language, vision-language, and multi-agent settings with separate evidence provenance and reliability labels rather than assuming all sources are equivalent.
6. In subjective cases without objective truth, code endorsement, support, integrity, and empathy without forcing binary correctness labels.

## High-value reviewer-facing deliverables

- A `study × claim × observation` matrix with observable identification limits.
- A transparent evidence extraction codebook with venue, model version, experimental unit, control arms, validity labels, and uncertainty estimates.
- A methods section identifying who coded and checked each paper and recording disagreements.
- A resistance-versus-receptiveness comparison **only for studies testing both arms**. No pooled quantitative claims without aligned denominators and measures.
- Transcript-level paired examples (if actually checked and licensed for reproduction).
- A structured limitations section distinguishing normative C1–C3 assumptions from testable behavioral proxies.

## Scientific safeguards

- A flip in the right direction does not prove the model used evidence.
- Source credibility may be legitimate evidence; do not label all authority cues as pressure.
- C2's exact Bayesian posterior is not observable in ordinary language-model experiments.
- C3's full truth and completeness condition is an idealized target; disclosure of an unknown error cannot be demanded without an error signal.
- Human preferences for apologies are not proof of correct error admission.
- Keep curated corpus counts separate from PRISMA flow counts until a reproducible search and screening actually occur.
- Validate all paper-level coding against the original papers before publication.

This guide is a proposed research workflow; no empirical claims about performance are introduced here.
