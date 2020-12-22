#!/usr/bin/env bash

rm ./lambda_deployment_package.zip
cd venv/lib/python3.8/site-packages
zip -r ../../../../lambda_deployment_package.zip . -x boto\*
cd ../../../../
zip -gr lambda_deployment_package.zip * -x venv/\* tests/\*
