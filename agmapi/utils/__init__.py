import logging


def init_logger(app):
    global logger

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    logger = app.logger

    logger.debug('Gunicorn logger added to Flask')


def get_logger():
    return logger
