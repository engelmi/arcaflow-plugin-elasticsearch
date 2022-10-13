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

def getEnvironmentVariables(params: ElasticsearchStorage) -> tuple[str, str, str]:
    """
    :return: a tuple [url, user, password] containing the extracted values 
    from the environment variables. 
    """
    return os.environ.get(params.url), \
        os.environ.get(params.user), \
        os.environ.get(params.password)


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
    :return: the string identifying which output it is, as well the output structure
    """

    url, user, password = getEnvironmentVariables(params)

    es = Elasticsearch(hosts=url, basic_auth=[user, password])
    try:
        es.index(index=params.index, document=params.data)

        return "success", SuccessOutput(
            "upload"
        )
    except Exception as ex:
        print(ex)
        return "error", ErrorOutput(
            format_exc()
        )

if __name__ == "__main__":
    sys.exit(plugin.run(plugin.build_schema(
        batch
    )))
