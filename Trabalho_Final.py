from Bio import SeqIO

lista = []  # lista para armazenar a frequencia de cada aminoácido
tamanho = 0 # variavel para armazenar qual seria o maior tamanho
for i in SeqIO.parse("multi_fasta.fasta", "fasta"): # abre todos as sequencias
    seq = i.seq # armazena a sequencia atual
    lista.append(str(seq)) # adiciona ela na lista em forma de string

    tamanho_aux = len(str(seq)) # armazena o tamanho da sequencia atual
    if tamanho_aux > tamanho:   # compara o tamanho da sequencia atual com a variavel anteriormente armazenada
        tamanho = tamanho_aux   # troca os valores da auxiliar para se ter o novo maior valor

matriz_aa = {  # dicionario da matriz com todos os aminoácidos e cada valor sendo uma lista vezes o tamanho da maior sequencia
    'A': [0]*tamanho,
    'B': [0]*tamanho,
    'C': [0]*tamanho,
    'D': [0]*tamanho,
    'E': [0]*tamanho,
    'F': [0]*tamanho,
    'G': [0]*tamanho,
    'H': [0]*tamanho,
    'I': [0]*tamanho,
    'K': [0]*tamanho,
    'L': [0]*tamanho,
    'M': [0]*tamanho,
    'N': [0]*tamanho,
    'P': [0]*tamanho,
    'Q': [0]*tamanho,
    'R': [0]*tamanho,
    'S': [0]*tamanho,
    'T': [0]*tamanho,
    'V': [0]*tamanho,
    'W': [0]*tamanho,
    'Y': [0]*tamanho,
    'Z': [0]*tamanho
    }

for seq in lista: # para cada sequencia na lista
    for posicao, aminoacido in enumerate(seq):  # usa o enumerate para pegar a sua posição e qual aminoácido é
        matriz_aa[aminoacido][posicao] += 1     # utiliza qual aminoácido é e em qual posição para adicionar +1 na lista dentro da matriz

final = "" # string para armazenar a sequencia consenso completa
for posicao in range(tamanho): # loop para ir em todas as posições
    posicao_aux = 0  # variavel auxiliar para poder armazenar a maior frequencia
    nucleotideo_aux = "" # variavel auxiliar para poder armazenar qual aminoácido apareceu em maior frequencia
    for aminoacido in matriz_aa: # loop para checar qual valor de frequencia apareceu mais vezes para cada posição
        if matriz_aa[aminoacido][posicao] > posicao_aux: # condição para ver se a frequencia atual é maior que a armazenada
            posicao_aux = matriz_aa[aminoacido][posicao] # atualiza a auxiliar com a nova frequencia
            nucleotideo_aux = aminoacido  # atualiza a auxilair com o novo nome de aminoácido mais frequente
    final += str(nucleotideo_aux)  # concatena a string vazia com o maior aminoácido

print(final) # imprime a sequencia consenso completa
print("\n")  # visual mais aesthetic

for aminoacido, posicao in matriz_aa.items(): # loop para fazer a exibição que o Rosalind pediu
  frequencia = " " # string vazia que irá armazenar a frequencia de cada aminoácido
  for posicao in posicao: # loop para transformar cada item da lista de frequencia em uma string
      frequencia += str(posicao) + " " # adiciona cada item da lista na string
  print(f'{aminoacido}: {frequencia}') # imprime no formato que o Rosalind pediu

with open("seq_final.fasta", "w") as arquivo: # cria um arquivo para armazenar a sequencia consenso
    arquivo.write(">Sequencia_Consenso" + "\n") # escreve no arquivo um titulo
    arquivo.write(final) # escreve no arquivo a sequencia consenso
    print("Arquivo Seq_Final.fasta criado com Sucesso!") # print para mostrar que deu certo