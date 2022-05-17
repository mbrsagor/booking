from __future__ import absolute_import, unicode_literals

from celery import current_app
from celery.bin import worker


if __name__ == '__main__':
    app = current_app._get_current_object()

    worker = worker.worker(app=app)

    options = {
        'broker': 'amqp://guest:guest@localhost:5672//',
        'loglevel': 'INFO',
        'traceback': True,
    }

    worker.run(**options)

