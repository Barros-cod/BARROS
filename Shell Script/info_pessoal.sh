#!/bin/bash

# Este script exibe informações usando variáveis.
# Data de criação: 11 de Junho de 2025
# Autor: Barros

# --- Declação de Variáveis ---
NOME="Barros"
CIDADE="RJ"
DATA_ATUAL=$(date +%F)

# ---Comandos para exibir as informações ---
echo "Olá, $NOME"
echo "Sua cidade e : $CIDADE."
echo "Que bom ter você por aqui."
echo "Hoje é $DATA_ATUAL."
echo "-- Comandos básicos --"
df -h /home/$NOME 
ls -l /home/$NOME
ls -a /home/$NOME 
pwd /home/$NOME


clear #Limpado o terminal


