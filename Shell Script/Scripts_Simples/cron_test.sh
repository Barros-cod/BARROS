#!/bin/bash

log_file="/tmp/meu_log_cron.log"

echo "$(date): Script cron_test.sh foi executado!" >> "$log_file"
echo "Conteúdo de $log_file:" >> "$log_file"
cat "$log_file" >> "log_file"
echo "---" >> "$log_file"

# Digite crontab -e e pressione Enter.
# Agendamento para testar o cron (a cada 1 minuto)
# * * * * * /home/nome_diretorio/cron_test.sh > /dev/null 2>&1
