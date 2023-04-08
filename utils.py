import time
from models.qos import Qos

from models.resource_unit import ResourceUnit
from example_functions.functions import *


def event_database(event_name: str) -> tuple(function, Qos):
    # Returns the function name and the assosciated QOS Specifications

    event = event_name.lower

    if event == "image resizing":
        return (image_resizing, Qos(1))
    elif event == "gif creator":
        return (gif_creation, Qos(1))
    elif event == "face detection":
        return (face_detection, Qos(2))
    elif event == "video conversion":
        return (video_conversion, Qos(3))
    else:
        return (None, None)


def get_execution_time(f, *params):
    # returns the estimated function execution time (in seconds)

    # TODO: Should also depend on the params
    if f == image_resizing:
        return 1
    elif f == gif_creation:
        return 1
    elif f == face_detection:
        return 2
    elif f == video_conversion:
        return 3
    else:
        return 0


def applyQosFilter(probableList: list[ResourceUnit], qos: Qos) -> list[ResourceUnit]:
    latency_metric = qos.latency
    cost_metric = qos.cost

    if latency_metric is not None:
        candidate_list = filter(
            lambda unit: unit.execution_time <= latency_metric, probableList
        )
        result = sorted(candidate_list, key=lambda x: x.execution_time)

    else:
        candidate_list = filter(
            lambda unit: unit.execution_cost <= cost_metric, probableList
        )
        result = sorted(candidate_list, key=lambda x: x.execution_cost)

    return result


def execute_function(res_unit: ResourceUnit, fi, *params):
    res_type = res_unit.resourceType

    print(f"Deploying funtion: {fi} with params: {params} on {res_type.name}\n")

    start = time.time()

    fi(params)

    end = time.time()

    et = end - start

    print(
        f"""
Function {fi} Executed on: {res_type.name} with params: {params}
    Execution Cost: Expected={res_unit.execution_cost}, Actual={et*res_type.ec_mul}
    Execution Time: Expected={res_unit.execution_time}, Actual={et}
"""
    )
    res_type.remove_worker_instance()
