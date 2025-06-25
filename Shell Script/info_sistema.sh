#!/bin/bash

while true; do
    echo "===============  Informações sobre o sistema  ===================" > log_sistema.txt
    uname -a >> log_sistema.txt
    echo "=============== Data e hora atuais ===================" >> log_sistema.txt
    timedatectl >> log_sistema.txt
    echo "=============== Diretório pessoal ===================" >> log_sistema.txt
    ls -l $HOME >> log_sistema.txt
    echo "=================== Partição raiz ===================" >> log_sistema.txt
    df -h / >> log_sistema.txt
    echo ""
    echo "Precione CTRL + C para sair"
    sleep 1
    clear
    cat log_sistema.txt
done