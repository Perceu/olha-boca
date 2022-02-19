# Olha Boca
Repositorio para registrar e controlar infrações de uma equipe ( Brincadeira para melhorar o ambiente de trabalho )


# Instalar

Para iniciar o projeto na sua maquina Linux

```
sh setup.sh
```

# RUN
Para iniciar o projeto na sua maquina Linux

```
make migrate
make run
```

ou

```
source .venv/bin/activate
python manage migrate
python manage runserver
```

# Criando o primero usuario

```
python manage createsuperuser
```