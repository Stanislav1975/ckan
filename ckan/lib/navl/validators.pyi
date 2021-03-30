from typing import Any, Callable, Dict, NoReturn, Tuple
import ckan.lib.navl.dictization_functions as df

missing = df.missing
StopOnError = df.StopOnError
Invalid = df.Invalid

def identity_converter(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> None: ...
def keep_extras(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> None: ...
def not_missing(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> None: ...
def not_empty(key: Tuple, data: Dict, errors: Dict, context: Dict) -> None: ...
def if_empty_same_as(other_key: str) -> Callable: ...
def both_not_empty(other_key: str) -> Callable: ...
def empty(key: Tuple, data: Dict, errors: Dict, context: Dict) -> None: ...
def ignore(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> NoReturn: ...
def default(default_value: Any) -> Callable: ...
def configured_default(
    config_name: str, default_value_if_not_configured: Any
) -> Callable: ...
def ignore_missing(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> None: ...
def ignore_empty(
    key: Tuple, data: Dict, errors: Dict, context: Dict
) -> None: ...
def convert_int(value: Any, context: Dict) -> int: ...
def unicode_only(value: Any) -> str: ...
def unicode_safe(value: Any) -> str: ...
def limit_to_configured_maximum(
    config_option: str, default_limit: int
) -> Callable: ...