import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, logger_name="AutomationLogger"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # Fixed logs directory
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logs_dir = os.path.join(project_root, "Logs")

        """print("[DEBUG] Logger initialized:", logger_name)
        print("[DEBUG] Logs directory will be:", logs_dir)"""

        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Always create the file handler
        log_file = os.path.join(
            logs_dir,
            f"automation_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        )

        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Prevent adding multiple handlers
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

        # Force-create file by writing a header log
        self.logger.info("===== Logger started =====")

    def get_logger(self):
        return self.logger
