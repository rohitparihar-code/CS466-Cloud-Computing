import time
from models.qos import Qos

from models.resource_unit import ResourceUnit
from example_functions.fn_examples import *


def get_execution_time(f, *params):
    # returns the estimated function execution time (in seconds)
    if f == fn_example_3:
        return 2.25
    elif f == fn_example_1:
        return 10 * params[0]
    elif f == fn_example_2:
        return 20 * params[0]
    else:
        return 20


def applyQosFilter(probableList: list[ResourceUnit], qos: Qos) -> list[ResourceUnit]:
    et_c = 0.5
    et_w = 1 - et_c

    user_w = qos.execution_cost * et_c + qos.execution_time * et_w

    candidate_list = []

    for x in probableList:
        score = x.execution_cost * et_c + x.execution_time * et_w
        if score <= user_w:
            candidate_list.append(x)

    if len(candidate_list) == 0:
        result = sorted(probableList, key=lambda x: x.execution_cost)
    else:
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
