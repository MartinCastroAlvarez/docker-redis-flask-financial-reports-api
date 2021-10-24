#!/bin/bash
black \
    --target-version "py38" \
    --line-length 70 \
    --color \
    --safe \
	"app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    error "Black failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
