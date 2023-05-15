#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

working_dir="$(dirname ${0})"

source "${working_dir}/_sourced/constants.sh"
source "${working_dir}/_sourced/messages.sh"

message_welcome "These are the backups you have got:"

ls -lht "${BACKUP_DIR_PATH}"