class geraGrafico:

    def geraGrafico(self, descricaoAlgoritmos, listaTempoExecucao):

        import matplotlib.pyplot as plt
        from matplotlib.ticker import ScalarFormatter

        # Criando o gráfico de barras
        plt.figure(figsize=(12, 6))
        plt.bar(descricaoAlgoritmos, listaTempoExecucao, color='purple')
        plt.xlabel('Algoritmo de Ordenação')
        plt.xlabel('')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.title('Tempo de Execução dos Algoritmos de Ordenação')

        # Ajustando a escala do eixo y para garantir que todos os tempos de execução sejam visíveis
        plt.yscale('log')  # Usando escala logarítmica no eixo y

        plt.savefig('grafico_tempo_execucao.png', bbox_inches='tight')  # bbox_inches='tight' para garantir que nada seja cortado

        # Exibindo o gráfico
        plt.tight_layout()
        plt.show()