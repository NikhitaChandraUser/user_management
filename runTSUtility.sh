#!/bin/bash

source: tsUtility_config.ini


echo "STARTING TS UTILITY BASH"


case ${type} in
    delete)
            python -m user_mgmt.ts_ug_util --ts_url ${url} --username ${username} --password {}
        ;;

    get)

        ;;

    sync_excel )

        ;;
esac


source ${venv}/activate


echo "Python env activated"

python -m user_mgmt.ts_ug_util -h

deactivate

echo "python deactivated"
