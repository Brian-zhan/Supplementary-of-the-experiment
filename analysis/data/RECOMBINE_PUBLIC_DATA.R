# Recombine the five public analysis-data parts.
# Each part contains the same header; this script keeps the first header only.
files <- sprintf("analysis/data/analysis_core_public_part%02d.csv", 1:5)
parts <- lapply(files, read.csv, stringsAsFactors = FALSE, check.names = FALSE)
dat <- do.call(rbind, parts)
stopifnot(nrow(dat) == 4104L)
write.csv(dat, "analysis/data/analysis_core_public.csv", row.names = FALSE, na = "")
message("Wrote analysis/data/analysis_core_public.csv with ", nrow(dat), " rows.")
