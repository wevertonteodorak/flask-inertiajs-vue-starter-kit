# Sobre
## Este projeto está em WIP (Work in progress)
Starter kit que integra Flask (backend python) com um frontend usando Vue 3 + Inertia.js + TypeScript, pronto para hot-reload.

# Funcionalidades
- Autentião Local - DONE
- Criar nova conta local - DONE
- Autenticaão SSO OAUTH - WIP
- Reset de senha - TBD

# Estrutura
```shell
  $ tree
/
├── Makefile
├── src                 ← arquivos fonte do backend
├── data                ← persistencia de dados
├── app.py              ← entrypoint do backend
├── static/
│   └── public/         ← arquivos compilados (js/css)
│   └── resources/      ← frontend Vue (source files)
├── templates/
│   └── base.html       ← template raiz com Inertia
└── README.md
```

# Pré requisitos

- Python 3.8+
- Node.js (22+) & npm
- make (para GNU Make ou equivalente)

# Como rodar em dev

## 1 - Instale o ambiente DEV
> #### Se você está usando LINUX rode apenas o comando abaixo e ele instalará as dependências tanto para backend quanto frontend

```sh
make install
```
Pule para etapa 2
> #### Se você NÃO está usando LINUX rode os comandos abaixo
### Crie e Ative o venv
```sh
python -m venv .venv
```
```sh
source .venv/bin/activate
```
### Instalar requirements do python (certifique de estar na raiz do projeto)
```sh
pip install -r requirements.txt
```

### Instalar os pacotes do npm
```sh
npm --prefix static/ install
```

## 2 - Inicie o banco de dados 
```sh
flask db:migrate
```
## 3 - Inicie os backends
> #### Se você está usando LINUX rode apenas o comando abaixo e ele iniciará tanto o backend quanto frontend para desenvolvimento
```sh
make dev
```

> #### Caso você não possua make disponível você deve executar o servidor backend usando
```sh
python app.py
```
E também deve executar o servidor de desenvolvimento do frontend
```sh
npm --prefix static/ run dev
```
Em ambiente de desenvolvimento o servidor backend e frontend devem estar em execução juntos
