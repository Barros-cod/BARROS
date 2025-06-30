#!/bin/bash

read -p "Digite um número: " NUMERO

if ! [[ "$NUMERO" =~ ^[0-9]+$ ]]; then
    echo "Erro: Por favor, digite um número inteiro válido."
    exit 1
fi

if (( NUMERO % 2 == 0 )); then
    echo "O $NUMERO e Par"
else
    echo "O $NUMERO e Ímpar"
fi

