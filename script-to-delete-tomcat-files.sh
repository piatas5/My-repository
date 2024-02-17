#!/bin/bash


echo "Welcome in the app! Here you can clear all tomcat files at once!"
echo

for directory in "/tmp/tomcat*";
do
rm -f $directory
done
