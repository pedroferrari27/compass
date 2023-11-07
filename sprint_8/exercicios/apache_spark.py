#1
from pyspark.sql import SparkSession

from pyspark import SparkContext, SQLContext

from pyspark.sql.functions import rand,when,lit,array,round

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

 
df = spark.read.csv("nomes_aleatorios.txt")

#2

df.show(10)

df = df.withColumnRenamed("_c0","nomes")

df.printSchema()

#3 

df= df.withColumn("Escolaridade", when(rand() < 1/3, lit("Fundamental"))
                                           .when(rand() < 2/3, lit("Médio"))
                                           .otherwise(lit("Superior")))

df.show(10)

#4

paises = ["Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela"]
quantidade = len(paises)
paises = array([lit(pais) for pais in paises])


df = df.withColumn("Pais", paises.getItem((rand()*quantidade).cast("int")))


df.show(10)

#5

df = df.withColumn("AnoNascimento", lit(1945 + round(rand() * (2010 - 1945)))                              .cast("int"))

df.show(10)

#6
df2 = df.select("*").filter(df["AnoNascimento"] >= 2000)

# Mostrar os 10 primeiros nomes do DataFrame resultante
df2.show(10)

#7
df.createOrReplaceTempView ("pessoas")

spark.sql("select * from pessoas where AnoNascimento >= 2000").show(10)

#8
df2 = df.select("*").where((df["AnoNascimento"] >= 1980 ) & (df["AnoNascimento"] <= 1994))
#print(contagem)
df2.show(10)

print(df2.count())

#9

df.createOrReplaceTempView ("pessoas")

print(spark.sql("select * from pessoas where AnoNascimento >= 1980 AND AnoNascimento <= 1994").count())

#10

df.createOrReplaceTempView ("pessoas")


df2 = spark.sql("""
SELECT Pais, 
       CASE WHEN AnoNascimento >= 1944 AND AnoNascimento <= 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento >= 1965 AND AnoNascimento <= 1979 THEN 'Geração X'
            WHEN AnoNascimento >= 1980 AND AnoNascimento <= 1994 THEN 'Millennials'
            WHEN AnoNascimento >= 1995 AND AnoNascimento <= 2015 THEN 'Geração Z'
            END AS Geracao,
       COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
ORDER BY Pais, Geracao, Quantidade 
""")

df2.show(10)


