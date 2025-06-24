#!/bin/bash

read -p "Digite um número: " NUMERO
COMECA=0

# Verifica se a entrada é um número inteiro 
if ! [[ "$NUMERO" =~  ^[0-9]+$ ]]; then
    echo "Erro: Por favor, digite um número inteiro válido."
    exit 1
fi
 
while [ "$NUMERO" -ge "$COMECA" ]; do
    echo "-----------------"
    echo "Número: $COMECA"
    COMECA=$((COMECA + 1))
    sleep 1
done