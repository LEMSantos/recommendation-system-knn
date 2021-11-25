# Sistema de recomendação de filmes

**Obs: Todos os comandos citados pressupõem a utilização do sistema operacional Linux.**

### Setup do projeto

Esse projeto utiliza o pipenv com gerenciador do ambiente virtual, por isso para executar o projeto é necessário que o mesmo esteja instalado no sistema. A instalação pode ser feita com o comando abaixo:

```bash
sudo apt install pipenv
```

Tendo o pipenv devidamente instalado no sistema, as dependências do projeto podem ser instaladas com o comando a seguir:

```
pipenv install
```

### Execução do projeto

Para que o sistema de recomendação funcione corretamente é necessário executar o script que realiza a preparação dos dados. O script pode ser executado com o seguinte comando:

```bash
pipenv run python prepare_data.py
```

Com os dados preparados, o projeto pode ser efetivamente executado com o comando:

```bash
pipenv run python main.py
```
