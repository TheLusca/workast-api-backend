# Instruções para instalação da API

## Criar ambiente virtual python
### É necessário ter o Python verões 3.+ e o PIP3.+ instalado

digitar no terminal:
> python3 -m venv .venv

## Acessar o ambiente virtual
> source .venv/bin/activate

## Desativar ambiente virtual 

> deactivate 

## instalar as bibliotecas

no terminal:
> pip3 install -r requirements.txt 

# Instruções para buildar a imagem MySQL

## buildar a imagem
> sudo docker build -t lucast-db .

## executar container 
> sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=lucast -e MYSQL_USER=userlucast -e MYSQL_PASSWORD=MainPassword lucast-db

## Acessar base de dados

> docker exec -it <id-do-container-criado>  mysql -uroot -p
