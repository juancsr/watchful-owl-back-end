# watchful-owl-back-end
Es una API REST para extracer información relevante de articulos.

# Front-end
Puedes encontrar el front de está app en: https://github.com/juancsr/watchful-owl-front-end

# Requierimientos
- Python 3.7.7
- pip 20.0.2 

# ¿Cómo puedo ejecutarlo?
* Crea un entorno virtual (puede ser utilizando [anaconda](https://www.anaconda.com/distribution/) o [virtualenv](https://virtualenv.pypa.io/en/stable/)).
* Clona el proyecto `git clone https://github.com/juancsr/watchful-owl-back-end`
* Ve al proyecto `cd watchful-owl-back-end`
* Dentro del proyecto, ejecuta `py app.py` para iniciar un servidor de desarrollo

* Abre tu navegador y ve al endpoint http://localhost:80/test
Este devería devolver: 
```json
{
  "message": "is working"
}
```

Sí es así, el API está listo para su uso :)

# Heroku
Puedes ver está API desplegada en heroku: https://watchful-owl.herokuapp.com/test
