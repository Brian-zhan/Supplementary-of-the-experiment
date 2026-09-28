table_dir <- file.path(analysis_root, "tables")
data_dir <- file.path(analysis_root, "data")

dat <- read.csv(file.path(data_dir, "analysis_long_clean_locked.csv"), check.names = FALSE)
required <- c("participant_id","item_id","inoculation","inoculation_code","stimulus_party","stimulus_party_code",
"information_type","information_type_code","social_consensus","social_consensus_code","trial_order",
"discrimination","attitude","discrimination_rt_s","discrimination_question_order","we_value","we_question_order","attitude_question_order")
missing_required <- setdiff(required, names(dat))
if (length(missing_required)) stop("Missing required columns: ", paste(missing_required, collapse = ", "))

dat$participant_id <- factor(dat$participant_id)
dat$item_id <- factor(dat$item_id)
dat$inoc_c <- dat$inoculation_code - 0.5
dat$party_c <- dat$stimulus_party_code - 0.5
dat$scap_c <- dat$information_type_code - 0.5
dat$cons_c <- dat$social_consensus_code - 0.5
dat$scap_cons_c <- dat$scap_c * dat$cons_c
dat$scapegoating <- ifelse(dat$information_type_code == 1, "High scapegoating", "Low scapegoating")
dat$consensus <- ifelse(dat$social_consensus_code == 1, "Angry-dominant", "Like-dominant")
dat$trial_z <- as.numeric(scale(dat$trial_order))

dat$cue_correct_recomputed <- ifelse(
  as.character(dat$item_id) == "101-1",
  as.integer(dat$we_value == 6),
  as.integer(dat$we_value == ifelse(dat$social_consensus_code == 1, 6, 0))
)

checks <- data.frame(
  check=c("rows","participants","items","rows_per_participant_min","rows_per_participant_max",
          "rows_per_item_min","rows_per_item_max","missing_discrimination","missing_attitude",
          "duplicate_participant_item","unique_discrimination_values","unique_attitude_values"),
  value=c(nrow(dat),nlevels(dat$participant_id),nlevels(dat$item_id),min(table(dat$participant_id)),
          max(table(dat$participant_id)),min(table(dat$item_id)),max(table(dat$item_id)),
          sum(is.na(dat$discrimination)),sum(is.na(dat$attitude)),
          sum(duplicated(dat[c("participant_id","item_id")])),
          length(unique(dat$discrimination)),length(unique(dat$attitude)))
)

stopifnot(nrow(dat)==4104,nlevels(dat$participant_id)==171,nlevels(dat$item_id)==24,
          all(table(dat$participant_id)==24),all(table(dat$item_id)==171),
          !anyNA(dat$discrimination),!anyNA(dat$attitude),
          sum(duplicated(dat[c("participant_id","item_id")]))==0)

item_map <- unique(dat[c("item_id","stimulus_file","stimulus_party","stimulus_party_code",
                         "scapegoating","information_type_code","consensus","social_consensus_code")])
item_map <- item_map[order(item_map$item_id), ]
cell_balance <- aggregate(as.character(item_map$item_id),
                          item_map[c("stimulus_party","scapegoating","consensus")], length)
names(cell_balance)[names(cell_balance)=="x"] <- "n_items"
stopifnot(all(cell_balance$n_items==3),nrow(cell_balance)==8)

participant_groups <- unique(dat[c("participant_id","inoculation","inoculation_code")])
participant_groups <- aggregate(participant_id ~ inoculation + inoculation_code, participant_groups, length)
names(participant_groups)[names(participant_groups)=="participant_id"] <- "n_participants"
stopifnot(participant_groups$n_participants[participant_groups$inoculation=="Control"]==82)
stopifnot(participant_groups$n_participants[participant_groups$inoculation=="Prebunk"]==89)

write.csv(checks,file.path(table_dir,"T01_data_audit.csv"),row.names=FALSE)
write.csv(item_map,file.path(table_dir,"T02_item_condition_map.csv"),row.names=FALSE)
write.csv(cell_balance,file.path(table_dir,"T03_item_cell_balance.csv"),row.names=FALSE)
write.csv(participant_groups,file.path(table_dir,"T04_participant_groups.csv"),row.names=FALSE)

cue_audit <- data.frame(
  item_id=levels(dat$item_id),
  consensus=item_map$consensus[match(levels(dat$item_id),item_map$item_id)],
  correct=as.integer(tapply(dat$cue_correct_recomputed,dat$item_id,sum)),
  n=as.integer(tapply(dat$cue_correct_recomputed,dat$item_id,length))
)
cue_audit$accuracy <- cue_audit$correct/cue_audit$n
write.csv(cue_audit,file.path(table_dir,"T05_cue_recognition_by_item.csv"),row.names=FALSE)
saveRDS(dat,file.path(analysis_root,"logs","locked_analysis_data.rds"))
