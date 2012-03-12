from pipeline.compilers import CompilerBase
import scss
import os

# setup scss load path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_paths = scss.LOAD_PATHS.split(',') # split it up so we can a path check.
scss_path = os.path.join(root, 'pipeline_compass', 'compass')

if scss_path not in load_paths:
    load_paths.append(scss_path)
    scss.LOAD_PATHS = ','.join(load_paths)


class CompassCompiler(CompilerBase):
  output_extension = 'css'

  def match_file(self, filename):
    return filename.endswith('.scss')

  def compile_file(self, content, path):
    return scss.Scss().compile(content)
