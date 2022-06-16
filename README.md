# Correlación de series de tiempo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mijailo/econofisica/master)
> Inspirado en [este](http://mybinder.org/v2/gh/binder-examples/requirements/master) repositorio. 

Esta colección de _notebooks_ tiene la intención de ejemplificar de forma simple una tarea de descarga de series de tiempo financieras ([Yahoo Finance](https://finance.yahoo.com/)), preparación y limpieza de los datos, y cálculo de matrices de [correlación de Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).

## Ambientación de Python con Jupyter+Binder

La idea de este repositorio es poder crear un ambiente de `**Jupyter**` con `Python 3.x` (ver archivo `runtime.txt`), instalando las dependencias necesarias listadas en `requirements.txt`.

## Notas

* El archivo `requirements.txt` debe listar todas las librerías de Python invocadas en los notebooks. Éstas se instalan con:
```bash
$ pip install -r requirements.txt
```
* Si el repositorio se clona, se pueden especificar las dependencias de forma _vaga_, en un archivo `requirements.in`, con [pip-compile](https://github.com/jazzband/pip-tools/); así, se genera el archivo `requirements.txt` con las versiones estrictamente necesarias _congeladas_ (una _snapshot_):
```txt
#requirements.in
pandas
numpy
...
```
