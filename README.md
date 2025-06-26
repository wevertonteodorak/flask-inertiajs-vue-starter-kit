# Sobre
## Este projeto está em WIP (Work in progress)
Starter kit que integra Flask (backend python) com um frontend usando Vue 3 + Inertia.js + TypeScript, pronto para hot-reload.

# Features
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

1 - criar venv python
```sh
python -m venv .venv
```
2 - ative o venv
```sh
source .venv/bin/activate
```
3 - instalar requirements do python (certifique de estar na raiz do projeto)
```sh
pip install -r requirements.txt
```

4 - instalar os pacotes do npm
```sh
cd static/
```
```sh
npm install
```

5 - volte para a raiz do projeto e inicie o banco de dados 
```sh
flask db:migrate
```
e em seguida inicie os backends com
```sh
make dev
```

Caso você não possua make disponível você deve executar o servidor backend usando
```sh
python app.py
```
E também deve executar o servidor de desenvolvimento do frontend
```sh
cd static/
```
```sh
npm run dev
```
Em ambiente de desenvolvimento o servidor backend e frontend devem estar em execução juntos
