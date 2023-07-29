import logging


class CustomLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M%S %p')

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger
