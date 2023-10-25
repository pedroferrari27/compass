
#carrega os dados em um rdd
linhas = sc.textFile("/dados/Cópia_README.md")               

#separa o texto em palavras, delimitando pelo uso do espaço
palavras = linhas.flatMap(lambda line: line.split(" "))

#separa as palavras em tuplas e conta a sua frequencia
contador = palavras.map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)

#faz um print no pyspark shell
contador.foreach(lambda x: print(f"{x[0]}: {x[1]}"))


