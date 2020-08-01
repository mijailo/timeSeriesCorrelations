import requests
from datetime import datetime
import calendar
import json
import csv
import re

def query(company):
    """
    type(company)=str
    Función para obtener una lista de diccionarios con las siguientes claves:
    {'symbol','name','exch','type','exchDisp','typeDisp'}
    """
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(company)
    result = requests.get(url).json()
    return result['ResultSet']['Result']

def get(yahoo_code,inicio,fin):
    """
    Función para bajar datos historicos de yahoo finance
    [inicio]=[fin]=(aaaa,mm,dd)
    """
    # parametros de conexion
    # ----------------------------------- #

    # http tiempo de espera
    timeout_secs = 5

    # reintentos
    num_retries = 5

    # url query
    yahoo_url = r'https://finance.yahoo.com/quote/{0}/history?p={0}'.format(yahoo_code)

    # iniciar encabezado
    headers = dict()
    headers['Connection'] = 'keep-alive'
    headers['Upgrade-Insecure-Requests'] = '1'
    headers['User-Agent'] = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"


    # manejo de conexion
    # ----------------------------------- #

    csv_data = None
    while num_retries>0:

        try:

            session = requests.Session()

            r = session.get(yahoo_url,headers=headers,timeout=timeout_secs)
            r.encoding = 'utf-8'
            html_text = r.text

            # get crumb
            pattern = r"(\"CrumbStore\":{\"crumb\":\")([^\"]+)(\"})"
            m = re.search(pattern, html_text)
            crumb = m.group(2).replace("\\u002F","/")

            # Obtener datos desde inicio=(aaaa,mm,dd) (UTC)
            start_time = calendar.timegm(datetime(inicio[0],inicio[1],inicio[2]).utctimetuple())
#           #hasta hoy: end_time = calendar.timegm(datetime.now().utctimetuple())   
            end_time = calendar.timegm(datetime(fin[0],fin[1],fin[2]).utctimetuple())

            # url para descargar datos
            data_url = r"https://query1.finance.yahoo.com/v7/finance/download/{0}?period1={1}&period2={2}&interval=1d&events=history&crumb={3}".format(yahoo_code, start_time, end_time, crumb)

            # bajar datos en formato csv
            r = session.get(data_url,headers=headers,timeout=timeout_secs)
            csv_data = csv.reader(r.content.decode().splitlines(),delimiter=',')

        except requests.exceptions.Timeout:

            wtext = 'Connection timeout, {0} reintentos restantes'.format(str(num_retries))

            # print or log
            print(wtext)

        except AttributeError:

            wtext = 'Error de migajas (crumb error), {0} reintentos restantes'.format(str(num_retries))

            # print or log
            print(wtext)

        except Exception:

            wtext = 'Error genérico, {0} intentos restantes'.format(str(num_retries))

            # print or log
            print(wtext)

        finally:

            if csv_data and r:
                wtext = 'Los datos para {0} se bajaron sin pedos.'.format(yahoo_code)

                # print or log
                print(wtext)
                break

            else:
                num_retries -= 1

    # asset-data
    if csv_data and r:
        eod_data = []
        for ii,row in enumerate(csv_data):

            if ii>0 and not 'null' in row:

                eod_data.append({
                    'date': row[0],
                    'open': float(row[1]),
                    'high': float(row[2]),
                    'low': float(row[3]),
                    'close': float(row[4]),
                    'adj_close': float(row[5]),
                    'volume': int(row[6])
                    })

        print('\nHay un total de {} registros.'.format(len(eod_data)))
        return eod_data
    else:

        wtext = 'No se pudo descargar {0} :c \n'.format(yahoo_code)

        # print or log
        print(wtext)

class TimeSeries:
    def __init__(self,company,initial_date,final_date):
        consulta=query(company)
        if len(consulta)>1:
            print('\n ***** \n')
            for i,c in enumerate(consulta):
                print('Opción {}:\n'.format(i),c)
                print('\n ***** \n')
            opcion=int(input('¿Cuál opción quieres?\n'))
            self.info=consulta[opcion]
            self.data=get(self.info['symbol'],initial_date,final_date)
        elif len(consulta)==1:
        	self.info=consulta[0]
        	self.data=get(self.info['symbol'],initial_date,final_date)
        else:
            self.info=dict()
            self.data=[]
            print('No encontré datos de {} :c.'.format(company))
