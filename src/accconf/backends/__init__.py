__all__ = ['BACKENDS', 'DEFAULT_BACKEND']
import logging
import os

logger = logging.getLogger(__name__)

# TODO: add json backend

def _get_backend(backend):
    if backend == 'yaml':
        from .yaml_db import YamlBackend
        return YamlBackend
    # if backend == 'json':
    #     from .json_db import JSONBackend
    #     return JSONBackend
    # raise ValueError(f'Unknown backend {backend!r}')


def _get_backends():
    # A hook for entrypoints or something similar later
    backends = {}
    try:
        backends['yaml'] = _get_backend('yaml')
    except ImportError as ex:
        logger.debug('YAML backend unavailable: %s', ex)
    # try:
    #     backends['json'] = _get_backend('json')
    # except ImportError as ex:
    #     logger.debug('JSON backend unavailable: %s', ex)

    return backends


BACKENDS = _get_backends()
try:
    # Check to see if the user has specified a specific backend as an
    # environment variable. Import this as the standard backend for other
    # places in the module. A user can always override this by explicitly
    # importing the backend
    DEFAULT_BACKEND = BACKENDS[os.environ.get("ACCCONF_BACKEND", 'yaml').lower()]
except KeyError:
    raise ImportError("Improper specification of AccConf backend. "
                      "Check the `$ACCCONF_BACKEND` environment variable.")
