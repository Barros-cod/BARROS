#!/bin/bash

echo "====================="
echo "Digite um caminho:  (ex: /home/barros/Documentos ou /etc/passwd)"
read -p "" CAMINHO
echo "====================="

if [ ! -e "$CAMINHO" ]; then 
    echo "O caminho '$CAMINHO' NÃO foi encontrado."
elif [ -f "$CAMINHO" ]; then 
    echo "O caminho '$CAMINHO' é um ARQUIVO."
elif [ -d "$CAMINHO" ]; then
    echo "O caminho '$CAMINHO' é um DIRETÓRIO."
else 
    echo "O caminho '$CAMINHO' existe, mas não é um arquivo regular nem um diretório (pode ser um tipo especial)."
fi

echo "====================="
