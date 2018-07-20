"""Unit tests for parse_yaml function in libs.data.yaml library."""
import io
import logging
from unittest.mock import call

import pytest
import yaml

from src.common.yaml_utils import parse_yaml


@pytest.fixture
def mock_io_open(mocker):
    """Mock io.open."""
    return mocker.patch('io.open')


@pytest.fixture
def mock_logger_error(mocker):
    """Mock logger."""
    logger = logging.getLogger('libs.data.yaml')
    return mocker.patch.object(logger, 'error')


def test_return_yaml_file_as_dict(mock_io_open):
    """Should return YAML file contents as a Dict."""
    # given ... io.open returns some YAML file contents as a string
    _file_contents = io.StringIO('aaa: 123')
    mock_io_open.return_value.__enter__.return_value = _file_contents

    # when ... I parse a YAML file
    result = parse_yaml('imaginary1.yaml')

    # then
    # ... it should open that file
    mock_io_open.assert_called_once_with('imaginary1.yaml', 'r')

    # ... and return the YAML contents as a dict
    assert type(result) == dict
    assert result == {'aaa': 123}


@pytest.mark.skip()
@pytest.mark.parametrize('file_name,exception,expected_error_log_msg,expected_result', [
    (
        'imaginary2.yaml',
        FileNotFoundError,
        'please create a imaginary2.yaml file',
        None,
    ),
    (
        'imaginary3.yaml',
        yaml.parser.ParserError,
        'imaginary3.yaml file is incorrectly formatted',
        None,
    ),
])
def test_should_log_as_expected_for_each_exception(
    mock_io_open,
    mock_logger_error,
    file_name,
    exception,
    expected_error_log_msg,
    expected_result,
):
    """Should log as expected for each exception."""
    # given ... that io.open will raise the given exception
    mock_io_open.side_effect = exception

    # when ... I parse the given file_name
    result = parse_yaml(file_name)

    # then
    # ... should make expected_log_calls
    assert mock_logger_error.call_args_list[0] == call(expected_error_log_msg)

    # ... and return expected_result
    assert result == expected_result


def test_should_be_memoized(mock_io_open):
    """Should be memoized."""
    # given
    # ... io.open returns the string 'aaa: 123'
    file_contents = io.StringIO('aaa: 123')
    mock_io_open.return_value.__enter__.return_value = file_contents

    # ... and the function's cache is cleared
    parse_yaml.cache_clear()

    # when ... I load 2 files for the first time
    parse_yaml('file1.yaml')
    parse_yaml('file2.yaml')

    # then ... should have 2 misses and 0 hits
    assert parse_yaml.cache_info().misses == 2
    assert parse_yaml.cache_info().hits == 0

    # when ... I load the same 2 files for a second time
    parse_yaml('file1.yaml')
    parse_yaml('file2.yaml')

    # then ... should still have 2 misses, but now 2 hits as well
    assert parse_yaml.cache_info().misses == 2
    assert parse_yaml.cache_info().hits == 2
