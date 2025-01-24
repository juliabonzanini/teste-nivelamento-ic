from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel, Field
import pandas as pd
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Criação da aplicação FastAPI
app = FastAPI()

# Configuração do middleware CORS para permitir comunicação com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os metodos HTTP
    allow_headers=["*"],  # Permite todos os headers
)

# Função assincrona para carregar dados de um arquivo CSV
async def load_data():
    try:
        csv_path = "Relatorio_cadop.csv"
        if not os.path.exists(csv_path):
            logger.error(f"Arquivo CSV não encontrado: {csv_path}")
            raise HTTPException(status_code=500, detail="Arquivo de dados não encontrado.")

        # Carrega o arquivo CSV e preenche valores nulos com strings vazias
        df = pd.read_csv('Relatorio_cadop.csv', delimiter=';', dtype=str)
        df = df.fillna('')
        return df
    except Exception as e:
        # Registra o erro e retorna uma exceção HTTP 500 em caso de falha
        logger.error(f"Erro ao carregar o CSV: {e}")
        raise HTTPException(status_code=500, detail="Erro ao carregar os dados.")

# Modelo de dados para representar informações de uma operadora
class Operadora(BaseModel):
    registro_ans: str = Field(..., alias="Registro_ANS")
    cnpj: str = Field(..., alias="CNPJ")
    razao_social: str = Field(..., alias="Razao_Social")
    nome_fantasia: Optional[str] = Field(None, alias="Nome_Fantasia")
    modalidade: Optional[str] = Field(None, alias="Modalidade")
    logradouro: Optional[str] = Field(None, alias="Logradouro")
    numero: Optional[str] = Field(None, alias="Numero")
    complemento: Optional[str] = Field(None, alias="Complemento")
    bairro: Optional[str] = Field(None, alias="Bairro")
    cidade: Optional[str] = Field(None, alias="Cidade")
    uf: Optional[str] = Field(None, alias="UF")
    cep: Optional[str] = Field(None, alias="CEP")
    ddd: Optional[str] = Field(None, alias="DDD")
    telefone: Optional[str] = Field(None, alias="Telefone")
    fax: Optional[str] = Field(None, alias="Fax")
    endereco_eletronico: Optional[str] = Field(None, alias="Endereco_eletronico")
    representante: Optional[str] = Field(None, alias="Representante")
    cargo_representante: Optional[str] = Field(None, alias="Cargo_Representante")
    regiao_de_comercializacao: Optional[str] = Field(None, alias="Regiao_de_Comercializacao")
    data_registro_ans: Optional[str] = Field(None, alias="Data_Registro_ANS")

# Modelo para representar a resposta do endpoint de busca
class SearchResponse(BaseModel):
    total_results: int
    results: List[Operadora]

# Endpoint para buscar registros de operadoras com base em uma query
@app.get("/search", response_model=SearchResponse)
async def search(query: str):
    """
    Endpoint para buscar registros de operadoras com base em uma query.

    Parâmetros:
    - query: string com o texto a ser buscado nos registros.

    Retorna:
    - Lista de dicionários com os registros que correspondem à query.
    """

    df = await load_data() # Carrega os dados do CSV

    # Log da query recebida
    logger.info(f"Query recebida: {query}")

    # Validação da query para evitar consultas vazias
    if not query.strip():
        logger.warning("Query vazia, retornando lista vazia.")
        raise HTTPException(status_code=400, detail="A query não pode estar vazia.")

    try:
        # Filtra os registros contendo a query em qualquer campo
        results = df[df.apply(lambda row: row.fillna('').astype(str).str.contains(query, case=False).any(), axis=1)]
        logger.info(f"Número de resultados encontrados: {len(results)}")

        # Define as colunas a serem incluidas na resposta
        fields_to_return = [
            'Registro_ANS', 'CNPJ', 'Razao_Social', 'Nome_Fantasia',
            'Logradouro', 'Numero', 'Bairro', 'Cidade',
            'UF', 'Telefone', 'Endereco_eletronico'
        ]

        # Verifica se todas as colunas necessárias estão presentes no DataFrame
        missing_fields = [field for field in fields_to_return if field not in results.columns]
        if missing_fields:
            # Preenche automaticamente os campos faltantes com valores padrão
            for field in missing_fields:
                results[field] = ""  # Adiciona a coluna com valores vazios
            logger.warning(f"Campos ausentes detectados e corrigidos: {missing_fields}")

        # Filtra o DataFrame para incluir apenas as colunas necessárias
        filtered_results = results[fields_to_return]

        # Converte os resultados filtrados em uma lista de dicionários para serem enviados como resposta no formato JSON
        return SearchResponse(total_results=len(filtered_results), results=filtered_results.to_dict(orient="records"))

    except HTTPException as http_exc:
        # Em caso de exceção HTTP, loga o erro e relança a exceção
        logger.error(f"Erro HTTP: {http_exc.detail}")
        raise http_exc

    except Exception as e:
        # Captura qualquer outro erro inesperado, loga o erro e retorna uma exceção HTTP generica
        logger.exception("Erro inesperado ao processar a busca.")
        raise HTTPException(status_code=500, detail="Erro interno no servidor. Tente novamente mais tarde.")

if __name__ == '__main__':
    import uvicorn

    # Inicia o servidor FastAPI usando Uvicorn.
    uvicorn.run("main:app", host="127.0.0.1", port=8083, reload=True, log_level="debug")
