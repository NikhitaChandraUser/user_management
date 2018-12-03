#!/bin/bash

. tsUtility_config.ini
source ${venv}/activate

echo "Python env activated"

echo ${tsadmin}
echo ${tspassword}

deactivate

echo "python deactivated"
