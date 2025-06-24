#!/bin/bash

echo "========================================="
echo "  GERENCIADOR SIMPLES DE ARQUIVOS/PASTAS "
echo "========================================="
echo "Escolha uma opção:"
echo "1 - Criar um novo arquivo"
echo "2 - Criar um novo diretório"
echo "3 - Apagar arquivo ou diretorio"
echo "4 - Listar conteúdo da pasta atual"
echo "0 - Sair do programa."
echo "========================================="

read -p "Digite o número da sua escolha (1-4): " OPCAO

case "$OPCAO" in
    0)
        echo "Saindo do gerenciador. Até mais!"
        exit 0
        ;;
    1)
        read -p "Qual o nome do arquivo a ser criado? " NOME_ARQUIVO
        touch "$NOME_ARQUIVO"
        echo "Arquivo '$NOME_ARQUIVO' criado com sucesso!"
        ;;
    2)
        read -p "Qual o nome do diretório a ser criado? " NOME_DIRETORIO
        mkdir "$NOME_DIRETORIO"
        echo "Diretório '$NOME_DIRETORIO' criado com sucesso!"
        ;;
    3)
        echo "Escolha os arquivo para remover:"
        ls 
        read -p "Escreva nome do arquivo ou diretorio (Ex: test1.txt test2.txt):" APAGAR_DIRC_ARQ
        rm -r "$APAGAR_DIRC_ARQ"
        echo "Arquivos apagado com sucesso."
        ;;
    4)
        echo "Conteúdo da pasta atual:"
        ls -l
        ;;
    *)
        echo "Opção inválida! Por favor, digite um número entre 1 e 4."
        ;;
esac