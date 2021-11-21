#! /bin/sh

if [ $# -lt 2 ]
then
echo "Required arguments not provided correctly!"
echo "Enter date and time in yyyy-mm-dd hh:mm:ss format"
exit 1
fi

setdate=$1
settime=$2

date --set=""$setdate" "$settime""