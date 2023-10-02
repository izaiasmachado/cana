# Select BFPRT

Esse código visa gerar muitas instâncias, executar o algoritmo [Select BFPRT](http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf) para diferentes tamanhos de partição e coletar os tempos de execução. O algoritmo Select BFPRT busca encontrar o i-ésimo maior elemento de um vetor utilizando a [mediana das medianas](https://en.wikipedia.org/wiki/Median_of_medians).

Além do código, esse repositório também acompanha [um relatório, que está dentro da pasta docs,](./docs/Izaias%20Machado%20Pessoa%20Neto%20-%20497372%20-%20Select%20BFPRT%20-%20CANA.pdf) que contempla a explicação do funcionamento dos algoritmos `Partition`, `Partition-BFPRT` e `Select-BFPRT`, prova da complexidade do `Select-BFPRT`, passos metodológicos e resultados desse experimento.

## Como rodar?

Por meio do terminal ou prompt de comandos do Windows, naveque até a raíz desse projeto e digite o seguinte comando:

```
python src/main.py
```

O programa já tem todas as instruções necessárias para que você consiga rodar suas próprias instâncias.

## Quais as funcionalidades implementadas?

Esse programa permite que você gere uma quantidade de instâncias, cada instância com um tamanho fixo e também que escolha uma quantidade de processos que deve ser instanciados. Esses processos permitem o código rode em diferentes núcleos do processador, isso permite se aproveitar de todo o processador e consequentemente uma execução mais rápida.

Além disso, o programa também permite que você digite uma instância manualmente. É importante citar que isso funciona mesmo para instâncias que são muito grandes, basta que os valores sejam separados por vírgula. Caso o usuário não digite o tamanho total da instância em uma linha, o programa pede novamente o restante das instâncias, só que em uma nova linha. Por isso, você pode colar no terminal uma instância vários números por linha e várias linhas.

## Para onde vão os resultados?

Para cada execução em massa, é criado um novo arquivo `.csv` dentro da pasta `src/data`. Além disso, os logs de execução pode ser encontrados no arquivo `logs.log`, também dentro da pasta `src/data`.

Para executar o programa por uma longa duração, utilize o [Screen](https://linuxize.com/post/how-to-use-linux-screen/) em ambientes Linux/MacOS. Com isso, o terminal da execução pode ser desacoplado e o arquivo de logs pode ser visualizado utilizando o `tail -f src/data/logs.log`

## Como visualizar os dados?

Garanta que você tem a biblioteca Pandas do Python instalada. Caso não tenham, rode o comando abaixo para a instalar utilizando o gerenciador de pacotes Pip.

```
pip install pandas
```

Com a biblioteca instalada, abra o arquivo `src/statistics.py` e o nome de arquivo escrito na variável `file_name` pelo arquivo de resultado que você quer analisar. Com isso feito, basta rodar o comando abaixo.

```
python src/statistics.py
```

O resultado vai ser similar ao da tabela abaixo

```
               Algoritmo  Tempo Médio de Execução  Desvio Padrão
0  Select BFPRT - r = 11                 3.330611      17.046008
1   Select BFPRT - r = 3                 5.093321      12.740226
2   Select BFPRT - r = 5                 3.700169      16.541186
3   Select BFPRT - r = 7                 3.265799      12.181696
4   Select BFPRT - r = 9                 3.162925      12.181599
```

## Árvore de Diretórios

Esta árvore está sendo disposta apenas que possa ser conferido os arquivos que estão anexados.

```
.
├── README.md
├── docs
│   └── Izaias Machado Pessoa Neto - 497372 - Select BFPRT - CANA.pdf
└── src
    ├── algorithms
    │   ├── __init__.py
    │   ├── algorithms.py
    │   ├── merge_sort.py
    │   └── select_bfprt.py
    ├── calculate.py
    ├── execution
    │   ├── __init__.py
    │   ├── algorithm.py
    │   ├── dataset.py
    │   ├── execution.py
    │   ├── executor.py
    │   └── instance.py
    ├── instances
    │   ├── __init__.py
    │   └── generate_instances.py
    ├── main.py
    ├── utils
    │   ├── __init__.py
    │   ├── files.py
    │   └── logger.py
    └── worker.py
```

## Disclaimer

Os testes foram feitos em máquina linux, utilizando a versão 3.8.10 do python.

Certifique-se que você tem uma versão igual ou mais nova do python 3, para garantir a compatibilidade. Para isso, digite em seu terminal o comando `python --version` ou `python3 --version`.
