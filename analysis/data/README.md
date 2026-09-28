# Public core analysis data

The five `analysis_core_public_part*.csv` files together contain 4,104 trial-level observations from the locked N = 171 analytic sample.

They were derived from the canonical locked analysis dataset after:
- replacing the original participant identifier with a release identifier;
- removing age, sex, height, education, national identity, political-future preference, self-reported political spectrum, vote preference, and reconstructed political-orientation variables;
- retaining only variables needed for the non-political core analyses and diagnostic checks.

Use `RECOMBINE_PUBLIC_DATA.R` to recreate a single `analysis_core_public.csv`.

Legacy internal labels such as `information_type` values “True Information” / “Misinformation” are retained for exact provenance. They should not be interpreted as the current manuscript construct definition. See `../../docs/TERMINOLOGY.md`.

The canonical manuscript-facing outcome is **perceived rhetorical bias**.
