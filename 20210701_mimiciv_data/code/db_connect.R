# R DB connect
library(dotenv)
library(here)
library(RMariaDB)

## read dotenv file
dotenv::load_dot_env(file=here('.env'))

## connect to db
con = DBI::dbConnect(RMariaDB::MariaDB(),
                     host = Sys.getenv('HOST'),
                     port = Sys.getenv('PORT'),
                     user = Sys.getenv("USER"),
                     password = Sys.getenv("PASSWORD"),
                     dbname = Sys.getenv('DBNAME'))
