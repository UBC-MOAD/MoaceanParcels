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

*****************************************************
How to Add a Kernel to :kbd:`moacean_parcels.kernels`
*****************************************************

#. Put your kernel code in a module in the
   :file:`MoaceanParcels/moacean_parcels/kernels/` directory
#. Register your kernel function in the
   :file:`MoaceanParcels/moacean_parcels/kernels/__init__.py` file
#. Add your kernel function to the automatic documentation generator in the
   :file:`MoaceanParcels/docs/kernel_functions.rst` file
#. more steps