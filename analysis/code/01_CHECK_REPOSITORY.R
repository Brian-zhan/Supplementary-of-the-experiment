find_root <- function() {
  candidates <- character()
  for (frame in sys.frames()) {
    if (!is.null(frame$ofile) && nzchar(frame$ofile)) candidates <- c(candidates, dirname(normalizePath(frame$ofile)))
  }
  args <- commandArgs(trailingOnly = FALSE)
  hit <- grep("^--file=", args, value = TRUE)
  if (length(hit)) candidates <- c(candidates, dirname(normalizePath(sub("^--file=", "", hit[[1L]]))))
  if (requireNamespace("rstudioapi", quietly = TRUE) && rstudioapi::isAvailable()) {
    path <- rstudioapi::getSourceEditorContext()$path
    if (nzchar(path)) candidates <- c(candidates, dirname(normalizePath(path)))
  }
  candidates <- c(candidates, normalizePath(getwd()))
  for (candidate in unique(candidates)) {
    current <- candidate
    for (i in seq_len(8L)) {
      if (file.exists(file.path(current, "OldStudy_Public.Rproj"))) return(current)
      parent <- dirname(current)
      if (identical(parent, current)) break
      current <- parent
    }
  }
  stop("Repository root not found. Open OldStudy_Public.Rproj and Source this file again.")
}

root <- find_root()
setwd(root)

required <- c(
  "engine/baseline/rcode/00_run_all.R",
  "engine/followup/rcode/00_run_all.R",
  "renv.lock",
  "FIGURE_TABLE_CODE_MAP.csv",
  "MANUSCRIPT_CLAIM_SOURCE_MAP.csv"
)
missing <- required[!file.exists(required)]
if (length(missing)) stop("Repository files missing: ", paste(missing, collapse = ", "))
if (as.character(getRversion()) != "4.5.3") stop("Expected R 4.5.3; observed ", getRversion())

if (!requireNamespace("jsonlite", quietly = TRUE)) stop("Run 00_BOOTSTRAP_RENV.R first (jsonlite missing).")
lock <- jsonlite::fromJSON("renv.lock", simplifyVector = FALSE)
expected <- vapply(lock$Packages, function(x) x$Version, character(1))
observed <- vapply(names(expected), function(pkg) {
  if (!requireNamespace(pkg, quietly = TRUE)) return(NA_character_)
  as.character(utils::packageVersion(pkg))
}, character(1))
bad <- names(expected)[is.na(observed) | observed != expected]
if (length(bad)) stop("Package mismatch: ", paste(sprintf("%s expected %s observed %s", bad, expected[bad], observed[bad]), collapse = "; "))

private_files <- c(
  "engine/baseline/data/analysis_long_clean_locked.csv",
  "engine/baseline/data/analysis_long_all198_minimal.csv",
  "engine/baseline/data/item_scapegoating_score_mapping.csv",
  "engine/baseline/data/participant_flow_audit.csv",
  "engine/followup/data/analysis_long_clean_locked.csv",
  "engine/followup/data/analysis_long_all198_minimal.csv",
  "engine/followup/data/item_scapegoating_score_mapping.csv",
  "engine/followup/data/participant_flow_audit.csv"
)
if (all(file.exists(private_files))) {
  cat("CHECK OK: code, exact R/package environment, and controlled core files are present.\n")
  cat("Next: source('02_RUN_AUTHORIZED_CORE_REFIT.R').\n")
} else {
  cat("CHECK OK: public code structure and exact R/package environment are present.\n")
  cat("Controlled participant data are intentionally absent. See data/README.md.\n")
}
