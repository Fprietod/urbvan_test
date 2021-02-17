hist.write.format("jdbc").option("url", "jdbc:postgresql://database-postgress.c295zanvccq2.us-east-1.rds.amazonaws.com:5432/postgres?user=urbvan@urbvan&password=root2022").option("Driver","org.postgresql.Driver").option("dbtable", "client").save()
--------------------------------------------------------
hist.write.format("csv").option("")
   .option("header", "true")
   .save("client_table.csv")
---------------------------------------------------------------
hist.write.option
-------------------------------------------------------

