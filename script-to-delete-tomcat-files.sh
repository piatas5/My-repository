#!/bin/bash

echo "Welcome in the app! Here you can clear all tomcat files at once!"
echo

DIRECTORY=/home/luke/Tomcat_Directories

DIRCOUNT=`find $DIRECTORY -maxdepth 1 -mindepth 1 -type d -name "tomcat*" | wc -l`

echo "Number of tomcat directories: $DIRCOUNT"
echo "Do you want to delete them all? [y/n]"

read answer

if [ $answer == "y" ] || [ $answer == "Y" ]
then
	for dir in "/home/luke/Tomcat_Directories/tomcat*";
	do
	rm -r -f $dir
	done
if [ $DIRCOUNT == 0 ]
then
echo "No directories to delete!"
else
echo "Directories deleted successfully!"
fi

elif [ $answer == "n" ] || [ $answer == "N" ]
then
echo "Bye!"
exit 0
fi
