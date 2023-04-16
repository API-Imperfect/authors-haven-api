#!/bin/bash

set -o errexit
set -o nounset

exec watchfiles celery.__main__.main --args '-A authors_api.celery worker -l INFO'