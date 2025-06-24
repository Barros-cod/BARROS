#!/bin/bash

ARQUIVO="backup_dia"
BACKUP_DIR="$HOME/Documentos/$ARQUIVO"
FILES=("doc1.txt" "relatorio.pdf" "foto.jpg")

# Cria o diretório de backup se não existir
if [ -d "$BACKUP_DIR" ]; then
    echo "O diretório $BACKUP_DIR já existe."
else
    echo "Criando o diretório de backup em $BACKUP_DIR..."
    mkdir -p "$BACKUP_DIR"
    echo "Diretório criado com sucesso!"
fi

# Cria arquivos de exemplo se não existirem
cd "$HOME/Documentos"
for file in "${FILES[@]}"; do
    if [ ! -e "$file" ]; then
        echo "Criando arquivo de exemplo: $file"
        touch "$file"
    fi
done

# Faz backup dos arquivos
for file in "${FILES[@]}"; do
    if [ -e "$file" ]; then
        echo "Copiando $file para $BACKUP_DIR"
        cp "$file" "$BACKUP_DIR/"
    else
        echo "Arquivo $file não encontrado, pulando..."
    fi
done

echo "Backup concluído!"