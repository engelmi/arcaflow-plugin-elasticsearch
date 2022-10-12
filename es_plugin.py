#!/usr/bin/env python3

import os
import sys
import typing
from traceback import format_exc

from elasticsearch import Elasticsearch

from arcaflow_plugin_sdk import plugin
from es_schema import (
    ErrorOutput,
    SuccessOutput,
    ElasticsearchStorage
)


@plugin.step(
    id="elasticsearch",
    name="Elasticsearch",
    description="Load data into elasticsearch instance",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def batch(
    params: ElasticsearchStorage
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:
    """

    :return: the string identifying which output it is,
             as well the output structure
    """
    es = Elasticsearch(
        hosts=os.environ.get(params.url_envvar),
        http_auth=(
            os.environ.get(params.username_envvar),
            os.environ.get(params.password_envvar)
        )
    )
    try:
        es.index(
            index=params.index,
            document=params.data
        )
        return "success", SuccessOutput(
            "upload"
        )
    except Exception:
        return "error", ErrorOutput(
            format_exc()
        )


if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        batch
    )))
