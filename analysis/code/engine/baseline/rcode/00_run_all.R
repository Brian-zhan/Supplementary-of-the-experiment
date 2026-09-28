options(stringsAsFactors = FALSE, width = 140, contrasts = c("contr.sum", "contr.poly"))
analysis_root <- Sys.getenv("ANALYSIS_ROOT", unset = "/project")
rcode_dir <- file.path(analysis_root, "rcode")
dir.create(file.path(analysis_root, "tables"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path(analysis_root, "figures"), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path(analysis_root, "logs"), recursive = TRUE, showWarnings = FALSE)

scripts <- c("01_data_audit.R","02_primary_mixed_models.R","03_randomization_and_auc.R",
"04_robustness_and_sensitivity.R","05_secondary_exploratory.R","07_verify_and_finalize.R","06_figures.R")
if (identical(Sys.getenv("SKIP_FIGURES"), "1")) scripts <- scripts[scripts != "06_figures.R"]

for (script in scripts) {
  cat(sprintf("START %s\n", script)); flush.console()
  started <- proc.time()[[3]]
  source(file.path(rcode_dir, script), local = globalenv(), echo = FALSE)
  cat(sprintf("DONE %s (%.1f seconds)\n", script, proc.time()[[3]] - started)); flush.console()
}
writeLines(capture.output(sessionInfo()), file.path(analysis_root, "logs", "session_info.txt"))
cat("All formal reanalysis modules completed.\n")
