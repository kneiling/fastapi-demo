#!/bin/sh

PRE_START_PATH=${PRE_START_PATH:-/src/app/scripts/prestart.sh}
if [ -f $PRE_START_PATH ] ; then
	echo "Running prestart script"
	. "$PRE_START_PATH"
else
	echo "Prestart script does not exist"
fi

exec uvicorn app.main:app --host ${HOST} --port ${PORT}
