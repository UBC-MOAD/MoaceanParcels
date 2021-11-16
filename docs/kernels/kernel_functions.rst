.. Copyright 2021, UBC EOAS MOAD Group and The University of British Columbia
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..    https://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.

*********************
MOAD Kernel Functions
*********************

.. automodule:: moacean_parcels.kernels
    :members:
    :undoc-members:
    :show-inheritance:


.. _ParticleMotionKernels:

Particle Motion Kernels
=======================

Coming soon...


.. _RecoveryKernels:

Recovery Kernels
================

Recovery kernels are used to handle error conditions during particle simulations.
In the absence of a recovery kernel for error condition encountered,
the simulation ends,
likely with no output generated.

Recovery kernels are specified via a :py:obj:`dict` whose keys are defined in
the :py:class`ErrorCode` class in :py:mod:`parcels.tools.statuscodes`
and whose values are recovery kernel functions.
Here's an example of using :py:func:`moacean_parcels.kernels.DeleteParticle`
as a recovery kernel for the particle out of bounds conditions:

.. code-block:: python

    from moacean_parcels.kernels import DeleteParticle

    # ...

    pset.execute(
        kernels,
        # ...
        recovery={ErrorCode.ErrorOutOfBounds: DeleteParticle},
        # ...
    )

.. note::
    If you specify only a :kbd:`ErrorCode.ErrorOutOfBounds` recovery kernel,
    it will be use at all of the boundaries,
    including the ocean surface.
    If you want to handle particles that go through the surface differently
    to those hitting the bottom,
    land,
    or the domain boundary,
    you should provide a recovery kernel for that condition via the
    :kbd:`ErrorCode.ErrorThroughSurface` key.

Recovery kernels are not JIT-compiled when the :py:class:`parcels.particle.JITParticle`
particle class is used.
So,
they are not subject to the same restrictions on Python standard library modules,
:py:func:`print` function style,
etc.
as :ref:`ParticleMotionKernels` .


:py:func:`DeleteParticle`
-------------------------

.. autofunction:: moacean_parcels.kernels.DeleteParticle
