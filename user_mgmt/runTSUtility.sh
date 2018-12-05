#!/bin/bash

source tsUtility_config.ini


#echo "STARTING TS UTILITY BASH"

type=$1

echo $venv

#alias activate="/Users/nikhita.chandra/venv/bin/activate"
#source activate

# install packages from the requirements.txt file

#pip install -r requirements.txt -f .


#echo "Python env activated"

echo "====================================================================================================================="
echo "User Group parser arguments"
echo "====================================================================================================================="
cmd='python -m ts_ug_util -h'
${cmd}

echo $type

case ${type} in
    delete)
           echo "====================================================================================================================="
           echo "Delete sub-parser arguments"
           echo "====================================================================================================================="
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' delete -h'
           ${cmd}
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' delete --users '"$users"''
           ${cmd}
        ;;

    get)
           echo "====================================================================================================================="
           echo "Get sub-parser arguments"
           echo "====================================================================================================================="
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' get -h'
           ${cmd}
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' get --output_type '"$output_type"' --filename '"$filename"''
           ${cmd}
        ;;

    sync_excel)
           echo "====================================================================================================================="
           echo "Sync excel sub-parser arguments"
           echo "====================================================================================================================="
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' sync_excel -h'
           ${cmd}
           cmd='python -m ts_ug_util --ts_url '"$url"' --username '"$username"' --password '"$password"' sync_excel --filename '"$filename"''

           # TO DO
           #if [ "$purge" = "yes" ]; then
           #    cmd = "$cmd' --purge'"
           #fi

           ${cmd}
        ;;

    validate_json)
           echo "====================================================================================================================="
           echo "Validate Json sub-parser arguments"
           echo "====================================================================================================================="
           cmd='python -m ts_ug_util validate_json -h'
           ${cmd}
           cmd='python -m ts_ug_util validate_json --filename '"$json_filename"''
           ${cmd}
        ;;
esac

${cmd}

#deactivate

#echo "python deactivated"
