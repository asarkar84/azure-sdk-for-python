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


class SharedAccessAuthorizationRuleCreateOrUpdateParameters(Model):
    """
    Parameters supplied to the CreateOrUpdate Namespace AuthorizationRules.

    :param location: Gets or sets Namespace data center location.
    :type location: str
    :param name: Gets or sets Name of the Namespace AuthorizationRule.
    :type name: str
    :param properties: Gets or sets properties of the Namespace
     AuthorizationRules.
    :type properties: :class:`SharedAccessAuthorizationRuleProperties
     <notificationhubsmanagementclient.models.SharedAccessAuthorizationRuleProperties>`
    """ 

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'SharedAccessAuthorizationRuleProperties'},
    }

    def __init__(self, properties, location=None, name=None):
        self.location = location
        self.name = name
        self.properties = properties
