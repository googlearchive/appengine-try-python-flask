"""`appengine_config` gets loaded when starting a new application instance."""
from vendor import insertsitedir
import os.path
# add `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions
insertsitedir(1, os.path.join(os.path.dirname(__file__), 'lib'))

