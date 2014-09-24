"""`appengine_config` gets loaded when starting a new application instance."""
import vendor
# add `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions
vendor.insertsitedir('lib')
