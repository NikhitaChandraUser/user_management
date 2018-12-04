#!/bin/bash

source: tsUtility_config.ini





source ${venv}/activate


echo "Python env activated"

python -m user_mgmt.ts_ug_util -h

deactivate

echo "python deactivated"
