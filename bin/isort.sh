#!/bin/bash
isort "app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Python3 isort failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
isort "tests"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Python3 isort failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
