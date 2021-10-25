#!/bin/bash
mypy \
    --ignore-missing-imports \
	"app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "MyPy failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
mypy \
    --ignore-missing-imports \
	"tests"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "MyPy failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
