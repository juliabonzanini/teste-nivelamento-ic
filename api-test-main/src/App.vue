<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>

    <!-- Container de busca -->
    <div class="search-container">

      <!-- Campo de input para inserir a query -->
      <input
        v-model="query"
        @keydown.enter="search"
        :disabled="loading"
        :placeholder="loading ? 'Buscando...' : 'Buscar operadora'"
        class="search-input"
      />

      <!-- Botao de busca -->
      <button @click="search" :disabled="loading" class="search-button">
        {{ loading ? 'Buscando...' : 'Buscar' }}
      </button>
    </div>

    <!-- Mensagem de carregamento -->
    <div v-if="loading" class="loading-message">Carregando...</div>

    <!-- Exibe resultados se houverem -->
    <ul v-else-if="results.length > 0" class="results-list">
      <li v-for="item in results" :key="item.Registro_ANS" class="result-item">
        <strong>{{ item.Razao_Social || 'Sem Razão Social' }}</strong> -
        {{ item.Nome_Fantasia || 'Sem Nome Fantasia' }}<br />
        CNPJ: {{ item.CNPJ || 'Sem CNPJ' }}<br />
        {{ item.Logradouro || 'Sem Logradouro' }}, {{ item.Numero || 'Sem Número' }} -
        {{ item.Bairro || 'Sem Bairro' }}<br />
        {{ item.Cidade || 'Sem Cidade' }} / {{ item.UF || 'Sem UF' }}<br />
        Telefone: {{ item.Telefone || 'Sem Telefone' }} -
        E-mail: {{ item.Endereco_eletronico || 'Sem E-mail' }}
      </li>
    </ul>

    <!-- Caso não haja resultados -->
    <div v-else class="no-results-message">
      Nenhuma operadora encontrada.
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',  // Armazena o termo de busca inserido pelo usuário
      results: [],  // Armazena os resultados da busca
      loading: false  // Indica se a busca está em andamento
    };
  },
  methods: {
    // Função para buscar as operadoras baseado na query
    async search() {
      // Verifica se a query está vazia
      if (this.query.trim() === '') {
        alert("Por favor, insira um termo de busca.");
        return;
      }

      this.loading = true;  // Inicia o processo de busca
      this.results = [];  // Limpa resultados anteriores

      try {
        // Faz a requisição para a API com a query
        const response = await fetch(`http://127.0.0.1:8083/search?query=${this.query}`);
        const data = await response.json();  // Converte a resposta para JSON

        // Verifica se ha resultados
        if (data.total_results > 0) {
          this.results = data.results;  // Armazena os resultados
        } else {
          alert("Nenhuma operadora encontrada.");
        }
      } catch (error) {
        console.error("Erro ao buscar operadora:", error);
        alert("Erro ao buscar operadora. Tente novamente.");  // Alerta caso ocorra um erro
      } finally {
        this.loading = false;  // Finaliza o carregamento
      }
    }
  }
};

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;  /* Fonte */
  -webkit-font-smoothing: antialiased;  /* Suaviza a fonte no Chrome */
  -moz-osx-font-smoothing: grayscale;  /* Suaviza a fonte no Firefox */
  text-align: center;  /* Centraliza o conteudo */
  margin-top: 20px;  /* Margem no topo */
}

.search-container {
  display: flex;  /* Layout flexivel */
  justify-content: center;  /* Alinha ao centro */
  gap: 10px;  /* Espaçamento entre os itens */
  margin-bottom: 20px;  /* Margem inferior */
}

.search-input {
  width: 300px;  /* Largura do input */
  padding: 10px;  /* Espaçamento interno */
  border: 1px solid #ccc;  /* Borda */
  border-radius: 4px;  /* Bordas arredondadas */
}

.search-button {
  padding: 10px 15px;  /* Padding do botão */
  background-color: #007BFF;  /* Cor de fundo */
  color: white;  /* Cor do texto */
  border: none;  /* Sem borda */
  border-radius: 4px;  /* Bordas arredondadas */
  cursor: pointer;  /* Cursor de clique */
}

.search-button:disabled {
  background-color: #ccc;  /* Cor quando desabilitado */
  cursor: not-allowed;  /* Cursor de não permitido */
}

.results-list {
  list-style-type: none;  /* Remove os marcadores */
  padding: 0;  /* Remove o padding */
}

.result-item {
  text-align: left;  /* Alinha o texto a esquerda */
  margin: 10px auto;  /* Margem automática */
  padding: 10px;  /* Padding interno */
  border: 1px solid #ccc;  /* Borda */
  border-radius: 4px;  /* Bordas arredondadas */
  max-width: 500px;  /* Largura máxima */
  background-color: #f9f9f9;  /* Cor de fundo */
}

.no-results-message, .loading-message {
  font-size: 1.2em;  /* Tamanho da fonte */
  color: #555;  /* Cor do texto */
}
</style>
