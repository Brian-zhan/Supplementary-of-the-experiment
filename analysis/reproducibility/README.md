# Canonical R 4.5.3 inferential code

This directory stores the complete canonical R 4.5.3 inferential-code archive in 16 base64 text parts because the connected GitHub interface cannot reliably transmit the binary ZIP directly.

## Rebuild the code archive

From the repository root:

```bash
python analysis/reproducibility/REBUILD_CODE_ARCHIVE.py
```

The script concatenates `code_parts/code_part01.b64` through `code_part16.b64`, decodes them, and verifies the reconstructed ZIP.

Expected output:

- filename: `Prebunking_Scapegoating_R453_Inferential_Code_COMPLETE.zip`
- byte size: **112,625**
- SHA-256: `81d505d2acf6efb5ca2483d433f12291314d0ad218c3ab00744bf1ef54675312`

The reconstructed archive contains 50 files, including:

- baseline engine R scripts;
- follow-up engine R scripts;
- S00–S15 story scripts;
- `RUN_CANONICAL_ALL.R`;
- `RUN_COMPLETE_R453.R`;
- `00_RESTORE_ENVIRONMENT.R`;
- `R453_ENVIRONMENT_SPEC.R`;
- `R453_COMPARE_RESULTS.R`;
- `VERIFY_CANONICAL_RESULTS.R`;
- `renv.lock` and renv bootstrap files;
- RStudio project files; and
- the R 4.5.3 numerical-comparison summary.

The public trial-level dataset is stored separately under `../data/` with demographic and political quasi-identifiers removed. Historical internal variable labels are retained for provenance; reader-facing terminology follows `../../docs/TERMINOLOGY.md`.
