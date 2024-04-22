#!/bin/bash

port=8000

if [ "$1" ]; then
    port=$1
fi

echo "Starte HTTP-Server auf Port $port"
python3 -m http.server $port
