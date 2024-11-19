# Copyright 2022 – present, UBC EOAS MOAD Group and The University of British Columbia
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


def Stokes_drift(particle, fieldset, time):
    """Include the effect of Stokes drift to your particles
    trajectory using WaveWatch3 data.

    This kernel is intended for use as a particle behaviour kernel
        Example usage:

    .. code-block:: python

        from moacean_parcels.kernels import Stokes_drift

        # ...

        Sd_kernel = pset.Kernel(Stokes_drift)

        # ...

        pset.execute(kernels ... + Sd_kernel,
            # ...
        )

    For a more detailed usage example,
    please see the example notebook for this kernel in the
    :ref:`ParticleBehaviourKernelExampleNotebooks` section.

    :param particle: Particle to add behaviour.
    :type particle: :py:class:`parcels.particle.JITParticle` or
                    :py:class:`parcels.particle.ScipyInteractionParticle`

    :param fieldset: Hydrodynamic fields that is moving the particle.
    :type fieldset: :py:class:`parcels.fieldset.FieldSet`

    :param time: Current time of the particle.
    :type time: :py:attr:`numpy.float64`"""

    Sd_lat = particle.lat
    if Sd_lat > 48 and Sd_lat < 51:  # Check that particle is inside WW3 data field
        Sd_deg2m = 111319.5
        Sd_lonc = cos((Sd_lat * math.pi) / 180)
        (Sd_u, Sd_v, Sd_wl) = fieldset.stokes[
            time, particle.depth, particle.lat, particle.lon
        ]

        k = (2 * math.pi) / Sd_wl
        Sd_u = (Sd_u * exp(-abs(2 * k * particle.depth))) / (Sd_deg2m * Sd_lonc)
        Sd_v = (Sd_v * exp(-abs(2 * k * particle.depth))) / Sd_deg2m
        particle.lon += Sd_u * particle.dt
        particle.lat += Sd_v * particle.dt
