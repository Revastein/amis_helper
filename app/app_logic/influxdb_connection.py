import os
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError, InfluxDBServerError
from dotenv import load_dotenv

load_dotenv()


def connect_to_influxdb(table_name):
    common_params = {
        'host': os.getenv('INFLUXDB_HOST'),
        'port': int(os.getenv('INFLUXDB_PORT')),
        'username': os.getenv('INFLUXDB_USERNAME'),
        'password': os.getenv('INFLUXDB_PASSWORD'),
        'ssl': os.getenv('INFLUXDB_SSL').lower() == 'true',
        'verify_ssl': os.getenv('INFLUXDB_VERIFY_SSL').lower() == 'true'
    }

    if table_name in ['axapta_av']:
        common_params['database'] = os.getenv('INFLUXDB_WINDOWS_TESTS_DATABASE')
    else:
        common_params['database'] = os.getenv('INFLUXDB_COMMON_DATABASE')

    return InfluxDBClient(**common_params)


def get_available_tables(client):
    try:
        result = client.get_list_measurements()
        return [table['name'] for table in result]
    except InfluxDBClientError as client_error:
        raise client_error


def format_status_message(available_tables, ping_response):
    supported_tables = ['api_avto_inkosaciya_av', 'api_tech_av', 'axapta_av', 'bitrix_portal_av',
                        'db_1c_av', 'devops_av', 'dixy_av', 'dixy_group_av', 'dostavka_av', 'dostavka_bd_av',
                        'gold_av_centr', 'gold_av_depo11', 'gold_av_depo3', 'gold_av_depo34', 'gold_av_depo35',
                        'gold_av_depo38', 'gold_av_depo5', 'gold_av_depo60', 'gold_av_depo7', 'gold_av_mobila',
                        'gold_av_total', 'IBP_public_av_total', 'itilium_av', 'itilium_db_av',
                        'mobile_dixy_av', 'mopod_db_1c_av', 'shina_av', 'syn_av', 'tessa_av']

    available = [table for table in supported_tables if table in available_tables]
    unavailable = [table for table in supported_tables if table not in available_tables]

    message = f"Доступные таблицы в InfluxDB: {', '.join(available)}\n" \
              f"Недоступные таблицы: {', '.join(unavailable)}\n"

    if ping_response.ok:
        if ping_response.reason.lower() == 'no content':
            message += "Состояние InfluxDB: ОК (No Content)\n"
        else:
            message += f"Состояние InfluxDB: {ping_response.reason}\n"

        message += f"Версия InfluxDB: {ping_response.headers.get('X-Influxdb-Version')}\n" \
                   f"Время обращения (ms): {ping_response.elapsed.total_seconds() * 1000}"
    else:
        message += f"Ошибка при обращении к InfluxDB: {ping_response.reason}"

    return message


def check_influxdb_minimal_status():
    try:
        common_params = {
            'host': os.getenv('INFLUXDB_HOST'),
            'port': int(os.getenv('INFLUXDB_PORT')),
            'username': os.getenv('INFLUXDB_USERNAME'),
            'password': os.getenv('INFLUXDB_PASSWORD'),
            'ssl': os.getenv('INFLUXDB_SSL').lower() == 'true',
            'verify_ssl': os.getenv('INFLUXDB_VERIFY_SSL').lower() == 'true',
            'database': os.getenv('INFLUXDB_COMMON_DATABASE')
        }

        client = InfluxDBClient(**common_params)
        ping_response = client.request('ping', expected_response_code=204)

        available_tables = ''
        message = format_status_message(available_tables, ping_response)

        return message

    except InfluxDBClientError as client_error:
        return f"Ошибка при работе с InfluxDB: {str(client_error)}"
    except InfluxDBServerError as server_error:
        return f"Ошибка сервера InfluxDB: {str(server_error)}"
    except Exception as e:
        return f"Необработанная ошибка: {str(e)}"


def check_influxdb_status_common_database():
    try:
        common_params = {
            'host': os.getenv('INFLUXDB_HOST'),
            'port': int(os.getenv('INFLUXDB_PORT')),
            'username': os.getenv('INFLUXDB_USERNAME'),
            'password': os.getenv('INFLUXDB_PASSWORD'),
            'ssl': os.getenv('INFLUXDB_SSL').lower() == 'true',
            'verify_ssl': os.getenv('INFLUXDB_VERIFY_SSL').lower() == 'true',
            'database': os.getenv('INFLUXDB_COMMON_DATABASE')
        }

        client = InfluxDBClient(**common_params)
        ping_response = client.request('ping', expected_response_code=204)

        available_tables = get_available_tables(client)
        available_tables = [table for table in available_tables if table != 'axapta_av']
        message = format_status_message(available_tables, ping_response)

        return message

    except InfluxDBClientError as client_error:
        return f"Ошибка при работе с InfluxDB: {str(client_error)}"
    except InfluxDBServerError as server_error:
        return f"Ошибка сервера InfluxDB: {str(server_error)}"
    except Exception as e:
        return f"Необработанная ошибка: {str(e)}"


def check_influxdb_status_windows_tests_database():
    try:
        common_params = {
            'host': os.getenv('INFLUXDB_HOST'),
            'port': int(os.getenv('INFLUXDB_PORT')),
            'username': os.getenv('INFLUXDB_USERNAME'),
            'password': os.getenv('INFLUXDB_PASSWORD'),
            'ssl': os.getenv('INFLUXDB_SSL').lower() == 'true',
            'verify_ssl': os.getenv('INFLUXDB_VERIFY_SSL').lower() == 'true',
            'database': os.getenv('INFLUXDB_WINDOWS_TESTS_DATABASE')
        }

        client = InfluxDBClient(**common_params)
        ping_response = client.request('ping', expected_response_code=204)

        available_tables = get_available_tables(client)
        available_tables = ['axapta_av'] if 'axapta_av' in available_tables else []
        message = format_status_message(available_tables, ping_response)

        return message

    except InfluxDBClientError as client_error:
        return f"Ошибка при работе с InfluxDB: {str(client_error)}"
    except InfluxDBServerError as server_error:
        return f"Ошибка сервера InfluxDB: {str(server_error)}"
    except Exception as e:
        return f"Необработанная ошибка: {str(e)}"
