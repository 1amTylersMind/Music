#!/bin/bash
cd $1
find -name '*.mp3' | while read song; do mpg123 $song; done
#EOF
