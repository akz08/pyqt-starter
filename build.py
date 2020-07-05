from fbs import activate_profile, SETTINGS
from fbs.builtin_commands import clean, freeze, installer
from fbs.builtin_commands._util import require_existing_project
from fbs.cmdline import command
import fbs.cmdline

import logging
from os.path import dirname

_LOG = logging.getLogger(__name__)

@command
def release_versioned(version):
    """
    Generate release with specified semantic version number
    - based on 'release' but accepts version as an argument
    """
    require_existing_project()
    activate_profile('release')
    SETTINGS['version'] = version
    log_level = _LOG.level
    if log_level == logging.NOTSET:
        _LOG.setLevel(logging.WARNING)
    try:
        clean()
        freeze()
        installer()
    finally:
        _LOG.setLevel(log_level)

if __name__ == '__main__':
    project_dir = dirname(__file__)
    fbs.cmdline.main(project_dir)