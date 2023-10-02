# Select BFPRT

Esse código visa gerar muitas instâncias, executar o algoritmo [Select BFPRT](http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf) para diferentes tamanhos de partição e coletar os tempos de execução. O algoritmo Select BFPRT busca encontrar o i-ésimo maior elemento de um vetor utilizando a [mediana das medianas](https://en.wikipedia.org/wiki/Median_of_medians).

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
