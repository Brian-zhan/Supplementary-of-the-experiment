# Prebunking Scapegoating in Political Social Media

Supplementary materials and reproducibility resources for the manuscript **Prebunking Scapegoating in Political Social Media**.

This repository uses the revised manuscript terminology. Historical internal variable names are retained where needed for exact provenance, but reader-facing documentation uses **perceived rhetorical bias**.

## Repository contents

- `experiment/` — original PsychoPy Builder source, 24 experimental stimuli, practice materials, task assets, counterbalancing files, and questionnaires.
- `experiment/stimulus_construction/` — the historical AI prompt and human coding rubric, retained for provenance with an explicit interpretation warning.
- `docs/TERMINOLOGY.md` — mapping between historical internal labels and the manuscript-facing construct **perceived rhetorical bias**.
- `analysis/data/` — sanitized trial-level public core data for the locked N = 171 sample (4,104 observations), split into five CSV parts plus a recombination script.
- `analysis/reproducibility/` — the complete canonical R 4.5.3 inferential-code archive stored as 16 base64 parts, with a one-command rebuild script and SHA-256 verification.
- `analysis/figures/` — verified figure-reproduction source tables, R preparation code, validation records, and the compact figure-source archive.

## Rebuild the canonical R code archive

From the repository root:

```bash
python analysis/reproducibility/REBUILD_CODE_ARCHIVE.py
```

Expected reconstructed archive:

- `Prebunking_Scapegoating_R453_Inferential_Code_COMPLETE.zip`
- 112,625 bytes
- SHA-256: `81d505d2acf6efb5ca2483d433f12291314d0ad218c3ab00744bf1ef54675312`

The archive contains the baseline and follow-up R engines, S00–S15 scripts, `RUN_CANONICAL_ALL.R`, `RUN_COMPLETE_R453.R`, environment restoration files, `renv.lock`, and verification code.

## Public data

The five `analysis_core_public_part*.csv` files contain exactly 4,104 trial-level rows from the locked sample. Run:

```r
source("analysis/data/RECOMBINE_PUBLIC_DATA.R")
```

to create a single `analysis_core_public.csv`.

The public data intentionally exclude unnecessary demographic and political quasi-identifiers. They support reproduction of the non-political core analyses and diagnostic checks. Participant-level political-congruence analyses require the controlled locked dataset because party-preference information is treated as sensitive; manuscript-consistent aggregate political results are retained in the public source tables.

## Data and privacy

Raw PsychoPy participant exports, direct researcher contact details, JASP files, and unnecessary participant-level demographic/political fields are intentionally excluded from this public repository.

## Peer-review note

This repository is author-linked and therefore is not itself an anonymous reviewer repository.
