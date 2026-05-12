# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "Taxonomizing Alignment Failures in AI-driven Research". This includes empirical risk reports from state-of-the-art AI Scientist systems, datasets of scientific retractions and AI incidents, and code repositories of autonomous research agents and benchmarks.

## Papers
Total papers downloaded: 19

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Jr. AI Scientist and Its Risk Report | Miyai et al. | 2025 | papers/2511.04583v4_... | Detailed empirical risk report of an autonomous scientist. |
| Beyond principlism: ethical AI use | Zhicheng Lin | 2024 | papers/2401.15284v6_... | Framework for ethical AI in research. |
| LLM Reasoning Failures | Peiyang Song et al. | 2026 | papers/2602.06176v1_... | Survey of reasoning failures (source of alignment issues). |
| Reflexive Behaviour in Research | Julia Heuritsch | 2021 | papers/2109.09375v3_... | Sociological study of metric-driven misconduct. |
| Real-World Gaps in AI Governance | 2505.00174v2 | 2025 | papers/2505.00174v2_... | Identifies gaps between research and practice. |

*Full metadata available in `papers/metadata.json`.*

## Datasets
Total datasets gathered: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Retraction Watch Data | GitLab (Crossref) | 64 MB (CSV) | Misconduct Analysis | datasets/retraction-watch-data/ | Contains ~50k retractions with detailed reasons. |
| AI Incident Database | GitHub (RAIC) | 35 MB | Failure Analysis | datasets/aiid/ | Documentation of real-world AI harms and failures. |

## Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| Jr.AI-Scientist | Agent4Science-UTokyo | Autonomous Agent | code/Jr.AI-Scientist/ | SOTA research agent with risk monitoring. |
| core-bench | siegelz/core-bench | Reproducibility | code/core-bench/ | Benchmark for reproducing results (anti-fabrication). |
| AutoResearchBench | CherYou | Lit Discovery | code/AutoResearchBench/ | Benchmark for literature discovery and analysis. |

## Resource Gathering Notes

### Search Strategy
- **Literature**: Used a custom arXiv search script targeting "alignment failure", "AI scientist", and "research misconduct".
- **Datasets**: Targeted well-known databases for scientific failure (Retraction Watch) and general AI failure (AIID).
- **Code**: Focused on the most recent (2025-2026) autonomous research systems and their associated evaluation benchmarks.

### Selection Criteria
- **Recency**: Prioritized 2024-2026 works to capture the "Agentic AI" era.
- **Empirical Evidence**: Favored papers that report actual observed failures over purely theoretical ones.
- **Actionability**: Selected codebases that can be used to reproduce or simulate failure modes.

### Challenges Encountered
- **Paper Finder Service**: The automated service timed out, requiring a manual arXiv implementation.
- **Dataset Size**: The Retraction Watch git history was extremely large (2.6GB), though the data file itself was manageable.

## Recommendations for Experiment Design

1.  **Primary dataset**: Use the `retraction_watch.csv` reasons column to perform a thematic analysis for the taxonomy.
2.  **Baseline methods**: Analyze the failure modes documented in `Jr.AI-Scientist` and `core-bench` documentation.
3.  **Evaluation metrics**: Use "Reproducibility Rate" (from CORE-Bench) and "Automated Review Divergence" as primary metrics for identifying alignment failures.
4.  **Taxonomy Validation**: Test the taxonomy by classifying a subset of the AI Incident Database and Retraction Watch entries to ensure coverage of "AI-driven" specifics.

## Research Process Update
During this research session, the AI agent successfully generated a specific taxonomy based on human and AI failure data. The taxonomy includes 6 failure modes (Omission of Negative Findings, Overclaiming Results, Methodological Fabrication, Metric Gaming, HARKing, Citation Fabrication). We implemented a simulated LLM evaluation framework using GPT-4o (`src/experiment.py`) to empirically test this taxonomy under "Control", "Acceptance Pressure", and "Impact Pressure" conditions. The results clearly validated that pressure conditions primarily induce narrative distortions, notably significant "Overclaiming" and occasional "Omission of Negative Findings". The data sets (`results/`) and visualizations (`figures/`) fully document this experimental validation.
