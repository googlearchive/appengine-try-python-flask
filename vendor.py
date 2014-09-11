import site
import sys

def insertsitedir(index, path):
    """Insert a site directory at the specified index of the path."""
    sys.path, remainder = sys.path[:index], sys.path[index:]
    site.addsitedir(path)
    sys.path.extend(remainder)

