#!/bin/bash

if [ -d "$HOME/gimp-scripts" ]; then
    mv -f $HOME/gimp-scripts/*/*.py $HOME/.gimp-2.8/plug-ins/
    rm -rf $HOME/gimp-scripts
else
    echo "Diretŕio não encontrado"
fi
