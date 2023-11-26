# Amis Helper

## Описание
Amis Helper - это приложение, написанное на языке Python, использующее библиотеки InfluxDB и PyQt5. 
Предоставляет удобный интерфейс для удаления и перезаписи данных в базе данных InfluxDB.

## Использование
- **Запуск приложения:** Запустите приложение.
- **Выбор таблицы:** Выберите таблицу или таблицы из списка доступных для перезаписи.
- **Техническое окно:** Выберите, использовать ли техническое окно.
- **Временной диапазон:** Введите начальное и конечное время удаления в формате "YYYY-MM-DD HH:MM:SS".
- **Выполнение операции:** Нажмите "Удалить и перезаписать данные" для проведения операции.
- **Копирование в буфер обмена:** Используйте кнопку "Выбрать таблицу и скопировать ее в буфер обмена", чтобы скопировать название выбранной таблицы.

## Зависимости
- influxdb
- PyQt6
   ```
   pip install -r requirements.txt
   ```

## Таблицы
Поддерживаемые таблицы:

- api_avto_inkosaciya_av
- api_tech_av
- axapta_av
- bitrix_portal_av
- db_1c_av
- devops_av
- dixy_av
- dixy_group_av
- dostavka_av
- dostavka_bd_av
- gold_av_centr
- gold_av_depo11
- gold_av_depo3
- gold_av_depo34
- gold_av_depo35
- gold_av_depo38
- gold_av_depo5
- gold_av_depo60
- gold_av_depo7
- gold_av_mobila
- gold_av_total
- IBP_public_av_total
- itilium_av
- itilium_db_av
- mobile_dixy_av
- mopod_db_1c_av
- shina_av
- syn_av
- tessa_av

## Автор
Yan Kovzel'
- [GitHub](https://github.com/Revastein)
- [GitLab](https://git.dixy.local/YaSKovzel)
