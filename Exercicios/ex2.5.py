#Na verdade, o Facebook não usa nem arrays nem listas encadeadas para armazenar informações. Vamos considerar uma estrutura de dados
#híbrida: um array de listas encadeadas. Você tem um array de 26 slots. Cada slot aponta para uma lista encadeada. Por exemplo,
#o primeiro slot do array aponta para uma lista encadeada que contém os usuários que começam com a letra A. O segundo slot aponta
#para a lista encadeada que contém os usuários que começam com a letra B, e assim por diante.

#Suponha que o Adit B se inscreva no Facebook e você queira adicioná-lo à lista. Você vai ao slot 1 do array, a seguir para a lista 
#encadeada do slot 1, e adiciona Adit B no final. Agora, suponha que você queira procurar o Zakhir H. Você vai ao slot 26, que
#aponta para a lista encadeada de todos os nomes começados em Z. Então, procura pela lista até encontrar o Zakhir H.

#Compara esta estrutura híbrida com arrays e listas encadeadas. É mais lento ou mais rápido fazer inserções e eliminações nesse caso?
#Você não precisa responder dando o tempo de execução Big(O), apenas diga se a nova estrutura de dados é mais rápida ou mais lenta do
#que os arrays e as listas encadeadas.

#Essa lista é mais rápida por conta que ela vai instantaneamente nas listas onde os usuários são devimente colocados em ordem alfa
#bética, elas são mais rápidas para inserção e rápida para tipo de lista de encadeamento por que revisa cada lista do A até o Z.
#Eles são mais rapidos do que array e lista encadeamento puras por conta funciona para os dois tipos de situações que a lista de
#encadeamento vai do A,B,C..etc e o arrays funciona aleatório por que acha rapido e remove rapido