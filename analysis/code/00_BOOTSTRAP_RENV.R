options(repos = c(CRAN = "https://cloud.r-project.org"))

find_root <- function() {
  candidates <- character()
  frames <- sys.frames()
  for (frame in frames) {
    if (!is.null(frame$ofile) && nzchar(frame$ofile)) candidates <- c(candidates, dirname(normalizePath(frame$ofile)))
  }
  args <- commandArgs(trailingOnly = FALSE)
  hit <- grep("^--file=", args, value = TRUE)
  if (length(hit)) candidates <- c(candidates, dirname(normalizePath(sub("^--file=", "", hit[[1L]]))))
  if (requireNamespace("rstudioapi", quietly = TRUE) && rstudioapi::isAvailable()) {
    p <- rstudioapi::getSourceEditorContext()$path
    if (nzchar(p)) candidates <- c(candidates, dirname(normalizePath(p)))
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
if (as.character(getRversion()) != "4.5.3") {
  stop("This repository is frozen for R 4.5.3; observed R ", getRversion())
}
if (!requireNamespace("renv", quietly = TRUE) || as.character(packageVersion("renv")) != "1.2.4") {
  install.packages("https://cran.r-project.org/src/contrib/Archive/renv/renv_1.2.4.tar.gz",
                   repos = NULL, type = "source")
}
renv::restore(project = root, prompt = FALSE)
renv::load(project = root)
cat("Environment restored. Next: source('01_CHECK_REPOSITORY.R').\n")
