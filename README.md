#### Instruções para o crypt_file.py

`python3 crypt_file.py -c sdes -k <key> -e -i <inputfile> -o <outputfile>`
`python3 crypt_file.py -c sdes -k <key> -d -i <inputfile> -o <outputfile>`
`python3 crypt_file.py -c rc4  -k <key> -e -i <inputfile> -o <outputfile>`
`python3 crypt_file.py -c rc4  -k <key> -d -i <inputfile> -o <outputfile>`


#### Instruções para o chat

Primeiramente é necessário iniciar o servidor (pode ser feito por um dos interessados do par em conversar):

`python3 server.py`

Em seguida, os usuários que desejam conversar entre si podem se conectar ao servidor executando:

`python3 client.py`

E então seguir as instruções para informar o endereço do servidor (rodando na porta 5354 como definido) e seu nome.
 
Após isso os usuários já podem se comunicar entre si usando a
criptografia padrão, que é a cifra RC4 e a chave 'segredo'.

Mas também é possível alterá-la enviando no chat o comando:

`/crypt [sdes | rc4] key`

Exemplos:

`/crypt sdes 10101010`
`/crypt rc4 novachave`

