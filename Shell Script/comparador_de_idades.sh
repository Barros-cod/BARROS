#!/bin/bash

echo "=-=-=-=-=-=-=-=-=-=-="
echo "Comparador de Idades"
echo "=-=-=-=-=-=-=-=-=-=-="

read -p "Informe sua idade: " IDADE
read -p "Informe a outra idade: " IDADE1

if ! [[ "$NUMERO" =~ ^[0-9]+$ ]]; then
    echo "Erro: Por favor, digite um número inteiro válido."
    exit 1
fi

if [[ "$IDADE" -gt "$IDADE1" ]]; then
    echo "Você e mais velho."
elif [[ "$IDADE" -lt "$IDADE1" ]]; then
    echo "humm você e mais novo."
else 
    echo "Vocês tem a mesma idade."
fi