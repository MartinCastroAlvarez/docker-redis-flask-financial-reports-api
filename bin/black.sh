#!/bin/bash
black \
    --target-version "py38" \
    --line-length 80 \
    --color \
    --safe \
	"app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Black failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
black \
    --target-version "py38" \
    --line-length 120 \
    --color \
    --safe \
	"tests"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Black failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
