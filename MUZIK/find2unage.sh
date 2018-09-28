#!/bin/bash
RED='\033[0;31m' 
GREEN='\033[0;32m'
BLUE='\033[0;34'
PURP='\033[0;35'
BOLD='\033[1;1m'
NCEND='\033[0m' # No Color /End
let I=1
cd /
printf "${RED}${BOLD}SEARCHING FOR ALL MUSIC${NCEND}\n"
find -name '*.mp3' | while read song; do
    printf "%d - ${BOLD}Found:${NCEND}${GREEN}${BOLD}' %s '${NCEND}\n" "$I" "$song"
    I=$((I+1))
    sleep 0.2
done;
#EOF
