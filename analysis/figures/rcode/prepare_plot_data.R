# Optional provenance step: rebuild the included plotting data from canonical R453 outputs.
# Usage: Rscript rcode/prepare_plot_data.R /path/to/canonical_R453 [bundle_directory]
# No models are fitted here. Original participant identifiers/demographics are not exported.
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1L) stop('Supply the canonical_R453 directory.')
root <- normalizePath(args[1], mustWork = TRUE)
cli <- commandArgs(FALSE); script <- sub('^--file=', '', cli[grepl('^--file=', cli)][1])
bundle <- if (length(args) > 1L) args[2] else dirname(dirname(normalizePath(script)))
out <- file.path(bundle, 'plot_data'); dir.create(out, recursive = TRUE, showWarnings = FALSE)
read_source <- function(path) read.csv(file.path(root, path), stringsAsFactors = FALSE)
sources <- c(T11='engine/baseline/tables/T11_primary_fixed_effects.csv',
 T14='engine/baseline/tables/T14_primary_estimated_marginal_means.csv',
 T23='engine/baseline/tables/T23_exact_item_randomization_tests.csv',
 T44='engine/baseline/tables/T44_RT_within_between_LMM.csv',
 P03='engine/followup/tables/P03_political_core_family_correction.csv',
 J02='engine/followup/tables/J02_stacked_joint_fixed_effects.csv',
 J03='engine/followup/tables/J03_stacked_joint_key_cross_outcome_tests.csv',
 E03='engine/additional_locked/E03_AUC_interaction_checks.csv',
 E07='engine/additional_locked/E07_RT_conflict_by_prebunk.csv')
for (nm in names(sources)) write.csv(read_source(sources[[nm]]), file.path(out, paste0(nm,'.csv')), row.names=FALSE, na='')
d <- read_source('engine/baseline/data/analysis_long_clean_locked.csv')
stopifnot(nrow(d)==4104L, length(unique(d$participant_id))==171L,
 length(unique(d$item_id))==24L, all(table(d$participant_id)==24L),
 all(is.finite(d$discrimination)), all(is.finite(d$attitude)),
 all(d$discrimination>=0 & d$discrimination<=10), all(d$attitude>=1 & d$attitude<=10))
p <- unique(d[c('participant_id','inoculation')]); stopifnot(sum(p$inoculation=='Control')==82L, sum(p$inoculation=='Prebunk')==89L)
# Reorder each exported distribution independently; rows cannot be joined by subject ID.
write_dist <- function(x, filename) {
 x <- x[do.call(order, x),,drop=FALSE]; rownames(x) <- NULL
 write.csv(x, file.path(out, filename), row.names=FALSE, na='')
}
gap_table <- function(value, grouping) {
 x <- aggregate(d[[value]], list(id=d$participant_id, condition=d$inoculation, level=grouping), mean)
 w <- reshape(x, idvar=c('id','condition'), timevar='level', direction='wide')
 stopifnot(nrow(w)==171L, all(is.finite(w$x.0)), all(is.finite(w$x.1)))
 data.frame(condition=w$condition, value=w$x.1-w$x.0)
}
write_dist(gap_table('discrimination', d$information_type_code), 'F1_participant_gaps.csv')
write_dist(gap_table('attitude', d$social_consensus_code), 'F2_participant_gaps.csv')
cong <- as.integer(d$stimulus_party_code==d$vote_preference_code)
a <- gap_table('discrimination',cong); a$outcome <- 'Perceived misleadingness'
b <- gap_table('attitude',cong); b$outcome <- 'Attitude'
write_dist(rbind(a[c('outcome','value')],b[c('outcome','value')]), 'F3_participant_gaps.csv')
auc <- function(r, label) {
 hi <- r[label==1]; lo <- r[label==0]
 stopifnot(length(hi)>0L, length(lo)>0L, all(is.finite(r)))
 delta <- outer(hi,lo,'-'); mean((delta>0)+0.5*(delta==0))
}
overall <- do.call(rbind, lapply(split(d,d$participant_id), function(z)
 data.frame(condition=z$inoculation[1], value=auc(z$discrimination,z$information_type_code))))
by_reaction <- do.call(rbind,lapply(split(d,interaction(d$participant_id,d$social_consensus_code,drop=TRUE)),function(z)
 data.frame(condition=z$inoculation[1], reaction=ifelse(z$social_consensus_code[1]==0,'Like-dominant','Angry-dominant'), value=auc(z$discrimination,z$information_type_code))))
write_dist(overall,'F5_overall_AUC.csv'); write_dist(by_reaction,'F5_reaction_AUC.csv')
checks <- data.frame(measure=c('participants','trials','items','control_n','prebunk_n','control_pooled_auc','prebunk_pooled_auc'),
 value=c(nrow(p),nrow(d),length(unique(d$item_id)),82,89,mean(overall$value[overall$condition=='Control']),mean(overall$value[overall$condition=='Prebunk'])))
write.csv(checks,file.path(bundle,'verification','source_checks.csv'),row.names=FALSE)
write.csv(data.frame(file=names(sources),canonical_relative_path=unname(sources)),file.path(bundle,'verification','source_map.csv'),row.names=FALSE)
cat('Exported verified aggregate estimates and unlinked participant plotting distributions.\n')