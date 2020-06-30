from fbs import activate_profile, SETTINGS
from fbs.builtin_commands import clean, freeze, installer
from fbs.builtin_commands._util import require_existing_project
from fbs.cmdline import command

import logging

_LOG = logging.getLogger(__name__)
from os.path import dirname

import fbs.cmdline

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
        # if is_windows() and _has_windows_codesigning_certificate():
        #     sign()
        installer()
        # if (is_windows() and _has_windows_codesigning_certificate()) or \
        #     is_arch_linux() or is_fedora():
        #     sign_installer()
        # repo()
    finally:
        _LOG.setLevel(log_level)
    # upload()
    base_json = 'src/build/settings/base.json'
    update_json(path(base_json), { 'version': version })
    _LOG.info('Also, %s was updated with the new version.', base_json)

if __name__ == '__main__':
    project_dir = dirname(__file__)
    fbs.cmdline.main(project_dir)