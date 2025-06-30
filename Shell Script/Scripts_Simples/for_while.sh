#!/bin/bash

# echo "Listando e compactando arquivos de texto na pasta atual::"
# for ARQUIVO in *.txt; do
#     if [ -f "$ARQUIVO" ]; then
#         echo "Processando arquivo: $ARQUIVO"
#         gzip "$ARQUIVO"
#     fi
# done
# echo "Compactação de arquivos .txt concluída!"

# echo "Contagem regressiva:"
# for (( I = 5; I >= 0; I-- )); do
#     echo "Contando: $I"
#     sleep 1
# done
# echo "Finalizado"

# CONTADOR=1
# echo "Contando de 1 a 5:"

# while [ "$CONTADOR" -le 5 ]; do
#     echo "Número: $CONTADOR"
#     CONTADOR=$((CONTADOR + 1))
#     sleep 0.5
# done
# echo "Contagem concluida!"

# echo "Monitorado a cada 5 segundos. Pressione Ctrl+C para sair."
# while true; do
#     echo "-----------------------------------"
#     echo "Uso atual de memória:"
#     free -h | grep "Mem:" # Mostra uso da RAM
#     sleep 5
#     echo "-----------------------------------"
# done

