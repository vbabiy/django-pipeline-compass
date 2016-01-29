import os
import scss

from pipeline.compilers import CompilerBase
from django.utils.encoding import smart_str
from django.conf import settings


def add_to_scss_path(path):
    load_paths = scss.config.LOAD_PATHS.split(
        ',')  # split it up so we can a path check.
    if path not in load_paths:
        load_paths.append(path)
        scss.config.LOAD_PATHS = ','.join(load_paths)


class CompassCompiler(CompilerBase):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith(('.scss', '.sass'))

    def compile_file(self, content, path, force=False, outdated=False):
        add_to_scss_path(os.path.dirname(
            path))  # add the current path of the parsed
                    # file to enable the local @import
        if force or outdated:
            self.save_file(path, scss.Scss(scss_opts={
                'compress': False,
                'debug_info': settings.DEBUG,
            }).compile(None, content))

    def save_file(self, path, content):
        return open(path, 'w').write(smart_str(content))

# setup scss load path
scss.config.STATIC_ROOT = settings.STATIC_MEDIA
if (hasattr(settings, 'SCSS_STATIC_ROOT')):
  if not os.path.exists(settings.SCSS_STATIC_ROOT):
    os.makedirs(settings.SCSS_STATIC_ROOT)
  scss.config.ASSETS_ROOT = settings.SCSS_STATIC_ROOT

scss.config.STATIC_URL = settings.STATIC_URL
scss.config.ASSETS_URL = settings.STATIC_URL
 
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scss_path = os.path.join(root, 'pipeline_compass', 'compass')
add_to_scss_path(scss_path)

