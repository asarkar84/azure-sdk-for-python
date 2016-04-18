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


class VirtualMachineScaleSetVMProfile(Model):
    """
    Describes a virtual machine scale set virtual machine profile.

    :param os_profile: Gets or sets the virtual machine scale set OS profile.
    :type os_profile: :class:`VirtualMachineScaleSetOSProfile
     <computemanagementclient.models.VirtualMachineScaleSetOSProfile>`
    :param storage_profile: Gets or sets the virtual machine scale set
     storage profile.
    :type storage_profile: :class:`VirtualMachineScaleSetStorageProfile
     <computemanagementclient.models.VirtualMachineScaleSetStorageProfile>`
    :param network_profile: Gets or sets the virtual machine scale set
     network profile.
    :type network_profile: :class:`VirtualMachineScaleSetNetworkProfile
     <computemanagementclient.models.VirtualMachineScaleSetNetworkProfile>`
    :param extension_profile: Gets the virtual machine scale set extension
     profile.
    :type extension_profile: :class:`VirtualMachineScaleSetExtensionProfile
     <computemanagementclient.models.VirtualMachineScaleSetExtensionProfile>`
    """ 

    _attribute_map = {
        'os_profile': {'key': 'osProfile', 'type': 'VirtualMachineScaleSetOSProfile'},
        'storage_profile': {'key': 'storageProfile', 'type': 'VirtualMachineScaleSetStorageProfile'},
        'network_profile': {'key': 'networkProfile', 'type': 'VirtualMachineScaleSetNetworkProfile'},
        'extension_profile': {'key': 'extensionProfile', 'type': 'VirtualMachineScaleSetExtensionProfile'},
    }

    def __init__(self, os_profile=None, storage_profile=None, network_profile=None, extension_profile=None):
        self.os_profile = os_profile
        self.storage_profile = storage_profile
        self.network_profile = network_profile
        self.extension_profile = extension_profile
