#!/bin/zsh

while true; do
#  for directory in *YTS.LT* *YTS.MX*; do
for directory in *YTS.MX* *YTS.LT*; do
  echo "$directory"
  if [[ -n "$directory" ]]; then
    ~/process_torrent.sh "$directory"
  fi
  done
  sleep 300
done
