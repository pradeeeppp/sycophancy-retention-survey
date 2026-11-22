# Survey evidence and PRISMA audit — current authoritative navigation

The **primary paper reading guide is now [the evidence-led 34-candidate Markdown map](../literature/prisma-core-papers.md)**. This supersedes the older 31-row shortlist as a *curation view*, not as a completed systematic-review inclusion list.

The new [PRISMA 2020 compliance audit](../research/PRISMA-2020-audit.md), [PRISMA-S search provenance](../research/PRISMA-search-provenance.md), and [cross-paper synthesis](../research/evidence-synthesis.md) distinguish verifiable publisher metadata, observed search counts, and unmeasured full-text eligibility. **Do not report 34 as the number of PRISMA-included studies, and do not add 34 to the historical 69-paper general reading list.**

The previous manifest [core-conference-manifest.csv](core-conference-manifest.csv) and its PDF downloader are retained only for historical reproducibility; they still reflect the **previous 31-candidate selection** and do not include the additional NeurIPS/ICML papers. Downloading publisher PDFs does not grant redistribution rights.

---

# Evidence-led conference core (revised for cross-venue coverage)

**Survey:** Agreeing for the Right Reasons: A Survey of Sycophancy, Apology, and Acknowledgement in Language, Vision-Language, and Multi-Agent Models.

**Status: 31 publisher-confirmed, abstract-screened candidates; NOT 31 PRISMA-included papers.** Read the paper-by-paper [manifest](core-conference-manifest.csv). Evidence extraction and full-text screening are still required.

## Publisher and track coverage

| Publisher venue | Candidate papers | Track |
|---|---:|---|
| ICLR | 5 | Official conference |
| ICML | 8 | PMLR main proceedings |
| NeurIPS | 1 | **Archival Datasets and Benchmarks track**, NOT a workshop |
| CHI | 2 | ACM conference proceedings |
| ACL | 6 | Main long papers |
| EMNLP | 7 | Main conference |
| NAACL | 2 | Main long papers |
| **Total** | **31** | **16 outside ACL-family; 15 ACL-family** |

This distribution is a *result* of finding directly relevant work—not a venue quota. **Do not fill CVPR, ICCV or ECCV with unrelated vision papers.** The highly relevant ["To Agree or To Be Right?" (CVPR 2026)](https://openaccess.thecvf.com/content/CVPR2026W/Med-Reasoner/html/Aranya_To_Agree_or_To_Be_Right_The_Grounding-Sycophancy_Tradeoff_in_CVPRW_2026_paper.html) is a **workshop** paper and therefore excluded from this strict collection. A search of these vision venues must continue with recorded queries and exports.

## Must-read comparative synthesis

| Research claim to assess | Published studies | What the review can actually compare |
|---|---|---|
| RLHF and preference optimization can reward agreeableness instead of correctness | [ICLR 2024: Towards Understanding Sycophancy](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html); [ICML 2026: How RLHF Amplifies Sycophancy](https://proceedings.mlr.press/v306/shapira26a.html); [ICML 2026: Spurious Correlation Learning](https://proceedings.mlr.press/v306/moya26a.html) | Behavioral preference rankings, causal/formal mechanisms, training interventions; avoid treating theory as behavioral replication |
| Models should reject incorrect user premises but accept valid revisions | [ICML 2026: BrokenMath](https://proceedings.mlr.press/v306/petrov26a.html); [NAACL 2025: Teaching Models to Balance Resisting and Accepting Persuasion](https://aclanthology.org/2025.naacl-long.412/); [ACL 2024: Ask Again, Then Fail](https://aclanthology.org/2024.acl-long.577/) | False-premise acceptance, resistance and correction selectivity; distinguish wrong-to-right from right-to-wrong |
| A model's apology, acknowledgement and factual stance are different things | [EMNLP 2026: Epistemic Authority](https://aclanthology.org/2026.emnlp-main.1595/); [ACL 2022: SaFeRDialogues](https://aclanthology.org/2022.acl-long.447/); [NAACL 2024: Grounding Gaps](https://aclanthology.org/2024.naacl-long.348/); [ACL 2026: Multi-Turn Repair](https://aclanthology.org/2026.acl-long.651/) | Apology occurrence and appropriateness, feedback grounding, claim retention and repair success |
| Vision-grounded models may defer to textual suggestions over image/video evidence | [ICLR 2025: Have the VLMs Lost Confidence?](https://proceedings.iclr.cc/paper_files/paper/2025/hash/07be1a0850e58ca29e2b6ce31fc0c791-Abstract-Conference.html); [EMNLP 2025: Pointing to a Llama](https://aclanthology.org/2025.emnlp-main.1020/); [ACL 2026: Flattery in Motion](https://aclanthology.org/2026.acl-long.369/) | Image/video correctness before hint, visual grounding and post-pressure reversal |
| Multi-agent consensus can reflect peer pressure rather than argument strength | [ICLR 2025: Do as We Do](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1da9ca7e9cef4b1af63913f05d1630a4-Abstract-Conference.html); [ICML 2026: A Diagnostic Study of Multi-Agent LLMs](https://proceedings.mlr.press/v306/pitre26a.html); [ACL 2025: Conformity in LLMs](https://aclanthology.org/2025.acl-long.195/); [EMNLP 2026: Consistency Illusion](https://aclanthology.org/2026.emnlp-main.1780/) | Majority size, identity, independence, rationale divergence, debate-process metrics |
| Sycophancy affects actual users, not only benchmark metrics | [CHI 2026: Invisible Saboteurs](https://doi.org/10.1145/3772318.3791365); [CHI 2026: Interaction Context Often Increases Sycophancy](https://doi.org/10.1145/3772318.3791915) | Novice problem-solving and inappropriate reliance; agreement with and without user memory/context |
| Dynamic reasoning interventions need to retain legitimate updating | [ICML 2026: Real-Time Monitoring of Chain-of-Thought Sycophancy](https://proceedings.mlr.press/v306/hu26bb.html); [ICLR 2025: Causally Motivated Sycophancy Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a52b0d191b619477cc798d544f4f0e4b-Abstract-Conference.html) | Inference-time monitor versus head-level intervention; report capability tradeoffs when assessed |

## What changed and what remains incomplete

The previous catalog counted **25/31 papers from ACL-family venues**. This revision is **15/31 ACL-family** and **16/31 from ICLR, ICML, NeurIPS and CHI**. It removes loosely selected papers from this *priority core* without deleting them from the existing general reading list. The publisher and paper type for the NeurIPS entry are explicit.

**No fabricated PRISMA counts:** this is a reproducible *candidate shortlist* built from prior repository work and targeted publisher searches, not a full title/abstract export or duplicate-controlled cross-database study. See the [search limitations and decisions](../research/cross-venue-discovery-log.md), [screening protocol](../research/main-conference-prisma-protocol.md), and [empty full-text extraction form](../research/full-text-screening-template.csv).

**PDF policy:** The manifest contains publisher-linked PDF URLs where identifiable; ACM CHI publisher landing/DOI links are given without inventing direct PDF URLs. The PDFs are **not committed** to this public repository, and a paper being online does not itself confer redistribution rights. Use [the local-only PDF helper](fetch_official_pdfs.py), and check individual licenses before sharing binaries.
