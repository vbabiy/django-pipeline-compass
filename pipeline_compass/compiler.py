from pipeline.compilers import CompilerBase
from django.utils.encoding import smart_str
from django.conf import settings

import scss
import os


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
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scss_path = os.path.join(root, 'pipeline_compass', 'compass')
add_to_scss_path(scss_path)
