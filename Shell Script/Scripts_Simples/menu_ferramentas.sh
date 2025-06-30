#!/bin/bash

while true; do
    clear
    echo "=================================="
    echo "1. Listar arquivos (ls -l)       ="  
    echo "2. Mostrar uso de disco (/)      ="
    echo "3. Verificar meu IP (ip a)       ="
    echo "== Pressione Ctrl+C para sair.   ="
    echo "=================================="

    read -p "Digite sua opção (1 - 3): " OPCAO

    case "$OPCAO" in
        1)
            echo "Opção 1 selecionada: Listando arquivos no diretório atual..."
            ls -l
            ;;
        2)
            echo "Opção 2 selecionada: Mostrando uso de disco da raiz..."
            df -h /
            ;;
        3)
            echo "Opção 3 selecionada: Verificando seu endereço IP..."
            ip a | grep inet | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1
            ;;
        *) 
            echo "Opção inválida: $OPCAO. Por favor, digite um número entre 1 e 3."
            ;;
    esac
    sleep 2
done
echo "=================================="
echo "Fim do script."