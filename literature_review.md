# Literature Review: Taxonomizing Alignment Failures in AI-driven Research

## Research Area Overview
The emergence of "AI Scientist" systems—autonomous agents capable of end-to-end scientific research—presents a transformative paradigm for scientific discovery. However, this automation introduces novel alignment failures where AI systems may prioritize intermediate metrics (like review scores or p-values) over genuine scientific truth. Current literature is beginning to document these failures, moving from hypothetical risks to empirical observations of autonomous systems.

## Key Papers

### Paper 1: Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper
- **Authors**: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari, Zaiying Zhao, Kiyoharu Aizawa
- **Year**: 2025 (arXiv:2511.04583v4)
- **Source**: arXiv / Transactions on Machine Learning Research
- **Key Contribution**: Develops a state-of-the-art autonomous research agent that mimics a novice researcher by building on baseline papers. Crucially, it provides a comprehensive "Risk Report" based on empirical observations.
- **Methodology**: Uses a three-stage workflow (Idea Generation, Experimentation, Paper Write-Up) leveraging coding agents like Claude Code.
- **Datasets Used**: NeurIPS, IJCV, and ICLR baseline papers and their associated codebases.
- **Results**: Achieves higher review scores than fully automated systems but identifies significant risks in autonomous operation.
- **Code Available**: Yes, [github.com/Agent4Science-UTokyo/Jr.AI-Scientist](https://github.com/Agent4Science-UTokyo/Jr.AI-Scientist)
- **Relevance**: Directly addresses empirical risks and failure modes in automated science.

### Paper 2: Beyond principlism: Practical strategies for ethical AI use in research practices
- **Authors**: Zhicheng Lin
- **Year**: 2024
- **Source**: arXiv:2401.15284
- **Key Contribution**: Proposes a user-centered, realism-inspired approach to AI ethics in research, moving beyond abstract principles to actionable strategies.
- **Methodology**: Qualitative analysis of AI adoption in science and proposal of five specific ethical goals.
- **Datasets Used**: N/A (Theoretical/Perspective)
- **Results**: Identifies the "Triple-Too" problem (too many initiatives, too abstract, too much focus on risk over utility).
- **Relevance**: Provides a framework for "what alignment looks like" in a research context.

### Paper 3: Large Language Model Reasoning Failures
- **Authors**: Peiyang Song, Pengrui Han, Noah Goodman
- **Year**: 2026
- **Source**: arXiv:2602.06176
- **Key Contribution**: A comprehensive survey of reasoning failures in LLMs, categorizing them into fundamental, application-specific, and robustness issues.
- **Relevance**: Explains the underlying cognitive failures that manifest as alignment failures in research agents.

### Paper 4: Reflexive Behaviour: How publication pressure affects research quality in Astronomy
- **Authors**: Julia Heuritsch
- **Year**: 2021
- **Source**: arXiv:2109.09375
- **Key Contribution**: Quantifies how publication pressure and metric-driven culture lead to scientific misconduct and questionable research practices.
- **Relevance**: Provides a sociological baseline for "human alignment failures" in research, which AI agents are likely to emulate or exacerbate.

## Common Methodologies
- **Autonomous Agent Scaffolding**: Using LLMs to chain research tasks (literature review -> hypothesis -> code -> paper).
- **LLM-as-a-Judge**: Using separate LLMs to review and score generated research (e.g., DeepReviewer).
- **Empirical Risk Reporting**: Documenting failure modes observed during the development of autonomous systems.

## Standard Baselines
- **AI Scientist v1 (Lu et al., 2024)**: The first major end-to-end automated research system.
- **Human-led Research**: Traditional peer-reviewed literature as the gold standard.

## Evaluation Metrics
- **Review Scores**: Scores from automated or human reviewers.
- **Reproducibility**: Ability of other agents or humans to run the generated code and get the same results.
- **Novelty & Utility**: Qualitative assessment of the scientific contribution.

## Datasets in the Literature
- **Retraction Watch Database**: Catalog of failed research due to misconduct or error.
- **AI Incident Database**: Documentation of real-world AI failures.
- **CORE-Bench**: Benchmark for computational reproducibility.

## Gaps and Opportunities
- **Intentional Sabotage**: While "hallucinations" are documented, intentional subversion of scientific constraints by agents (to achieve a goal) is under-explored.
- **Taxonomy of Scientific Alignment**: A unified classification of failure modes specific to the *scientific process* (vs. general AI safety) is missing.

## Recommendations for Our Experiment
- **Focus on the Retraction Watch taxonomy**: Use the "Reasons for Retraction" to seed the taxonomy of AI failures.
- **Utilize Jr. AI Scientist's Risk Report**: Map their empirical risks to our theoretical categories.
- **Benchmark against CORE-Bench**: Use reproducibility as a proxy for alignment (unaligned agents may fabricate results that are non-reproducible).
