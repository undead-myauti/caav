# Financeiro Turbinado

Este projeto é um trabalho acadêmico para a disciplina Construção de Aplicações em Ambientes Virtuais (CAAV), ministrada pelo docente Diogo Olsen.

### Como rodar o projeto?

Para começarmos, vamos utilizar o Docker para subir nosso banco de dados sem instalá-lo diretamente em nossa máquina. Caso você ainda não tenha configurado, siga o tutorial de instalação no [*site oficial*](https://docs.docker.com/desktop/setup/install/linux/)

Assim que estiver com o Docker configurado (Estamos considerando o Docker Engine e o Docker Compose), podemos começar a subir o projeto!

 * Clone o repositório
    > `git clone https://github.com/undead-myauti/caav.git`
 * Entre na pasta do repositório
    > `cd caav`
 * Suba o container do banco
    > `docker compose up -d`
 * Instale as dependencias do projeto
    > `pip install -r requirements.txt`
 * Agora devemos aplicar as migrations no nosso banco
    > `alembic upgrade head`
 * Com as migrations aplicadas, podemos enfim rodar o projeto com
    > `python main.py`

Com isso, a aplicação deve aparecer em uma janela, pronta para uso!