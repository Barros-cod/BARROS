#!/bin/bash

ls /diretorio_que_nao_existe 2> /dev/null
echo "Tentativa de listar diretório inexistente concluída (erros foram silenciados)."
ls