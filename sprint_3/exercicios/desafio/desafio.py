def check_nomes(i):
    #funcao para correção de erros decorentes do split para a formação da tabela
    #para isso, approveitamos o fato de que nesta tabela, colunas de nomes estão intercaladas com colunas de valores numericos
    #assim, usamos esse fato para identificar até onde foi criado colunas extras medindo a quantidade de colunas consecutivas não numericas
  
    mark = []
   #inicializamos uma ista para marcar os elementos que foram divididos erroneamente
  
   #neste for, checkamos os indices consecutivos com valores não numericos, e se ocorrer, marcamos ele colocando em mark
    for k in range(len(i)-1):
         if i[k][0].isdigit() == False:
             if i[k+1][0].isdigit() == False:
                 mark.append(k)      
                 
    #colocamos o mark em ordem decrescente para alterar os indices             
    mark = mark[::-1] 
    
    #concatenamos os elementos divididos erroneamente em uma só coluna
    for element in mark:
       i[element] = i[element] + "," + i[element+1]
       
    #eliminamos as colunas extras do split erroneo   
    for element in mark:   
       i.pop(element+1)



with open("actors.csv","r") as arquivo:
    linha = [] 
    #pegando cada linha do csv em uma lista
    for lin in arquivo:
        linha.append(lin.strip())
    #print(linha)
    titulos = linha[0]
    linha.pop(0)
    
    #separando os elementos
    titulos = list(titulos.split(","))
   
    tabela = []
    for i in linha:
        tabela.append(list(i.split(",")))
    
    #tratamento de nomes na tabela
    #erros ocorrem pela forma que usamos para separar as colunas, pois certos nomes podem ter virgulas
    for i in tabela:
        if len(i) > 6:  #checamos o numero de colunas,se for maior que o padrão, sabemos que houve erro na divisão
           
            check_nomes(i)  #usamos esta função para acertar o numero de colunas actor e #1 movie
           
    #ex:1
    
    #iterando sobre o objeto, atualizando o valor do maior numero de filmes
    maior = (0,0)
    #armazenando o valor do indice e o maior total de filmes em uma tupla 
    k = -1
    for i in tabela:
        k = k+1
        if int(i[2]) >= maior[1]:
            maior = (k,int(i[2]))
    #infelizmente não mostra outros atores com a mesma quantidade de filmes
            
    #imprimir resultados no output file
    with open("etapa-1.txt","w") as ex1:
        print("o ator/atriz com maior número de filmes é " + str(tabela[maior[0]][0]) +  " com " + str(maior[1]) + " filmes.", file = ex1 )
    
    
    #ex 2
    gross = []
    #armazenando todos os valores de gross
    for i in tabela:
        gross.append(float(i[5]))
    
    #calculando a media
    media = sum(gross)/len(tabela)
    
    #imprimir resultados no output file
    with open("etapa-2.txt","w") as ex2:
        print("a média de receita de bilheteria bruta dos principais filmes é " + str(media) + " de dólares ",file = ex2)
    
    
    #ex3
    
    
    #iterando sobre o objeto, atualizando o valor do maior numero de filmes
    maior = (0,0)
    #armazenando o valor do indice e o maior total de filmes em uma tupla 
    k = -1
    for i in tabela:
        k = k+1
        if float(i[3]) >= maior[1]:
            maior = (k,float(i[3]))
    #infelizmente não mostra outros atores com a mesma quantidade de filmes
            
    #imprimir resultados no output file
    with open("etapa-3.txt","w") as ex3:
        print("o ator/atriz com maior arecadação media por filme é " + str(tabela[maior[0]][0]) +  " com " + str(maior[1]) + " por filme.", file = ex3 )
           
        
    #ex 4 
    
    # criamos um lista com os nomes do filmes
    nomes = []
    for i in tabela:
        nomes.append(i[4])
    apearences = ()
    listacount = []
    #pegamos uma lista com os nomes unicos
    setnomes = set(nomes)
    
    #então comparamos as duas e fazemos o count, armazenando o resultado em um lista de tuplas com o nome e a contagem de repetiçoes
    for i in setnomes:
        apearences = (nomes.count(i),i) 
        listacount.append(apearences)
    
    #colocando em ordem decrescente de aparições
    listacount.sort(reverse = True)
    
    with open("etapa-4.txt","w") as ex4:
     
     #verbose print   
     #print("fimes de maior bilheteria por atores na database", file = ex4 )
     # print("listado por quantidade de atores então nome no filme", file = ex4 )
     #  for i in listacount:
     #     print("  | " + str(i[0]) +  " | " + i[1], file = ex4 )
           
     sequencia = 1
     for i in listacount:
         print(str(sequencia) +" - O filme "+i[1]+" aparece "+ str(i[0]) +"  vez(es) no dataset", file = ex4 )
         sequencia =  sequencia +1
           
    #ex 5 
    
    # mesmo proscesso do ex4, mas sem fazer a contagem
    #pegamos cada linha da tabela e criamos a partir dela uma lista de tuplas com o nome e total_gross
    gross_actor_list = []
    gross_actor = ()
    for i in tabela:
        gross_actor = (float(i[1]),i[0])
        gross_actor_list.append(gross_actor)
        
    #e a partir disso ordemanos descrescente
    gross_actor_list.sort(reverse = True)
    
    
    with open("etapa-5.txt","w") as ex5:
        for i in gross_actor_list:
            print( i[1] + " - " +  str(i[0])  +"," , file = ex5 )
        
        
    
    
    
                        