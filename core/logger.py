import logging
def get_logger(name:str)->logging.Logger:
    logger=logging.get_logger(name)
    if not logger.handler:
        handler=logging.StreamHandler()
        formater=logging.Formatter(
            "" \
            "%(asctime)s |%(levelname)s |%(name)s |%(message)s"
        )
        handler.setFormatter(formater)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
