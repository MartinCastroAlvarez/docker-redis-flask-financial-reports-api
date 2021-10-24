#!/bin/bash
VARS="logger,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,id,blue,config,log,app,http_server,db,level,url,uri,pk"
DISABLED="no-member,import-error,no-name-in-module,no-self-use,no-value-for-parameter"
pylint \
    --jobs "2" \
    --output-format "colorized" \
    --reports "no" \
    --init-import "no" \
    --no-docstring-rgx "__.*__" \
    --max-args "8" \
    --max-locals "10" \
    --max-returns "2" \
    --max-statements "30" \
    --max-parents "5" \
    --max-attributes "7" \
    --max-public-methods "8" \
    --min-public-methods "0" \
    --deprecated-modules "regsub,TERMIOS,Bastion,rexec" \
    --ignore-comments "no" \
    --min-similarity-lines "30" \
    --max-line-length "100" \
    --max-module-lines "500" \
    --indent-string "    " \
    --good-names "${VARS}" \
    --fail-under 10 \
    --disable "${DISABLED}" \
	"app"
LAST_COMMAND_EXIT_CODE=$?
if [ ${LAST_COMMAND_EXIT_CODE} != 0 ]
then
    echo "PyLint failed."
    exit ${LAST_COMMAND_EXIT_CODE}
fi
