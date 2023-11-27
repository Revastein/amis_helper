from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import datetime
import app.app_logic.influxdb_connection


class DataManagementAppUI(QWidget):
    """Класс для графического интерфейса приложения"""

    def __init__(self, app_logic):
        super().__init__()
        self.app_logic = app_logic

        # Темы
        self.light_style = './app/app_styles/themes/light_theme.qss'
        self.dark_style = './app/app_styles/themes/dark_theme.qss'
        self.current_style = self.dark_style

        # Иконка
        icon_path = "app/app_styles/icons/terminal_icon"
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)
        self.show()

        # Метки
        self.table_name_list = QLabel('Доступные таблицы для перезаписи:')
        self.table_name_entry = QLabel(self)  # Отображает выбранную таблицу для перезаписи
        self.table_name_label = QLabel('Выбранная таблица для перезаписи:')
        self.tech_window_entry = QLabel(self)  # Отображает выбранное значение для тех. окна
        self.tech_window_entry.setHidden(True)
        self.start_time_label = QLabel('Введите начальное время удаления (в формате YYYY-MM-DD HH:MM:SS):')
        self.end_time_label = QLabel('Введите конечное время удаления (в формате YYYY-MM-DD HH:MM:SS):')

        # Поля ввода
        self.start_time_entry = QLineEdit(self)
        self.end_time_entry = QLineEdit(self)

        # Установка текущей даты для start_time_entry и end_time_entry
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.start_time_entry.setText(current_date)
        self.end_time_entry.setText(current_date)

        # Переключатели
        self.tech_window_label = QLabel('Использовать техническое окно?')
        self.true_button = QRadioButton('Да', self)
        self.false_button = QRadioButton('Нет', self)
        self.true_button.clicked.connect(lambda: self.set_tech_window_value(True))
        self.false_button.clicked.connect(lambda: self.set_tech_window_value(False))
        self.false_button.setChecked(True)

        # Список
        self.table_names_list = QListWidget(self)
        self.table_names_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        # Метка результата
        self.result_label = QLabel(self)

        # Кнопки
        self.copy_button = QPushButton('Выбрать таблицу и скопировать ее в буфер обмена', self)
        self.copy_button.clicked.connect(self.copy_table)
        self.select_all_button = QPushButton('Выбрать все таблицы', self)
        self.select_all_button.clicked.connect(self.select_all_tables)
        self.clear_selection_button = QPushButton('Сбросить выбор', self)
        self.clear_selection_button.clicked.connect(self.clear_selection)
        self.delete_button = QPushButton('Удалить и перезаписать данные', self)
        self.delete_button.clicked.connect(self.handle_delete_and_rewrite)
        self.exit_button = QPushButton('Выход', self)
        self.exit_button.clicked.connect(self.exit_application)
        self.theme_button = QPushButton('Сменить тему', self)

        # Кнопка для проверки статуса InfluxDB
        self.check_influxdb_button = QPushButton('Проверить статус InfluxDB', self)
        self.check_influxdb_button.clicked.connect(self.show_influxdb_status)
        self.check_common_database_button = QPushButton('Проверить статус общей базы данных', self)
        self.check_common_database_button.clicked.connect(self.show_common_database_status)
        self.check_windows_tests_database_button = QPushButton('Проверить статус базы данных тестов на Windows', self)
        self.check_windows_tests_database_button.clicked.connect(self.show_windows_tests_database_status)

        # Бокс для отображения выбранных таблиц
        self.selected_tables_box = QTextEdit(self)
        self.selected_tables_box.setReadOnly(True)
        self.selected_tables_box.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.selected_tables_box.setWordWrapMode(QTextOption.WrapMode.WordWrap)

        # Инициализация UI
        self.init_ui()

    def init_ui(self):
        # Установка фиксированного размера окна
        self.setFixedSize(1024, 600)
        # Центрирование окна на экране
        self.center()

        # Названия таблиц для отображения в списке
        table_names = [
            'api_avto_inkosaciya_av', 'api_tech_av', 'axapta_av',
            'bitrix_portal_av',
            'db_1c_av', 'devops_av', 'dixy_av', 'dixy_group_av', 'dostavka_av', 'dostavka_bd_av',
            'gold_av_centr', 'gold_av_depo11', 'gold_av_depo3', 'gold_av_depo34', 'gold_av_depo35',
            'gold_av_depo38', 'gold_av_depo5', 'gold_av_depo60', 'gold_av_depo7', 'gold_av_mobila', 'gold_av_total',
            'IBP_public_av_total', 'itilium_av', 'itilium_db_av',
            'mobile_dixy_av', 'mopod_db_1c_av',
            'shina_av', 'syn_av',
            'tessa_av'
        ]
        self.table_names_list.addItems(table_names)

        # Подключение обработчика для кнопки смены темы
        self.theme_button.clicked.connect(self.toggle_theme)

        # Установка стилей из файла
        with open(self.current_style, 'r', encoding='utf-8') as style_file:
            self.setStyleSheet(style_file.read())

        # Создание разделителя горизонтального положения
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Левая часть (Доступные таблицы для перезаписи)
        left_layout = QVBoxLayout()
        self.setup_table_name_widgets(left_layout)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)
        self.clear_selection_button.clicked.connect(self.clear_selection)

        # Правая часть (остальной интерфейс)
        right_layout = QVBoxLayout()
        self.setup_tech_window_widgets(right_layout)
        self.setup_time_widgets(right_layout)
        self.setup_result_widget(right_layout)
        right_layout.addWidget(self.selected_tables_box)

        # Создание группы для кнопок смены темы и проверки статуса InfluxDB
        button_group_layout = QVBoxLayout()
        button_group_layout.addWidget(self.theme_button)
        button_group_layout.addWidget(self.check_influxdb_button)
        button_group_layout.addWidget(self.exit_button)

        right_layout.addLayout(button_group_layout)

        right_widget = QWidget()
        right_widget.setLayout(right_layout)

        # Добавление виджетов в разделитель
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)

        # Основной горизонтальный макет
        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)

        # Установка макета
        self.setLayout(main_layout)
        # Установка заголовка окна
        self.setWindowTitle('Управление данными InfluxDB')

    def center(self):
        """Центрирование окна на экране"""
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def load_style(self, style_path):
        """Загрузка стилей из файла"""
        with open(style_path, 'r', encoding='utf-8') as style_file:
            self.setStyleSheet(style_file.read())

    def toggle_theme(self):
        """Переключение темы приложения"""
        if self.current_style == self.light_style:
            self.current_style = self.dark_style
        else:
            self.current_style = self.light_style

        self.load_style(self.current_style)

    def handle_delete_and_rewrite(self):
        """Обработчик кнопки 'Удалить и перезаписать данные'"""
        selected_items = self.table_names_list.selectedItems()
        if not selected_items:
            self.result_label.setText('Выберите хотя бы одну таблицу для удаления и перезаписи данных.')
            return

        selected_tables = [item.text() for item in selected_items]
        tech_window_value = self.tech_window_entry.text()
        start_time_value = self.start_time_entry.text()
        end_time_value = self.end_time_entry.text()

        self.app_logic.delete_and_rewrite_data(
            selected_tables,
            tech_window_value,
            start_time_value,
            end_time_value,
            self.result_label
        )

    def setup_table_name_widgets(self, vbox):
        """Настройка виджетов для отображения доступных таблиц"""
        table_group_box = QGroupBox()
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table_name_list)
        table_layout.addWidget(self.table_names_list)
        table_layout.addWidget(self.copy_button)
        table_layout.addWidget(self.select_all_button)
        table_layout.addWidget(self.clear_selection_button)
        table_group_box.setLayout(table_layout)
        vbox.addWidget(table_group_box)

    def setup_time_widgets(self, vbox):
        """Настройка виджетов для управления временем"""
        time_group_box = QGroupBox()
        time_layout = QVBoxLayout()
        time_layout.addWidget(self.start_time_label)
        time_layout.addWidget(self.start_time_entry)
        time_layout.addWidget(self.end_time_label)
        time_layout.addWidget(self.end_time_entry)
        time_layout.addWidget(self.delete_button)
        time_layout.addWidget(self.exit_button)
        time_group_box.setLayout(time_layout)
        vbox.addWidget(time_group_box)

    def setup_tech_window_widgets(self, vbox):
        """Настройка виджетов для технического окна"""
        tech_window_group_box = QGroupBox()
        tech_window_layout = QVBoxLayout()
        tech_window_layout.addWidget(self.tech_window_label)
        tech_window_layout.addWidget(self.true_button)
        tech_window_layout.addWidget(self.false_button)
        tech_window_layout.addWidget(self.tech_window_entry)
        tech_window_group_box.setLayout(tech_window_layout)
        vbox.addWidget(tech_window_group_box)

    def setup_result_widget(self, vbox):
        """Настройка виджетов для отображения результата"""
        vbox.addWidget(self.result_label)

    def select_all_tables(self):
        """Выбор всех таблиц в списке"""
        for i in range(self.table_names_list.count()):
            item = self.table_names_list.item(i)
            item.setSelected(True)

    def copy_table(self):
        """Копирование выбранных таблиц в буфер обмена"""
        selected_items = self.table_names_list.selectedItems()
        if selected_items:
            selected_tables = [item.text() for item in selected_items]
            clipboard = QApplication.clipboard()
            clipboard.setText(', '.join(selected_tables))
            self.table_name_entry.setText(', '.join(selected_tables))

            self.selected_tables_box.setPlainText(', '.join(selected_tables))
            print(f'Скопирован текст: {", ".join(selected_tables)}')

    def clear_selection(self):
        """Сброс выбора таблиц"""
        self.table_names_list.clearSelection()
        self.table_name_entry.clear()
        self.selected_tables_box.clear()

    def set_tech_window_value(self, value):
        """Установка значения технического окна"""
        self.tech_window_entry.setText(str(value))

    def show_common_database_status(self):
        """Показ статуса общей базы данных InfluxDB в диалоговом окне"""
        status_message = app.app_logic.influxdb_connection.check_influxdb_status_common_database()
        QMessageBox().information(self, 'Статус таблиц InfluxDB (amis)', status_message)

    def show_windows_tests_database_status(self):
        """Показ статуса базы данных тестов на Windows InfluxDB в диалоговом окне"""
        status_message = app.app_logic.influxdb_connection.check_influxdb_status_windows_tests_database()
        QMessageBox().information(self, 'Статус таблиц InfluxDB (windows tests)', status_message)

    def show_influxdb_status(self):
        """Показ статуса InfluxDB в диалоговом окне"""
        status_message = app.app_logic.influxdb_connection.check_influxdb_minimal_status()
        self.center()

        dialog = QDialog(self)
        dialog.setWindowTitle('Статус InfluxDB')
        dialog.setGeometry(100, 100, 400, 400)

        status_text_edit = QTextEdit(dialog)
        status_text_edit.setPlainText(status_message)
        status_text_edit.setReadOnly(True)

        close_button = QPushButton('Закрыть', dialog)
        close_button.clicked.connect(dialog.close)

        check_common_button = QPushButton('Проверить статус общей базы данных', dialog)
        check_common_button.clicked.connect(self.show_common_database_status)

        check_windows_button = QPushButton('Проверить статус базы данных тестов на Windows', dialog)
        check_windows_button.clicked.connect(self.show_windows_tests_database_status)

        layout = QVBoxLayout()
        layout.addWidget(status_text_edit)
        layout.addWidget(check_common_button)
        layout.addWidget(check_windows_button)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec()

    @staticmethod
    def exit_application():
        """Выход из приложения"""
        QApplication.quit()
