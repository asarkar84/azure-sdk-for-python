# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobExecutionInformation(Model):
    """
    Contains information about the execution of a job in the Azure Batch
    service.

    :param start_time: Gets or sets the start time of the job.
    :type start_time: datetime
    :param end_time: Gets or sets the completion time of the job. This
     property is set only if the job is in the completed state.
    :type end_time: datetime
    :param pool_id: Gets or sets the id of the pool to which this job is
     assigned.
    :type pool_id: str
    :param scheduling_error: Gets or sets details of any error encountered by
     the service in starting the job.
    :type scheduling_error: :class:`JobSchedulingError
     <batchserviceclient.models.JobSchedulingError>`
    :param terminate_reason: Gets or sets a string describing the reason the
     job ended.
    :type terminate_reason: str
    """ 

    _validation = {
        'start_time': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'pool_id': {'key': 'poolId', 'type': 'str'},
        'scheduling_error': {'key': 'schedulingError', 'type': 'JobSchedulingError'},
        'terminate_reason': {'key': 'terminateReason', 'type': 'str'},
    }

    def __init__(self, start_time, end_time=None, pool_id=None, scheduling_error=None, terminate_reason=None):
        self.start_time = start_time
        self.end_time = end_time
        self.pool_id = pool_id
        self.scheduling_error = scheduling_error
        self.terminate_reason = terminate_reason
