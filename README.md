# Prebunking Scapegoating in Political Social Media

Supplementary materials and reproducibility resources for the manuscript **Prebunking Scapegoating in Political Social Media**.

This repository uses the revised manuscript terminology. Historical JASP analyses and earlier truth/misinformation framing are not treated as the current inferential analysis.

## Contents

- `experiment/`: original PsychoPy Builder source, stimuli, task assets, and questionnaire/counterbalancing files needed to document the administered experiment.
- `experiment/stimulus_construction/`: historical AI prompt and human coding rubric, preserved for provenance with an explicit interpretation warning.
- `docs/TERMINOLOGY.md`: mapping between historical internal labels and the manuscript-facing construct **perceived rhetorical bias**.
- `analysis/`: manuscript-consistent analysis documentation and the verified figure-reproduction layer.
- `analysis/figures/figure_reproduction_source.zip`: complete compact source bundle containing the six-figure R code, plotting tables, anonymous plotting distributions, verification files, and R session information.

Raw participant-level PsychoPy exports are intentionally excluded from this public repository.

The canonical inferential analyses were rebuilt in R 4.5.3 using crossed participant-by-item mixed-effects models and associated robustness checks. The figure bundle reproduces the manuscript figures from archived canonical outputs; it does **not** refit every inferential model. Only manuscript-consistent analysis artifacts should be used for inference.

### Peer-review note

This GitHub repository is author-linked and therefore is not an anonymous reviewer repository.