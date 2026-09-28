options(stringsAsFactors = FALSE, width = 160)

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

if (as.character(getRversion()) != "4.5.3") stop("Expected R 4.5.3; observed ", getRversion())
if (!requireNamespace("digest", quietly = TRUE)) stop("Run 00_BOOTSTRAP_RENV.R first (digest missing).")

expected_hash <- c(
  analysis_long_clean_locked.csv = "fd3692d5f533a799bc2cad25ac017137ce4e9487e732e8c6f68c4d404eb8238b",
  analysis_long_all198_minimal.csv = "98158ad321d1eb6c44737ba564682c4ab8dc54c80fcbd13ed526c859120507ec",
  item_scapegoating_score_mapping.csv = "bf4bc6dc7ea64b9b8a5f35875a3450fcd75ed35e1442bf85d8b4bfcadd115596",
  participant_flow_audit.csv = "3ad87d39e7d427fb401d782a81ae1990ed605f924dee4f2a4dacffe435cbdb2b"
)
engines <- normalizePath(c("engine/baseline", "engine/followup"), mustWork = TRUE)
for (engine in engines) {
  paths <- file.path(engine, "data", names(expected_hash))
  if (!all(file.exists(paths))) stop("Controlled files missing under ", engine)
  observed <- vapply(paths, digest::digest, character(1), algo = "sha256", file = TRUE)
  bad <- names(expected_hash)[observed != unname(expected_hash)]
  if (length(bad)) stop("Controlled data hash mismatch under ", engine, ": ", paste(bad, collapse = ", "))
}
dir.create("verification", showWarnings = FALSE)
for (engine in engines) {
  generated <- file.path(engine, c("tables", "figures", "logs"))
  for (path in generated) {
    if (dir.exists(path)) unlink(path, recursive = TRUE, force = TRUE)
    dir.create(path, recursive = TRUE, showWarnings = FALSE)
  }
  entry <- file.path(engine, "rcode", "00_run_all.R")
  log <- file.path("verification", paste0("AUTHORIZED_", toupper(basename(engine)), "_REFIT.log"))
  env <- c(paste0("ANALYSIS_ROOT=", engine), paste0("R_LIBS_USER=", paste(.libPaths(), collapse = .Platform$path.sep)))
  status <- system2(file.path(R.home("bin"), "Rscript"), shQuote(entry), stdout = log, stderr = log, env = env)
  if (!identical(status, 0L)) stop("Engine failed: ", engine, ". See ", log)
}
cat("Authorized core refit complete.\n")
