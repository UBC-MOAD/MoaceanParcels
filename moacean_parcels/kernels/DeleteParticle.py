# Copyright 2021 – present, UBC EOAS MOAD Group and The University of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0


def DeleteParticle(particle, fieldset, time):
    """Delete a particle that has been lost during execution
    of the simulation and print its id number as well as information
    about where and when it was lost.

    This kernel is intended for use as an error recovery kernel,
    most likely for the
    :py:exc:`parcels.tools.statuscodes.OutOfBoundsError` or
    :py:exc:`parcels.tools.statuscodes.ThroughSurfaceError`
    error conditions.

    Example usage:

    .. code-block:: python

        from moacean_parcels.kernels import DeleteParticle

        # ...

        pset.execute(
            kernels,
            # ...
            recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle},
            # ...
        )

    For a more detailed usage example,
    please see the example notebook for this kernel in the
    :ref:`RecoveryKernelExampleNotebooks` section.

    :param particle: Particle that has gone out of bounds.
    :type particle: :py:class:`parcels.particle.JITParticle` or
                    :py:class:`parcels.particle.ScipyInteractionParticle`

    :param fieldset: Hydrodynamic fields that is moving the particle.
    :type fieldset: :py:class:`parcels.fieldset.FieldSet`

    :param time: Current time of the particle.
    :type time: :py:attr:`numpy.float64`
    """
    print(
        f"Particle [{particle.id}] lost!! "
        f"(lon, lat: {particle.lon}, {particle.lat}, "
        f"depth: {particle.depth}, time: {particle.time}s)"
    )
    particle.delete()
