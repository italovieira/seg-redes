# para encriptar
openssl enc -aes-128-ecb -in lock.bmp
# para copiar o cabeçalho para o arquivo encriptado
dd bs=54 count=1 conv=notrunc if=lock.bmp of=lock-ecb.bmp
