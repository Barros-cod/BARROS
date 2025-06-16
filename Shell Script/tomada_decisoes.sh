#!/bin/bash

# Este script verifica o usuário atual e tambem a existência de um diretório.

#Verificando o usuário atual:
USUARIO_ATUAL=$(whoami)
#Verificando o diretorio atual:
DIRETORIO_HOME=$(pwd)

ARQUIVO_EXEMPLO="teste.txt"

echo "==================="
echo "INICIANDO VERIFICAÇÕES..."
echo ""

#Verificando o usuario:

if [ "$USUARIO_ATUAL" = "root" ]; then
    echo "Ateção! Você está logado como ROOT, Cuidado com o que faz!"
elif [ "$USUARIO_ATUAL" = "Barros" ]; then
    echo "Olá, $USUARIO_ATUAL! Seu usuário padrão está ativo."
else
    echo "Usuário desconhecido: $USUARIO_ATUAL."
fi

if [ -d "$DIRETORIO_HOME" ]; then
    echo "O diretorio '$DIRETORIO_HOME' existe."
    if [ -w "$DIRETORIO_HOME" ]; then
        echo "Você tem permissão de escrita neste diretório."
        touch "$DIRETORIO_HOME/$ARQUIVO_EXEMPLO"
        echo "Arquivo 'ARQUIVO_EXEMPLO' criado em '$DIRETORIO_HOME'."
    else
        echo "Você NÃO tem permissão de escrita neste diretorio."
    fi
else
    echo "Não existe...."
fi

echo "==================="
echo "Verificações concluidas."


