from app.app_logic.delete_and_rewrite_data import AppLogic
from app.app_styles.ui import DataManagementAppUI
from PyQt6.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])
    app_logic = AppLogic()
    app_ui = DataManagementAppUI(app_logic)

    app.exec()
