from dataclasses import dataclass, field
from typing import Annotated
import typing

from arcaflow_plugin_sdk import validation, schema

@dataclass
class ElasticsearchStorage:
    url: str = field(
        metadata={
            'name': 'url',
            'description': """Name of the environment variable containing """
            """the URL for the Elasticsearch instance."""
        }
    )

    user: Annotated[str, validation.min(1)] = field(
        metadata={
            'name': 'user',
            'description': """Name of the environment variable containing """
            """an authorized user for the given Elasticsearch instance."""
        }
    )

    password: str = field(
        metadata={
            'name': 'password',
            'description': """Name of the environment variable containing the"""
            """password for the given user."""
        }
    )

    index: Annotated[str, validation.min(1)] = field(
        metadata={
            'name': 'index',
            'description': """Name of the Elasticsearch index that will receive the data. """
        }
    )

    data: typing.Dict[str, schema.ANY_TYPE] = field(
        metadata={
            'name': 'data',
            'description': """Data to upload to your Elasticsearch index."""
        }
    )

    # integration test in workflow: uperf schauen (plugin?)
    # arcaflow sdk from main commit for any_type

@dataclass
class SuccessOutput:
    """
    This is the output data structure for the success case.
    """
    message: str

@dataclass
class ErrorOutput:
    """
    This is the output data structure in the error case.
    """
    error: str
