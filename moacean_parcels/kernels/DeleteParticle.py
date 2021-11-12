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
    please see the DeleteParticle-example notebook.

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
