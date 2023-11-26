import os
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError
from dotenv import load_dotenv

load_dotenv()


def connect_to_influxdb(table_name):
    common_params = {
        'host': os.getenv('INFLUXDB_HOST'),
        'port': str(os.getenv('INFLUXDB_PORT')),
        'username': os.getenv('INFLUXDB_USERNAME'),
        'password': os.getenv('INFLUXDB_PASSWORD'),
        'ssl': bool(os.getenv('INFLUXDB_SSL')),
        'verify_ssl': bool(os.getenv('INFLUXDB_VERIFY_SSL'))
    }

    if table_name in ['axapta_av']:
        common_params['database'] = 'tests_on_windows'
    else:
        common_params['database'] = 'amis'

    return InfluxDBClient(**common_params)


def check_influxdb_status():
    try:
        common_params = {
            'host': os.getenv('INFLUXDB_HOST'),
            'port': int(os.getenv('INFLUXDB_PORT')),
            'username': os.getenv('INFLUXDB_USERNAME'),
            'password': os.getenv('INFLUXDB_PASSWORD'),
            'ssl': bool(os.getenv('INFLUXDB_SSL')),
            'verify_ssl': bool(os.getenv('INFLUXDB_VERIFY_SSL'))
        }

        client = InfluxDBClient(**common_params)
        client.ping()

        result = client.get_list_measurements()
        available_tables = [table['name'] for table in result]

        supported_tables = ['api_avto_inkosaciya_av', 'api_tech_av', 'axapta_av', 'bitrix_portal_av',
                            'db_1c_av', 'devops_av', 'dixy_av', 'dixy_group_av', 'dostavka_av', 'dostavka_bd_av',
                            'gold_av_centr', 'gold_av_depo11', 'gold_av_depo3', 'gold_av_depo34', 'gold_av_depo35',
                            'gold_av_depo38', 'gold_av_depo5', 'gold_av_depo60', 'gold_av_depo7', 'gold_av_mobila',
                            'gold_av_total', 'IBP_public_av_total', 'itilium_av', 'itilium_db_av',
                            'mobile_dixy_av', 'mopod_db_1c_av', 'shina_av', 'syn_av', 'tessa_av']

        available = [table for table in supported_tables if table in available_tables]
        unavailable = [table for table in supported_tables if table not in available_tables]

        message = f"Доступные таблицы в InfluxDB: {', '.join(available)}\n" \
                  f"Недоступные таблицы: {', '.join(unavailable)}"

        return message

    except InfluxDBClientError as client_error:
        return f"Ошибка при работе с InfluxDB: {str(client_error)}"
    except InfluxDBServerError as server_error:
        return f"Ошибка сервера InfluxDB: {str(server_error)}"
    except Exception as e:
        return f"Необработанная ошибка: {str(e)}"
