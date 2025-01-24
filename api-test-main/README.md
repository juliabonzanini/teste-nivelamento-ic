# Teste API - Busca de Operadoras

## Descrição
Este projeto consiste em uma interface web desenvolvida com Vue.js que interage com um servidor Python utilizando FastAPI. Ele realiza buscas textuais na lista de cadastros de operadoras a partir de um arquivo CSV fornecido, retornando os registros mais relevantes. O projeto também inclui uma coleção no Postman para demonstrar os resultados.

### Funcionalidades
- Busca textual na lista de cadastros de operadoras.
- Retorno dos registros mais relevantes baseados na consulta.
- Interface intuitiva para o usuário realizar buscas.
- Backend utilizando FastAPI.

## Pré-requisitos
Certifique-se de que você tem instalado:
- [Node.js](https://nodejs.org)
- [Python](https://www.python.org/)
- [Postman](https://www.postman.com/)

## Setup do Projeto

### Instalação
```bash
npm install
```

### Executar em modo de desenvolvimento
```bash
npm run serve
```

### Compilar e minimizar para produção
```bash
npm run build
```

### Analisar e corrigir arquivos
```bash
npm run lint
```

### Configuração personalizada
Veja [Configuration Reference](https://cli.vuejs.org/config/).

---

## Backend (FastAPI)

### Endereço do servidor
O servidor está configurado para rodar no endereço:
```
http://127.0.0.1:8083
```

### Endpoint de busca
- **URL**: `/search`
- **Método**: GET
- **Parâmetro**: `query` (string)
- **Descrição**: Retorna os registros de operadoras que correspondem à consulta.

Exemplo de requisição:
```bash
curl "http://127.0.0.1:8083/search?query=termo"
```

---

## Frontend (Vue.js)

A interface web permite:

1. Inserir um termo de busca em um campo de texto.
2. Visualizar os resultados da busca com os dados das operadoras.
3. Exibir mensagens de carregamento ou resultados não encontrados.

### Como executar
Após instalar as dependências com `npm install`, inicie o servidor de desenvolvimento:
```bash
npm run serve
```

---

## Demonstração no Postman

Inclua a coleção fornecida no Postman para testar o endpoint `/search`. A coleção demonstra como realizar consultas e interpretar os resultados.

## Contato
- E-mail: juliavbonzanini@gmail.com