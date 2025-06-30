#!/bin/bash

quantidade_arquivos=$(ls -l "$HOME/Documentos" | grep "^-" | wc -l)
echo "No diretório $HOME/Documentos, existem $quantidade_arquivos arquivo regulares."