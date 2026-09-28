# Analysis and reproducibility

The inferential analyses were rebuilt in **R 4.5.3** using crossed participant-by-item mixed-effects models and associated robustness checks.

## Canonical code

The complete canonical code archive is stored under `reproducibility/code_parts/` as 16 base64 text parts because the connected GitHub interface could not reliably transmit the binary ZIP directly.

Run:

```bash
python analysis/reproducibility/REBUILD_CODE_ARCHIVE.py
```

The rebuild script verifies both the expected byte size (112,625) and SHA-256 hash before accepting the reconstructed archive.

The archive contains 50 files, including:
- baseline analysis engine;
- follow-up analysis engine;
- S00–S15 story scripts;
- `RUN_CANONICAL_ALL.R`;
- `RUN_COMPLETE_R453.R`;
- `00_RESTORE_ENVIRONMENT.R`;
- `R453_ENVIRONMENT_SPEC.R`;
- `R453_COMPARE_RESULTS.R`;
- `VERIFY_CANONICAL_RESULTS.R`;
- `renv.lock` and renv bootstrap files.

## Public core data

`data/` contains five sanitized CSV parts totaling exactly **4,104 observations** from **171 participants** (89 prebunk, 82 control; 24 trials each).

The release removes demographic and political quasi-identifiers that are unnecessary for the public core analyses. Participant-level political congruence requires controlled data; aggregate manuscript-consistent political estimates are provided in the public source tables.

## Figure reproduction

`figures/` contains the verified manuscript-figure layer. The figure code reads archived canonical outputs; it does not substitute for the inferential code archive above.

Historical internal names such as `discrimination`, `misleadingness`, or legacy information-type labels may appear inside frozen code/data objects. Reader-facing interpretation follows `../docs/TERMINOLOGY.md`: the focal outcome is **perceived rhetorical bias**, not objective truth accuracy.
