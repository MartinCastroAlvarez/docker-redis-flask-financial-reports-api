#!/bin/bash
mypy "app" \
    --ignore-missing-imports
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "MyPy failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
