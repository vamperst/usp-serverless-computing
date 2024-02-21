#!/bin/bash


wget -c https://github.com/rebuy-de/aws-nuke/releases/download/v2.25.0/aws-nuke-v2.25.0-linux-amd64.tar.gz

tar -xvf aws-nuke-v2.25.0-linux-amd64.tar.gz

mv aws-nuke-v2.25.0-linux-amd64 aws-nuke

sudo mv aws-nuke /usr/local/bin/aws-nuke

aws-nuke -h

alias=`tr -dc A-Za </dev/urandom | tr '[:upper:]' '[:lower:]' | head -c 13; echo`
accountID=`aws sts get-caller-identity --query Account --output text`
aws iam create-account-alias --account-alias $alias

sed -i "s/<IDCONTA>/$accountID/" nuke-config.yml



