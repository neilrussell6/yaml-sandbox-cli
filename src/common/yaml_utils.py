"""Data Library of functions that provide YAML related functionality."""
import io
import logging
import os
from functools import lru_cache

import yaml

logger = logging.getLogger(__name__)


# impure
@lru_cache(maxsize=16)
def parse_yaml(filename):
    """Parse YAML file."""
    path = os.path.join(filename)

    try:
        with io.open(path, 'r') as f:
            return yaml.load(f)
    except FileNotFoundError:
        logger.error(f'please create a {filename} file')
        return None
    except yaml.parser.ParserError as e:
        logger.error(f'{filename} file is incorrectly formatted')
        logger.error(e)
        return None
