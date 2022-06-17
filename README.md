# Correlación de series de tiempo

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mijailo/timeSeriesCorrelations/HEAD) (Dame click we)
> Inspirado en [este](http://mybinder.org/v2/gh/binder-examples/requirements/master) repositorio. 

Esta colección de _notebooks_ tiene la intención de ejemplificar de forma simple una tarea de descarga de series de tiempo financieras ([Yahoo Finance](https://finance.yahoo.com/)), preparación y limpieza de los datos, y cálculo de matrices de [correlación de Pearson](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).

## Contenido del repositorio

```sh
.
├── 1 - Descarga y preparación de datos.ipynb
├── 2 - Matrices de correlación locales.ipynb
├── binder
│   ├── requirements.in
│   ├── requirements.txt
│   └── runtime.txt
├── data
│   ├── ^MXX_from2008-09-15_to2022-06-16_downloaded20220616.json
│   ├── returns^MXX_from2008-09-15_to2022-06-16_downloaded20220616.csv
│   ├── returns_SP500.csv
│   └── worldIndices_20220616.json
├── LICENSE
└── README.md
```

## Ambientación de Python con Jupyter+Binder

La idea de este repositorio es poder crear un ambiente de `**Jupyter**` con `Python 3.x` (ver archivo `runtime.txt`), instalando las dependencias necesarias listadas en `requirements.txt`.

### Notas

* El archivo `binder/requirements.txt` debe listar todas las librerías de Python invocadas en los notebooks. Éstas se instalan con:
```bash
$ pip install -r requirements.txt
```
* Si el repositorio se clona, se pueden especificar las dependencias de forma _vaga_, en un archivo `binder/requirements.in`, con [pip-compile](https://github.com/jazzband/pip-tools/); así, se genera el archivo `requirements.txt` con las versiones estrictamente necesarias _congeladas_ (una _snapshot_):
```txt
#requirements.in
pandas
numpy
...
```