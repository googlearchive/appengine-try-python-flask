"""
Helpers for adding dependencies to the import path.

Usage:
    from vendor import insertsitedir
    insertsitedir('lib')
"""

import os
import site
import sys


def insertsitedir(directory, index=1):
    """
    Adds the given folder to the python path. Supports namespaced packages.
    By default, packages in the given folder take precedence over site-packages
    and any previous path manipulations.

    Args:
    directory: Path to the directory containing packages, relative to the
    current working directory.
    index: Where in ``sys.path`` to insert the vendor packages. By default
    this is set to 1. It is inadvisable to set it to 0 as it will override
    any modules in the current working directory.
    """
    # Use site.addsitedir() because it appropriately reads .pth
    # files for namespaced packages. Unfortunately, there's not an
    # option to choose where addsitedir() puts its paths in sys.path
    # so we have to do a little bit of magic to make it play along.

    # We're going to grab the current sys.path and split it up into
    # the first entry and then the rest. Essentially turning
    #   ['.', '/site-packages/x', 'site-packages/y']
    # into
    #   ['.'] and ['/site-packages/x', 'site-packages/y']
    # The reason for this is we want '.' to remain at the top of the
    # list but we want our vendor files to override everything else.
    sys.path, remainder = sys.path[:index], sys.path[index:]

    # Now we call addsitedir which will append our vendor directories
    # to sys.path (which was truncated by the last step.)
    site.addsitedir(directory)

    # Finally, we'll add the paths we removed back, resulting in
    # ['.', '/vendor', '/site-packages/x', 'site-packages/y']
    sys.path.extend(remainder)


def insertvenv(directory, index=1):
    """
    Adds the given virtualenv's site-packages directory to the python path.

    Args:
    directory: Path to the root directory of the virtualenv, relative
    to the current working directory.
    index: passed through to insertsitedir().
    """
    site_dir = os.path.join(directory, 'lib', 'python' + sys.version[:3],
                            'site-packages')
    insertsitedir(site_dir, index=index)
