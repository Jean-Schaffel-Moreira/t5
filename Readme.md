
TRABALHO REFERENTE DISCIPLINA DE SISTEMAS DISTRIBUÍDOS 2022/1

INSTALAÇÃO DOS PROGRAMAS UTILIZADOS:
Caso dê erro na loja, sudo apt-get update pode ajudar
Neste trabalho não foi usado o mosquitto em docker ou vm, pois tivemos problemas
utilizando ambos (sh*t happens)

Mosquitto:
	sudo apt install mosquitto
	sudo apt install mosquitto-clients

Python 3:
Normalmente python já vem instalado no linux, para verificar se é a versão correta
(3): python -V 
	sudo apt install python3

Para instalar o gerenciador de bibliotecas python
	sudo apt install python3-pip

Para instalar os pacotes utilizados:
	pip3 install paho-mqtt python-etcd pymongo

Criar o espaço padrão para o mongodb
	mkdir ./data && mkdir ./data/db

Para rodar o Mosquitto:
	mosquitto
Caso dê problema de endereço, trocar a porta, passando o parâmetro -p
(porta padrão é a 1883), o comando netstat -tulpn mostra se está sendo utilizada


Para rodar o mongodb:
	mongod --dbpath /home/NOME/data/db
Novamente, caso dê problema de endereço, trocar a porta passando o parâmetro -port
(porta padrão é a 27017)

Rodar o publisher.sh, o sub.py e o get.py
Lembrar de trocar o usuário e as portas utilizadas nos arquivos (foram utilizadas
portas diferentes da padrão, por motivo de erro)
