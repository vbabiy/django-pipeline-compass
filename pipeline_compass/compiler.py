from pipeline.compilers import CompilerBase
from django.core.files.base import ContentFile
from django.utils.encoding import smart_str

import scss
import os

def add_to_scss_path(path):
  load_paths = scss.LOAD_PATHS.split(',') # split it up so we can a path check.
  if path not in load_paths:
      load_paths.append(path)
      scss.LOAD_PATHS = ','.join(load_paths)

class CompassCompiler(CompilerBase):
  output_extension = 'css'

  def match_file(self, filename):
    return filename.endswith('.scss')

  def compile_file(self, content, path, force=False, outdated=False):
    add_to_scss_path(os.path.dirname(path)) # add the current path of the parsed file to enable the local @import
    if force or outdated:
        self.save_file(path, scss.Scss().compile(None, content))

  def save_file(self, path, content):
    return open(path, 'w').write(smart_str(content))

# setup scss load path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scss_path = os.path.join(root, 'pipeline_compass', 'compass')
add_to_scss_path(scss_path)