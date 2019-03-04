#!/bin/sh

CMDNAME=`basename $0`
SEQUENCE='test'

usage() {
  echo "Usage: $CMDNAME [-s lint|create|check|converge|destroy]" 1>&2
  exit 1
}

while getopts s:h OPT
do
  case $OPT in
    s ) SEQUENCE=$OPTARG ;;
    h ) usage ;;
    ? ) usage ;;
    * ) usage ;;
  esac
done

docker-compose run runner bash -lc "molecule $SEQUENCE"
docker-compose down
exit 0

# gitlab-runner exec docker --docker-volumes /var/run/docker.sock:/var/run/docker.sock ansible_build
