# load data from SQL
library(RODBC);
conn <- odbcConnect("[DSN]");
df <- sqlQuery(conn, "SELECT * FROM tvfXXX (param_1, param_2, param_3");
