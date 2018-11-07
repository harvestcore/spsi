openssl enc -aes-128-ecb -k password -in a1024.bin -out a1024_ecb.bin -nosalt
openssl enc -aes-128-ecb -k password -in b1024.bin -out b1024_ecb.bin -nosalt
openssl enc -aes-128-ecb -k password -in a1024.bin -out a1024_cbc.bin -nosalt
openssl enc -aes-128-ecb -k password -in b1024.bin -out b1024_cbc.bin -nosalt
openssl enc -aes-128-ecb -k password -in a1024.bin -out a1024_ofb.bin -nosalt
openssl enc -aes-128-ecb -k password -in b1024.bin -out b1024_ofb.bin -nosalt
