Multi_Fasta_Consensus
Overview
Este script em Python foi desenvolvido para processar um arquivo no formato Multi Fasta (".fasta") contendo múltiplas sequências de aminoácidos e gerar a sequência consenso, além de uma matriz mostrando a frequência de cada aminoácido em cada posição.

Requisitos
Python 3.x
Biblioteca BioPython (instalável via pip install biopython)
Uso
Certifique-se de ter o Python instalado em sua máquina.
Instale a biblioteca BioPython executando pip install biopython.
Coloque o arquivo de entrada no formato Multi Fasta ("multi_fasta.fasta") na mesma pasta que o script.
Execute o script.

Funcionamento
O script lê o arquivo "multi_fasta.fasta" e armazena todas as sequências de aminoácidos em uma lista.
Determina o tamanho da maior sequência encontrada.
Cria uma matriz onde cada linha representa um aminoácido e cada coluna representa uma posição na sequência, inicializando todas as células com zeros.
Itera sobre cada sequência na lista e incrementa a contagem de cada aminoácido na posição correspondente na matriz.
Constrói a sequência consenso, que é a sequência de aminoácidos mais frequentes em cada posição.
Imprime a sequência consenso e a matriz de frequência.
Cria um arquivo de saída ("seq_final.fasta") contendo a sequência consenso.
Saída
O arquivo "seq_final.fasta" contém a sequência consenso sob o título ">Sequencia_Consenso".