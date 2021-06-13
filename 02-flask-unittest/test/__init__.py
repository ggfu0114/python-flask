import sys
import pathlib
import os

path_to_src_code = os.path.join(pathlib.Path(__file__).parent.parent.absolute(),'codes')
sys.path.append(path_to_src_code)

for path in sys.path:
    print(f'[Path] - {path}')