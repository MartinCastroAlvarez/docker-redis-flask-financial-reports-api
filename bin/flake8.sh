#!/bin/bash
flake8\
    --max-line-length 120 \
    --max-complexity 17 \
	"app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Flake8 failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
