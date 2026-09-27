# Analysis and figure reproducibility

The manuscript inferential analyses were rebuilt in R 4.5.3 using crossed participant-by-item mixed-effects models and associated robustness checks.

This repository currently contains the verified **figure-reproduction layer** from that pipeline. It is important to distinguish this from the full canonical inferential pipeline:

- `figures/rcode/prepare_plot_data.R` maps archived canonical R 4.5.3 outputs into de-identified plotting tables.
- `figures/rcode/make_figures.R` renders the six manuscript figures from those plotting tables.
- The figure script **does not refit the inferential models**.
- Historical internal keys such as `discrimination` or display strings containing “misleadingness” are retained where needed for provenance; the rendering code applies the manuscript-facing term **perceived rhetorical bias**.

Verified reference facts for the locked analysis are N = 171, 24 items, and 4,104 participant-item observations (82 control; 89 prebunk).

A full public inferential-analysis release should only be added from the canonical R 4.5.3 source package, not reconstructed from superseded JASP analyses.