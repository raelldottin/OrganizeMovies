#!/bin/zsh

while true; do
  if ls *YTS.MX* > /dev/null 2>&1; then
    for directory in *YTS.MX*; do
      echo "$directory"
      if [[ -n "$directory" ]]; then
        ~/process_torrent.sh "$directory"
      fi
    done
    sleep 300
  elif ls *YTS.LT* > /dev/null 2>&1; then
    for directory in *YTS.LT*; do
      echo "$directory"
      if [[ -n "$directory" ]]; then
        ~/process_torrent.sh "$directory"
      fi
    done
    sleep 300
  fi
done
