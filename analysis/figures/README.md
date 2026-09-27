# Six-figure reproduction

These files reproduce the six manuscript figures from archived canonical result tables and de-identified plotting distributions.

Figure numbering matches the later manuscript draft:

1. Prebunk × scapegoating / perceived rhetorical bias
2. Reaction profile / attitude
3. Political congruence
4. Signed cross-outcome coefficients
5. Rank-based differentiation (AUC)
6. Exploratory response-time patterns

Run:

```sh
Rscript rcode/make_figures.R
```

Required packages: `ggplot2`, `patchwork`, and `ragg`.

The script renders reader-facing labels using **rhetorical bias** terminology. It does not refit the statistical models.