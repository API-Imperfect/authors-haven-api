#!/usr/bin/env bash

countdown(){

  declare desc="A simple countdown."

  local seconds="${1}"

  local d=$(($(date +%s) + "${seconds}"))

  while [ "$d" -ge `date +%s` ]; do
  
    echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r";

    sleep 0.1
  done

}