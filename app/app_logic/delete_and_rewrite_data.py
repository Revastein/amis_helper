from datetime import datetime, timedelta
from app.app_logic.influxdb_connection import connect_to_influxdb
from app.app_logic.conditions import get_conditions_for_table


class AppLogic:
    @staticmethod
    def delete_and_rewrite_data(table_names, tech_window, start_time, end_time, result_label):
        for table_name in table_names:
            try:
                timestamp_start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                timestamp_end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

                if timestamp_end < timestamp_start:
                    raise ValueError('Неправильный ввод даты.'
                                     ' Конечное время должно быть больше или равно начальному времени.')

                client = connect_to_influxdb(table_name)

                client.query(
                    f"DELETE FROM {table_name} WHERE time >= '{(timestamp_start - timedelta(hours=3))}'"
                    f" AND time <= '{(timestamp_end - timedelta(hours=3))}'")

                conditions = get_conditions_for_table(table_name)
                data_tech = []

                while timestamp_start <= timestamp_end:
                    timestamp_start = timestamp_start + timedelta(seconds=300)
                    print(timestamp_start)
                    for condition in conditions:
                        if table_name == condition["MEASUREMENT"]:
                            measurement = condition["MEASUREMENT"]
                            it_service = condition["IT_SERVICE"]
                            tests = condition["TESTS"]

                            data_tech.append(
                                {
                                    "measurement": measurement,
                                    "tags": {
                                        "it_service": it_service,
                                        "source": "script",
                                        "tech_window": tech_window
                                    },
                                    "fields": tests,
                                    "time": (timestamp_start - timedelta(hours=3) - timedelta(
                                        minutes=5)).isoformat('T')
                                })

                    print(data_tech)

                client.write_points(data_tech)
                client.close()

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                success_message = (f'Успешно перезаписано в {current_time}.\nТаблица:'
                                   f' {table_name}\nУсловия: {tech_window}')
                result_label.setText(success_message)

            except Exception as e:
                result_label.setText(f'Ошибка: {str(e)}')
