#!/bin/bash

echo "====================="
echo " Verificando servido apache2... "
sleep 2

STATUS_TEXT=$(systemctl is-active apache2)
systemctl is-active apache2 > /dev/null 2>&1
STATUS_CODE=$?

if [ "$STATUS_CODE" -eq 0 ]; then 
    echo "Status: O serviço Apache2 está ATIVO e rodando."
elif [ "$STATUS_CODE" -eq 3 ]; then
    echo "Status: O serviço Apache2 está INATIVO ou não encontrado."
else
    echo "Status: O serviço Apache2 está em um estado desconhecido ($STATUS_TEXT)."
fi

echo "====================="

