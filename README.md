#  Repositório dedicado ao trabalho final da disciplina de Sistemas ditribuídos referente ao semestre 2023.1

![Logo Helport](/Materiais/Logo_Helport.png)

## Microserviços Implementados:

* API Chat GPT

* API TelegramBOT

* Banco de dados Sqlite

### Foto da modelagem dos microserviços:

![Modelagem microserviços](/Materiais/fotoModelagem.png)

## Como rodar o  ChatBot:

### pré requisitos:
* Ter o docker instalado na máquina;
    * Link de como instalar o docker: 
        * [Para Linux](https://www.digitalocean.com/community/tutorial_collections/how-to-install-and-use-docker)
        * [Para Windowns](https://docs.docker.com/desktop/install/windows-install/r)
* Substituir o token open ai no arquivo openai_api.py;
* Substituir o token do bot do telegram no arquivo telegram_bot.py.

### configurando o docker:

1. Navegue até o diretório que contém o arquivo Dockerfile e os outros arquivos do projeto.

2. Execute o comando a seguir para construir a imagem Docker:

```
sudo docker build -t nome_imagem .
```

3. Após a construção bem-sucedida da imagem, você pode criar e executar o contêiner com o comando abaixo:

```
sudo docker run -d -p 8443:8443 --name nome_que_sera_dado_ao_contêiner nome_imagem_criada
```

[lista de comandos relevantes do docker](https://github.com/Rosialdo/helport_project/blob/master/instru%C3%A7%C3%B5es/principais_comandos_docker.md)
