#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURP='\033[0;35m'
BOLD='\033[1;1m'
END='\033[0m'

printf "${BOLD}${BLUE}Enter the YouTube Link for Audio Extraction:${END}\n"
read url
printf "${BOLD}${PURP}Enter Name for Output File: ${END}\n"
read name
printf "${GREEN}Downloading source...${END}\n"
youtube-dl $url --format 251 -o song.webm
clear
printf "${BLUE}${BOLD}Download Successful!${END}\n"
printf "${BOLD} Converting to MP3 ${END}\n" 
ffmpeg -i song.webm $name
clear
rm song.webm
printf "${BOLD}${RED}Playing %s\n${END}" $name
mpg123 $name

