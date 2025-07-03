#!/bin/bash

echo "=+-/ Bem-vindo calculadora simples =+-/"

read numb0
read numb1

echo "Selecione qual opção: + - / *"
read -p " " seleciona

if [[ "$seleciona" = "+" ]]; then
    soma=$((numb0+numb1))
    echo "A soma de $numb0 e $num1 é: $soma"
elif [[ "$seleciona" = "-" ]]; then
    sub=$((numb0-numb1))
    echo "A subtração de $numb0 e $num1 é: $sub"
elif [[ "$seleciona" = "/" ]]; then
    div=$((numb0/numb1))
    echo "A divisão de $numb0 e $num1 é: $div"
elif [[ "$seleciona" = "*" ]]; then
    mult=$((numb0*numb1))
    echo "A multiplicação de $numb0 e $num1 é: $mult"
fi