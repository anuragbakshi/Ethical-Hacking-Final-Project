#!/bin/bash

#Start exim4
service exim4 start

#Launch email spoofer program with email list and ip/domain name of website
java -jar SpoofEmail.jar CS378EH_EmailSpoofer/textfiles/email_list.txt 10.202.208.211

