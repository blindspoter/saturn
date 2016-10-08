import os
import pkg_resources


__all__ = ['get_repository_root']


def get_repository_root():
    """Gets the root path of repository.

    :returns: the string path.
    """
    top_package = __package__.split('.')[0]
    package_root = pkg_resources.resource_filename(top_package, '')
    return os.path.dirname(os.path.abspath(package_root))
