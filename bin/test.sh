#!/bin/bash
nosetests \
    --cover-min-percentage 99 \
    --cover-erase \
    --cover-tests \
    --with-coverage \
    --cover-package "app" \
    "tests"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "Tests failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
