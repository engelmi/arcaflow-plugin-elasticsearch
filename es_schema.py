from dataclasses import dataclass, field
import typing
from typing import Annotated

from arcaflow_plugin_sdk import validation, schema


@dataclass
class ElasticsearchStorage:
    username_envvar: Annotated[str] = field(
        metadata={
            'name': 'username_envvar',
            'description': """Environment variable that points to """
            """an authorized username for the given Elasticsearch instance."""
        }
    )
    username: Annotated[typing.Optional[str]] = field(
        metadata={
            'name': 'username',
            'description': """Authorized username for the given """
            """Elasticsearch instance."""
        }
    )
    password_envvar: Annotated[str, validation.min(0)] = field(
        metadata={
            'name': 'password_envvar',
            'description': """Environment variable that points to the""" 
            """password for the given username."""
        }
    )
    password: Annotated[typing.Optional[str], validation.min(0)] = field(
        metadata={
            'name': 'password',
            'description': """Password for username for the given """
            """username."""
        }
    )
    url_envvar: Annotated[str] = field(
        metadata={
            'name': 'url',
            'description': """Environment variable that points """
            """to the URL of your Elasticsearch instance."""
        }
    )
    url: Annotated[typing.Optional[str]] = field(
        metadata={
            'name': 'url',
            'description': """URL to your Elasticsearch """
            """instance."""
        }
    )
    index: Annotated[str, validation.min(1)] = field(
        metadata={
            'name': 'index',
            'description': """Name of the index that """
            """will receive this data."""
        }
    )
    data: Annotated[typing.Optional[schema.ANY_TYPE]] = field(
        metadata={
            'name': 'data',
            'description': """Data to upload to your """
            """Elasticsearch index."""
        }
    )


@dataclass
class SuccessOutput:
    """
    This is the output data structure for the success case.
    """
    message: str


@dataclass
class ErrorOutput:
    """
    This is the output data structure in the error  case.
    """
    error: str


