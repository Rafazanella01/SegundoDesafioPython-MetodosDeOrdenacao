class geraGrafico:

    def geraGrafico(self, descricaoAlgoritmos, listaTempoExecucao):

        import matplotlib.pyplot as plt

        # Criando o gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(descricaoAlgoritmos, listaTempoExecucao, color='purple')
        plt.xlabel('Algoritmo de Ordenação')
        plt.xlabel('')
        plt.ylabel('Tempo de Execução (segundos)')
        plt.title('Tempo de Execução dos Algoritmos de Ordenação')
        #plt.xticks(rotation=45, ha='right')

        # Exibindo o gráfico
        plt.tight_layout()
        plt.show()