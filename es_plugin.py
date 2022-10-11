#!/usr/bin/env python3

import sys
import typing
from dataclasses import dataclass

from arcaflow_plugin_sdk import plugin


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


@plugin.step(
    id="elasticsearch",
    name="Elasticsearch",
    description="Load data into elasticsearch instance",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def run(

) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """

    :return: the string identifying which output it is,
             as well the output structure
    """
    try:
        pass
        return "success", SuccessOutput(
            "upload"
        )
    except BaseException:
        return "error", ErrorOutput(
            "failed"
        )


if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        run,
    )))