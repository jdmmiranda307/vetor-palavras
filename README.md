# vetor-palavras

## Instalação do projeto
Para realizar a instalação do projeto, dentro de seu ambiente virtual, rodar `pip install -r requirements.txt` e aguardar a instalação de todas as dependencias do projeto.
Após isso, deverá rodar o comando `python manage.py makemigrations & python manage.py migrate` para iniciar a base de dados com as tabelas do projeto. A base de dado é um sqlite simples.

## Endpoints

### Adicionar textos
Para adicionar textos na base de dados, deverá ser realizado um `POST` no endpoint `/processador-palavras/documento/` com o seguinte dict:

    {
        "texts": [
            {"text": "esse é um texto de exemplo"}
        ]
    }

Sendo possivel, então, enviar diversos textos para a API simultaneamente.
Nessa mesma API, é possivel também fazer um `GET` que retornará uma lista com todos os documentos cadastrados

### Vocabulários
Para visualização dos vocabulários criados, existem 2 APIs distintas.
A que retornará o vocabulário padrão, de palavras únicas, está no endpoint de `/processador-palavras/vocabulario-default`, onde você fará uma requisção do tipo GET.
Esse endpoint retornará um vetor como o no exemplo abaixo:

    [
        {
            "id": 1,
            "word": "joao"
        },
        {
            "id": 2,
            "word": "victor"
        },
    ]

Enquanto, para visualizar o vocabulário agrupado em 2 palavras, é necessário consumir o endpoint `/processador-palavras/vocabulario-grupo`, onde você fará uma requisção do tipo GET. Ela retornará um vetor como no exemplo abaixo:

    [
        {
            "id": 1,
            "words": "joao victor"
        },
    ]

### Vocabulário por Documento

Para visualizar o vocabulário de um documento existem 2 APIs, sendo que uma retornará o vocabulário agrupado e a outra o padrão.
Para consumir a com o vocabulário padrão, você precisará fazer uma requisição do tipo `GET` no endpoint `/processador-palavras/documento-vocabularios-default`. Ele retornará um objeto como o abaixo

    {
        "documents": [
            {
              "document": 1,
              "text": "joao victor",
              "vocabulary": [
                "joao",
                "victor"
              ]
            }
        ]
    }

E para consumir o vocabulário agrupado de todos os documentos, você precisará fazer uma requisição do tipo `GET` no endpoint `/processador-palavras/documento-vocabularios-grupo`. Ele retornará um objeto como o abaixo

    {
      "documents": [
            {
                "document": 1,
                "text": "joao victor",
                "vocabulary": [
                    "joao victor"
                ]
            }
        ]
    }

