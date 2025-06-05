# CRUD com arquivos TXT em Python

Esse é um dos primeiros CRUDs que desenvolvi em Python. Mistura a lógica de programação, necessária para as operações do CRUD, com manipulações de arquivos TXT no sistema. Decidi subir este código para o GitHub como forma de documentar minha evolução como programador. Pretendo usar este repositório no futuro como comparação com projetos mais avançados.



## Execução:
Baixe os arquivos. No terminal, siga até o diretório onde eles estão e execute:
```
python main.py
```

Ao executar o código, é apresentado um menu interativo onde é possível criar um arquivo novo ou selecionar um arquivo já existente. Além de poder listar os arquivos TXTs contidos no diretório atual, você pode ler ou excluir um arquivo. Caso selecione um arquivo, será apresentado um outro menu interativo, agora com opções para manipular o arquivo selecionado. Podendo escrever, ler, editar ou remover o conteúdo de dentro do arquivo.

Dentro do arquivo, a cada linha adicionada, é informado o índice da linha. Esse índice é utilizado nas funções para selecionar a linha em específica que será modificada/excluída.