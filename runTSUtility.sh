#!/bin/bash

source tsUtility_config.ini


echo "STARTING TS UTILITY BASH"

type=$1

echo $venv

source /Users/rajesh.ravindran/environment/vpyenv27/bin/activate

echo "Python env activated"

echo $type

case ${type} in
    delete)
           cmd='python -m user_mgmt.ts_ug_util --ts_url ${url} --username ${username} --password ${password} delete -h'
        ;;

    get)
            cmd='python -m user_mgmt.ts_ug_util --ts_url ${url} --username ${username} --password ${password} get -h'
        ;;

    sync_excel )

        ;;
esac

${cmd}

deactivate

#echo "python deactivated"
