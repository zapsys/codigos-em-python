# Códigos em Python
Utilização da linguagem de programação Python na resolução de algoritmos, com exemplos de uso de comandos básicos, estruturas de repetição, definições de funções, classes, etc.

## Requisitos para execução:

- Linux, Mac ou Windows:
    - [Python 3](https://www.python.org/downloads/)
- Android
    - [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)

## Instalação:
No terminal clone o projeto:
```
$ git clone https://github.com/zapsys/codigos-em-python.git
```
Ou baixe o zip do projeto e descompacte-o:
```
https://github.com/zapsys/codigos-em-python/archive/refs/heads/main.zip
```
Entre na pasta do projeto:
```
$ cd codigos-em-python
```
Execute o script desejado:
```
$ python nome_do_script.py
```
ou

```
$ python3 nome_do_script.py
```
ou execute através de sua IDE de preferência.

## Ambiente Virtual
Para executar alguns algoritmos há a necessidade de criar um *Virtual Environment* (Ambiente virtual), pois se faz necessária a instalação de algumas bibliotecas para a execução ou renderização das informações. Assim se cria um ambiente isolado do sistema (nível local), onde só os pacotes necessários para executar tal algoritmo/aplicação são instalados.

## Criando o ambiente virtual
Execute o seguinte comando dentro da pasta de trabalho:
```
$ python -m venv env
```
*env* é um nome comum escolhido para o ambiente, mas você pode escolher um outro caso deseje, mas o mesmo não pode conter espaços ou acentos.

**Ative o ambiente:**

- No terminal do Linux/MacOS use `source env/bin/activate`.

- No Windows use `source env\Scripts\Activate.bat` se estiver no *CMD* ou `source env\Scripts\Activate.ps1` para o *Powershell*.

Após ativar o ambiente instale as bibliotecas necessárias usando o comando [pip](https://pip.pypa.io/en/stable/installation/). O mesmo deve estar instalado globalmente no sistema.

```
$ pip install nome_biblioteca 
```
Após esses passos o algoritmo/programa pode ser executado conforme explicado anteriormente.

## Dúvidas ou sugestões
Caso tenha alguma dúvida ou sugestão sinta-se a vontade para nos contactar e contribuir.

## Licença
Este projeto está sob a licença MIT, que permite o download, execução, alteração, redistribuição, tanto para uso privado como comercial do código fonte, desde que citado o autor. 

[MIT License](LICENSE.md)