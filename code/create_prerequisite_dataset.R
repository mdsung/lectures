library(tidyverse)
library(DBI)
library(RMariaDB)
library(glue)

con <- DBI::dbConnect(RMariaDB::MariaDB(),
                      host   = "103.22.220.153",
                      # UID      = rstudioapi::askForPassword("Database user"),
                      # PWD      = rstudioapi::askForPassword("Database password"),
                      user = 'root',
                      password = 'yonsei2020!',
                      port     = 13306, 
                      dbname = 'mimiciv')